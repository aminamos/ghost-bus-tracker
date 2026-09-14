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
        with patch.object(FeedFetcher, "load_sample_feeds", side_effect=Exception("Sample failed")):
            code = main([
                "scan",
                "--live",
                "--quiet",
                "--latest-file", str(tmp_path / "none.json"),
            ])
            assert code == 1


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

    code = main([
        "report",
        "--input", str(missing_input),
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
