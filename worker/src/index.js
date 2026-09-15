/**
 * Cloudflare Worker for Ghost Bus Tracker
 * Automated public transit reliability and ghost bus monitoring
 */

import { DEFAULT_LATEST, DEFAULT_HISTORY } from "./snapshot_data.js";

const DATA_BASE =
  "https://raw.githubusercontent.com/aminamos/ghost-bus-tracker/main/data";
const UPSTREAM_CACHE_TTL = 300; // git-scraping workflow commits every 30 min

// Serve the freshest committed snapshot from the repo, cached at the edge.
// Falls back to the bundled snapshot (deploy-time copy) if GitHub is down.
async function fetchSnapshot(file, fallback) {
  try {
    const res = await fetch(`${DATA_BASE}/${file}`, {
      cf: { cacheEverything: true, cacheTtl: UPSTREAM_CACHE_TTL },
      headers: { "User-Agent": "GhostBusTracker-Worker/0.1.0" },
    });
    if (!res.ok) throw new Error(`upstream ${res.status}`);
    return await res.json();
  } catch {
    return fallback;
  }
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data, null, 2), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    },
  });
}

function renderHtml(latest, history) {
  const isHealthy = latest.ghost_bus_rate_pct < 5.0;
  const isElevated = latest.ghost_bus_rate_pct < 15.0;
  const statusBadge = isHealthy
    ? `<span class="badge badge-success">🟢 Healthy (&lt;5% Ghosts)</span>`
    : isElevated
    ? `<span class="badge badge-warning">🟡 Elevated Ghosts (${latest.ghost_bus_rate_pct}%)</span>`
    : `<span class="badge badge-danger">🔴 Critical Ghosting (${latest.ghost_bus_rate_pct}%)</span>`;

  const dist = latest.delay_distribution || {};
  const totalTrips = latest.total_scheduled_trips || 1;
  const pct = (n) => ((n / totalTrips) * 100).toFixed(1);

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ghost Bus Tracker | ${latest.agency}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090d16;
      --card: #111827;
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover: rgba(255, 255, 255, 0.12);
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --primary: #3b82f6;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --ghost: #ec4899;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.5;
      padding: 2rem 1rem;
      min-height: 100vh;
    }
    .container { max-width: 1200px; margin: 0 auto; }
    header {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--card-border);
      margin-bottom: 2rem;
    }
    .brand { display: flex; align-items: center; gap: 1rem; }
    .brand-icon {
      font-size: 2.25rem;
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(236, 72, 153, 0.2));
      border: 1px solid rgba(255, 255, 255, 0.1);
      width: 60px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 16px;
    }
    h1 { font-size: 1.75rem; font-weight: 800; letter-spacing: -0.025em; }
    .subtitle { color: var(--text-muted); font-size: 0.925rem; margin-top: 0.25rem; }
    .header-actions { display: flex; align-items: center; gap: 0.75rem; }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.45rem 0.9rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid transparent;
    }
    .badge-success { background: rgba(16, 185, 129, 0.15); color: #34d399; border-color: rgba(16, 185, 129, 0.3); }
    .badge-warning { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border-color: rgba(245, 158, 11, 0.3); }
    .badge-danger { background: rgba(239, 68, 68, 0.15); color: #f87171; border-color: rgba(239, 68, 68, 0.3); }
    .btn {
      background: var(--card);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 0.5rem 1rem;
      border-radius: 10px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
      text-decoration: none;
    }
    .btn:hover { background: var(--card-hover); border-color: rgba(255, 255, 255, 0.2); }
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }
    .kpi-card {
      background: var(--card);
      border: 1px solid var(--card-border);
      padding: 1.25rem;
      border-radius: 16px;
      position: relative;
      overflow: hidden;
    }
    .kpi-title { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); font-weight: 600; margin-bottom: 0.5rem; }
    .kpi-value { font-size: 2rem; font-weight: 800; font-family: var(--font-mono); }
    .kpi-desc { font-size: 0.8rem; color: var(--text-muted); margin-top: 0.35rem; }
    .text-ghost { color: var(--ghost); }
    .text-success { color: var(--success); }
    .text-warning { color: var(--warning); }
    .text-primary { color: var(--primary); }

    .card {
      background: var(--card);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.5rem;
      margin-bottom: 2rem;
    }
    .card-title { font-size: 1.15rem; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }
    
    /* Distribution Bar */
    .dist-bar {
      display: flex;
      height: 24px;
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 1rem;
      background: rgba(255, 255, 255, 0.05);
    }
    .dist-seg { height: 100%; transition: width 0.3s ease; }
    .bg-ontime { background: #10b981; }
    .bg-early { background: #3b82f6; }
    .bg-minor { background: #f59e0b; }
    .bg-severe { background: #ef4444; }
    .bg-ghost { background: #ec4899; }
    .bg-canceled { background: #6b7280; }

    .dist-legend {
      display: flex;
      flex-wrap: wrap;
      gap: 1.25rem;
      font-size: 0.85rem;
    }
    .legend-item { display: flex; align-items: center; gap: 0.5rem; }
    .legend-dot { width: 10px; height: 10px; border-radius: 50%; }

    /* Tables */
    .table-container { overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; font-size: 0.9rem; text-align: left; }
    th {
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--card-border);
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    td { padding: 0.85rem 1rem; border-bottom: 1px solid rgba(255, 255, 255, 0.04); }
    tr:hover td { background: rgba(255, 255, 255, 0.02); }
    .route-pill {
      background: rgba(59, 130, 246, 0.15);
      color: #93c5fd;
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
      font-weight: 700;
      font-family: var(--font-mono);
      font-size: 0.85rem;
    }
    .search-box {
      width: 100%;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 0.65rem 1rem;
      border-radius: 10px;
      font-size: 0.9rem;
      margin-bottom: 1rem;
      outline: none;
    }
    .search-box:focus { border-color: var(--primary); }

    footer {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
      padding-top: 2rem;
      border-top: 1px solid var(--card-border);
      margin-top: 2rem;
    }
    footer a { color: var(--primary); text-decoration: none; }
    footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="brand">
        <div class="brand-icon">🚌</div>
        <div>
          <h1>Ghost Bus Tracker</h1>
          <div class="subtitle">Automated Public Transit Reliability &amp; Ghost Run Detection for <strong>${latest.agency}</strong></div>
        </div>
      </div>
      <div class="header-actions">
        ${statusBadge}
        <button class="btn" onclick="fetchLiveMetrics()">🔄 Refresh Feed</button>
        <a class="btn" href="/api/latest" target="_blank">⚡ JSON API</a>
      </div>
    </header>

    <!-- KPI Grid -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-title">Ghost Bus Rate</div>
        <div class="kpi-value text-ghost">${latest.ghost_bus_rate_pct}%</div>
        <div class="kpi-desc">${latest.total_ghost_trips} missing or dropped runs</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">On-Time Adherence</div>
        <div class="kpi-value text-success">${latest.overall_on_time_pct}%</div>
        <div class="kpi-desc">Departures within -1m to +5m</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">Active GPS Fleet</div>
        <div class="kpi-value text-primary">${latest.total_tracked_vehicles}</div>
        <div class="kpi-desc">Transponders reporting live coordinates</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">Scheduled Runs</div>
        <div class="kpi-value">${latest.total_scheduled_trips}</div>
        <div class="kpi-desc">Total active service runs scheduled</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">Mean Schedule Deviation</div>
        <div class="kpi-value text-warning">+${(latest.mean_delay_sec / 60.0).toFixed(1)}m</div>
        <div class="kpi-desc">+${latest.mean_delay_sec}s average delay</div>
      </div>
    </div>

    <!-- Delay Distribution Bar -->
    <div class="card">
      <div class="card-title">⏱️ Schedule Adherence &amp; Delay Breakdown</div>
      <div class="dist-bar">
        <div class="dist-seg bg-ontime" style="width: ${pct(dist.on_time || 0)}%" title="On-Time: ${dist.on_time}"></div>
        <div class="dist-seg bg-early" style="width: ${pct(dist.early || 0)}%" title="Early: ${dist.early}"></div>
        <div class="dist-seg bg-minor" style="width: ${pct(dist.minor_delay || 0)}%" title="Minor Delay: ${dist.minor_delay}"></div>
        <div class="dist-seg bg-severe" style="width: ${pct(dist.severe_delay || 0)}%" title="Severe Delay: ${dist.severe_delay}"></div>
        <div class="dist-seg bg-ghost" style="width: ${pct(dist.ghost || 0)}%" title="Ghost/Missing: ${dist.ghost}"></div>
      </div>
      <div class="dist-legend">
        <div class="legend-item"><span class="legend-dot bg-ontime"></span> On-Time: <strong>${dist.on_time || 0}</strong> (${pct(dist.on_time || 0)}%)</div>
        <div class="legend-item"><span class="legend-dot bg-early"></span> Early (&gt;1m): <strong>${dist.early || 0}</strong> (${pct(dist.early || 0)}%)</div>
        <div class="legend-item"><span class="legend-dot bg-minor"></span> Minor Delay (+5-15m): <strong>${dist.minor_delay || 0}</strong> (${pct(dist.minor_delay || 0)}%)</div>
        <div class="legend-item"><span class="legend-dot bg-severe"></span> Severe Delay (&gt;15m): <strong>${dist.severe_delay || 0}</strong> (${pct(dist.severe_delay || 0)}%)</div>
        <div class="legend-item"><span class="legend-dot bg-ghost"></span> Ghost / Missing: <strong>${dist.ghost || 0}</strong> (${pct(dist.ghost || 0)}%)</div>
      </div>
    </div>

    <!-- Worst Routes Table -->
    <div class="card">
      <div class="card-title">🚨 Worst Routes by Ghost Bus Rate</div>
      <input type="text" id="routeSearch" class="search-box" placeholder="Filter by route ID or name..." onkeyup="filterRoutes()">
      <div class="table-container">
        <table id="routesTable">
          <thead>
            <tr>
              <th>Route</th>
              <th>Total Runs</th>
              <th>Tracked Fleet</th>
              <th>Ghost Runs</th>
              <th>Ghost Rate</th>
              <th>On-Time %</th>
              <th>Avg Delay</th>
            </tr>
          </thead>
          <tbody>
            ${(latest.worst_routes_by_ghost || []).map(r => `
              <tr>
                <td><span class="route-pill">${r.route_name || r.route_id}</span></td>
                <td>${r.total_trips}</td>
                <td>${r.tracked_vehicles}</td>
                <td><strong class="text-ghost">${r.ghost_trips}</strong></td>
                <td><strong class="text-ghost">${r.ghost_rate_pct}%</strong></td>
                <td>${r.on_time_pct}%</td>
                <td>+${(r.avg_delay_sec / 60.0).toFixed(1)}m</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    </div>

    <!-- Active Ghost Trips Log -->
    <div class="card">
      <div class="card-title">👻 Confirmed Ghost Runs (Active Feed Diagnostics)</div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Trip ID</th>
              <th>Route</th>
              <th>Scheduled Time</th>
              <th>Status</th>
              <th>Diagnostic Reason</th>
            </tr>
          </thead>
          <tbody>
            ${(latest.sample_ghost_trips || []).slice(0, 10).map(g => `
              <tr>
                <td><code style="font-family: var(--font-mono); color: #93c5fd;">${g.trip_id}</code></td>
                <td>Route ${g.route_id}</td>
                <td>${g.start_time || 'N/A'}</td>
                <td><span class="badge badge-warning">${g.status}</span></td>
                <td style="color: #fca5a5;">${g.reason}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    </div>

    <footer>
      <p>Ghost Bus Tracker &bull; Powered by Cloudflare Workers &amp; Git-Scraping &bull; <a href="https://github.com/aminamos/ghost-bus-tracker" target="_blank">GitHub Repository</a></p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem;">Feed Snapshot Time: <code>${latest.scan_time}</code></p>
    </footer>
  </div>

  <script>
    function filterRoutes() {
      const q = document.getElementById('routeSearch').value.toLowerCase();
      const rows = document.querySelectorAll('#routesTable tbody tr');
      rows.forEach(r => {
        const text = r.textContent.toLowerCase();
        r.style.display = text.includes(q) ? '' : 'none';
      });
    }

    async function fetchLiveMetrics() {
      try {
        const btn = document.querySelector('button');
        btn.textContent = '⏳ Refreshing...';
        const res = await fetch('/api/latest');
        if (res.ok) {
          window.location.reload();
        }
      } catch (e) {
        alert('Failed to refresh feed: ' + e);
      }
    }
  </script>
</body>
</html>`;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Health check
    if (path === "/health" || path === "/api/health") {
      return jsonResponse({
        status: "ok",
        service: "ghost-bus-tracker-worker",
        agency: env?.AGENCY_NAME || "Metro Transit (Twin Cities)",
        timestamp: new Date().toISOString(),
      });
    }

    // Latest Snapshot API
    if (path === "/api/latest") {
      return jsonResponse(await fetchSnapshot("latest.json", DEFAULT_LATEST));
    }

    // History API
    if (path === "/api/history") {
      return jsonResponse(await fetchSnapshot("history.json", DEFAULT_HISTORY));
    }

    // Summary Scorecard API
    if (path === "/api/summary") {
      const latest = await fetchSnapshot("latest.json", DEFAULT_LATEST);
      return jsonResponse({
        agency: latest.agency,
        scan_time: latest.scan_time,
        ghost_bus_rate_pct: latest.ghost_bus_rate_pct,
        overall_on_time_pct: latest.overall_on_time_pct,
        total_scheduled_trips: latest.total_scheduled_trips,
        total_tracked_vehicles: latest.total_tracked_vehicles,
        total_ghost_trips: latest.total_ghost_trips,
        mean_delay_sec: latest.mean_delay_sec,
      });
    }

    // Proxy live routes from NextTrip REST API
    if (path === "/api/routes") {
      try {
        const upstream = await fetch("https://svc.metrotransit.org/nextrip/routes", {
          headers: { "User-Agent": "GhostBusTracker-Worker/0.1.0" },
        });
        const data = await upstream.json();
        return jsonResponse(data);
      } catch (err) {
        return jsonResponse({ error: "Failed to fetch upstream routes: " + err.message }, 502);
      }
    }

    // Web Dashboard (Root)
    if (path === "/" || path === "/index.html") {
      const [latest, history] = await Promise.all([
        fetchSnapshot("latest.json", DEFAULT_LATEST),
        fetchSnapshot("history.json", DEFAULT_HISTORY),
      ]);
      const html = renderHtml(latest, history);
      return new Response(html, {
        headers: {
          "Content-Type": "text/html; charset=utf-8",
          "Cache-Control": "public, max-age=60",
        },
      });
    }

    return new Response("Not Found", { status: 404 });
  },
};
