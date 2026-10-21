/**
 * Markdown reliability report generator.
 *
 * Line-for-line port of ReportGenerator.generate_markdown in src/reporter.py,
 * including Python float formatting (40.0 stays "40.0") and round-half-even,
 * so Worker-generated RELIABILITY*.md files match the Python output exactly.
 */

// Python round(): half-to-even on the exact binary value. Deciding from a
// long fixed-point expansion avoids the error that value * 10**digits adds
// (e.g. 681/60 = 11.34999... must round to 11.3, not 11.4).
export function pyRound(value, digits) {
  const sign = value < 0 ? -1 : 1;
  const s = Math.abs(value).toFixed(Math.max(digits + 25, 30));
  const dot = s.indexOf(".");
  let intPart = s.slice(0, dot);
  const frac = s.slice(dot + 1);
  let kept = frac.slice(0, digits);
  const nextDigit = Number(frac[digits]);
  const restNonZero = /[1-9]/.test(frac.slice(digits + 1));
  let roundUp = nextDigit > 5 || (nextDigit === 5 && restNonZero);
  if (nextDigit === 5 && !restNonZero) {
    const lastKept = digits > 0 ? Number(kept[digits - 1]) : Number(intPart[intPart.length - 1]);
    roundUp = lastKept % 2 === 1;
  }
  if (roundUp) {
    const digitsArr = (intPart + kept).split("").map(Number);
    let i = digitsArr.length - 1;
    while (i >= 0 && digitsArr[i] === 9) { digitsArr[i] = 0; i--; }
    if (i < 0) digitsArr.unshift(1); else digitsArr[i]++;
    const joined = digitsArr.join("");
    intPart = joined.slice(0, joined.length - digits) || "0";
    kept = digits > 0 ? joined.slice(joined.length - digits) : "";
  }
  return sign * Number(digits > 0 ? `${intPart}.${kept}` : intPart);
}

// Python str(float): integral floats keep a trailing ".0".
export function pyFloatStr(value) {
  const n = Number(value);
  if (!Number.isFinite(n)) return String(n);
  if (Number.isInteger(n) && Math.abs(n) < 1e16) return `${n}.0`;
  return String(n);
}

function fmtDelayFloat(sec) {
  const sign = sec >= 0 ? "+" : "-";
  return `${sign}${pyFloatStr(Math.abs(sec))}s`;
}

function fmtDelayInt(sec) {
  const sign = sec >= 0 ? "+" : "-";
  return `${sign}${Math.abs(sec)}s`;
}

function fmtDelayMin(sec) {
  const sign = sec >= 0 ? "+" : "-";
  return `${sign}${pyFloatStr(pyRound(Math.abs(sec) / 60.0, 1))} min`;
}

export function generateMarkdown(snapshot, history = null) {
  const statusBadge =
    snapshot.ghost_bus_rate_pct < 5.0
      ? "🟢 **HEALTHY**"
      : snapshot.ghost_bus_rate_pct < 15.0
        ? "🟡 **ELEVATED GHOSTS**"
        : "🔴 **CRITICAL GHOSTING**";

  const sourceLabel =
    snapshot.source === "sample"
      ? "⚠️ SAMPLE feed (live fetch failed — not persisted)"
      : "live GTFS-RT feed";

  const agencyVal = snapshot.agency;
  const cityVal = snapshot.city || "Minneapolis–Saint Paul, MN";
  const systemVal = snapshot.transit_system || agencyVal;
  const regionVal = snapshot.region || "Twin Cities Metropolitan Area, Minnesota";

  const md = [
    "# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker",
    "",
    `> Real-time monitoring and git-scraping reliability index for **${agencyVal}** in **${cityVal}** (${regionVal}).`,
    `> **Transit System:** ${systemVal} | **Location:** ${cityVal} | **Status:** ${statusBadge} | **Last Scan:** \`${snapshot.scan_time}\` | **Source:** ${sourceLabel}`,
    "",
    "---",
    "",
    "## 📊 Executive Summary Scorecard",
    "",
    "| Metric | Value | Status / Description |",
    "| :--- | :--- | :--- |",
    `| **Ghost Bus Rate** | **\`${pyFloatStr(snapshot.ghost_bus_rate_pct)}%\`** | Scheduled runs with missing transponders or unannounced cuts |`,
    `| **On-Time Adherence** | **\`${pyFloatStr(snapshot.overall_on_time_pct)}%\`** | Departures within standard window (-1m to +5m) |`,
    `| **Scheduled Active Trips** | \`${snapshot.total_scheduled_trips}\` | Total runs operating in current transit schedule window |`,
    `| **Tracked Fleet Vehicles** | \`${snapshot.total_tracked_vehicles}\` | GPS transponders broadcasting valid coordinates |`,
    `| **Confirmed Ghost Trips** | \`${snapshot.total_ghost_trips}\` | Disappeared or unassigned scheduled runs |`,
    `| **Mean Delay** | \`${fmtDelayFloat(snapshot.mean_delay_sec)}\` (\`${fmtDelayMin(snapshot.mean_delay_sec)}\`) | Average delay across all active tracked runs |`,
    `| **Median Delay** | \`${fmtDelayFloat(snapshot.median_delay_sec)}\` (\`${fmtDelayMin(snapshot.median_delay_sec)}\`) | Median schedule deviation |`,
    "",
    "---",
    "",
    "## ⏱️ Delay & Reliability Breakdown",
    "",
    "| Category | Threshold / Definition | Trip Count | Percentage |",
    "| :--- | :--- | :--- | :--- |",
  ];

  const dist = snapshot.delay_distribution || {};
  const tot = snapshot.total_scheduled_trips;
  const pct = (n) => (tot > 0 ? `${pyFloatStr(pyRound((n / tot) * 100, 1))}%` : "0%");

  md.push(`| 🟢 **On-Time** | Within -60s to +300s | ${dist.on_time} | ${pct(dist.on_time)} |`);
  md.push(`| ⏩ **Early Departure** | More than 1 min ahead of schedule | ${dist.early} | ${pct(dist.early)} |`);
  md.push(`| 🟡 **Minor Delay** | +5m to +15m late | ${dist.minor_delay} | ${pct(dist.minor_delay)} |`);
  md.push(`| 🔴 **Severe Delay** | Over 15m late | ${dist.severe_delay} | ${pct(dist.severe_delay)} |`);
  md.push(`| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | ${dist.ghost} | ${pct(dist.ghost)} |`);
  md.push(`| ❌ **Agency Canceled** | Explicitly reported CANCELED | ${dist.canceled} | ${pct(dist.canceled)} |`);

  md.push(
    "",
    "---",
    "",
    "## 🚨 Top Worst Routes by Ghost Bus Rate",
    "",
    "| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |",
    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
  );

  const worst = snapshot.worst_routes_by_ghost || [];
  if (worst.length) {
    for (const r of worst) {
      const avgM = r.avg_delay_sec > 0 ? fmtDelayMin(r.avg_delay_sec) : fmtDelayFloat(r.avg_delay_sec);
      md.push(
        `| **${r.route_name || r.route_id}** | ${r.total_trips} | ${r.tracked_vehicles} | ${r.ghost_trips} | **\`${pyFloatStr(r.ghost_rate_pct)}%\`** | \`${pyFloatStr(r.on_time_pct)}%\` | \`${avgM}\` |`,
      );
    }
  } else {
    md.push("| *No multi-trip routes recorded in current window* | - | - | - | - | - | - |");
  }

  md.push(
    "",
    "---",
    "",
    "## 🐌 Most Delayed Routes",
    "",
    "| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |",
    "| :--- | :---: | :---: | :---: | :---: |",
  );

  const delayed = snapshot.most_delayed_routes || [];
  if (delayed.length) {
    for (const r of delayed) {
      const avgM = `${fmtDelayMin(r.avg_delay_sec)} (${fmtDelayFloat(r.avg_delay_sec)})`;
      const maxM = `${fmtDelayMin(r.max_delay_sec)} (${fmtDelayInt(r.max_delay_sec)})`;
      md.push(
        `| **${r.route_name || r.route_id}** | \`${avgM}\` | \`${maxM}\` | ${r.tracked_vehicles} | \`${pyFloatStr(r.on_time_pct)}%\` |`,
      );
    }
  } else {
    md.push("| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |");
  }

  md.push(
    "",
    "---",
    "",
    "## ⏱️ Headway Regularity & Excess Wait Time (EWT)",
    "",
    "> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.",
    "",
    "| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |",
    "| :--- | :---: | :---: | :---: | :---: |",
  );

  const headways = snapshot.headway_metrics || [];
  if (headways.length) {
    for (const hw of headways) {
      const ewtM = fmtDelayMin(hw.excess_wait_time_min || 0.0);
      md.push(
        `| **Route ${hw.route_id}** | ~${pyFloatStr(hw.scheduled_headway_min)}m | ~${pyFloatStr(hw.observed_headway_min)}m | **\`${ewtM}\`** | \`${pyFloatStr(hw.headway_regularity_score)} / 100\` |`,
      );
    }
  } else {
    md.push("| *Insufficient route frequency data in current snapshot* | - | - | - | - |");
  }

  md.push(
    "",
    "---",
    "",
    "## 👻 Active Ghost Trips Sample",
    "",
    "| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |",
    "| :--- | :---: | :---: | :--- | :--- |",
  );

  const ghosts = snapshot.sample_ghost_trips || [];
  if (ghosts.length) {
    for (const g of ghosts) {
      md.push(
        `| \`${g.trip_id}\` | Route ${g.route_id} | \`${g.start_time}\` | \`${g.status}\` | ${g.reason} |`,
      );
    }
  } else {
    md.push("| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |");
  }

  if (history && history.length > 1) {
    md.push(
      "",
      "---",
      "",
      "## 📈 Recent Reliability Trend (Git-Scraping History)",
      "",
      "| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |",
      "| :--- | :---: | :---: | :---: | :---: | :---: |",
    );
    for (const h of [...history.slice(-8)].reverse()) {
      const tStr = String(h.scan_time).slice(0, 19).replace("T", " ");
      md.push(
        `| \`${tStr}\` | \`${pyFloatStr(h.ghost_bus_rate_pct)}%\` | \`${pyFloatStr(h.overall_on_time_pct)}%\` | ${h.total_scheduled_trips} | ${h.total_tracked_vehicles} | \`${fmtDelayFloat(h.mean_delay_sec)}\` |`,
      );
    }
  }

  md.push(
    "",
    "---",
    "",
    "## 🔬 Methodology & Definitions",
    "",
    "- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.",
    "- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.",
    "- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.",
    "- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.",
    "- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.",
    "",
    `*Generated by Ghost Bus Tracker v0.1.0 at \`${snapshot.scan_time}\`.*`,
  );

  return md.join("\n") + "\n";
}
