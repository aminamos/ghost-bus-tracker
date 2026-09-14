"""Additional tests to maximize branch coverage across CLI and edge cases."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

from src.cli import main, run_scan
from src.fetcher import FeedFetcher
from src.reporter import ReportGenerator


def test_cli_scan_live_with_fallback(tmp_path):
    """Test scan with live flag and fallback when mock fails."""
    latest_file = tmp_path / "latest.json"
    history_file = tmp_path / "history.json"
    report_file = tmp_path / "RELIABILITY.md"

    real_read = FeedFetcher._read_bytes

    def fake_read(self, source):
        if str(source).startswith("http"):
            raise requests.ConnectionError("Network down")
        return real_read(self, source)

    with patch.object(FeedFetcher, "_read_bytes", side_effect=fake_read, autospec=True):
        code = main([
            "scan",
            "--live",
            "--save",
            "--report",
            "--quiet",
            "--fallback-sample",
            "--latest-file", str(latest_file),
            "--history-file", str(history_file),
            "--report-file", str(report_file),
        ])
        assert code == 0
        assert latest_file.is_file()


def test_cli_scan_error_without_fallback(tmp_path):
    """Test scan error when network fails and fallback is disabled."""
    with patch.object(FeedFetcher, "fetch_vehicle_positions", side_effect=Exception("Network failure")):
        code = main([
            "scan",
            "--live",
            "--no-fallback-sample",
            "--debug",
            "--quiet",
            "--latest-file", str(tmp_path / "none.json"),
        ])
        assert code == 1


def test_cli_scan_report_without_save_and_with_summary(tmp_path, capsys):
    """Test scan with --report, without --save, and without --quiet."""
    report_file = tmp_path / "RELIABILITY.md"
    code = main([
        "scan",
        "--sample",
        "--report",
        "--latest-file", str(tmp_path / "latest.json"),
        "--history-file", str(tmp_path / "history.json"),
        "--report-file", str(report_file),
    ])
    assert code == 0
    assert report_file.is_file()
    captured = capsys.readouterr()
    assert "Ghost Bus Rate" in captured.out or "TRANSIT" in captured.out


def test_cli_report_corrupted_history(tmp_path, sample_snapshot):
    """Test report subcommand when history.json exists but is corrupted."""
    input_file = tmp_path / "latest.json"
    input_file.write_text(sample_snapshot.model_dump_json(), encoding="utf-8")
    bad_hist = tmp_path / "history.json"
    bad_hist.write_text("{ corrupt json", encoding="utf-8")
    report_file = tmp_path / "RELIABILITY.md"

    code = main([
        "report",
        "--input", str(input_file),
        "--history", str(bad_hist),
        "--output", str(report_file),
    ])
    assert code == 0
    assert report_file.is_file()


def test_cli_report_corrupted_input_file(tmp_path):
    """Test report subcommand when input snapshot is corrupted."""
    bad_input = tmp_path / "bad_latest.json"
    bad_input.write_text("{ invalid json", encoding="utf-8")
    report_file = tmp_path / "RELIABILITY.md"

    code = main([
        "report",
        "--input", str(bad_input),
        "--output", str(report_file),
    ])
    assert code == 1


def test_cli_unknown_command_fallback(capsys):
    """Test cli main falls back to printing help when command is unknown."""
    import argparse
    with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(command="unknown_action")):
        code = main([])
        assert code == 1
    captured = capsys.readouterr()
    assert "usage:" in captured.out or "usage:" in captured.err


def test_fetcher_read_bytes_from_raw_bytes():
    """Test FeedFetcher._read_bytes directly returning raw bytes."""
    fetcher = FeedFetcher()
    raw = b"protobuf_raw_bytes"
    assert fetcher._read_bytes(raw) == raw


def test_fetcher_parse_vehicle_positions_skips_non_vehicle():
    """Test parse_vehicle_positions skips feed entities without vehicle field."""
    from google.transit import gtfs_realtime_pb2

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.header.gtfs_realtime_version = "2.0"
    feed.header.timestamp = 1700000000

    entity1 = feed.entity.add()
    entity1.id = "trip_only"
    entity1.trip_update.trip.trip_id = "t1"

    entity2 = feed.entity.add()
    entity2.id = "v1"
    entity2.vehicle.vehicle.id = "bus_101"

    fetcher = FeedFetcher()
    vehicles, ts = fetcher.parse_vehicle_positions(feed.SerializeToString())
    assert ts == 1700000000
    assert len(vehicles) == 1
    assert vehicles[0].vehicle_id == "bus_101"


def test_fetcher_parse_trip_updates_skips_non_trip_update():
    """Test parse_trip_updates skips feed entities without trip_update field."""
    from google.transit import gtfs_realtime_pb2

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.header.gtfs_realtime_version = "2.0"
    feed.header.timestamp = 1700000000

    entity1 = feed.entity.add()
    entity1.id = "v1"
    entity1.vehicle.vehicle.id = "bus_101"

    entity2 = feed.entity.add()
    entity2.id = "t1"
    entity2.trip_update.trip.trip_id = "trip_202"

    fetcher = FeedFetcher()
    trips, ts = fetcher.parse_trip_updates(feed.SerializeToString())
    assert ts == 1700000000
    assert len(trips) == 1
    assert trips[0].trip_id == "trip_202"


def test_cli_summary_missing_file(tmp_path, capsys):
    """Test summary command when target file does not exist."""
    missing = tmp_path / "not_there.json"
    code = main(["summary", "--input", str(missing)])
    assert code == 1


def test_cli_summary_corrupted_file(tmp_path, capsys):
    """Test summary command when file has invalid json."""
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("invalid json content!", encoding="utf-8")
    code = main(["summary", "--input", str(bad_file)])
    assert code == 1


def test_cli_report_fallback_scan(tmp_path):
    """Test report command auto-triggering scan when input file is missing."""
    target_report = tmp_path / "auto_gen.md"
    missing_input = tmp_path / "auto_snap.json"
    target_history = tmp_path / "history.json"

    code = main([
        "report",
        "--input", str(missing_input),
        "--history", str(target_history),
        "--output", str(target_report),
    ])
    assert code == 0
    assert target_report.is_file()


def test_cli_no_args():
    """Test calling CLI with no args prints help and returns 0."""
    code = main([])
    assert code == 0


def test_reporter_corrupted_history_recovery(tmp_path, sample_snapshot):
    """Test that corrupted history.json is safely recovered."""
    bad_history = tmp_path / "bad_hist.json"
    bad_history.write_text("{ corrupt json", encoding="utf-8")

    reporter = ReportGenerator(history_path=bad_history)
    hist = reporter.update_history_json(sample_snapshot, history_path=bad_history)
    assert len(hist) == 1
