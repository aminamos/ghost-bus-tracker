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

    # New Recommended Cities
    philly = config.get_preset("philly")
    assert philly is not None and philly["name"] == "SEPTA"
    assert config.get_preset("septa") == philly

    dc = config.get_preset("dc")
    assert dc is not None and dc["name"] == "WMATA"
    assert config.get_preset("wmata") == dc

    la = config.get_preset("la")
    assert la is not None and la["name"] == "LA Metro"
    assert config.get_preset("lametro") == la

    seattle = config.get_preset("seattle")
    assert seattle is not None and "King County" in seattle["agency"]
    assert config.get_preset("kcm") == seattle

    denver = config.get_preset("denver")
    assert denver is not None and denver["name"] == "RTD"
    assert config.get_preset("rtd") == denver

    portland = config.get_preset("portland")
    assert portland is not None and portland["name"] == "TriMet"
    assert config.get_preset("trimet") == portland

    atlanta = config.get_preset("atlanta")
    assert atlanta is not None and atlanta["name"] == "MARTA"
    assert config.get_preset("marta") == atlanta

    toronto = config.get_preset("toronto")
    assert toronto is not None and toronto["name"] == "TTC"
    assert config.get_preset("ttc") == toronto


def test_cli_presets_command(capsys):
    """Verify 'ghost-bus presets' prints available presets."""
    from src.cli import main
    code = main(["presets"])
    assert code == 0
    captured = capsys.readouterr()
    assert "CHICAGO" in captured.out
    assert "BOSTON" in captured.out
    assert "TWIN-CITIES" in captured.out
    assert "SF" in captured.out
    assert "PHILLY" in captured.out
    assert "DC" in captured.out
    assert "LA" in captured.out
    assert "SEATTLE" in captured.out
    assert "DENVER" in captured.out
    assert "PORTLAND" in captured.out
    assert "ATLANTA" in captured.out
    assert "TORONTO" in captured.out



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

    # Verify New Recommended Markets
    assert "SEPTA" in cities_content
    assert "Route 23 Germantown Ave" in cities_content
    assert "WMATA" in cities_content
    assert "Route S2 16th Street Line" in cities_content
    assert "LA Metro" in cities_content
    assert "Line 720 Wilshire Rapid" in cities_content
    assert "King County Metro" in cities_content
    assert "RapidRide E Line (Aurora)" in cities_content
    assert "RTD" in cities_content
    assert "Route 15 / 15L Colfax Ave" in cities_content
    assert "TriMet" in cities_content
    assert "Line 4 Division/Fessenden" in cities_content
    assert "MARTA" in cities_content
    assert "Route 83 Campbellton Rd" in cities_content
    assert "TTC" in cities_content
    assert "501 Queen Streetcar" in cities_content

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


def test_worker_mobility_catalog_integration():
    """Verify MobilityDatabase global catalog integration in Cloudflare Worker."""
    catalog_path = Path("worker/src/mobility_catalog.js")
    index_path = Path("worker/src/index.js")
    assert catalog_path.is_file(), "mobility_catalog.js should exist"
    assert index_path.is_file(), "index.js should exist"

    catalog_content = catalog_path.read_text(encoding="utf-8")
    index_content = index_path.read_text(encoding="utf-8")

    # Catalog contents
    assert "Broward County Transit" in catalog_content
    assert "Carcassonne Agglo" in catalog_content
    assert "Dallas Area Rapid Transit (DART)" in catalog_content
    assert "searchGlobalCatalog" in catalog_content
    assert "GLOBAL_TRANSIT_CATALOG" in catalog_content

    # Index integration
    assert "GLOBAL_TRANSIT_CATALOG" in index_content
    assert "searchGlobalCatalog" in index_content
    assert "/api/catalog" in index_content
    assert "/api/feeds" in index_content
    assert "catalogTable" in index_content
    assert "filterGlobalCatalog" in index_content
    assert "setCatalogFilter" in index_content


def test_cloudflare_worker_deploy_defaults():
    """Verify repository conforms with default Cloudflare Worker deploy standards."""
    root_wrangler = Path("wrangler.jsonc")
    worker_wrangler = Path("worker/wrangler.jsonc")
    root_pkg = Path("package.json")
    index_path = Path("worker/src/index.js")

    assert root_wrangler.is_file(), "Root wrangler.jsonc should exist for standard deploy"
    assert worker_wrangler.is_file(), "Worker wrangler.jsonc should exist"
    assert root_pkg.is_file(), "Root package.json should exist for standard npm deploy script"

    root_wrangler_text = root_wrangler.read_text(encoding="utf-8")
    assert "ghost-bus-tracker" in root_wrangler_text
    assert "worker/src/index.js" in root_wrangler_text
    assert "crons" in root_wrangler_text

    root_pkg_text = root_pkg.read_text(encoding="utf-8")
    assert '"deploy": "wrangler deploy"' in root_pkg_text

    index_text = index_path.read_text(encoding="utf-8")
    assert "scheduled(" in index_text
    assert 'request.method === "OPTIONS"' in index_text
    assert "/api/live/vp" in index_text
    assert "/api/live/tu" in index_text




