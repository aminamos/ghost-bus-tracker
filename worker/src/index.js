/**
 * Cloudflare Worker for Ghost Bus Tracker
 * Automated public transit reliability, schedule adherence, and ghost bus monitoring.
 * Supports multi-city transit markets: Minneapolis–Saint Paul (Metro Transit),
 * San Francisco (SFMTA Muni), Chicago (CTA), Boston (MBTA), New York City (MTA).
 */

import { DEFAULT_LATEST, DEFAULT_HISTORY } from "./snapshot_data.js";
import {
  CITY_PRESETS,
  CITY_ALIASES,
  normalizeCityKey,
  getAllCitiesData,
} from "./cities_data.js";

const DATA_BASE =
  "https://raw.githubusercontent.com/aminamos/ghost-bus-tracker/main/data";
const UPSTREAM_CACHE_TTL = 300; // git-scraping workflow commits every 30 min

// Escape feed-derived values before interpolating them into HTML.
function esc(v) {
  return String(v ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// Serve the freshest committed snapshot from the repo, cached at the edge via
// Cache API under a fixed internal key (TTL: UPSTREAM_CACHE_TTL).
async function fetchSnapshot(file, fallback, ctx, fresh = false) {
  const cache = caches.default;
  const cacheKey = `https://gbt-cache.internal/${file}`;
  const upstreamUrl = fresh
    ? `${DATA_BASE}/${file}?_=${Date.now()}`
    : `${DATA_BASE}/${file}`;

  if (!fresh) {
    try {
      const hit = await cache.match(cacheKey);
      if (hit) return await hit.json();
    } catch {
      // Cache read failed — continue to upstream.
    }
  }

  try {
    const res = await fetch(upstreamUrl, {
      headers: { "User-Agent": "GhostBusTracker-Worker/0.1.0" },
    });
    if (!res.ok) throw new Error(`upstream ${res.status}`);
    const body = await res.text();
    const data = JSON.parse(body);
    const toStore = new Response(body, {
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": `public, max-age=${UPSTREAM_CACHE_TTL}`,
      },
    });
    const put = cache.put(cacheKey, toStore).catch(() => {});
    if (ctx && typeof ctx.waitUntil === "function") ctx.waitUntil(put);
    else await put;
    return data;
  } catch {
    try {
      const hit = await cache.match(cacheKey);
      if (hit) return await hit.json();
    } catch {
      // ignore — use bundled fallback
    }
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

function renderHtml(activeKey, allCities) {
  const cityData = allCities[activeKey] || allCities["twin-cities"];
  const latest = cityData.latest;
  const history = cityData.history || [];

  const isHealthy = latest.ghost_bus_rate_pct < 5.0;
  const isElevated = latest.ghost_bus_rate_pct < 15.0;
  const statusBadge = isHealthy
    ? `<span class="badge badge-success" id="statusBadge">🟢 Healthy (&lt;5% Ghosts)</span>`
    : isElevated
    ? `<span class="badge badge-warning" id="statusBadge">🟡 Elevated Ghosts (${esc(latest.ghost_bus_rate_pct)}%)</span>`
    : `<span class="badge badge-danger" id="statusBadge">🔴 Critical Ghosting (${esc(latest.ghost_bus_rate_pct)}%)</span>`;

  const dist = latest.delay_distribution || {};
  const totalTrips = latest.total_scheduled_trips || 1;
  const pct = (n) => ((n / totalTrips) * 100).toFixed(1);
  const cov = latest.coverage_details || {};

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="pageTitle">Ghost Bus Tracker | ${esc(latest.transit_system)} — ${esc(latest.city)}</title>
  <meta name="description" content="Automated transit reliability, schedule adherence, and ghost bus tracking for ${esc(latest.transit_system)} in ${esc(latest.city)}.">
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
      padding: 1.5rem 1rem 3rem;
      min-height: 100vh;
    }
    .container { max-width: 1200px; margin: 0 auto; }
    
    /* Market Selector Bar */
    .market-selector-container {
      background: rgba(17, 24, 39, 0.7);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 0.75rem 1rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.75rem;
    }
    .market-selector-label {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      white-space: nowrap;
    }
    .market-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      align-items: center;
    }
    .city-chip {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--card-border);
      color: #cbd5e1;
      padding: 0.4rem 0.8rem;
      border-radius: 9999px;
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
      font-family: inherit;
      user-select: none;
    }
    .city-chip:hover {
      background: rgba(255, 255, 255, 0.09);
      border-color: rgba(255, 255, 255, 0.2);
      color: #fff;
    }
    .city-chip.active {
      background: rgba(59, 130, 246, 0.25);
      border-color: #3b82f6;
      color: #93c5fd;
      box-shadow: 0 0 12px rgba(59, 130, 246, 0.35);
    }
    .city-chip .chip-icon { font-size: 1rem; }

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
    .brand { display: flex; align-items: flex-start; gap: 1rem; }
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
      flex-shrink: 0;
    }
    h1 { font-size: 1.75rem; font-weight: 800; letter-spacing: -0.025em; }
    .subtitle { color: var(--text-muted); font-size: 0.925rem; margin-top: 0.25rem; }
    .header-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.6rem;
    }
    .header-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.25rem 0.65rem;
      border-radius: 8px;
      font-size: 0.78rem;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      color: #cbd5e1;
    }
    .header-pill strong { color: #f1f5f9; font-weight: 700; }
    .header-pill.accent {
      background: rgba(59, 130, 246, 0.15);
      border-color: rgba(59, 130, 246, 0.35);
      color: #93c5fd;
    }
    .header-actions { display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; }
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
      font-family: inherit;
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
      transition: transform 0.2s ease;
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
    .dist-seg { height: 100%; transition: width 0.4s ease; }
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

    /* Trend Chart */
    .chart-container {
      width: 100%;
      height: 220px;
      position: relative;
    }
    svg.trend-chart {
      width: 100%;
      height: 100%;
      overflow: visible;
    }

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
    <!-- Market Selector Bar -->
    <div class="market-selector-container">
      <span class="market-selector-label">📍 Select Transit Market:</span>
      <div class="market-chips" role="tablist" aria-label="Transit Market Selector">
        ${CITY_PRESETS.map((cp) => `
          <button
            class="city-chip ${cp.id === activeKey ? 'active' : ''}"
            data-city="${cp.id}"
            onclick="switchCity('${cp.id}')"
            role="tab"
            aria-selected="${cp.id === activeKey ? 'true' : 'false'}"
          >
            <span class="chip-icon">${cp.icon}</span>
            <span>${esc(cp.shortName)} (${esc(cp.agency.split(' ')[0])})</span>
          </button>
        `).join("")}
      </div>
    </div>

    <header>
      <div class="brand">
        <div class="brand-icon" id="brandIcon">${esc(cityData.icon || "🚌")}</div>
        <div>
          <div style="display: flex; align-items: baseline; gap: 0.65rem; flex-wrap: wrap;">
            <h1>Ghost Bus Tracker</h1>
            <span class="header-pill accent" id="headerCityPill" style="font-size: 0.8rem;">📍 ${esc(latest.city)}</span>
          </div>
          <div class="subtitle" id="subtitleText">
            Automated Transit Reliability &amp; Ghost Bus Detection for <strong>${esc(latest.transit_system)}</strong> in <strong>${esc(latest.city)}</strong>
          </div>
          <div class="header-pills">
            <span class="header-pill" id="pillCity">🏙️ <strong>City:</strong> ${esc(latest.city)}</span>
            <span class="header-pill" id="pillSystem">🚍 <strong>Transit System:</strong> ${esc(latest.transit_system)}</span>
            <span class="header-pill" id="pillCoverage">🗺️ <strong>Coverage:</strong> ${esc(latest.region)}</span>
            <span class="header-pill" id="pillModes">🚊 <strong>Modes:</strong> ${esc(cov.modes || "Bus, Light Rail & Rapid Transit")}</span>
          </div>
        </div>
      </div>
      <div class="header-actions">
        <div id="badgeContainer">${statusBadge}</div>
        <button class="btn" id="refreshBtn" onclick="fetchLiveMetrics()">🔄 Refresh Feed</button>
        <a class="btn" id="apiLink" href="/api/latest?city=${esc(activeKey)}" target="_blank">⚡ JSON API</a>
      </div>
    </header>

    <!-- KPI Grid -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-title">Ghost Bus Rate</div>
        <div class="kpi-value text-ghost" id="kpiGhostRate">${esc(latest.ghost_bus_rate_pct)}%</div>
        <div class="kpi-desc" id="kpiGhostDesc">${esc(latest.total_ghost_trips)} missing or dropped runs</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">On-Time Adherence</div>
        <div class="kpi-value text-success" id="kpiOnTime">${esc(latest.overall_on_time_pct)}%</div>
        <div class="kpi-desc">Departures within -1m to +5m</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">Active GPS Fleet</div>
        <div class="kpi-value text-primary" id="kpiFleet">${esc(latest.total_tracked_vehicles)}</div>
        <div class="kpi-desc">Transponders reporting live coordinates</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">Scheduled Runs</div>
        <div class="kpi-value" id="kpiScheduled">${esc(latest.total_scheduled_trips)}</div>
        <div class="kpi-desc">Total active service runs scheduled</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-title">Mean Schedule Deviation</div>
        <div class="kpi-value text-warning" id="kpiMeanDelay">+${esc((latest.mean_delay_sec / 60.0).toFixed(1))}m</div>
        <div class="kpi-desc" id="kpiMeanDelayDesc">+${esc(latest.mean_delay_sec)}s average delay</div>
      </div>
    </div>

    <!-- Delay Distribution Bar -->
    <div class="card">
      <div class="card-title">⏱️ Schedule Adherence &amp; Delay Breakdown</div>
      <div class="dist-bar" id="distBar">
        <div class="dist-seg bg-ontime" id="segOnTime" style="width: ${pct(dist.on_time || 0)}%" title="On-Time"></div>
        <div class="dist-seg bg-early" id="segEarly" style="width: ${pct(dist.early || 0)}%" title="Early"></div>
        <div class="dist-seg bg-minor" id="segMinor" style="width: ${pct(dist.minor_delay || 0)}%" title="Minor Delay"></div>
        <div class="dist-seg bg-severe" id="segSevere" style="width: ${pct(dist.severe_delay || 0)}%" title="Severe Delay"></div>
        <div class="dist-seg bg-ghost" id="segGhost" style="width: ${pct(dist.ghost || 0)}%" title="Ghost/Missing"></div>
      </div>
      <div class="dist-legend">
        <div class="legend-item"><span class="legend-dot bg-ontime"></span> On-Time: <strong id="legOnTime">${esc(dist.on_time || 0)} (${pct(dist.on_time || 0)}%)</strong></div>
        <div class="legend-item"><span class="legend-dot bg-early"></span> Early (&gt;1m): <strong id="legEarly">${esc(dist.early || 0)} (${pct(dist.early || 0)}%)</strong></div>
        <div class="legend-item"><span class="legend-dot bg-minor"></span> Minor Delay (+5-15m): <strong id="legMinor">${esc(dist.minor_delay || 0)} (${pct(dist.minor_delay || 0)}%)</strong></div>
        <div class="legend-item"><span class="legend-dot bg-severe"></span> Severe Delay (&gt;15m): <strong id="legSevere">${esc(dist.severe_delay || 0)} (${pct(dist.severe_delay || 0)}%)</strong></div>
        <div class="legend-item"><span class="legend-dot bg-ghost"></span> Ghost / Missing: <strong id="legGhost">${esc(dist.ghost || 0)} (${pct(dist.ghost || 0)}%)</strong></div>
      </div>
    </div>

    <!-- Trend Chart Card -->
    <div class="card">
      <div class="card-title">📈 Ghost Bus Rate &amp; Reliability History (Recent Scans)</div>
      <div class="chart-container" id="chartContainer">
        <!-- SVG Trend Chart rendered here -->
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
          <tbody id="routesTableBody">
            ${(latest.worst_routes_by_ghost || []).map((r) => `
              <tr>
                <td><span class="route-pill">${esc(r.route_name || r.route_id)}</span></td>
                <td>${esc(r.total_trips)}</td>
                <td>${esc(r.tracked_vehicles)}</td>
                <td><strong class="text-ghost">${esc(r.ghost_trips)}</strong></td>
                <td><strong class="text-ghost">${esc(r.ghost_rate_pct)}%</strong></td>
                <td>${esc(r.on_time_pct)}%</td>
                <td>+${esc((r.avg_delay_sec / 60.0).toFixed(1))}m</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    </div>

    <!-- Active Ghost Trips Log -->
    <div class="card">
      <div class="card-title">👻 Confirmed Ghost Runs (Active Feed Diagnostics)</div>
      <div class="table-container">
        <table id="ghostTripsTable">
          <thead>
            <tr>
              <th>Trip ID</th>
              <th>Route</th>
              <th>Scheduled Time</th>
              <th>Status</th>
              <th>Diagnostic Reason</th>
            </tr>
          </thead>
          <tbody id="ghostTripsBody">
            ${(latest.sample_ghost_trips || []).slice(0, 10).map((g) => `
              <tr>
                <td><code style="font-family: var(--font-mono); color: #93c5fd;">${esc(g.trip_id)}</code></td>
                <td>Route ${esc(g.route_id)}</td>
                <td>${esc(g.start_time || "N/A")}</td>
                <td><span class="badge badge-warning">${esc(g.status)}</span></td>
                <td style="color: #fca5a5;">${esc(g.reason)}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    </div>

    <!-- Transit System & Regional Coverage Details -->
    <div class="card" style="background: rgba(17, 24, 39, 0.7); border: 1px solid var(--card-border);">
      <div class="card-title">📍 Transit System &amp; Regional Coverage</div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem; font-size: 0.875rem;" id="coverageGrid">
        <div>
          <div style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.35rem;">🚍 Transit System &amp; Agency</div>
          <div style="color: var(--text); font-weight: 600;" id="covAgency">${esc(latest.transit_system)}</div>
          <div style="color: var(--text-muted); font-size: 0.8rem; margin-top: 0.25rem;" id="covAgencyDesc">${esc(cov.agency_desc || latest.agency)}</div>
        </div>
        <div>
          <div style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.35rem;">🏙️ Primary Cities &amp; Jurisdiction</div>
          <div style="color: var(--text); font-weight: 600;" id="covJurisdiction">${esc(latest.city)}</div>
          <div style="color: var(--text-muted); font-size: 0.8rem; margin-top: 0.25rem;" id="covJurisdictionDesc">${esc(cov.jurisdiction_desc || latest.region)}</div>
        </div>
        <div>
          <div style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.35rem;">🚊 Transit Network Modes</div>
          <div style="color: var(--text); font-weight: 600;" id="covModes">${esc(cov.modes || "Bus, Rail & Rapid Transit")}</div>
          <div style="color: var(--text-muted); font-size: 0.8rem; margin-top: 0.25rem;" id="covModesDesc">${esc(cov.modes_desc || "Transit services in metropolitan area")}</div>
        </div>
        <div>
          <div style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.35rem;">📡 Real-Time Data Protocol</div>
          <div style="color: var(--text); font-weight: 600;" id="covProtocol">${esc(cov.protocol || "GTFS Realtime (GTFS-RT)")}</div>
          <div style="color: var(--text-muted); font-size: 0.8rem; margin-top: 0.25rem;" id="covProtocolDesc">${esc(cov.protocol_desc || "VehiclePositions & TripUpdates protobuf feeds")}</div>
        </div>
        <div>
          <div style="font-weight: 700; color: #f1f5f9; margin-bottom: 0.35rem;">🏙️ Multi-City Presets &amp; Origin</div>
          <div style="color: var(--text); font-weight: 600;" id="covPresetTitle">${esc(cov.preset_info || "Multi-City Presets")}</div>
          <div style="color: var(--text-muted); font-size: 0.8rem; margin-top: 0.25rem;" id="covPresetDesc">${esc(cov.preset_info_desc || "CLI presets available for mpls, sf, chicago, boston, nyc.")}</div>
        </div>
      </div>
    </div>

    <footer>
      <p id="footerText">Tracking <strong>${esc(latest.transit_system)}</strong> • Serving <strong>${esc(latest.city)}</strong> (${esc(latest.region)}) • Powered by Cloudflare Workers &amp; Git-Scraping • <a href="https://github.com/aminamos/ghost-bus-tracker" target="_blank" rel="noopener">GitHub Repository</a> • <a href="${esc(cityData.website || 'https://www.metrotransit.org')}" target="_blank" rel="noopener" id="footerAgencyLink">${esc(latest.transit_system)} Official Site</a></p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem;">GTFS-RT Feed Snapshot Time: <code id="footerScanTime">${esc(latest.scan_time)}</code></p>
    </footer>
  </div>

  <script>
    // Embedded client data for instant, zero-latency market switching
    const CITIES_DATA = ${JSON.stringify(allCities)};
    const CITY_ALIASES = ${JSON.stringify(CITY_ALIASES)};
    let currentCityKey = "${activeKey}";

    function escHtml(str) {
      return String(str ?? "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }

    function renderTrendChart(history) {
      const container = document.getElementById("chartContainer");
      if (!container) return;
      if (!history || history.length === 0) {
        container.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100%;color:#9ca3af;font-size:0.875rem;">No historical scans available for this transit market yet.</div>';
        return;
      }

      // Sort chronological
      const pts = [...history].sort((a, b) => new Date(a.scan_time) - new Date(b.scan_time));
      const width = container.clientWidth || 900;
      const height = 200;
      const padLeft = 45;
      const padRight = 20;
      const padTop = 20;
      const padBottom = 35;
      const chartW = width - padLeft - padRight;
      const chartH = height - padTop - padBottom;

      const maxRate = Math.max(...pts.map(p => p.ghost_bus_rate_pct), 30);
      const minRate = 0;

      const getX = (idx) => padLeft + (idx / Math.max(pts.length - 1, 1)) * chartW;
      const getY = (val) => padTop + chartH - ((val - minRate) / (maxRate - minRate)) * chartH;

      const ghostPoints = pts.map((p, i) => \`\${getX(i)},\${getY(p.ghost_bus_rate_pct)}\`).join(" ");
      const onTimePoints = pts.map((p, i) => \`\${getX(i)},\${getY(p.overall_on_time_pct / 3)}\`).join(" "); // scaled for visual context

      let svg = \`<svg class="trend-chart" viewBox="0 0 \${width} \${height}">
        <defs>
          <linearGradient id="ghostGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ec4899" stop-opacity="0.35"/>
            <stop offset="100%" stop-color="#ec4899" stop-opacity="0.0"/>
          </linearGradient>
        </defs>

        <!-- Grid Lines -->
        <line x1="\${padLeft}" y1="\${getY(0)}" x2="\${width - padRight}" y2="\${getY(0)}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
        <line x1="\${padLeft}" y1="\${getY(10)}" x2="\${width - padRight}" y2="\${getY(10)}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
        <line x1="\${padLeft}" y1="\${getY(20)}" x2="\${width - padRight}" y2="\${getY(20)}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>
        <line x1="\${padLeft}" y1="\${getY(30)}" x2="\${width - padRight}" y2="\${getY(30)}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3,3"/>

        <!-- Y Axis Labels -->
        <text x="\${padLeft - 8}" y="\${getY(0) + 4}" fill="#9ca3af" font-size="11" text-anchor="end" font-family="JetBrains Mono">0%</text>
        <text x="\${padLeft - 8}" y="\${getY(10) + 4}" fill="#9ca3af" font-size="11" text-anchor="end" font-family="JetBrains Mono">10%</text>
        <text x="\${padLeft - 8}" y="\${getY(20) + 4}" fill="#9ca3af" font-size="11" text-anchor="end" font-family="JetBrains Mono">20%</text>
        <text x="\${padLeft - 8}" y="\${getY(30) + 4}" fill="#9ca3af" font-size="11" text-anchor="end" font-family="JetBrains Mono">30%</text>

        <!-- Area fill under ghost rate -->
        <polygon points="\${padLeft},\${getY(0)} \${ghostPoints} \${getX(pts.length - 1)},\${getY(0)}" fill="url(#ghostGrad)" />

        <!-- Line: Ghost Bus Rate -->
        <polyline points="\${ghostPoints}" fill="none" stroke="#ec4899" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />\`;

      // Data dots and labels
      pts.forEach((p, i) => {
        const x = getX(i);
        const y = getY(p.ghost_bus_rate_pct);
        const dateObj = new Date(p.scan_time);
        const timeLabel = isNaN(dateObj.getTime()) ? p.scan_time.slice(-8) : dateObj.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

        svg += \`
          <circle cx="\${x}" cy="\${y}" r="4.5" fill="#ec4899" stroke="#111827" stroke-width="2" />
          <text x="\${x}" y="\${y - 9}" fill="#f472b6" font-size="10.5" font-weight="700" text-anchor="middle" font-family="JetBrains Mono">\${p.ghost_bus_rate_pct}%</text>
          <text x="\${x}" y="\${height - 10}" fill="#9ca3af" font-size="10" text-anchor="middle" font-family="JetBrains Mono">\${timeLabel}</text>
        \`;
      });

      svg += \`</svg>\`;
      container.innerHTML = svg;
    }

    function switchCity(cityKey) {
      const normalized = CITY_ALIASES[cityKey.toLowerCase()] || cityKey;
      const data = CITIES_DATA[normalized];
      if (!data) return;

      currentCityKey = normalized;

      // 1. Update chip buttons
      document.querySelectorAll('.city-chip').forEach(btn => {
        const isMatch = btn.getAttribute('data-city') === normalized;
        btn.classList.toggle('active', isMatch);
        btn.setAttribute('aria-selected', isMatch ? 'true' : 'false');
      });

      // 2. Update page title & URLs without full reload
      const latest = data.latest;
      const cov = latest.coverage_details || {};
      document.getElementById('pageTitle').textContent = \`Ghost Bus Tracker | \${latest.transit_system} — \${latest.city}\`;
      
      const newUrl = new URL(window.location);
      newUrl.searchParams.set('city', normalized);
      window.history.replaceState({ city: normalized }, '', newUrl);
      try { localStorage.setItem('gbt_selected_city', normalized); } catch(e){}

      // 3. Update Header & Pills
      document.getElementById('brandIcon').textContent = data.icon || "🚌";
      document.getElementById('headerCityPill').textContent = \`📍 \${latest.city}\`;
      document.getElementById('subtitleText').innerHTML = \`Automated Transit Reliability &amp; Ghost Bus Detection for <strong>\${escHtml(latest.transit_system)}</strong> in <strong>\${escHtml(latest.city)}</strong>\`;
      document.getElementById('pillCity').innerHTML = \`🏙️ <strong>City:</strong> \${escHtml(latest.city)}\`;
      document.getElementById('pillSystem').innerHTML = \`🚍 <strong>Transit System:</strong> \${escHtml(latest.transit_system)}\`;
      document.getElementById('pillCoverage').innerHTML = \`🗺️ <strong>Coverage:</strong> \${escHtml(latest.region)}\`;
      document.getElementById('pillModes').innerHTML = \`🚊 <strong>Modes:</strong> \${escHtml(cov.modes || "Bus, Rail & Transit")}\`;

      // 4. Update Status Badge
      const isHealthy = latest.ghost_bus_rate_pct < 5.0;
      const isElevated = latest.ghost_bus_rate_pct < 15.0;
      const badgeHtml = isHealthy
        ? \`<span class="badge badge-success" id="statusBadge">🟢 Healthy (&lt;5% Ghosts)</span>\`
        : isElevated
        ? \`<span class="badge badge-warning" id="statusBadge">🟡 Elevated Ghosts (\${escHtml(latest.ghost_bus_rate_pct)}%)</span>\`
        : \`<span class="badge badge-danger" id="statusBadge">🔴 Critical Ghosting (\${escHtml(latest.ghost_bus_rate_pct)}%)</span>\`;
      document.getElementById('badgeContainer').innerHTML = badgeHtml;

      // 5. Update KPI Cards
      document.getElementById('kpiGhostRate').textContent = \`\${latest.ghost_bus_rate_pct}%\`;
      document.getElementById('kpiGhostDesc').textContent = \`\${latest.total_ghost_trips} missing or dropped runs\`;
      document.getElementById('kpiOnTime').textContent = \`\${latest.overall_on_time_pct}%\`;
      document.getElementById('kpiFleet').textContent = latest.total_tracked_vehicles;
      document.getElementById('kpiScheduled').textContent = latest.total_scheduled_trips;
      document.getElementById('kpiMeanDelay').textContent = \`+\${(latest.mean_delay_sec / 60.0).toFixed(1)}m\`;
      document.getElementById('kpiMeanDelayDesc').textContent = \`+\${latest.mean_delay_sec}s average delay\`;

      // 6. Update Delay Distribution Bar & Legend
      const dist = latest.delay_distribution || {};
      const totalTrips = latest.total_scheduled_trips || 1;
      const pct = (n) => ((n / totalTrips) * 100).toFixed(1);

      document.getElementById('segOnTime').style.width = \`\${pct(dist.on_time || 0)}%\`;
      document.getElementById('segEarly').style.width = \`\${pct(dist.early || 0)}%\`;
      document.getElementById('segMinor').style.width = \`\${pct(dist.minor_delay || 0)}%\`;
      document.getElementById('segSevere').style.width = \`\${pct(dist.severe_delay || 0)}%\`;
      document.getElementById('segGhost').style.width = \`\${pct(dist.ghost || 0)}%\`;

      document.getElementById('legOnTime').textContent = \`\${dist.on_time || 0} (\${pct(dist.on_time || 0)}%)\`;
      document.getElementById('legEarly').textContent = \`\${dist.early || 0} (\${pct(dist.early || 0)}%)\`;
      document.getElementById('legMinor').textContent = \`\${dist.minor_delay || 0} (\${pct(dist.minor_delay || 0)}%)\`;
      document.getElementById('legSevere').textContent = \`\${dist.severe_delay || 0} (\${pct(dist.severe_delay || 0)}%)\`;
      document.getElementById('legGhost').textContent = \`\${dist.ghost || 0} (\${pct(dist.ghost || 0)}%)\`;

      // 7. Render Trend Chart
      renderTrendChart(data.history);

      // 8. Update Worst Routes Table
      const routesBody = document.getElementById('routesTableBody');
      const routes = latest.worst_routes_by_ghost || [];
      routesBody.innerHTML = routes.map(r => \`
        <tr>
          <td><span class="route-pill">\${escHtml(r.route_name || r.route_id)}</span></td>
          <td>\${escHtml(r.total_trips)}</td>
          <td>\${escHtml(r.tracked_vehicles)}</td>
          <td><strong class="text-ghost">\${escHtml(r.ghost_trips)}</strong></td>
          <td><strong class="text-ghost">\${escHtml(r.ghost_rate_pct)}%</strong></td>
          <td>\${escHtml(r.on_time_pct)}%</td>
          <td>+\${(r.avg_delay_sec / 60.0).toFixed(1)}m</td>
        </tr>
      \`).join('');

      // 9. Update Ghost Trips Diagnostics Log
      const ghostBody = document.getElementById('ghostTripsBody');
      const ghosts = latest.sample_ghost_trips || [];
      ghostBody.innerHTML = ghosts.slice(0, 10).map(g => \`
        <tr>
          <td><code style="font-family: var(--font-mono); color: #93c5fd;">\${escHtml(g.trip_id)}</code></td>
          <td>Route \${escHtml(g.route_id)}</td>
          <td>\${escHtml(g.start_time || "N/A")}</td>
          <td><span class="badge badge-warning">\${escHtml(g.status)}</span></td>
          <td style="color: #fca5a5;">\${escHtml(g.reason)}</td>
        </tr>
      \`).join('');

      // 10. Update Coverage Card
      document.getElementById('covAgency').textContent = latest.transit_system;
      document.getElementById('covAgencyDesc').textContent = cov.agency_desc || latest.agency;
      document.getElementById('covJurisdiction').textContent = latest.city;
      document.getElementById('covJurisdictionDesc').textContent = cov.jurisdiction_desc || latest.region;
      document.getElementById('covModes').textContent = cov.modes || "Bus, Rail & Transit";
      document.getElementById('covModesDesc').textContent = cov.modes_desc || "Transit routes across metro area";
      document.getElementById('covProtocol').textContent = cov.protocol || "GTFS Realtime (GTFS-RT)";
      document.getElementById('covProtocolDesc').textContent = cov.protocol_desc || "Protobuf feeds";
      document.getElementById('covPresetTitle').textContent = cov.preset_info || "Multi-City Presets";
      document.getElementById('covPresetDesc').textContent = cov.preset_info_desc || "CLI presets available for mpls, sf, chicago, boston, nyc.";

      // 11. Update API link & Footer
      document.getElementById('apiLink').href = \`/api/latest?city=\${normalized}\`;
      document.getElementById('footerAgencyLink').href = data.website || "https://www.metrotransit.org";
      document.getElementById('footerAgencyLink').textContent = \`\${latest.transit_system} Official Site\`;
      document.getElementById('footerScanTime').textContent = latest.scan_time;
      document.getElementById('footerText').innerHTML = \`Tracking <strong>\${escHtml(latest.transit_system)}</strong> • Serving <strong>\${escHtml(latest.city)}</strong> (\${escHtml(latest.region)}) • Powered by Cloudflare Workers &amp; Git-Scraping • <a href="https://github.com/aminamos/ghost-bus-tracker" target="_blank" rel="noopener">GitHub Repository</a> • <a href="\${escHtml(data.website || 'https://www.metrotransit.org')}" target="_blank" rel="noopener">\${escHtml(latest.transit_system)} Official Site</a>\`;

      // Clear search box filter
      const searchBox = document.getElementById('routeSearch');
      if (searchBox) searchBox.value = '';
    }

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
        const btn = document.getElementById('refreshBtn');
        btn.textContent = '⏳ Refreshing...';
        const res = await fetch(\`/api/latest?city=\${currentCityKey}&fresh=1\`);
        if (res.ok) {
          const freshData = await res.json();
          if (CITIES_DATA[currentCityKey]) {
            CITIES_DATA[currentCityKey].latest = freshData;
            switchCity(currentCityKey);
          }
          btn.textContent = '🔄 Refresh Feed';
        }
      } catch (e) {
        alert('Failed to refresh feed: ' + e);
        const btn = document.getElementById('refreshBtn');
        if (btn) btn.textContent = '🔄 Refresh Feed';
      }
    }

    // Auto-detect city from query string or localStorage on load
    window.addEventListener('DOMContentLoaded', () => {
      const urlParams = new URLSearchParams(window.location.search);
      const cityQuery = urlParams.get('city') || urlParams.get('location') || urlParams.get('preset');
      const initialKey = cityQuery || currentCityKey;
      const normalized = CITY_ALIASES[String(initialKey).toLowerCase()] || initialKey;
      if (normalized && CITIES_DATA[normalized]) {
        switchCity(normalized);
      } else {
        renderTrendChart(CITIES_DATA[currentCityKey]?.history);
      }
    });

    // Handle browser back/forward buttons
    window.addEventListener('popstate', (e) => {
      if (e.state && e.state.city) {
        switchCity(e.state.city);
      }
    });
  </script>
</body>
</html>`;
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const fresh = url.searchParams.has("fresh");

    // Resolve requested city (defaults to twin-cities)
    const rawCity =
      url.searchParams.get("city") ||
      url.searchParams.get("location") ||
      url.searchParams.get("preset");
    const cityKey = normalizeCityKey(rawCity);

    // Health check
    if (path === "/health" || path === "/api/health") {
      return jsonResponse({
        status: "ok",
        service: "ghost-bus-tracker-worker",
        agency: env?.AGENCY_NAME || "Metro Transit (Twin Cities)",
        supported_markets: CITY_PRESETS.map((p) => p.id),
        timestamp: new Date().toISOString(),
      });
    }

    // Prepare live Twin Cities data from GitHub git-scraping workflow
    const [liveTwinCitiesLatest, liveTwinCitiesHistory] = await Promise.all([
      fetchSnapshot("latest.json", DEFAULT_LATEST, ctx, fresh),
      fetchSnapshot("history.json", DEFAULT_HISTORY, ctx, fresh),
    ]);

    const allCities = getAllCitiesData(
      liveTwinCitiesLatest,
      liveTwinCitiesHistory
    );
    const targetCityData = allCities[cityKey] || allCities["twin-cities"];

    // Latest Snapshot API
    if (path === "/api/latest") {
      return jsonResponse(targetCityData.latest);
    }

    // History API
    if (path === "/api/history") {
      return jsonResponse(targetCityData.history);
    }

    // Summary Scorecard API
    if (path === "/api/summary") {
      const snap = targetCityData.latest;
      return jsonResponse({
        market_id: cityKey,
        agency: snap.agency,
        transit_system: snap.transit_system,
        city: snap.city,
        region: snap.region,
        state: snap.state,
        country: snap.country,
        scan_time: snap.scan_time,
        ghost_bus_rate_pct: snap.ghost_bus_rate_pct,
        overall_on_time_pct: snap.overall_on_time_pct,
        total_scheduled_trips: snap.total_scheduled_trips,
        total_tracked_vehicles: snap.total_tracked_vehicles,
        total_ghost_trips: snap.total_ghost_trips,
        mean_delay_sec: snap.mean_delay_sec,
      });
    }

    // List supported markets API
    if (path === "/api/markets" || path === "/api/cities" || path === "/api/presets") {
      return jsonResponse({
        markets: CITY_PRESETS,
        aliases: CITY_ALIASES,
      });
    }

    // Proxy live routes from NextTrip REST API (for Twin Cities)
    if (path === "/api/routes") {
      try {
        const upstream = await fetch(
          "https://svc.metrotransit.org/nextrip/routes",
          {
            headers: { "User-Agent": "GhostBusTracker-Worker/0.1.0" },
          }
        );
        const data = await upstream.json();
        return jsonResponse(data);
      } catch (err) {
        return jsonResponse(
          { error: "Failed to fetch upstream routes: " + err.message },
          502
        );
      }
    }

    // Web Dashboard (Root)
    if (path === "/" || path === "/index.html") {
      const html = renderHtml(cityKey, allCities);
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
