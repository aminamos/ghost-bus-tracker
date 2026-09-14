"""Pytest fixtures and mock GTFS-RT feed generators for Ghost Bus Tracker tests."""

import time
from pathlib import Path
import pytest
from google.transit import gtfs_realtime_pb2

from src.models import (
    DelayCategoryBreakdown,
    ReliabilitySnapshot,
    RouteReliability,
    TripSnapshot,
    VehicleSnapshot,
)


@pytest.fixture
def sample_data_dir() -> Path:
    """Returns the sample_data directory path."""
    return Path(__file__).resolve().parent.parent / "sample_data"


@pytest.fixture
def mock_gtfs_rt_bytes():
    """Generates synthetic GTFS-RT protobuf bytes for vehicle positions and trip updates."""
    # Build vehicle positions
    vp_feed = gtfs_realtime_pb2.FeedMessage()
    vp_feed.header.gtfs_realtime_version = "2.0"
    vp_feed.header.incrementality = 0
    vp_feed.header.timestamp = 1789345000

    # Vehicle 1: Active on Trip 101, Route 1
    ent1 = vp_feed.entity.add()
    ent1.id = "ent_v1"
    ent1.vehicle.trip.trip_id = "trip_101"
    ent1.vehicle.trip.route_id = "1"
    ent1.vehicle.vehicle.id = "bus_1001"
    ent1.vehicle.position.latitude = 44.9778
    ent1.vehicle.position.longitude = -93.2650
    ent1.vehicle.position.bearing = 180.0
    ent1.vehicle.position.speed = 12.5

    # Vehicle 2: Active on Trip 102, Route 1
    ent2 = vp_feed.entity.add()
    ent2.id = "ent_v2"
    ent2.vehicle.trip.trip_id = "trip_102"
    ent2.vehicle.trip.route_id = "1"
    ent2.vehicle.vehicle.id = "bus_1002"
    ent2.vehicle.position.latitude = 44.9800
    ent2.vehicle.position.longitude = -93.2700

    # Build trip updates
    tu_feed = gtfs_realtime_pb2.FeedMessage()
    tu_feed.header.gtfs_realtime_version = "2.0"
    tu_feed.header.incrementality = 0
    tu_feed.header.timestamp = 1789345000

    # Trip 101: Active with Vehicle 1001, on-time (delay=60s)
    tu1 = tu_feed.entity.add()
    tu1.id = "ent_tu1"
    tu1.trip_update.trip.trip_id = "trip_101"
    tu1.trip_update.trip.route_id = "1"
    tu1.trip_update.trip.schedule_relationship = 0  # SCHEDULED
    tu1.trip_update.vehicle.id = "bus_1001"
    stu1 = tu1.trip_update.stop_time_update.add()
    stu1.stop_sequence = 1
    stu1.departure.delay = 60

    # Trip 102: Active with Vehicle 1002, severe delay (delay=1200s)
    tu2 = tu_feed.entity.add()
    tu2.id = "ent_tu2"
    tu2.trip_update.trip.trip_id = "trip_102"
    tu2.trip_update.trip.route_id = "1"
    tu2.trip_update.vehicle.id = "bus_1002"
    stu2 = tu2.trip_update.stop_time_update.add()
    stu2.stop_sequence = 1
    stu2.departure.delay = 1200

    # Trip 103: Ghost Bus - scheduled in trip update with no vehicle assigned & no GPS
    tu3 = tu_feed.entity.add()
    tu3.id = "ent_tu3"
    tu3.trip_update.trip.trip_id = "trip_103"
    tu3.trip_update.trip.route_id = "2"
    tu3.trip_update.trip.schedule_relationship = 0  # SCHEDULED
    stu3 = tu3.trip_update.stop_time_update.add()
    stu3.stop_sequence = 1
    stu3.departure.delay = 0

    # Trip 104: Explicitly CANCELED
    tu4 = tu_feed.entity.add()
    tu4.id = "ent_tu4"
    tu4.trip_update.trip.trip_id = "trip_104"
    tu4.trip_update.trip.route_id = "2"
    tu4.trip_update.trip.schedule_relationship = 3  # CANCELED

    # Trip 105: Ghost Bus - vehicle_id assigned ("bus_9999"), but that vehicle has no GPS broadcast
    tu5 = tu_feed.entity.add()
    tu5.id = "ent_tu5"
    tu5.trip_update.trip.trip_id = "trip_105"
    tu5.trip_update.trip.route_id = "3"
    tu5.trip_update.vehicle.id = "bus_9999"

    return vp_feed.SerializeToString(), tu_feed.SerializeToString()


@pytest.fixture
def sample_snapshot() -> ReliabilitySnapshot:
    """Provides a valid ReliabilitySnapshot object for testing reporting."""
    return ReliabilitySnapshot(
        scan_time="2026-09-14T00:00:00Z",
        feed_timestamp=1789345000,
        agency="Metro Transit Test",
        total_scheduled_trips=10,
        total_tracked_vehicles=7,
        total_ghost_trips=3,
        ghost_bus_rate_pct=30.0,
        vehicle_tracking_rate_pct=70.0,
        overall_on_time_pct=71.4,
        delay_distribution=DelayCategoryBreakdown(
            early=1,
            on_time=5,
            minor_delay=1,
            severe_delay=0,
            ghost=3,
            canceled=1,
        ),
        mean_delay_sec=120.0,
        median_delay_sec=60.0,
        worst_routes_by_ghost=[
            RouteReliability(
                route_id="2",
                route_name="Route 2",
                total_trips=4,
                tracked_vehicles=2,
                ghost_trips=2,
                canceled_trips=1,
                on_time_trips=2,
                delayed_trips=0,
                ghost_rate_pct=50.0,
                on_time_pct=100.0,
                avg_delay_sec=30.0,
                max_delay_sec=60,
            )
        ],
        most_delayed_routes=[],
        route_metrics=[],
        sample_ghost_trips=[
            {
                "trip_id": "trip_103",
                "route_id": "2",
                "start_time": "12:00:00",
                "start_date": "20260914",
                "status": "SCHEDULED",
                "reason": "No vehicle assigned and no active GPS broadcast",
            }
        ],
        headway_metrics=[],
    )
