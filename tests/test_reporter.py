"""Unit tests for ReportGenerator module."""

import json
from pathlib import Path
import pytest
from src.models import ReliabilitySnapshot
from src.reporter import ReportGenerator


def test_save_latest_json(tmp_path, sample_snapshot):
    """Test saving latest snapshot to JSON file."""
    output_file = tmp_path / "latest.json"
    reporter = ReportGenerator(latest_path=output_file)

    saved = reporter.save_latest_json(sample_snapshot, output_path=output_file)
    assert saved.is_file()

    with open(saved, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["agency"] == "Metro Transit Test"
    assert data["ghost_bus_rate_pct"] == 30.0
    assert data["total_scheduled_trips"] == 10
    assert len(data["sample_ghost_trips"]) == 1


def test_update_history_json(tmp_path, sample_snapshot):
    """Test updating and appending to history.json with max limit."""
    history_file = tmp_path / "history.json"
    reporter = ReportGenerator(history_path=history_file)

    # First entry
    h1 = reporter.update_history_json(sample_snapshot, history_path=history_file, max_entries=2)
    assert len(h1) == 1
    assert h1[0]["ghost_bus_rate_pct"] == 30.0

    # Second entry
    h2 = reporter.update_history_json(sample_snapshot, history_path=history_file, max_entries=2)
    assert len(h2) == 2

    # Third entry (should cap at 2)
    h3 = reporter.update_history_json(sample_snapshot, history_path=history_file, max_entries=2)
    assert len(h3) == 2


def test_generate_markdown_content(sample_snapshot):
    """Test generation of Markdown dashboard text."""
    reporter = ReportGenerator()
    history = [
        {"scan_time": "2026-09-13T23:00:00Z", "ghost_bus_rate_pct": 25.0, "overall_on_time_pct": 75.0, "total_scheduled_trips": 10, "total_tracked_vehicles": 7, "total_ghost_trips": 2, "mean_delay_sec": 100.0},
        {"scan_time": "2026-09-14T00:00:00Z", "ghost_bus_rate_pct": 30.0, "overall_on_time_pct": 71.4, "total_scheduled_trips": 10, "total_tracked_vehicles": 7, "total_ghost_trips": 3, "mean_delay_sec": 120.0},
    ]

    md = reporter.generate_markdown(sample_snapshot, history=history)

    assert "# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker" in md
    assert "Metro Transit Test" in md
    assert "30.0%" in md
    assert "Executive Summary Scorecard" in md
    assert "Delay & Reliability Breakdown" in md
    assert "Top Worst Routes by Ghost Bus Rate" in md
    assert "Recent Reliability Trend" in md
    assert "Methodology & Definitions" in md


def test_write_markdown_report_to_disk(tmp_path, sample_snapshot):
    """Test writing markdown report file to disk."""
    report_file = tmp_path / "RELIABILITY.md"
    reporter = ReportGenerator(report_path=report_file)

    target = reporter.write_markdown_report(sample_snapshot, output_path=report_file)
    assert target.is_file()
    content = target.read_text(encoding="utf-8")
    assert "Scorecard" in content


def test_console_summary(sample_snapshot):
    """Test terminal summary scorecard formatting."""
    reporter = ReportGenerator()
    summary = reporter.generate_console_summary(sample_snapshot)

    assert "GHOST BUS TRACKER" in summary
    assert "Scheduled Trips:    10" in summary
    assert "Ghost Bus Rate:     30.0%" in summary
    assert "Route 2" in summary
