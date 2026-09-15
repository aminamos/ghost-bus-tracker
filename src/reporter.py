"""Reporter module for generating Markdown reports and JSON metrics."""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
from src import config
from src.models import HistoryEntry, ReliabilitySnapshot

logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generates Markdown reliability dashboards, JSON snapshots, and historical tracking logs."""

    def __init__(
        self,
        latest_path: Path = config.LATEST_FILE,
        history_path: Path = config.HISTORY_FILE,
        report_path: Path = config.REPORT_FILE,
    ):
        self.latest_path = latest_path
        self.history_path = history_path
        self.report_path = report_path

    def save_latest_json(
        self, snapshot: ReliabilitySnapshot, output_path: Optional[Path] = None
    ) -> Path:
        """Saves the latest reliability snapshot to JSON."""
        target = output_path or self.latest_path
        target.parent.mkdir(parents=True, exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(snapshot.model_dump_json(indent=2))
        logger.info(f"Saved latest snapshot to {target}")
        return target

    def update_history_json(
        self,
        snapshot: ReliabilitySnapshot,
        history_path: Optional[Path] = None,
        max_entries: int = config.MAX_HISTORY_SNAPSHOTS,
    ) -> List[Dict[str, Any]]:
        """Appends snapshot summary to history.json, maintaining a rolling window."""
        target = history_path or self.history_path
        target.parent.mkdir(parents=True, exist_ok=True)

        history: List[Dict[str, Any]] = []
        if target.is_file():
            try:
                with open(target, "r", encoding="utf-8") as f:
                    history = json.load(f)
            except Exception as e:
                logger.warning(f"Could not read existing history ({e}), creating fresh log")
                history = []

        entry = HistoryEntry(
            scan_time=snapshot.scan_time,
            ghost_bus_rate_pct=snapshot.ghost_bus_rate_pct,
            overall_on_time_pct=snapshot.overall_on_time_pct,
            total_scheduled_trips=snapshot.total_scheduled_trips,
            total_tracked_vehicles=snapshot.total_tracked_vehicles,
            total_ghost_trips=snapshot.total_ghost_trips,
            mean_delay_sec=snapshot.mean_delay_sec,
            source=snapshot.source,
        ).model_dump()

        history.append(entry)

        # Keep rolling window of most recent snapshots
        if len(history) > max_entries:
            history = history[-max_entries:]

        with open(target, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)

        logger.info(f"Updated history in {target} (total records: {len(history)})")
        return history

    def generate_markdown(
        self,
        snapshot: ReliabilitySnapshot,
        history: Optional[List[Dict[str, Any]]] = None,
    ) -> str:
        """Generates comprehensive Markdown reliability report."""
        status_badge = (
            "🟢 **HEALTHY**"
            if snapshot.ghost_bus_rate_pct < 5.0
            else (
                "🟡 **ELEVATED GHOSTS**"
                if snapshot.ghost_bus_rate_pct < 15.0
                else "🔴 **CRITICAL GHOSTING**"
            )
        )

        source_label = (
            "⚠️ SAMPLE feed (live fetch failed — not persisted)"
            if snapshot.source == "sample"
            else "live GTFS-RT feed"
        )

        md: List[str] = [
            "# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker",
            "",
            f"> Real-time monitoring and git-scraping reliability index for **{snapshot.agency}**.",
            f"> **Status:** {status_badge} | **Last Scan:** `{snapshot.scan_time}` | **Source:** {source_label}",
            "",
            "---",
            "",
            "## 📊 Executive Summary Scorecard",
            "",
            "| Metric | Value | Status / Description |",
            "| :--- | :--- | :--- |",
            f"| **Ghost Bus Rate** | **`{snapshot.ghost_bus_rate_pct}%`** | Scheduled runs with missing transponders or unannounced cuts |",
            f"| **On-Time Adherence** | **`{snapshot.overall_on_time_pct}%`** | Departures within standard window (-1m to +5m) |",
            f"| **Scheduled Active Trips** | `{snapshot.total_scheduled_trips}` | Total runs operating in current transit schedule window |",
            f"| **Tracked Fleet Vehicles** | `{snapshot.total_tracked_vehicles}` | GPS transponders broadcasting valid coordinates |",
            f"| **Confirmed Ghost Trips** | `{snapshot.total_ghost_trips}` | Disappeared or unassigned scheduled runs |",
            f"| **Mean Delay** | `+{snapshot.mean_delay_sec}s` (`{round(snapshot.mean_delay_sec / 60.0, 1)} min`) | Average delay across all active tracked runs |",
            f"| **Median Delay** | `+{snapshot.median_delay_sec}s` (`{round(snapshot.median_delay_sec / 60.0, 1)} min`) | Median schedule deviation |",
            "",
            "---",
            "",
            "## ⏱️ Delay & Reliability Breakdown",
            "",
            "| Category | Threshold / Definition | Trip Count | Percentage |",
            "| :--- | :--- | :--- | :--- |",
        ]

        dist = snapshot.delay_distribution
        tot = snapshot.total_scheduled_trips
        pct = lambda n: f"{round((n / tot) * 100, 1)}%" if tot > 0 else "0%"

        md.append(f"| 🟢 **On-Time** | Within -60s to +300s | {dist.on_time} | {pct(dist.on_time)} |")
        md.append(f"| ⏩ **Early Departure** | More than 1 min ahead of schedule | {dist.early} | {pct(dist.early)} |")
        md.append(f"| 🟡 **Minor Delay** | +5m to +15m late | {dist.minor_delay} | {pct(dist.minor_delay)} |")
        md.append(f"| 🔴 **Severe Delay** | Over 15m late | {dist.severe_delay} | {pct(dist.severe_delay)} |")
        md.append(f"| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | {dist.ghost} | {pct(dist.ghost)} |")
        md.append(f"| ❌ **Agency Canceled** | Explicitly reported CANCELED | {dist.canceled} | {pct(dist.canceled)} |")

        md.extend([
            "",
            "---",
            "",
            "## 🚨 Top Worst Routes by Ghost Bus Rate",
            "",
            "| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
        ])

        if snapshot.worst_routes_by_ghost:
            for r in snapshot.worst_routes_by_ghost:
                avg_m = f"+{round(r.avg_delay_sec / 60.0, 1)}m" if r.avg_delay_sec > 0 else f"{r.avg_delay_sec}s"
                md.append(
                    f"| **{r.route_name or r.route_id}** | {r.total_trips} | {r.tracked_vehicles} | {r.ghost_trips} | **`{r.ghost_rate_pct}%`** | `{r.on_time_pct}%` | `{avg_m}` |"
                )
        else:
            md.append("| *No multi-trip routes recorded in current window* | - | - | - | - | - | - |")

        md.extend([
            "",
            "---",
            "",
            "## 🐌 Most Delayed Routes",
            "",
            "| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |",
            "| :--- | :---: | :---: | :---: | :---: |",
        ])

        if snapshot.most_delayed_routes:
            for r in snapshot.most_delayed_routes:
                avg_m = f"+{round(r.avg_delay_sec / 60.0, 1)} min ({r.avg_delay_sec}s)"
                max_m = f"+{round(r.max_delay_sec / 60.0, 1)} min ({r.max_delay_sec}s)"
                md.append(
                    f"| **{r.route_name or r.route_id}** | `{avg_m}` | `{max_m}` | {r.tracked_vehicles} | `{r.on_time_pct}%` |"
                )
        else:
            md.append("| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |")

        md.extend([
            "",
            "---",
            "",
            "## ⏱️ Headway Regularity & Excess Wait Time (EWT)",
            "",
            "> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.",
            "",
            "| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |",
            "| :--- | :---: | :---: | :---: | :---: |",
        ])

        if snapshot.headway_metrics:
            for hw in snapshot.headway_metrics:
                md.append(
                    f"| **Route {hw.route_id}** | ~{hw.scheduled_headway_min}m | ~{hw.observed_headway_min}m | **`+{hw.excess_wait_time_min} min`** | `{hw.headway_regularity_score} / 100` |"
                )
        else:
            md.append("| *Insufficient route frequency data in current snapshot* | - | - | - | - |")

        md.extend([
            "",
            "---",
            "",
            "## 👻 Active Ghost Trips Sample",
            "",
            "| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |",
            "| :--- | :---: | :---: | :--- | :--- |",
        ])

        if snapshot.sample_ghost_trips:
            for g in snapshot.sample_ghost_trips:
                md.append(
                    f"| `{g['trip_id']}` | Route {g['route_id']} | `{g['start_time']}` | `{g['status']}` | {g['reason']} |"
                )
        else:
            md.append("| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |")

        # Historical trend table
        if history and len(history) > 1:
            md.extend([
                "",
                "---",
                "",
                "## 📈 Recent Reliability Trend (Git-Scraping History)",
                "",
                "| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |",
                "| :--- | :---: | :---: | :---: | :---: | :---: |",
            ])
            # Display last 8 records in reverse chronological order
            for h in reversed(history[-8:]):
                t_str = h["scan_time"][:19].replace("T", " ")
                md.append(
                    f"| `{t_str}` | `{h['ghost_bus_rate_pct']}%` | `{h['overall_on_time_pct']}%` | {h['total_scheduled_trips']} | {h['total_tracked_vehicles']} | `+{h['mean_delay_sec']}s` |"
                )

        md.extend([
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
            f"*Generated by Ghost Bus Tracker v0.1.0 at `{snapshot.scan_time}`.*",
        ])

        return "\n".join(md) + "\n"

    def write_markdown_report(
        self,
        snapshot: ReliabilitySnapshot,
        history: Optional[List[Dict[str, Any]]] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """Renders and writes the Markdown dashboard to disk."""
        target = output_path or self.report_path
        target.parent.mkdir(parents=True, exist_ok=True)
        content = self.generate_markdown(snapshot, history)
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Generated Markdown report at {target}")
        return target

    def generate_console_summary(self, snapshot: ReliabilitySnapshot) -> str:
        """Formats a clean terminal scorecard."""
        lines = [
            "=" * 60,
            f" [BUS] GHOST BUS TRACKER: {snapshot.agency.upper()}",
            f" Scan Time: {snapshot.scan_time}",
            "=" * 60,
            f" Scheduled Trips:    {snapshot.total_scheduled_trips}",
            f" Active GPS Fleet:   {snapshot.total_tracked_vehicles}",
            f" Confirmed Ghosts:   {snapshot.total_ghost_trips}",
            f" Ghost Bus Rate:     {snapshot.ghost_bus_rate_pct}%",
            f" On-Time Adherence:  {snapshot.overall_on_time_pct}%",
            f" Mean Delay:         +{snapshot.mean_delay_sec}s ({round(snapshot.mean_delay_sec / 60.0, 1)}m)",
            "-" * 60,
            " Delay Breakdown:",
            f"   On-Time (-1m..+5m): {snapshot.delay_distribution.on_time}",
            f"   Early (>1m early):  {snapshot.delay_distribution.early}",
            f"   Minor (+5m..+15m):  {snapshot.delay_distribution.minor_delay}",
            f"   Severe (>15m late): {snapshot.delay_distribution.severe_delay}",
            f"   Ghost / Missing:    {snapshot.delay_distribution.ghost}",
            "-" * 60,
        ]
        if snapshot.worst_routes_by_ghost:
            lines.append(" Top Worst Routes by Ghost Rate:")
            for r in snapshot.worst_routes_by_ghost[:5]:
                lines.append(
                    f"   Route {r.route_id:5s} | Ghost Rate: {r.ghost_rate_pct:5.1f}% ({r.ghost_trips}/{r.total_trips} trips) | Avg Delay: +{r.avg_delay_sec}s"
                )
            lines.append("=" * 60)
        return "\n".join(lines)
