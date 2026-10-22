import { test } from "node:test";
import assert from "node:assert/strict";
import { zipSync, strToU8 } from "fflate";
import {
  buildScheduleFromZip,
  applyDerivedDelays,
  serviceDayStartEpoch,
} from "../src/static_schedule.js";

function makeZip() {
  return zipSync({
    "agency.txt": strToU8(
      "agency_id,agency_name,agency_url,agency_timezone\nA,Test,http://x,America/New_York\n",
    ),
    "stop_times.txt": strToU8(
      [
        "trip_id,arrival_time,departure_time,stop_id,stop_sequence",
        "T1,08:00:00,08:00:00,S1,1",
        "T1,08:10:00,08:10:00,S2,2",
        "T2,25:10:00,25:10:00,S9,1", // after-midnight trip (25:10 = 01:10 next day)
        "OTHER,09:00:00,09:00:00,S1,1",
      ].join("\n") + "\n",
    ),
  });
}

test("buildScheduleFromZip keeps only wanted trips and reads timezone", () => {
  const { tz, trips } = buildScheduleFromZip(makeZip(), new Set(["T1", "T2"]));
  assert.equal(tz, "America/New_York");
  assert.equal(trips.size, 2);
  assert.equal(trips.get("T1").bySeq.get(2), 29400);
  assert.equal(trips.get("T1").byStop.get("S1"), 28800);
});

test("static trip ids join RT ids by suffix after first underscore (NYCT)", () => {
  const zip = zipSync({
    "agency.txt": strToU8("agency_id,agency_name,agency_url,agency_timezone\nA,Test,http://x,America/New_York\n"),
    "stop_times.txt": strToU8(
      "trip_id,arrival_time,departure_time,stop_id,stop_sequence\n" +
      "ASP26GEN-1038-Sunday-00_000600_1..S03R,00:06:00,00:06:00,101S,1\n",
    ),
  });
  const { trips } = buildScheduleFromZip(zip, new Set(["000600_1..S03R"]));
  assert.equal(trips.size, 1);
  assert.equal(trips.get("000600_1..S03R").bySeq.get(1), 360);
});

test("derived delay: median of RT time minus scheduled, service-date anchored", () => {
  const { tz, trips: sched } = buildScheduleFromZip(makeZip(), new Set(["T1", "T2"]));
  const schedule = { tz, trips: sched };
  const epoch0 = serviceDayStartEpoch(tz, "20261022");
  // 2026-10-22 is EDT (UTC-4): local midnight = 04:00Z.
  assert.equal(epoch0, Date.UTC(2026, 9, 22, 4, 0, 0) / 1000);
  const trips = [
    {
      trip_id: "T1", start_date: "20261022", delay_seconds: null,
      rt_times: [
        { seq: 1, stop_id: "S1", time: epoch0 + 28800 + 300 }, // +5m
        { seq: 2, stop_id: "S2", time: epoch0 + 29400 + 60 }, // +1m -> median +3m
      ],
    },
    {
      trip_id: "T2", start_date: "20261022", delay_seconds: null,
      rt_times: [{ seq: 1, stop_id: "S9", time: epoch0 + 90600 - 120 }], // 2m early, >24h schedule
    },
    {
      trip_id: "T1", start_date: "20261022", delay_seconds: 42, // feed delay wins
      rt_times: [{ seq: 1, stop_id: "S1", time: epoch0 + 28800 + 9999 }],
    },
  ];
  applyDerivedDelays(trips, schedule, null);
  assert.equal(trips[0].delay_seconds, 180);
  assert.equal(trips[0].delay_derived, true);
  assert.equal(trips[1].delay_seconds, -120);
  assert.equal(trips[2].delay_seconds, 42);
});

test("derived delay joins by stop_id when sequence misses, ignores absurd values", () => {
  const { tz, trips: sched } = buildScheduleFromZip(makeZip(), new Set(["T1"]));
  const epoch0 = serviceDayStartEpoch(tz, "20261022");
  const trips = [{
    trip_id: "T1", start_date: "20261022", delay_seconds: null,
    rt_times: [
      { seq: 99, stop_id: "S2", time: epoch0 + 29400 + 600 },
      { seq: 1, stop_id: "S1", time: epoch0 + 28800 + 99999 }, // >6h off: discarded
    ],
  }];
  applyDerivedDelays(trips, { tz, trips: sched }, null);
  assert.equal(trips[0].delay_seconds, 600);
});
