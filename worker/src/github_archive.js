/**
 * Worker -> GitHub git-scraping archive.
 *
 * Replaces the old GitHub Actions scrapers (track.yml / archive.yml): the
 * Worker itself commits fresh snapshots to the repo via the GitHub Git Data
 * API, one atomic commit per archive run. Requires the GITHUB_TOKEN secret
 * (fine-grained PAT with Contents read/write on this repo).
 */

import { generateMarkdown } from "./report.js";

export const HISTORY_CAP = 500;
export const DEFAULT_REPO = "aminamos/ghost-bus-tracker";
export const DEFAULT_BRANCH = "main";

// Worker read-time decorations that must not land in the raw snapshot files.
function stripDecorations(latest) {
  const { live, stale, coverage_details, ...snapshot } = latest;
  return snapshot;
}

/**
 * Build the { path: content } file map for one archive commit from live
 * market data: [{ id, latest, history }]. Twin Cities also mirrors to the
 * legacy root files, matching the former archive.yml behavior.
 */
export function buildArchiveFiles(markets) {
  const files = {};
  for (const { id, latest, history } of markets) {
    if (!latest) continue;
    const snapshot = stripDecorations(latest);
    const capped = (history || []).slice(-HISTORY_CAP);
    const latestJson = JSON.stringify(snapshot, null, 2);
    const historyJson = JSON.stringify(capped, null, 2);
    const report = generateMarkdown(snapshot, capped);
    files[`data/latest/${id}.json`] = latestJson;
    files[`data/history/${id}.json`] = historyJson;
    files[`RELIABILITY-${id}.md`] = report;
    if (id === "twin-cities") {
      files["data/latest.json"] = latestJson;
      files["data/history.json"] = historyJson;
      files["RELIABILITY.md"] = report;
    }
  }
  return files;
}

async function gh(fetchImpl, token, method, path, body = null) {
  const res = await fetchImpl(`https://api.github.com${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "GhostBusTracker-Worker-Archive/0.1.0",
      ...(body ? { "Content-Type": "application/json" } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(`GitHub ${method} ${path} -> ${res.status}: ${text.slice(0, 300)}`);
  }
  return res.json();
}

/**
 * Commit `files` ({ path: utf8 content }) to the repo in a single commit.
 * No-ops (committed: false) when the resulting tree matches HEAD, and
 * retries once if the branch moved underneath us.
 */
export async function commitFilesToGitHub({
  token,
  repo = DEFAULT_REPO,
  branch = DEFAULT_BRANCH,
  files,
  message,
  fetchImpl = fetch,
}) {
  if (!token) throw new Error("GITHUB_TOKEN is not configured");
  const paths = Object.keys(files);
  if (!paths.length) return { committed: false, reason: "no files", files: 0 };

  const blobShas = {};
  await Promise.all(
    paths.map(async (path) => {
      const blob = await gh(fetchImpl, token, "POST", `/repos/${repo}/git/blobs`, {
        content: files[path],
        encoding: "utf-8",
      });
      blobShas[path] = blob.sha;
    }),
  );

  for (let attempt = 1; attempt <= 2; attempt++) {
    const ref = await gh(fetchImpl, token, "GET", `/repos/${repo}/git/ref/heads/${branch}`);
    const headSha = ref.object.sha;
    const headCommit = await gh(fetchImpl, token, "GET", `/repos/${repo}/git/commits/${headSha}`);
    const tree = await gh(fetchImpl, token, "POST", `/repos/${repo}/git/trees`, {
      base_tree: headCommit.tree.sha,
      tree: paths.map((path) => ({ path, mode: "100644", type: "blob", sha: blobShas[path] })),
    });
    if (tree.sha === headCommit.tree.sha) {
      return { committed: false, reason: "unchanged", files: paths.length };
    }
    const commit = await gh(fetchImpl, token, "POST", `/repos/${repo}/git/commits`, {
      message,
      tree: tree.sha,
      parents: [headSha],
    });
    try {
      await gh(fetchImpl, token, "PATCH", `/repos/${repo}/git/refs/heads/${branch}`, {
        sha: commit.sha,
        force: false,
      });
      return { committed: true, sha: commit.sha, files: paths.length };
    } catch (e) {
      if (attempt === 2) throw e;
      // Branch moved since we read it (422); rebuild on the new HEAD.
    }
  }
  throw new Error("unreachable");
}
