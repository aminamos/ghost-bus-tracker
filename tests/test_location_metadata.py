"""Tests verifying that city, transit system, and jurisdiction are properly surfaced."""

from pathlib import Path
import json

from src.models import ReliabilitySnapshot, DelayCategoryBreakdown
from src.analyzer import ReliabilityAnalyzer
from src.reporter import ReportGenerator
from src import config


def test_snapshot_includes_location_metadata():
    """Verify default and explicit city/transit system fields on ReliabilitySnapshot."""
    snapshot = ReliabilitySnapshot(
        scan_time="2026-09-19T12:00:00Z",
        agency="Metro Transit",
    )
    assert snapshot.city == "Minneapolis–Saint Paul, MN"
    assert snapshot.transit_system == "Metro Transit"
    assert "Twin Cities" in snapshot.region
    assert snapshot.state == "Minnesota"
    assert snapshot.country == "USA"


def test_reporter_surfaces_city_and_system():
    """Verify Markdown report and console summary explicitly declare city and transit system."""
    snapshot = ReliabilitySnapshot(
        scan_time="2026-09-19T12:00:00Z",
        agency="Metro Transit (Twin Cities)",
        city="Minneapolis–Saint Paul, MN",
        transit_system="Metro Transit",
        region="Twin Cities Metropolitan Area, Minnesota",
    )
    reporter = ReportGenerator()
    md = reporter.generate_markdown(snapshot)
    assert "Minneapolis–Saint Paul, MN" in md
    assert "Metro Transit" in md
    assert "Transit System:" in md
    assert "Location:" in md

    console = reporter.generate_console_summary(snapshot)
    assert "Minneapolis–Saint Paul, MN" in console
    assert "Metro Transit" in console


def test_worker_index_html_includes_city_and_system():
    """Verify the Cloudflare Worker HTML template clearly mentions city and transit system."""
    worker_index = Path(__file__).parent.parent / "worker" / "src" / "index.js"
    assert worker_index.exists(), "worker/src/index.js must exist"
    code = worker_index.read_text(encoding="utf-8")

    assert "Minneapolis &amp; Saint Paul" in code or "Minneapolis–Saint Paul" in code
    assert "Metro Transit" in code
    assert "Transit System &amp; Regional Coverage" in code
    assert "Twin Cities" in code
