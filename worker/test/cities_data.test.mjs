import { test } from "node:test";
import assert from "node:assert/strict";
import { CITY_PRESETS, CITY_FEED_URLS, getAllCitiesData, lookupCityKey } from "../src/cities_data.js";
import { SCAN_PRESETS } from "../src/scan.js";

test("every market resolves across presets, scan presets, and feed URLs", () => {
  const presetIds = new Set(CITY_PRESETS.map((p) => p.id));
  assert.equal(presetIds.size, CITY_PRESETS.length, "duplicate preset ids");
  for (const p of CITY_PRESETS) {
    assert.ok(CITY_FEED_URLS[p.id], `missing feed URLs for ${p.id}`);
    assert.equal(lookupCityKey(p.id), p.id, `lookupCityKey rejects ${p.id}`);
  }
  for (const p of SCAN_PRESETS) {
    assert.ok(presetIds.has(p.id), `scan preset ${p.id} has no city preset`);
  }
  assert.ok(CITY_PRESETS.length >= 43);
});

test("new markets get a synthesized entry with coverage details once live", () => {
  const cities = getAllCitiesData({
    austin: {
      latest: {
        scan_time: "2026-10-22T19:00:00+00:00", agency: "Capital Metropolitan Transportation Authority",
        city: "Austin, TX", transit_system: "CapMetro", region: "Austin–Round Rock Metropolitan Area, Texas",
        total_scheduled_trips: 100, total_tracked_vehicles: 50, total_ghost_trips: 10,
        ghost_bus_rate_pct: 10, vehicle_tracking_rate_pct: 90, overall_on_time_pct: 55,
        delay_distribution: { early: 0, on_time: 10, minor_delay: 0, severe_delay: 0, ghost: 10, canceled: 0 },
        worst_routes_by_ghost: [], most_delayed_routes: [], route_metrics: [], sample_ghost_trips: [], headway_metrics: [],
      },
      history: [], live: true,
    },
  });
  assert.ok(cities.austin, "austin entry synthesized");
  assert.equal(cities.austin.latest.coverage_details.modes, "Bus & Commuter Rail");
  assert.match(cities.austin.latest.coverage_details.jurisdiction, /Austin/);
  // Preset-derived coverage also shows on the pre-scan placeholder entry.
  assert.equal(cities.edmonton.latest.coverage_details.modes, "Bus & Light Rail");
});
