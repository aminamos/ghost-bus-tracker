/**
 * Static GTFS schedule support for derived on-time performance.
 *
 * Some agencies publish GTFS-RT trip updates with absolute predicted times
 * but no `delay` field. For those markets we derive delay ourselves:
 * delay = RT predicted departure - scheduled departure (static GTFS
 * stop_times.txt), anchored on the trip's service date in the agency
 * timezone. Static feeds refresh at most daily; only stop times for trips
 * present in the current RT feed are kept, so the R2 cache stays small.
 */

import { unzipSync, strFromU8 } from "fflate";

const CACHE_TTL_MS = 24 * 3600 * 1000;
const MAX_STOP_TIMES_BYTES = 256 * 1024 * 1024; // hard guard; parsing itself is chunked

function cacheKey(marketId) {
  return `static/${marketId}/schedule.json`;
}

// Parse one CSV line, honoring double-quoted fields.
function parseCsvLine(line) {
  const out = [];
  let cur = "";
  let quoted = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (quoted) {
      if (c === '"') {
        if (line[i + 1] === '"') { cur += '"'; i++; } else quoted = false;
      } else cur += c;
    } else if (c === '"') quoted = true;
    else if (c === ",") { out.push(cur); cur = ""; }
    else cur += c;
  }
  out.push(cur);
  return out;
}

function hmsToSec(s) {
  const parts = String(s || "").split(":");
  if (parts.length !== 3) return null;
  const [h, m, sec] = parts.map(Number);
  if (![h, m, sec].every(Number.isFinite)) return null;
  return h * 3600 + m * 60 + sec;
}

/**
 * Build { tz, trips } from GTFS zip bytes, keeping only wantedTripIds.
 * trips: Map<tripId, { bySeq: Map<seq, depSec>, byStop: Map<stopId, depSec> }>
 */
export function buildScheduleFromZip(zipBytes, wantedTripIds) {
  const files = unzipSync(zipBytes, {
    filter: (f) => f.name === "stop_times.txt" || f.name === "agency.txt",
  });
  let tz = "UTC";
  const agencyFile = files["agency.txt"];
  if (agencyFile) {
    const lines = strFromU8(agencyFile).split(/\r?\n/);
    const header = parseCsvLine(lines[0] || "");
    const tzIdx = header.indexOf("agency_timezone");
    if (tzIdx >= 0) {
      for (let i = 1; i < lines.length; i++) {
        if (!lines[i]) continue;
        const v = parseCsvLine(lines[i])[tzIdx];
        if (v) { tz = v; break; }
      }
    }
  }
  const stopTimes = files["stop_times.txt"];
  if (!stopTimes) throw new Error("static GTFS has no stop_times.txt");
  if (stopTimes.length > MAX_STOP_TIMES_BYTES) {
    throw new Error(`stop_times.txt too large (${stopTimes.length} bytes)`);
  }
  const trips = new Map();
  // Decode in chunks and process line-by-line: stop_times.txt can exceed
  // 50MB uncompressed, which must never materialize as one string.
  const decoder = new TextDecoder();
  let header = null;
  let iTrip = -1, iDep = -1, iArr = -1, iStop = -1, iSeq = -1;
  const handleLine = (line) => {
    if (!line) return;
    if (!header) {
      header = parseCsvLine(line.replace(/^\uFEFF/, ""));
      iTrip = header.indexOf("trip_id");
      iDep = header.indexOf("departure_time");
      iArr = header.indexOf("arrival_time");
      iStop = header.indexOf("stop_id");
      iSeq = header.indexOf("stop_sequence");
      if (iTrip < 0 || (iDep < 0 && iArr < 0)) throw new Error("stop_times.txt missing required columns");
      return;
    }
    const cols = parseCsvLine(line);
    // Join key: exact RT trip id, else the suffix after the first "_"
    // (NYCT static ids prefix the RT id, e.g. "ASP26GEN-.._000600_1..S03R"
    // vs RT "000600_1..S03R").
    let tripId = cols[iTrip];
    if (!wantedTripIds.has(tripId)) {
      const u = tripId.indexOf("_");
      if (u > 0 && wantedTripIds.has(tripId.slice(u + 1))) tripId = tripId.slice(u + 1);
      else return;
    }
    const dep = hmsToSec(cols[iDep] ?? cols[iArr]);
    if (dep == null) return;
    let entry = trips.get(tripId);
    if (!entry) { entry = { bySeq: new Map(), byStop: new Map() }; trips.set(tripId, entry); }
    const seq = iSeq >= 0 ? Number(cols[iSeq]) : NaN;
    if (Number.isFinite(seq)) entry.bySeq.set(seq, dep);
    const stopId = iStop >= 0 ? cols[iStop] : "";
    if (stopId) entry.byStop.set(stopId, dep);
  };
  let buf = "";
  const CHUNK = 1024 * 1024;
  for (let off = 0; off < stopTimes.length; off += CHUNK) {
    buf += decoder.decode(stopTimes.subarray(off, off + CHUNK), { stream: true });
    let nl;
    while ((nl = buf.indexOf("\n")) >= 0) {
      handleLine(buf.slice(0, nl).replace(/\r$/, ""));
      buf = buf.slice(nl + 1);
    }
  }
  buf += decoder.decode();
  if (buf) handleLine(buf.replace(/\r$/, ""));
  if (!header) throw new Error("stop_times.txt is empty");
  return { tz, trips };
}

function serializeSchedule(tz, trips) {
  const out = {};
  for (const [id, e] of trips) {
    out[id] = [[...e.bySeq.entries()], [...e.byStop.entries()]];
  }
  return JSON.stringify({ tz, built_at: new Date().toISOString(), trips: out });
}

function deserializeSchedule(json) {
  const data = JSON.parse(json);
  const trips = new Map();
  for (const [id, [seqs, stops]] of Object.entries(data.trips || {})) {
    trips.set(id, { bySeq: new Map(seqs), byStop: new Map(stops) });
  }
  return { tz: data.tz || "UTC", trips, builtAt: data.built_at || null };
}

/**
 * Load the static schedule for a market: fresh R2 cache if present, else
 * build from the agency zip (filtered to current RT trip ids) and cache.
 * Returns null on any failure; scans then proceed without derived delays.
 */
export async function getStaticSchedule(env, marketId, staticUrl, wantedTripIds, fetchImpl = fetch) {
  const bucket = env?.SNAPSHOT_BUCKET;
  if (bucket) {
    try {
      const obj = await bucket.get(cacheKey(marketId));
      if (obj) {
        const sched = deserializeSchedule(await obj.text());
        const age = Date.now() - Date.parse(sched.builtAt || 0);
        // Reuse while fresh, or while it still covers most wanted trips.
        const covered = [...wantedTripIds].filter((t) => sched.trips.has(t)).length;
        if (age < CACHE_TTL_MS || covered >= wantedTripIds.size * 0.8) return sched;
      }
    } catch {
      // fall through to rebuild
    }
  }
  try {
    const res = await fetchImpl(staticUrl, {
      headers: { "User-Agent": "GhostBusTracker/0.1.0 (+https://github.com/aminamos/ghost-bus-tracker)" },
      signal: AbortSignal.timeout(120000),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status} fetching static GTFS`);
    const zipBytes = new Uint8Array(await res.arrayBuffer());
    const { tz, trips } = buildScheduleFromZip(zipBytes, wantedTripIds);
    if (bucket) {
      await bucket.put(cacheKey(marketId), serializeSchedule(tz, trips), {
        httpMetadata: { contentType: "application/json; charset=utf-8" },
      }).catch(() => {});
    }
    return { tz, trips, builtAt: new Date().toISOString() };
  } catch {
    return null;
  }
}

// UTC offset (ms) of an IANA timezone at a given UTC instant.
function tzOffsetMs(tz, utcMs) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: tz, year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23",
  }).formatToParts(new Date(utcMs));
  const p = {};
  for (const part of parts) p[part.type] = Number(part.value);
  const asUTC = Date.UTC(p.year, p.month - 1, p.day, p.hour, p.minute, p.second);
  return asUTC - Math.floor(utcMs / 1000) * 1000;
}

// Epoch seconds of local midnight on a YYYYMMDD service date in tz.
export function serviceDayStartEpoch(tz, yyyymmdd) {
  const y = Number(yyyymmdd.slice(0, 4));
  const m = Number(yyyymmdd.slice(4, 6));
  const d = Number(yyyymmdd.slice(6, 8));
  const utcMidnight = Date.UTC(y, m - 1, d);
  return Math.floor((utcMidnight - tzOffsetMs(tz, utcMidnight)) / 1000);
}

// YYYYMMDD of an epoch instant in tz (fallback service date).
export function serviceDateInTz(tz, epochSec) {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: tz, year: "numeric", month: "2-digit", day: "2-digit",
  }).formatToParts(new Date(epochSec * 1000));
  const p = {};
  for (const part of parts) p[part.type] = part.value;
  return `${p.year}${p.month}${p.day}`;
}

const MAX_SANE_DELAY_SEC = 6 * 3600;

/**
 * Fill delay_seconds (median, seconds) for trips that lack a feed delay,
 * using RT absolute times vs the static schedule. Mutates and returns trips.
 */
export function applyDerivedDelays(trips, schedule, feedTimestamp) {
  if (!schedule) return trips;
  for (const trip of trips) {
    if (trip.delay_seconds != null || !trip.rt_times || !trip.rt_times.length) continue;
    const entry = schedule.trips.get(trip.trip_id);
    if (!entry) continue;
    const serviceDate = trip.start_date || (feedTimestamp ? serviceDateInTz(schedule.tz, feedTimestamp) : null);
    if (!serviceDate) continue;
    const epoch0 = serviceDayStartEpoch(schedule.tz, serviceDate);
    const delays = [];
    for (const rt of trip.rt_times) {
      let dep = null;
      if (rt.seq != null && entry.bySeq.has(rt.seq)) dep = entry.bySeq.get(rt.seq);
      else if (rt.stop_id && entry.byStop.has(rt.stop_id)) dep = entry.byStop.get(rt.stop_id);
      if (dep == null) continue;
      const d = rt.time - (epoch0 + dep);
      if (Math.abs(d) <= MAX_SANE_DELAY_SEC) delays.push(d);
    }
    if (delays.length) {
      delays.sort((a, b) => a - b);
      const mid = Math.floor(delays.length / 2);
      const median = delays.length % 2 ? delays[mid] : (delays[mid - 1] + delays[mid]) / 2;
      trip.delay_seconds = Math.trunc(median);
      trip.delay_derived = true;
    }
  }
  return trips;
}
