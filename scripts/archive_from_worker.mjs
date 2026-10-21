#!/usr/bin/env node
/**
 * One-shot local backfill of the git-scraping archive.
 *
 * Fetches live snapshots from the deployed Worker and commits them to GitHub
 * using the exact code the Worker's daily cron runs (worker/src/github_archive.js).
 * This is the manual replacement for the retired archive.yml workflow.
 *
 * Usage:
 *   GITHUB_TOKEN=$(gh auth token) node scripts/archive_from_worker.mjs
 *   ARCHIVE_DRY_RUN=1 node scripts/archive_from_worker.mjs   # no commit
 */
import { buildArchiveFiles, commitFilesToGitHub } from "../worker/src/github_archive.js";

const WORKER_URL = process.env.WORKER_URL || "https://ghost-bus-tracker.a-8c6.workers.dev";

async function getJson(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`GET ${url} -> ${res.status}`);
  return res.json();
}

const { markets: presets } = await getJson(`${WORKER_URL}/api/markets`);
const markets = [];
for (const p of presets) {
  const latest = await getJson(`${WORKER_URL}/api/latest?city=${p.id}`);
  if (!latest.live) {
    console.log(`skip ${p.id}: no live Worker snapshot`);
    continue;
  }
  const history = await getJson(`${WORKER_URL}/api/history?city=${p.id}`);
  markets.push({ id: p.id, latest, history });
  console.log(`ok   ${p.id}: scan_time=${latest.scan_time} history=${history.length}`);
}

const files = buildArchiveFiles(markets);
console.log(`\n${Object.keys(files).length} files:`);
for (const [path, content] of Object.entries(files)) {
  console.log(`  ${path} (${Buffer.byteLength(content)} bytes)`);
}

if (process.env.ARCHIVE_DRY_RUN) {
  console.log("\nARCHIVE_DRY_RUN set; not committing.");
  process.exit(0);
}

const scanTime = new Date().toISOString().replace(/\.\d{3}Z$/, "Z");
const result = await commitFilesToGitHub({
  token: process.env.GITHUB_TOKEN,
  files,
  message: `Daily Worker snapshot archive: ${scanTime} [skip ci]`,
});
console.log("\narchive result:", JSON.stringify(result));
