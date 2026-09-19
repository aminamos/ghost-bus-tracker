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


def test_agency_presets_config():
    """Verify built-in agency presets for Chicago, Boston, Minneapolis, and NYC."""
    chicago = config.get_preset("chicago")
    assert chicago is not None
    assert chicago["name"] == "CTA"
    assert "Chicago" in chicago["city"]
    assert chicago["requires_key"] is True

    # Test aliases
    assert config.get_preset("cta") == chicago

    boston = config.get_preset("boston")
    assert boston is not None
    assert boston["name"] == "MBTA"
    assert boston["requires_key"] is False
    assert config.get_preset("mbta") == boston

    twin_cities = config.get_preset("twin-cities")
    assert twin_cities is not None
    assert config.get_preset("msp") == twin_cities
    assert config.get_preset("mpls") == twin_cities

    sf = config.get_preset("sf")
    assert sf is not None
    assert sf["name"] == "SFMTA"
    assert "San Francisco" in sf["city"]
    assert config.get_preset("sfmta") == sf
    assert config.get_preset("muni") == sf
    assert config.get_preset("san-francisco") == sf


def test_cli_presets_command(capsys):
    """Verify 'ghost-bus presets' prints available presets."""
    from src.cli import main
    code = main(["presets"])
    assert code == 0
    captured = capsys.readouterr()
    assert "CHICAGO" in captured.out
    assert "BOSTON" in captured.out
    assert "TWIN-CITIES" in captured.out
    assert "CTA" in captured.out
    assert "MBTA" in captured.out


def test_cli_scan_with_preset_sample(tmp_path):
    """Verify 'ghost-bus scan --preset chicago --sample' works."""
    from src.cli import main
    latest_file = tmp_path / "latest_chicago.json"
    history_file = tmp_path / "history_chicago.json"
    code = main([
        "scan",
        "--preset", "chicago",
        "--sample",
        "--save",
        "--quiet",
        "--latest-file", str(latest_file),
        "--history-file", str(history_file),
        "--report-file", str(tmp_path / "RELIABILITY.md"),
    ])
    assert code == 0
    assert latest_file.is_file()
    assert history_file.is_file()
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["city"] == "Chicago, IL"
    assert data["transit_system"] == "CTA"


def test_cli_scan_unknown_preset():
    """Verify scanning an invalid preset returns error."""
    from src.cli import main
    code = main(["scan", "--preset", "atlantis-transit"])
    assert code == 1


def test_worker_multi_city_data_and_location_switching():
    """Verify worker files support interactive location switching from Minneapolis to SF, Chicago, etc."""
    worker_dir = Path(__file__).parent.parent / "worker" / "src"
    cities_file = worker_dir / "cities_data.js"
    index_file = worker_dir / "index.js"

    assert cities_file.is_file(), "worker/src/cities_data.js must exist"
    assert index_file.is_file(), "worker/src/index.js must exist"

    cities_content = cities_file.read_text(encoding="utf-8")
    index_content = index_file.read_text(encoding="utf-8")

    # Verify San Francisco SFMTA Muni data and specific routes
    assert "San Francisco, CA" in cities_content
    assert "SFMTA (Muni)" in cities_content
    assert "14R Mission Rapid" in cities_content
    assert "38R Geary Rapid" in cities_content

    # Verify Chicago CTA and Boston MBTA
    assert "Chicago Transit Authority" in cities_content
    assert "79 79th" in cities_content
    assert "Massachusetts Bay Transportation Authority" in cities_content
    assert "1 Harvard - Nubian" in cities_content

    # Verify interactive UI elements in index.js
    assert "switchCity" in index_content
    assert "renderTrendChart" in index_content
    assert "market-chips" in index_content
    assert "city-chip" in index_content
    assert "chartContainer" in index_content


def test_cli_scan_with_sf_preset_sample(tmp_path):
    """Verify scanning SF preset with sample feeds sets location metadata properly."""
    from src.cli import main
    latest_file = tmp_path / "latest_sf.json"
    history_file = tmp_path / "history_sf.json"
    code = main([
        "scan",
        "--preset", "sf",
        "--sample",
        "--save",
        "--quiet",
        "--latest-file", str(latest_file),
        "--history-file", str(history_file),
        "--report-file", str(tmp_path / "RELIABILITY.md"),
    ])
    assert code == 0
    assert latest_file.is_file()
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["city"] == "San Francisco, CA"
    assert data["transit_system"] == "SFMTA"


