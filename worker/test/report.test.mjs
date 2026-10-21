import { readFileSync } from "node:fs";
import { test } from "node:test";
import assert from "node:assert/strict";
import { generateMarkdown, pyFloatStr, pyRound } from "../src/report.js";

const root = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, root), "utf8");

test("pyRound matches Python round() on binary edge cases", () => {
  const cases = [
    [11.35, 1, 11.3],
    [11.25, 1, 11.2],
    [2.5, 0, 2],
    [3.5, 0, 4],
    [-2.5, 0, -2],
    [0.125, 2, 0.12],
    [0.375, 2, 0.38],
    [99.95, 1, 100],
    [681 / 60, 1, 11.3],
  ];
  for (const [v, d, expected] of cases) assert.equal(pyRound(v, d), expected, `${v},${d}`);
});

test("pyFloatStr matches Python str(float)", () => {
  assert.equal(pyFloatStr(40.0), "40.0");
  assert.equal(pyFloatStr(12.34), "12.34");
  assert.equal(pyFloatStr(0), "0.0");
  assert.equal(pyFloatStr(-5.0), "-5.0");
});

// The committed RELIABILITY-*.md files were rendered by src/reporter.py from
// the committed data files; the JS port must reproduce them byte-for-byte.
test("generateMarkdown reproduces committed reports from committed data", () => {
  const markets = ["twin-cities", "atlanta", "boston", "denver", "philly", "seattle", "toronto"];
  for (const m of markets) {
    const latest = JSON.parse(read(`data/latest/${m}.json`));
    const history = JSON.parse(read(`data/history/${m}.json`));
    assert.equal(generateMarkdown(latest, history), read(`RELIABILITY-${m}.md`), m);
  }
  const latest = JSON.parse(read("data/latest.json"));
  const history = JSON.parse(read("data/history.json"));
  assert.equal(generateMarkdown(latest, history), read("RELIABILITY.md"), "root");
});
