"""Unit tests for ReliabilityAnalyzer module."""

import pytest
from src.analyzer import ReliabilityAnalyzer
from src.models import (
    ScheduleRelationship,
    TripSnapshot,
    VehicleSnapshot,
)


def test_identify_ghost_trips_canceled():
    """Verify that trips marked CANCELED are identified as ghosts."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(
            trip_id="T1",
            route_id="5",
            schedule_relationship=ScheduleRelationship.CANCELED.value,
            is_canceled=True,
        )
    ]
    vehicles = []

    annotated = analyzer.identify_ghost_trips(trips, vehicles)
    assert len(annotated) == 1
    assert annotated[0].is_ghost is True
    assert "CANCELED" in annotated[0].ghost_reason


def test_identify_ghost_trips_missing_vehicle_and_gps():
    """Verify that unassigned trips with no GPS transponder are ghosts."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(
            trip_id="T2",
            route_id="5",
            vehicle_id=None,
            has_vehicle_assigned=False,
        )
    ]
    vehicles = []

    annotated = analyzer.identify_ghost_trips(trips, vehicles)
    assert len(annotated) == 1
    assert annotated[0].is_ghost is True
    assert "No vehicle assigned" in annotated[0].ghost_reason


def test_identify_ghost_trips_assigned_vehicle_offline():
    """Verify that trips with assigned vehicle that is not broadcasting are ghosts."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(
            trip_id="T3",
            route_id="5",
            vehicle_id="bus_777",
            has_vehicle_assigned=True,
        )
    ]
    # Vehicles contains a different bus
    vehicles = [
        VehicleSnapshot(vehicle_id="bus_888", trip_id="T99", route_id="10")
    ]

    annotated = analyzer.identify_ghost_trips(trips, vehicles)
    assert len(annotated) == 1
    assert annotated[0].is_ghost is True
    assert "missing from active GPS" in annotated[0].ghost_reason


def test_identify_active_trip_not_ghost():
    """Verify that a trip with active matching vehicle broadcast is NOT a ghost."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(
            trip_id="T4",
            route_id="5",
            vehicle_id="bus_501",
            has_vehicle_assigned=True,
            delay_seconds=45,
        )
    ]
    vehicles = [
        VehicleSnapshot(vehicle_id="bus_501", trip_id="T4", route_id="5")
    ]

    annotated = analyzer.identify_ghost_trips(trips, vehicles)
    assert len(annotated) == 1
    assert annotated[0].is_ghost is False
    assert annotated[0].ghost_reason is None


def test_full_analysis_calculation():
    """Test full analysis calculation and metric formulas."""
    analyzer = ReliabilityAnalyzer()

    trips = [
        # Trip 1: Active, On-Time (+60s)
        TripSnapshot(trip_id="T1", route_id="10", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=60),
        # Trip 2: Active, Early (-90s)
        TripSnapshot(trip_id="T2", route_id="10", vehicle_id="V2", has_vehicle_assigned=True, delay_seconds=-90),
        # Trip 3: Active, Minor Delay (+400s)
        TripSnapshot(trip_id="T3", route_id="10", vehicle_id="V3", has_vehicle_assigned=True, delay_seconds=400),
        # Trip 4: Active, Severe Delay (+1200s)
        TripSnapshot(trip_id="T4", route_id="20", vehicle_id="V4", has_vehicle_assigned=True, delay_seconds=1200),
        # Trip 5: Ghost (No vehicle assigned, no GPS)
        TripSnapshot(trip_id="T5", route_id="20", vehicle_id=None, has_vehicle_assigned=False),
    ]

    vehicles = [
        VehicleSnapshot(vehicle_id="V1", trip_id="T1", route_id="10"),
        VehicleSnapshot(vehicle_id="V2", trip_id="T2", route_id="10"),
        VehicleSnapshot(vehicle_id="V3", trip_id="T3", route_id="10"),
        VehicleSnapshot(vehicle_id="V4", trip_id="T4", route_id="20"),
    ]

    snapshot = analyzer.analyze(vehicles, trips, feed_timestamp=1789345000)

    assert snapshot.total_scheduled_trips == 5
    assert snapshot.total_tracked_vehicles == 4
    assert snapshot.total_ghost_trips == 1
    assert snapshot.ghost_bus_rate_pct == 20.0  # 1/5 * 100
    assert snapshot.vehicle_tracking_rate_pct == 80.0  # 4/5 * 100

    # Delay distribution check
    dist = snapshot.delay_distribution
    assert dist.on_time == 1
    assert dist.early == 1
    assert dist.minor_delay == 1
    assert dist.severe_delay == 1
    assert dist.ghost == 1

    # On-time % out of tracked trips with delay = 1/4 = 25.0%
    assert snapshot.overall_on_time_pct == 25.0

    # Route metrics
    r10 = next(r for r in snapshot.route_metrics if r.route_id == "10")
    assert r10.total_trips == 3
    assert r10.ghost_trips == 0
    assert r10.ghost_rate_pct == 0.0

    r20 = next(r for r in snapshot.route_metrics if r.route_id == "20")
    assert r20.total_trips == 2
    assert r20.ghost_trips == 1
    assert r20.ghost_rate_pct == 50.0


def test_analyze_empty_feeds():
    """Verify that analyzer handles empty feeds gracefully without division by zero."""
    analyzer = ReliabilityAnalyzer()
    snapshot = analyzer.analyze([], [])

    assert snapshot.total_scheduled_trips == 0
    assert snapshot.total_tracked_vehicles == 0
    assert snapshot.total_ghost_trips == 0
    assert snapshot.ghost_bus_rate_pct == 0.0
    assert snapshot.overall_on_time_pct == 0.0
    assert snapshot.worst_routes_by_ghost == []
    assert snapshot.route_metrics == []


def test_headway_regularity_calculation():
    """Test Excess Wait Time (EWT) and headway regularity metrics."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(trip_id="T1", route_id="1", vehicle_id="V1", delay_seconds=0),
        TripSnapshot(trip_id="T2", route_id="1", vehicle_id="V2", delay_seconds=600),
        TripSnapshot(trip_id="T3", route_id="2", vehicle_id="V3", delay_seconds=10),
    ]
    # Route 1 has 2 trips with variance; Route 2 has 1 trip
    metrics = analyzer.calculate_headway_metrics(trips)
    assert len(metrics) == 1
    assert metrics[0].route_id == "1"
    assert metrics[0].excess_wait_time_min > 0.0
    assert metrics[0].headway_regularity_score <= 100.0
