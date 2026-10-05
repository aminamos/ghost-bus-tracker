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
