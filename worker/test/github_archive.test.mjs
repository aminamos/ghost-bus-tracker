import { test } from "node:test";
import assert from "node:assert/strict";
import { buildArchiveFiles, pyJsonStringify } from "../src/github_archive.js";

test("pyJsonStringify matches Python float and ascii conventions", () => {
  const entry = {
    scan_time: "2026-10-21T22:30:36.612000+00:00",
    ghost_bus_rate_pct: 5.39,
    overall_on_time_pct: 0,
    total_scheduled_trips: 482,
    mean_delay_sec: 0,
    city: "Minneapolis–Saint Paul, MN",
  };
  // json.dump(..., indent=2): floats keep .0, non-ASCII escaped.
  assert.equal(
    pyJsonStringify([entry], true),
    '[\n  {\n    "scan_time": "2026-10-21T22:30:36.612000+00:00",\n    "ghost_bus_rate_pct": 5.39,\n    "overall_on_time_pct": 0.0,\n    "total_scheduled_trips": 482,\n    "mean_delay_sec": 0.0,\n    "city": "Minneapolis\\u2013Saint Paul, MN"\n  }\n]',
  );
  // model_dump_json(indent=2): raw UTF-8.
  assert.ok(pyJsonStringify(entry, false).includes("Minneapolis–Saint Paul"));
});

test("buildArchiveFiles strips decorations, caps history, mirrors twin-cities", () => {
  const latest = {
    scan_time: "2026-10-21T22:30:36.045000+00:00",
    agency: "Metro Transit (Twin Cities)",
    city: "Minneapolis–Saint Paul, MN",
    transit_system: "Metro Transit",
    region: "Twin Cities Metropolitan Area, Minnesota",
    source: "live",
    total_scheduled_trips: 10,
    total_tracked_vehicles: 8,
    total_ghost_trips: 2,
    ghost_bus_rate_pct: 20,
    overall_on_time_pct: 50,
    mean_delay_sec: 0,
    median_delay_sec: 0,
    delay_distribution: { early: 0, on_time: 8, minor_delay: 0, severe_delay: 0, ghost: 2, canceled: 0 },
    worst_routes_by_ghost: [],
    most_delayed_routes: [],
    headway_metrics: [],
    sample_ghost_trips: [],
    live: true,
    stale: false,
    coverage_details: { x: 1 },
  };
  const history = Array.from({ length: 600 }, (_, i) => ({
    scan_time: `2026-10-21T00:${String(i % 60).padStart(2, "0")}:00+00:00`,
    ghost_bus_rate_pct: 1,
    overall_on_time_pct: 2,
    total_scheduled_trips: 3,
    total_tracked_vehicles: 4,
    total_ghost_trips: 5,
    mean_delay_sec: 6,
  }));
  const files = buildArchiveFiles([{ id: "twin-cities", latest, history }]);
  assert.deepEqual(Object.keys(files).sort(), [
    "RELIABILITY-twin-cities.md",
    "RELIABILITY.md",
    "data/history.json",
    "data/history/twin-cities.json",
    "data/latest.json",
    "data/latest/twin-cities.json",
  ]);
  const saved = JSON.parse(files["data/latest.json"]);
  assert.equal("live" in saved, false);
  assert.equal("stale" in saved, false);
  assert.equal("coverage_details" in saved, false);
  assert.equal(JSON.parse(files["data/history.json"]).length, 500);
  assert.ok(files["data/latest.json"].includes('"ghost_bus_rate_pct": 20.0'));
});
