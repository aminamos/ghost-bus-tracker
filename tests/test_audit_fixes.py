"""Regression tests for the audit fix batch (crash, metrics, CLI defaults)."""

import json

from src import config
from src.analyzer import ReliabilityAnalyzer
from src.cli import build_parser, main
from src.fetcher import FeedFetcher
from src.models import TripSnapshot, VehicleSnapshot


def test_get_preset_normalizes_underscores():
    assert config.get_preset("twin_cities")["id"] == "twin-cities"
    assert config.get_preset("twin-cities")["id"] == "twin-cities"
    assert config.get_preset("new_york")["id"] == "nyc"
    assert config.get_preset("cta")["id"] == "chicago"


def test_fallback_sample_defaults_off():
    args = build_parser().parse_args(["scan"])
    assert args.fallback_sample is False


def test_live_and_sample_conflict():
    assert main(["scan", "--live", "--sample", "--quiet"]) == 1


def test_preset_chicago_missing_files_fails_cleanly():
    """Exercises the requires_key block (os.getenv) without network access."""
    code = main([
        "scan", "--preset", "chicago",
        "--vp-feed", "/nonexistent-vp-123.pb",
        "--tu-feed", "/nonexistent-tu-123.pb",
        "--quiet",
    ])
    assert code == 1


def test_ghost_pairing_busy_vehicle_is_ghost():
    analyzer = ReliabilityAnalyzer()
    trips = [TripSnapshot(trip_id="T", route_id="5", vehicle_id="V", has_vehicle_assigned=True)]
    vehicles = [VehicleSnapshot(vehicle_id="V", trip_id="OTHER", route_id="5")]
    annotated = analyzer.identify_ghost_trips(trips, vehicles)
    assert annotated[0].is_ghost is True


def test_ghost_pairing_substitute_bus_covers_trip():
    analyzer = ReliabilityAnalyzer()
    trips = [TripSnapshot(trip_id="T", route_id="5", vehicle_id="V1", has_vehicle_assigned=True)]
    vehicles = [VehicleSnapshot(vehicle_id="V2", trip_id="T", route_id="5")]
    annotated = analyzer.identify_ghost_trips(trips, vehicles)
    assert annotated[0].is_ghost is False


def test_headway_splits_directions():
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(trip_id="A1", route_id="1", direction_id=0, delay_seconds=0, start_time="08:00:00"),
        TripSnapshot(trip_id="A2", route_id="1", direction_id=0, delay_seconds=0, start_time="08:30:00"),
        TripSnapshot(trip_id="B1", route_id="1", direction_id=1, delay_seconds=0, start_time="08:15:00"),
        TripSnapshot(trip_id="B2", route_id="1", direction_id=1, delay_seconds=0, start_time="08:45:00"),
    ]
    metrics = analyzer.calculate_headway_metrics(trips)
    assert len(metrics) == 2
    assert {m.scheduled_headway_min for m in metrics} == {30.0}
    assert all(m.observed_headway_min == m.scheduled_headway_min for m in metrics)


def test_early_trips_count_against_route_on_time():
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(trip_id="T1", route_id="9", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=60),
        TripSnapshot(trip_id="T2", route_id="9", vehicle_id="V2", has_vehicle_assigned=True, delay_seconds=-90),
        TripSnapshot(trip_id="T3", route_id="9", vehicle_id="V3", has_vehicle_assigned=True, delay_seconds=-120),
    ]
    vehicles = [
        VehicleSnapshot(vehicle_id="V1", trip_id="T1", route_id="9"),
        VehicleSnapshot(vehicle_id="V2", trip_id="T2", route_id="9"),
        VehicleSnapshot(vehicle_id="V3", trip_id="T3", route_id="9"),
    ]
    snapshot = analyzer.analyze(vehicles, trips)
    route = next(r for r in snapshot.route_metrics if r.route_id == "9")
    assert route.on_time_pct == 33.33


def test_e2e_mock_feeds_ghost_and_canceled_buckets(mock_gtfs_rt_bytes):
    vp_bytes, tu_bytes = mock_gtfs_rt_bytes
    fetcher = FeedFetcher()
    vehicles, _ = fetcher.parse_vehicle_positions(vp_bytes)
    trips, _ = fetcher.parse_trip_updates(tu_bytes)
    snapshot = ReliabilityAnalyzer().analyze(vehicles, trips)
    assert snapshot.total_scheduled_trips == 5
    ghost_ids = {g["trip_id"] for g in snapshot.sample_ghost_trips}
    assert ghost_ids == {"trip_103", "trip_105"}
    assert snapshot.delay_distribution.canceled == 1
    canceled = [t for t in trips if t.trip_id == "trip_104"][0]
    assert canceled.is_canceled is True


def test_sample_scan_with_foreign_preset_stays_twin_cities(tmp_path):
    latest = tmp_path / "latest.json"
    history = tmp_path / "history.json"
    report = tmp_path / "RELIABILITY.md"
    code = main([
        "scan", "--preset", "sf", "--sample", "--save",
        "--latest-file", str(latest),
        "--history-file", str(history),
        "--report-file", str(report),
        "--quiet",
    ])
    assert code == 0
    data = json.loads(latest.read_text(encoding="utf-8"))
    assert data["source"] == "sample"
    assert data["city"] == config.CITY_NAME


def test_history_defaults_to_unbounded(tmp_path, sample_snapshot):
    from src.reporter import ReportGenerator

    history_file = tmp_path / "history.json"
    reporter = ReportGenerator(history_path=history_file)
    for _ in range(3):
        history = reporter.update_history_json(sample_snapshot, history_path=history_file)
    assert len(history) == 3


def test_history_explicit_cap_still_trims(tmp_path, sample_snapshot):
    from src.reporter import ReportGenerator

    history_file = tmp_path / "history.json"
    reporter = ReportGenerator(history_path=history_file)
    for _ in range(3):
        history = reporter.update_history_json(
            sample_snapshot, history_path=history_file, max_entries=2
        )
    assert len(history) == 2


def test_scan_all_rejects_sample():
    from src.cli import run_scan_all
    import argparse

    args = argparse.Namespace(sample=True, presets=None)
    assert run_scan_all(args) == 1


def test_scan_all_skips_keyed_without_env(monkeypatch):
    for var in ["CTA_API_KEY", "MTA_API_KEY", "BAY_AREA_511_KEY", "WMATA_API_KEY",
                "TRIMET_APP_ID", "LAMETRO_API_KEY", "OBA_API_KEY", "SOCRATA_API_KEY"]:
        monkeypatch.delenv(var, raising=False)
    assert main(["scan-all", "--presets", "chicago,nyc,sf,dc,portland"]) == 0

def test_scan_all_unknown_preset_fails():
    assert main(["scan-all", "--presets", "atlantis"]) == 1


def test_resolve_api_key_order(monkeypatch):
    preset = config.get_preset("chicago")
    monkeypatch.delenv("CTA_API_KEY", raising=False)
    monkeypatch.delenv("SOCRATA_API_KEY", raising=False)
    assert config.resolve_api_key(preset) is None
    # A Socrata group token must not leak into an unrelated provider.
    monkeypatch.setenv("SOCRATA_API_KEY", "socrata-123")
    assert config.resolve_api_key(preset) is None
    monkeypatch.setenv("CTA_API_KEY", "cta-456")
    assert config.resolve_api_key(preset) == "cta-456"
    assert config.resolve_api_key(preset, cli_key="flag-789") == "flag-789"


def test_group_key_resolves_only_within_group(monkeypatch):
    socrata_preset = {"id": "soc", "requires_key": True, "key_group": "socrata"}
    monkeypatch.delenv("CTA_API_KEY", raising=False)
    monkeypatch.delenv("SOCRATA_API_KEY", raising=False)
    assert config.resolve_api_key(socrata_preset) is None
    monkeypatch.setenv("SOCRATA_API_KEY", "socrata-123")
    assert config.resolve_api_key(socrata_preset) == "socrata-123"
    # Same token does not unskip an unrelated keyed city.
    assert config.resolve_api_key(config.get_preset("chicago")) is None
