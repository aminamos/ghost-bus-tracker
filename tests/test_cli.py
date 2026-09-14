"""Unit tests for the CLI entrypoint."""

import json
from pathlib import Path
import pytest

from src.cli import main


def test_cli_version(capsys):
    """Test `ghost-bus --version`."""
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "0.1.0" in captured.out or "ghost-bus" in captured.out


def test_cli_help(capsys):
    """Test `ghost-bus --help`."""
    with pytest.raises(SystemExit) as exc:
        main(["--help"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "scan" in captured.out
    assert "report" in captured.out
    assert "summary" in captured.out


def test_cli_scan_sample(tmp_path):
    """Test `ghost-bus scan --sample --save --report`."""
    latest_file = tmp_path / "latest.json"
    history_file = tmp_path / "history.json"
    report_file = tmp_path / "RELIABILITY.md"

    code = main([
        "scan",
        "--sample",
        "--save",
        "--report",
        "--quiet",
        "--latest-file", str(latest_file),
        "--history-file", str(history_file),
        "--report-file", str(report_file),
    ])

    assert code == 0
    assert latest_file.is_file()
    assert history_file.is_file()
    assert report_file.is_file()

    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["total_scheduled_trips"] > 0


def test_cli_summary(tmp_path, capsys):
    """Test `ghost-bus summary --input <path>`."""
    snapshot_file = tmp_path / "snapshot.json"
    snapshot_data = {
        "scan_time": "2026-09-14T00:00:00Z",
        "agency": "Test Transit",
        "total_scheduled_trips": 50,
        "total_tracked_vehicles": 45,
        "total_ghost_trips": 5,
        "ghost_bus_rate_pct": 10.0,
        "vehicle_tracking_rate_pct": 90.0,
        "overall_on_time_pct": 80.0,
        "delay_distribution": {
            "early": 2, "on_time": 35, "minor_delay": 5, "severe_delay": 3, "ghost": 5, "canceled": 0
        },
        "mean_delay_sec": 90.0,
        "median_delay_sec": 30.0,
        "worst_routes_by_ghost": [],
        "most_delayed_routes": [],
        "route_metrics": [],
        "sample_ghost_trips": [],
        "headway_metrics": [],
    }
    snapshot_file.write_text(json.dumps(snapshot_data), encoding="utf-8")

    code = main(["summary", "--input", str(snapshot_file)])
    assert code == 0
    captured = capsys.readouterr()
    assert "TEST TRANSIT" in captured.out
    assert "Ghost Bus Rate:     10.0%" in captured.out


def test_cli_report(tmp_path):
    """Test `ghost-bus report --input <path> --output <path>`."""
    snapshot_file = tmp_path / "snapshot.json"
    report_file = tmp_path / "output.md"

    snapshot_data = {
        "scan_time": "2026-09-14T00:00:00Z",
        "agency": "Test Transit",
        "total_scheduled_trips": 20,
        "total_tracked_vehicles": 18,
        "total_ghost_trips": 2,
        "ghost_bus_rate_pct": 10.0,
        "vehicle_tracking_rate_pct": 90.0,
        "overall_on_time_pct": 85.0,
        "delay_distribution": {
            "early": 0, "on_time": 15, "minor_delay": 2, "severe_delay": 1, "ghost": 2, "canceled": 0
        },
        "mean_delay_sec": 50.0,
        "median_delay_sec": 20.0,
        "worst_routes_by_ghost": [],
        "most_delayed_routes": [],
        "route_metrics": [],
        "sample_ghost_trips": [],
        "headway_metrics": [],
    }
    snapshot_file.write_text(json.dumps(snapshot_data), encoding="utf-8")

    code = main(["report", "--input", str(snapshot_file), "--output", str(report_file)])
    assert code == 0
    assert report_file.is_file()
    assert "Executive Summary Scorecard" in report_file.read_text(encoding="utf-8")
