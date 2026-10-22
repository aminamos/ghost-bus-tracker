/**
 * In-Worker GTFS-RT scan pipeline for Ghost Bus Tracker.
 *
 * Mirrors the Python engine (src/fetcher.py + src/analyzer.py): fetches the
 * same VehiclePositions/TripUpdates feeds per market, decodes them with the
 * official gtfs-realtime-bindings (protobufjs, no hand-rolled parsing), and
 * runs the same ghost-detection analysis. Output snapshots match the
 * ReliabilitySnapshot JSON shape field-for-field.
 */

import { CITY_FEED_URLS } from "./cities_data.js";
import { getStaticSchedule, applyDerivedDelays } from "./static_schedule.js";
import gtfsBindings from "gtfs-realtime-bindings";

const FeedMessage = gtfsBindings.transit_realtime.FeedMessage;

const USER_AGENT = "GhostBusTracker/0.1.0 (+https://github.com/aminamos/ghost-bus-tracker)";
const REQUEST_TIMEOUT_MS = 15000;

// Reliability thresholds (seconds), mirroring src/config.py defaults.
const DEFAULT_THRESHOLDS = {
  earlySec: -60,
  onTimeSec: 300,
  minorDelaySec: 900,
};

// Per-market labels + auth, mirroring AGENCY_PRESETS in src/config.py.
// Feed URLs stay single-sourced in CITY_FEED_URLS (shared with the live proxy).
export const SCAN_PRESETS = [
  { id: "twin-cities", name: "Metro Transit", agency: "Metro Transit (Twin Cities)", city: "Minneapolis–Saint Paul, MN", region: "Twin Cities Metropolitan Area, Minnesota", state: "Minnesota", country: "USA", requiresKey: false },
  { id: "chicago", name: "CTA", agency: "Chicago Transit Authority", city: "Chicago, IL", region: "Chicagoland / Cook County, Illinois", state: "Illinois", country: "USA", requiresKey: true, keyEnvVar: "CTA_API_KEY", keyParam: "key" },
  { id: "boston", name: "MBTA", agency: "Massachusetts Bay Transportation Authority", city: "Boston, MA", region: "Greater Boston, Massachusetts", state: "Massachusetts", country: "USA", requiresKey: false },
  { id: "nyc", name: "MTA", agency: "Metropolitan Transportation Authority", city: "New York, NY", region: "New York Metropolitan Area", state: "New York", country: "USA", requiresKey: false, staticUrl: "https://web.mta.info/developers/data/nyct/subway/google_transit.zip" },
  { id: "sf", name: "SFMTA", agency: "San Francisco Municipal Transportation Agency", city: "San Francisco, CA", region: "San Francisco Bay Area, California", state: "California", country: "USA", requiresKey: true, keyEnvVar: "BAY_AREA_511_KEY", keyParam: "api_key" },
  { id: "philly", name: "SEPTA", agency: "Southeastern Pennsylvania Transportation Authority", city: "Philadelphia, PA", region: "Greater Philadelphia / Delaware Valley, Pennsylvania", state: "Pennsylvania", country: "USA", requiresKey: false },
  { id: "dc", name: "WMATA", agency: "Washington Metropolitan Area Transit Authority", city: "Washington, DC", region: "Washington Metropolitan Area (DC, MD, VA)", state: "District of Columbia", country: "USA", requiresKey: true, keyEnvVar: "WMATA_API_KEY", keyHeader: "api_key" },
  { id: "la", name: "LA Metro", agency: "Los Angeles County Metropolitan Transportation Authority", city: "Los Angeles, CA", region: "Los Angeles County, California", state: "California", country: "USA", requiresKey: true, keyEnvVar: "LAMETRO_API_KEY", keyHeader: "Authorization" },
  { id: "seattle", name: "Sound Transit & KCM", agency: "King County Metro / Sound Transit", city: "Seattle, WA", region: "Central Puget Sound Region, Washington", state: "Washington", country: "USA", requiresKey: false },
  { id: "denver", name: "RTD", agency: "Regional Transportation District", city: "Denver, CO", region: "Denver Metropolitan Area, Colorado", state: "Colorado", country: "USA", requiresKey: false },
  { id: "portland", name: "TriMet", agency: "Tri-County Metropolitan Transportation District of Oregon", city: "Portland, OR", region: "Portland Metropolitan Area, Oregon", state: "Oregon", country: "USA", requiresKey: true, keyEnvVar: "TRIMET_APP_ID", keyParam: "appID" },
  { id: "atlanta", name: "MARTA", agency: "Metropolitan Atlanta Rapid Transit Authority", city: "Atlanta, GA", region: "Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia", state: "Georgia", country: "USA", requiresKey: false, staticUrl: "https://www.itsmarta.com/google_transit_feed/google_transit.zip" },
  { id: "toronto", name: "TTC", agency: "Toronto Transit Commission", city: "Toronto, ON", region: "Greater Toronto Area, Ontario", state: "Ontario", country: "Canada", requiresKey: false },
  { id: "austin", name: "CapMetro", agency: "Capital Metropolitan Transportation Authority", city: "Austin, TX", region: "Austin–Round Rock Metropolitan Area, Texas", state: "Texas", country: "USA", requiresKey: false, staticUrl: "https://data.texas.gov/download/r4v4-vz24/application/zip" },
  { id: "phoenix", name: "Valley Metro", agency: "Valley Metro", city: "Phoenix, AZ", region: "Phoenix–Mesa Metropolitan Area, Arizona", state: "Arizona", country: "USA", requiresKey: false },
  { id: "pittsburgh", name: "PRT", agency: "Pittsburgh Regional Transit", city: "Pittsburgh, PA", region: "Pittsburgh Metropolitan Area, Pennsylvania", state: "Pennsylvania", country: "USA", requiresKey: false },
  { id: "edmonton", name: "ETS", agency: "Edmonton Transit Service", city: "Edmonton, AB", region: "Edmonton Metropolitan Region, Alberta", state: "Alberta", country: "Canada", requiresKey: false },
  { id: "halifax", name: "Halifax Transit", agency: "Halifax Transit", city: "Halifax, NS", region: "Halifax Regional Municipality, Nova Scotia", state: "Nova Scotia", country: "Canada", requiresKey: false, staticUrl: "http://gtfs.halifax.ca/static/google_transit.zip" },
  { id: "orlando", name: "LYNX", agency: "Central Florida Regional Transportation Authority", city: "Orlando, FL", region: "Orlando Metropolitan Area, Florida", state: "Florida", country: "USA", requiresKey: false },
  { id: "broward", name: "Broward County Transit", agency: "Broward County Transit", city: "Fort Lauderdale, FL", region: "Broward County, Florida", state: "Florida", country: "USA", requiresKey: false },
  { id: "albany", name: "CDTA", agency: "Capital District Transportation Authority", city: "Albany, NY", region: "Capital District, New York", state: "New York", country: "USA", requiresKey: false },
  { id: "lansing", name: "CATA", agency: "Capital Area Transportation Authority", city: "Lansing, MI", region: "Lansing Metropolitan Area, Michigan", state: "Michigan", country: "USA", requiresKey: false },
  { id: "champaign-urbana", name: "MTD", agency: "Champaign-Urbana Mass Transit District", city: "Champaign–Urbana, IL", region: "Champaign County, Illinois", state: "Illinois", country: "USA", requiresKey: false },
  { id: "cincinnati", name: "Metro", agency: "Southwest Ohio Regional Transit Authority", city: "Cincinnati, OH", region: "Cincinnati Metropolitan Area, Ohio", state: "Ohio", country: "USA", requiresKey: false, staticUrl: "http://www.go-metro.com/uploads/GTFS/google_transit_info.zip" },
  { id: "hartford", name: "CTtransit", agency: "Connecticut Transit", city: "Hartford, CT", region: "Hartford Metropolitan Area, Connecticut", state: "Connecticut", country: "USA", requiresKey: false, staticUrl: "https://www.cttransit.com/sites/default/files/gtfs/googlect_transit.zip" },
  { id: "des-moines", name: "DART", agency: "Des Moines Area Regional Transit Authority", city: "Des Moines, IA", region: "Des Moines Metropolitan Area, Iowa", state: "Iowa", country: "USA", requiresKey: false, staticUrl: "https://www.ridedart.com/gtfs/data/gtfsdata" },
  { id: "duluth", name: "DTA", agency: "Duluth Transit Authority", city: "Duluth, MN", region: "Duluth–Superior Metropolitan Area, Minnesota", state: "Minnesota", country: "USA", requiresKey: false, staticUrl: "https://duluthtransit.com/gtf/google_transit.zip" },
  { id: "durham", name: "DRT", agency: "Durham Region Transit", city: "Durham, ON", region: "Regional Municipality of Durham, Ontario", state: "Ontario", country: "Canada", requiresKey: false, staticUrl: "https://maps.durham.ca/OpenDataGTFS/GTFS_Durham_TXT.zip" },
  { id: "cleveland", name: "GCRTA", agency: "Greater Cleveland Regional Transit Authority", city: "Cleveland, OH", region: "Cleveland Metropolitan Area, Ohio", state: "Ohio", country: "USA", requiresKey: false },
  { id: "guelph", name: "Guelph Transit", agency: "Guelph Transit", city: "Guelph, ON", region: "City of Guelph, Ontario", state: "Ontario", country: "Canada", requiresKey: false },
  { id: "hamilton", name: "HSR", agency: "Hamilton Street Railway", city: "Hamilton, ON", region: "City of Hamilton, Ontario", state: "Ontario", country: "Canada", requiresKey: false, staticUrl: "https://opendata.hamilton.ca/GTFS-Static/google_transit.zip" },
  { id: "kingston", name: "Kingston Transit", agency: "Kingston Transit", city: "Kingston, ON", region: "City of Kingston, Ontario", state: "Ontario", country: "Canada", requiresKey: false },
  { id: "london", name: "LTC", agency: "London Transit Commission", city: "London, ON", region: "City of London, Ontario", state: "Ontario", country: "Canada", requiresKey: false, staticUrl: "http://www.londontransit.ca/gtfsfeed/google_transit.zip" },
  { id: "st-louis", name: "Metro Transit", agency: "Metro Transit (Bi-State Development)", city: "St. Louis, MO", region: "St. Louis Metropolitan Area, Missouri", state: "Missouri", country: "USA", requiresKey: false, staticUrl: "http://metrostlouis.org/Transit/google_transit.zip" },
  { id: "madison", name: "Metro Transit", agency: "Metro Transit (City of Madison)", city: "Madison, WI", region: "Madison Metropolitan Area, Wisconsin", state: "Wisconsin", country: "USA", requiresKey: false, staticUrl: "http://transitdata.cityofmadison.com/GTFS/mmt_gtfs.zip" },
  { id: "miway", name: "MiWay", agency: "MiWay", city: "Mississauga, ON", region: "City of Mississauga, Ontario", state: "Ontario", country: "Canada", requiresKey: false, staticUrl: "https://www.miapp.ca/GTFS/google_transit.zip" },
  { id: "milwaukee", name: "MCTS", agency: "Milwaukee County Transit System", city: "Milwaukee, WI", region: "Milwaukee Metropolitan Area, Wisconsin", state: "Wisconsin", country: "USA", requiresKey: false, staticUrl: "https://kamino.mcts.org/gtfs/google_transit.zip" },
  { id: "nashville", name: "WeGo", agency: "WeGo Public Transit", city: "Nashville, TN", region: "Nashville Metropolitan Area, Tennessee", state: "Tennessee", country: "USA", requiresKey: false, staticUrl: "https://www.wegotransit.com/googleexport/google_transit.zip" },
  { id: "providence", name: "RIPTA", agency: "Rhode Island Public Transit Authority", city: "Providence, RI", region: "Rhode Island", state: "Rhode Island", country: "USA", requiresKey: false },
  { id: "louisville", name: "TARC", agency: "Transit Authority of River City", city: "Louisville, KY", region: "Louisville Metropolitan Area, Kentucky", state: "Kentucky", country: "USA", requiresKey: false },
  { id: "york", name: "YRT", agency: "York Region Transit", city: "York Region, ON", region: "Regional Municipality of York, Ontario", state: "Ontario", country: "Canada", requiresKey: false },
  { id: "barrie", name: "Barrie Transit", agency: "Barrie Transit", city: "Barrie, ON", region: "City of Barrie, Ontario", state: "Ontario", country: "Canada", requiresKey: false },
  { id: "knoxville", name: "KAT", agency: "Knoxville Area Transit", city: "Knoxville, TN", region: "Knoxville Metropolitan Area, Tennessee", state: "Tennessee", country: "USA", requiresKey: false, staticUrl: "https://knoxville.syncromatics.com/gtfs" },
];

export function getScanPreset(id) {
  return SCAN_PRESETS.find((p) => p.id === id) || null;
}

// ---------------------------------------------------------------------------
// Numeric helpers matching Python semantics (statistics + round)
// ---------------------------------------------------------------------------

// Python round(): round-half-to-even on the binary value.
export function pyRound(value, digits) {
  const factor = 10 ** digits;
  const n = value * factor;
  const floor = Math.floor(n);
  const diff = n - floor;
  if (diff < 0.5) return floor / factor;
  if (diff > 0.5) return (floor + 1) / factor;
  return (floor % 2 === 0 ? floor : floor + 1) / factor;
}

export function pyMean(values) {
  return values.reduce((a, b) => a + b, 0) / values.length;
}

export function pyMedian(values) {
  const s = [...values].sort((a, b) => a - b);
  const mid = Math.floor(s.length / 2);
  if (s.length % 2 === 1) return s[mid];
  return (s[mid - 1] + s[mid]) / 2;
}

// Population stddev (statistics.pstdev).
export function pyPstdev(values) {
  const mean = pyMean(values);
  const varSum = values.reduce((a, x) => a + (x - mean) ** 2, 0);
  return Math.sqrt(varSum / values.length);
}

// Python datetime.now(timezone.utc).isoformat(), e.g. 2026-10-05T12:57:00.123000+00:00
export function pyIsoNow() {
  const d = new Date();
  const ms = String(d.getUTCMilliseconds()).padStart(3, "0");
  return d.toISOString().replace(/\.\d{3}Z$/, `.${ms}000+00:00`);
}

// ---------------------------------------------------------------------------
// GTFS-RT decoding (mirrors FeedFetcher.parse_*)
// ---------------------------------------------------------------------------

// protobufjs decodes with prototype defaults ("" / 0) for absent scalar
// fields, so wire presence is tested via own-property, like HasField().
function has(msg, field) {
  return msg != null && Object.hasOwn(msg, field);
}

// uint64/int64 may decode as Long, number, or string depending on field.
function toNum(v) {
  if (v == null) return null;
  if (typeof v === "number") return v;
  if (typeof v === "object" && typeof v.toNumber === "function") return v.toNumber();
  return Number(v);
}

const SCHEDULE_RELATIONSHIP = {
  0: "SCHEDULED",
  1: "ADDED",
  2: "UNSCHEDULED",
  3: "CANCELED",
  5: "REPLACEMENT",
  6: "DUPLICATED",
};

export function parseVehiclePositions(rawBytes) {
  const feed = FeedMessage.decode(rawBytes);
  const feedTimestamp = has(feed.header, "timestamp") ? toNum(feed.header.timestamp) : null;
  const vehicles = [];
  for (const entity of feed.entity || []) {
    const v = entity.vehicle;
    if (v == null) continue;
    const trip = v.trip;
    // Descriptor id wins. Feeds like NYCT subway omit the descriptor but
    // identify the run by entity.id and carry the trip id ghost correlation
    // keys on, so keep those; rows with neither identity stay skipped.
    const vehicleId =
      v.vehicle != null && v.vehicle.id
        ? String(v.vehicle.id)
        : trip != null && trip.tripId && entity.id
          ? String(entity.id)
          : null;
    if (!vehicleId) continue;
    const pos = v.position;
    vehicles.push({
      vehicle_id: vehicleId,
      trip_id: trip != null && trip.tripId ? trip.tripId : null,
      route_id: trip != null && trip.routeId ? trip.routeId : null,
      direction_id: trip != null && has(trip, "directionId") ? toNum(trip.directionId) : null,
      // Missing GPS is unknown (None), never (0.0, 0.0) off Ghana.
      latitude: pos != null ? pos.latitude : null,
      longitude: pos != null ? pos.longitude : null,
      bearing: pos != null && has(pos, "bearing") ? pos.bearing : null,
      speed: pos != null && has(pos, "speed") ? pos.speed : null,
      timestamp: has(v, "timestamp") ? toNum(v.timestamp) : null,
    });
  }
  return { vehicles, feedTimestamp };
}

export function parseTripUpdates(rawBytes) {
  const feed = FeedMessage.decode(rawBytes);
  const feedTimestamp = has(feed.header, "timestamp") ? toNum(feed.header.timestamp) : null;
  const trips = [];
  for (const entity of feed.entity || []) {
    const tu = entity.tripUpdate;
    if (tu == null) continue;
    const desc = tu.trip;
    // entity.id is a feed envelope id, not a trip id. Skip rather than
    // pollute the trip namespace used by ghost correlation.
    if (desc == null || !desc.tripId) continue;
    const relInt = has(desc, "scheduleRelationship") ? desc.scheduleRelationship : 0;
    const relName = SCHEDULE_RELATIONSHIP[relInt] || "SCHEDULED";
    const vehicleId = tu.vehicle != null && tu.vehicle.id ? String(tu.vehicle.id) : null;
    const delays = [];
    const stopUpdates = tu.stopTimeUpdate || [];
    for (const stu of stopUpdates) {
      if (stu.departure != null && has(stu.departure, "delay")) {
        delays.push(stu.departure.delay);
      } else if (stu.arrival != null && has(stu.arrival, "delay")) {
        delays.push(stu.arrival.delay);
      }
    }
    // Representative delay = median across per-stop delays.
    const repDelay = delays.length > 0 ? Math.trunc(pyRound(pyMedian(delays), 0)) : null;
    // Feeds without delay fields: keep absolute predicted times so the
    // static schedule join can derive delays (see static_schedule.js).
    const rtTimes = [];
    if (repDelay == null) {
      for (const stu of stopUpdates) {
        const ev = stu.departure != null ? stu.departure : stu.arrival;
        if (ev != null && has(ev, "time")) {
          rtTimes.push({
            seq: has(stu, "stopSequence") ? stu.stopSequence : null,
            stop_id: stu.stopId || null,
            time: toNum(ev.time),
          });
        }
      }
    }
    const isCanceled = relName === "CANCELED";
    trips.push({
      trip_id: String(desc.tripId),
      route_id: desc.routeId ? String(desc.routeId) : "UNKNOWN",
      direction_id: has(desc, "directionId") ? toNum(desc.directionId) : null,
      start_time: has(desc, "startTime") ? desc.startTime : null,
      start_date: has(desc, "startDate") ? desc.startDate : null,
      schedule_relationship: relName,
      vehicle_id: vehicleId,
      delay_seconds: repDelay,
      rt_times: rtTimes,
      stop_updates_count: stopUpdates.length,
      is_canceled: isCanceled,
      has_vehicle_assigned: vehicleId != null && vehicleId !== "",
      is_ghost: false,
      ghost_reason: null,
    });
  }
  return { trips, feedTimestamp };
}

// ---------------------------------------------------------------------------
// Analysis (mirrors ReliabilityAnalyzer)
// ---------------------------------------------------------------------------

export function identifyGhostTrips(trips, vehicles) {
  const activeTripIds = new Set(vehicles.map((v) => v.trip_id).filter((t) => t));
  const scheduledTripIds = new Set(trips.map((t) => t.trip_id).filter((t) => t));
  const tripsByVehicle = new Map();
  for (const v of vehicles) {
    if (v.vehicle_id) {
      if (!tripsByVehicle.has(v.vehicle_id)) tripsByVehicle.set(v.vehicle_id, []);
      tripsByVehicle.get(v.vehicle_id).push(v.trip_id);
    }
  }

  return trips.map((trip) => {
    const updated = { ...trip };
    if (updated.is_canceled) {
      updated.is_ghost = false;
      updated.ghost_reason = null;
    } else if (!updated.has_vehicle_assigned && !activeTripIds.has(updated.trip_id)) {
      updated.is_ghost = true;
      updated.ghost_reason = "No vehicle assigned and no active GPS broadcast";
    } else if (updated.vehicle_id && !activeTripIds.has(updated.trip_id)) {
      const assignedBroadcasts = tripsByVehicle.get(updated.vehicle_id) || [];
      if (assignedBroadcasts.length === 0) {
        updated.is_ghost = true;
        updated.ghost_reason = `Assigned vehicle ${updated.vehicle_id} is missing from active GPS transponder fleet`;
      } else if (
        assignedBroadcasts.some((bt) => bt == null || bt === "" || scheduledTripIds.has(bt))
      ) {
        updated.is_ghost = false;
        updated.ghost_reason = null;
      } else {
        updated.is_ghost = true;
        updated.ghost_reason =
          `Assigned vehicle ${updated.vehicle_id} is broadcasting ` +
          `off-schedule with no vehicle covering ${updated.trip_id}`;
      }
    } else {
      updated.is_ghost = false;
      updated.ghost_reason = null;
    }
    return updated;
  });
}

export function parseStartTimeSeconds(startTime) {
  try {
    const parts = String(startTime).trim().split(":");
    if (parts.length !== 3) return null;
    if (!parts.every((p) => /^-?\d+$/.test(p.trim()))) return null;
    const [h, m, s] = parts.map((p) => Number(p));
    if (!Number.isInteger(h) || !Number.isInteger(m) || !Number.isInteger(s)) return null;
    if (h < 0 || !(m >= 0 && m < 60) || !(s >= 0 && s < 60)) return null;
    return h * 3600 + m * 60 + s;
  } catch {
    return null;
  }
}

export function calculateHeadwayMetrics(trips) {
  const routeDelays = new Map();
  const routeStartTimes = new Map();
  const keyOf = (routeId, directionId) => `${routeId}␟${directionId}`;

  for (const trip of trips) {
    if (trip.is_canceled) continue;
    const key = keyOf(trip.route_id, trip.direction_id);
    if (trip.start_time) {
      const startSec = parseStartTimeSeconds(trip.start_time);
      if (startSec != null) {
        if (!routeStartTimes.has(key)) routeStartTimes.set(key, []);
        routeStartTimes.get(key).push(startSec);
      }
    }
    if (!trip.is_ghost && trip.delay_seconds != null) {
      if (!routeDelays.has(key)) routeDelays.set(key, { routeId: trip.route_id, directionId: trip.direction_id, delays: [] });
      routeDelays.get(key).delays.push(trip.delay_seconds);
    }
  }

  const metrics = [];
  for (const [key, group] of routeDelays) {
    const delays = group.delays;
    if (delays.length < 2) continue;
    const starts = (routeStartTimes.get(key) || []).sort((a, b) => a - b);
    const gaps = [];
    for (let i = 1; i < starts.length; i++) {
      if (starts[i] - starts[i - 1] > 0) gaps.push(starts[i] - starts[i - 1]);
    }
    if (gaps.length === 0) continue;
    const scheduledHeadwaySec = pyMedian(gaps);
    const scheduledHeadwayMin = pyRound(scheduledHeadwaySec / 60.0, 1);
    const delayStd = pyPstdev(delays);
    const observedHeadwayMin = scheduledHeadwayMin;
    const headwayVar = delayStd ** 2;
    const ewtMin = pyRound(headwayVar / (2.0 * scheduledHeadwaySec) / 60.0, 2);
    const regularityScore = Math.max(0.0, pyRound(100.0 * (1.0 - delayStd / scheduledHeadwaySec), 1));
    metrics.push({
      route_id: group.routeId,
      direction_id: group.directionId,
      scheduled_headway_min: scheduledHeadwayMin,
      observed_headway_min: observedHeadwayMin,
      excess_wait_time_min: ewtMin,
      headway_regularity_score: Math.min(100.0, regularityScore),
    });
  }
  metrics.sort((a, b) => (b.excess_wait_time_min || 0.0) - (a.excess_wait_time_min || 0.0));
  return metrics;
}

export function analyzeReliability(vehicles, trips, labels, options = {}) {
  const {
    feedTimestamp = null,
    scanTime = null,
    thresholds = DEFAULT_THRESHOLDS,
  } = options;
  const nowIso = scanTime || pyIsoNow();
  const { earlySec, onTimeSec, minorDelaySec } = thresholds;

  const annotated = identifyGhostTrips(trips, vehicles);
  const totalScheduled = annotated.length;
  const totalVehicles = vehicles.length;
  const ghostTrips = annotated.filter((t) => t.is_ghost);
  const totalGhosts = ghostTrips.length;

  const ghostRate = totalScheduled > 0 ? pyRound((totalGhosts / totalScheduled) * 100, 2) : 0.0;
  const totalCanceled = annotated.filter((t) => t.is_canceled).length;
  const trackedCount = totalScheduled - totalGhosts - totalCanceled;
  const trackingRate = totalScheduled > 0 ? pyRound((trackedCount / totalScheduled) * 100, 2) : 0.0;

  const breakdown = { early: 0, on_time: 0, minor_delay: 0, severe_delay: 0, ghost: totalGhosts, canceled: totalCanceled };
  const validDelays = [];
  const routeMap = new Map();

  const activeVehicleIds = new Set(vehicles.map((v) => v.vehicle_id).filter((v) => v));
  const tripRouteById = new Map();
  for (const t of annotated) {
    if (t.trip_id) tripRouteById.set(t.trip_id, t.route_id);
  }
  const routeVehicleIds = new Map();
  const addRouteVehicle = (route, vid) => {
    if (!routeVehicleIds.has(route)) routeVehicleIds.set(route, new Set());
    routeVehicleIds.get(route).add(vid);
  };
  for (const v of vehicles) {
    if (!v.vehicle_id) continue;
    const vRoute = v.route_id || tripRouteById.get(v.trip_id);
    if (vRoute) addRouteVehicle(vRoute, v.vehicle_id);
  }

  for (const trip of annotated) {
    const rId = trip.route_id || "UNKNOWN";
    if (!routeMap.has(rId)) {
      routeMap.set(rId, {
        route_id: rId, total_trips: 0, ghost_trips: 0, canceled_trips: 0,
        on_time_trips: 0, early_trips: 0, delayed_trips: 0, delays: [],
      });
    }
    const rm = routeMap.get(rId);
    rm.total_trips += 1;

    if (trip.is_canceled) {
      rm.canceled_trips += 1;
    } else if (trip.is_ghost) {
      rm.ghost_trips += 1;
    } else {
      if (trip.vehicle_id && activeVehicleIds.has(trip.vehicle_id)) {
        addRouteVehicle(rId, trip.vehicle_id);
      }
      if (trip.delay_seconds != null) {
        validDelays.push(trip.delay_seconds);
        rm.delays.push(trip.delay_seconds);
        if (trip.delay_seconds < earlySec) {
          breakdown.early += 1;
          rm.early_trips += 1;
        } else if (trip.delay_seconds <= onTimeSec) {
          breakdown.on_time += 1;
          rm.on_time_trips += 1;
        } else if (trip.delay_seconds <= minorDelaySec) {
          breakdown.minor_delay += 1;
          rm.delayed_trips += 1;
        } else {
          breakdown.severe_delay += 1;
          rm.delayed_trips += 1;
        }
      }
    }
  }

  const meanDelay = validDelays.length > 0 ? pyRound(pyMean(validDelays), 1) : 0.0;
  const medianDelay = validDelays.length > 0 ? pyRound(pyMedian(validDelays), 1) : 0.0;

  const totalDelayTracked = breakdown.early + breakdown.on_time + breakdown.minor_delay + breakdown.severe_delay;
  const overallOnTimePct = totalDelayTracked > 0 ? pyRound((breakdown.on_time / totalDelayTracked) * 100, 2) : 0.0;

  const routeMetrics = [];
  for (const [rId, stats] of routeMap) {
    const tot = stats.total_trips;
    const gRate = tot > 0 ? pyRound((stats.ghost_trips / tot) * 100, 2) : 0.0;
    const dList = stats.delays;
    const avgD = dList.length > 0 ? pyRound(pyMean(dList), 1) : 0.0;
    const maxD = dList.length > 0 ? Math.max(...dList) : 0;
    const delayReported = stats.on_time_trips + stats.delayed_trips + stats.early_trips;
    const otRate = delayReported > 0 ? pyRound((stats.on_time_trips / delayReported) * 100, 2) : 0.0;
    routeMetrics.push({
      route_id: rId,
      route_name: `Route ${rId}`,
      total_trips: tot,
      tracked_vehicles: (routeVehicleIds.get(rId) || new Set()).size,
      ghost_trips: stats.ghost_trips,
      canceled_trips: stats.canceled_trips,
      on_time_trips: stats.on_time_trips,
      delayed_trips: stats.delayed_trips,
      ghost_rate_pct: gRate,
      on_time_pct: otRate,
      avg_delay_sec: avgD,
      max_delay_sec: maxD,
    });
  }

  const worstRoutes = routeMetrics
    .filter((r) => r.total_trips >= 2)
    .sort((a, b) => (b.ghost_rate_pct - a.ghost_rate_pct) || (b.ghost_trips - a.ghost_trips))
    .slice(0, 10);
  const mostDelayed = routeMetrics
    .filter((r) => r.avg_delay_sec > 0)
    .sort((a, b) => b.avg_delay_sec - a.avg_delay_sec)
    .slice(0, 10);

  const sampleGhosts = ghostTrips.slice(0, 15).map((g) => ({
    trip_id: g.trip_id,
    route_id: g.route_id,
    start_time: g.start_time || "N/A",
    start_date: g.start_date || "N/A",
    status: g.schedule_relationship,
    reason: g.ghost_reason,
  }));

  const headwayMetrics = calculateHeadwayMetrics(annotated).slice(0, 10);

  // Key order matches ReliabilitySnapshot.model_dump for diff-friendly JSON.
  return {
    scan_time: nowIso,
    feed_timestamp: feedTimestamp,
    agency: labels.agency,
    city: labels.city,
    transit_system: labels.transitSystem,
    region: labels.region,
    state: labels.state,
    country: labels.country,
    source: "live",
    total_scheduled_trips: totalScheduled,
    total_tracked_vehicles: totalVehicles,
    total_ghost_trips: totalGhosts,
    ghost_bus_rate_pct: ghostRate,
    vehicle_tracking_rate_pct: trackingRate,
    overall_on_time_pct: overallOnTimePct,
    delay_distribution: breakdown,
    mean_delay_sec: meanDelay,
    median_delay_sec: medianDelay,
    worst_routes_by_ghost: worstRoutes,
    most_delayed_routes: mostDelayed,
    route_metrics: routeMetrics,
    sample_ghost_trips: sampleGhosts,
    headway_metrics: headwayMetrics,
  };
}

// ---------------------------------------------------------------------------
// Fetch + scan + persist
// ---------------------------------------------------------------------------

async function fetchFeedBytes(url, headers = {}) {
  const res = await fetch(url, {
    headers: { "User-Agent": USER_AGENT, ...headers },
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} fetching ${url}`);
  return new Uint8Array(await res.arrayBuffer());
}

function presetLabels(preset) {
  return {
    agency: preset.agency,
    city: preset.city,
    transitSystem: preset.name,
    region: preset.region,
    state: preset.state,
    country: preset.country,
  };
}

function resolveThresholds(env) {
  const num = (v, d) => {
    const n = Number.parseInt(v ?? "", 10);
    return Number.isFinite(n) ? n : d;
  };
  return {
    earlySec: num(env?.GBT_EARLY_SEC, DEFAULT_THRESHOLDS.earlySec),
    onTimeSec: num(env?.GBT_ON_TIME_SEC, DEFAULT_THRESHOLDS.onTimeSec),
    minorDelaySec: num(env?.GBT_MINOR_DELAY_SEC, DEFAULT_THRESHOLDS.minorDelaySec),
  };
}

// Scan one market. Never throws: returns { status, snapshot?, error? }.
export async function scanMarket(preset, env = {}) {
  const feeds = CITY_FEED_URLS[preset.id];
  if (!feeds) return { status: "failed", marketId: preset.id, error: `no feed URLs for ${preset.id}` };
  const apiKey = preset.keyEnvVar ? env[preset.keyEnvVar] : null;
  if (preset.requiresKey && !apiKey) {
    return { status: "skipped", marketId: preset.id, error: `set ${preset.keyEnvVar} to scan it` };
  }
  let vpUrl = feeds.vp;
  let tuUrl = feeds.tu;
  const headers = {};
  if (preset.requiresKey && apiKey) {
    if (preset.keyParam) {
      const sep1 = vpUrl.includes("?") ? "&" : "?";
      const sep2 = tuUrl.includes("?") ? "&" : "?";
      vpUrl = `${vpUrl}${sep1}${preset.keyParam}=${encodeURIComponent(apiKey)}`;
      tuUrl = `${tuUrl}${sep2}${preset.keyParam}=${encodeURIComponent(apiKey)}`;
    } else if (preset.keyHeader) {
      headers[preset.keyHeader] = apiKey;
    }
  }
  try {
    const [vpBytes, tuBytes] = await Promise.all([
      fetchFeedBytes(vpUrl, headers),
      fetchFeedBytes(tuUrl, headers),
    ]);
    const { vehicles, feedTimestamp: vTs } = parseVehiclePositions(vpBytes);
    const { trips, feedTimestamp: tTs } = parseTripUpdates(tuBytes);
    if (preset.staticUrl) {
      const wanted = new Set(trips.map((t) => t.trip_id).filter(Boolean));
      const schedule = await getStaticSchedule(env, preset.id, preset.staticUrl, wanted);
      if (schedule) applyDerivedDelays(trips, schedule, tTs || vTs);
    }
    for (const t of trips) delete t.rt_times;
    const snapshot = analyzeReliability(vehicles, trips, presetLabels(preset), {
      feedTimestamp: tTs || vTs,
      thresholds: resolveThresholds(env),
    });
    return { status: "ok", marketId: preset.id, snapshot };
  } catch (err) {
    return { status: "failed", marketId: preset.id, error: String((err && err.message) || err) };
  }
}

// Scan every market (or a subset). Markets run concurrently; one market's
// failure never blocks the others.
export async function scanAllMarkets(env = {}, onlyIds = null) {
  const presets = onlyIds
    ? SCAN_PRESETS.filter((p) => onlyIds.includes(p.id))
    : SCAN_PRESETS;
  const results = await Promise.all(presets.map((p) => scanMarket(p, env)));
  return results;
}

export function snapshotR2Keys(marketId, scanTime) {
  const safeTime = String(scanTime).replace(/[:]/g, "-");
  return {
    versioned: `snapshots/${marketId}/${safeTime}.json`,
    latest: `snapshots/${marketId}/latest.json`,
  };
}

// Persist one snapshot: versioned + latest JSON in R2, summary row in D1.
// Missing bindings are skipped gracefully (local dev without --remote).
export async function persistSnapshot(env, marketId, snapshot) {
  const stored = { r2: false, d1: false };
  if (env?.SNAPSHOT_BUCKET && snapshot?.scan_time) {
    try {
      const body = JSON.stringify(snapshot);
      const keys = snapshotR2Keys(marketId, snapshot.scan_time);
      const meta = { httpMetadata: { contentType: "application/json; charset=utf-8" } };
      await Promise.all([
        env.SNAPSHOT_BUCKET.put(keys.versioned, body, meta),
        env.SNAPSHOT_BUCKET.put(keys.latest, body, meta),
      ]);
      stored.r2 = true;
    } catch {
      // Next tick retries.
    }
  }
  if (env?.HISTORY_DB && snapshot?.scan_time) {
    try {
      await env.HISTORY_DB.prepare(
        "INSERT OR IGNORE INTO scans (market_id, scan_time, ghost_bus_rate_pct, " +
        "overall_on_time_pct, total_scheduled_trips, total_tracked_vehicles, " +
        "total_ghost_trips, mean_delay_sec, agency, city, transit_system, source) " +
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
      ).bind(
        marketId, snapshot.scan_time, snapshot.ghost_bus_rate_pct, snapshot.overall_on_time_pct,
        snapshot.total_scheduled_trips, snapshot.total_tracked_vehicles, snapshot.total_ghost_trips,
        snapshot.mean_delay_sec ?? null, snapshot.agency ?? null, snapshot.city ?? null,
        snapshot.transit_system ?? null, snapshot.source ?? "live"
      ).run();
      stored.d1 = true;
    } catch {
      // Next tick retries.
    }
  }
  return stored;
}
