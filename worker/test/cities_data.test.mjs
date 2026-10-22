import { test } from "node:test";
import assert from "node:assert/strict";
import { CITY_PRESETS, CITY_FEED_URLS, lookupCityKey } from "../src/cities_data.js";
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
