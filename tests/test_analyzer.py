"""Unit tests for ReliabilityAnalyzer module."""

import pytest
from src.analyzer import ReliabilityAnalyzer
from src.models import (
    ScheduleRelationship,
    TripSnapshot,
    VehicleSnapshot,
)


def test_identify_ghost_trips_canceled():
    """Verify that trips marked CANCELED are their own bucket, NOT ghosts."""
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
    assert annotated[0].is_canceled is True
    assert annotated[0].is_ghost is False
    assert annotated[0].ghost_reason is None


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
        # Trip 1: Active, On-Time (+60s), departs 08:00
        TripSnapshot(trip_id="T1", route_id="10", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=60, start_time="08:00:00"),
        # Trip 2: Active, Early (-90s), departs 08:15
        TripSnapshot(trip_id="T2", route_id="10", vehicle_id="V2", has_vehicle_assigned=True, delay_seconds=-90, start_time="08:15:00"),
        # Trip 3: Active, Minor Delay (+400s), departs 08:30, served by the SAME physical bus V1
        TripSnapshot(trip_id="T3", route_id="10", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=400, start_time="08:30:00"),
        # Trip 4: Active, Severe Delay (+1200s), departs 09:00
        TripSnapshot(trip_id="T4", route_id="20", vehicle_id="V4", has_vehicle_assigned=True, delay_seconds=1200, start_time="09:00:00"),
        # Trip 5: Ghost (No vehicle assigned, no GPS), departs 09:30
        TripSnapshot(trip_id="T5", route_id="20", vehicle_id=None, has_vehicle_assigned=False, start_time="09:30:00"),
        # Trip 6: CANCELED — own bucket, NOT a ghost, delay must be excluded from stats
        TripSnapshot(trip_id="T6", route_id="30", schedule_relationship=ScheduleRelationship.CANCELED.value, is_canceled=True, delay_seconds=300, start_time="10:00:00"),
    ]

    vehicles = [
        VehicleSnapshot(vehicle_id="V1", trip_id="T1", route_id="10"),
        VehicleSnapshot(vehicle_id="V2", trip_id="T2", route_id="10"),
        VehicleSnapshot(vehicle_id="V4", trip_id="T4", route_id="20"),
    ]

    snapshot = analyzer.analyze(vehicles, trips, feed_timestamp=1789345000)

    assert snapshot.total_scheduled_trips == 6
    assert snapshot.total_tracked_vehicles == 3
    assert snapshot.total_ghost_trips == 1
    assert snapshot.ghost_bus_rate_pct == pytest.approx(16.67)  # 1/6 * 100
    # Tracked = 6 - 1 ghost - 1 canceled = 4 -> 66.67%
    assert snapshot.vehicle_tracking_rate_pct == pytest.approx(66.67)

    # Delay distribution check: each category is a distinct bucket
    dist = snapshot.delay_distribution
    assert dist.on_time == 1
    assert dist.early == 1
    assert dist.minor_delay == 1
    assert dist.severe_delay == 1
    assert dist.ghost == 1
    assert dist.canceled == 1
    # Buckets partition the total — no canceled/ghost double counting
    assert (
        dist.early + dist.on_time + dist.minor_delay + dist.severe_delay
        + dist.ghost + dist.canceled
    ) == snapshot.total_scheduled_trips

    # Canceled trip's 300s delay excluded: mean(60, -90, 400, 1200) = 392.5
    assert snapshot.mean_delay_sec == pytest.approx(392.5)
    assert snapshot.median_delay_sec == pytest.approx(230.0)

    # On-time % out of tracked trips with delay = 1/4 = 25.0%
    assert snapshot.overall_on_time_pct == 25.0

    # Route metrics
    r10 = next(r for r in snapshot.route_metrics if r.route_id == "10")
    assert r10.total_trips == 3
    assert r10.ghost_trips == 0
    assert r10.canceled_trips == 0
    assert r10.ghost_rate_pct == 0.0
    # 3 tracked trips but only 2 UNIQUE vehicles (V1 serves T1 and T3)
    assert r10.tracked_vehicles == 2

    r20 = next(r for r in snapshot.route_metrics if r.route_id == "20")
    assert r20.total_trips == 2
    assert r20.ghost_trips == 1
    assert r20.ghost_rate_pct == 50.0
    assert r20.tracked_vehicles == 1  # V4 only; the ghost run has no vehicle

    r30 = next(r for r in snapshot.route_metrics if r.route_id == "30")
    assert r30.total_trips == 1
    assert r30.canceled_trips == 1
    assert r30.ghost_trips == 0
    assert r30.tracked_vehicles == 0

    # Only true ghosts appear in the sample list — not the canceled trip
    sample_ids = [g["trip_id"] for g in snapshot.sample_ghost_trips]
    assert sample_ids == ["T5"]

    # Headway metrics for route 10: real scheduled headway from start times
    # 08:00, 08:15, 08:30 -> median gap 900s = 15.0 min
    hw = next(h for h in snapshot.headway_metrics if h.route_id == "10")
    assert hw.scheduled_headway_min == pytest.approx(15.0)


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
        TripSnapshot(trip_id="T1", route_id="1", vehicle_id="V1", delay_seconds=0, start_time="08:00:00"),
        TripSnapshot(trip_id="T2", route_id="1", vehicle_id="V2", delay_seconds=600, start_time="08:15:00"),
        TripSnapshot(trip_id="T3", route_id="2", vehicle_id="V3", delay_seconds=10, start_time="08:05:00"),
    ]
    # Route 1 has 2 trips with variance; Route 2 has 1 trip
    metrics = analyzer.calculate_headway_metrics(trips)
    assert len(metrics) == 1
    assert metrics[0].route_id == "1"
    # Real scheduled headway from start_times: gap of 900s = 15.0 min
    assert metrics[0].scheduled_headway_min == pytest.approx(15.0)
    # Observed headway = scheduled + avg_delay (15 + 300s/60 = 20.0)
    assert metrics[0].observed_headway_min == pytest.approx(20.0)
    # Standard EWT = Var(headway)/(2*mean headway): pstdev(0,600)=300 ->
    # 300^2 / (2*900) = 50s = 0.83 min
    assert metrics[0].excess_wait_time_min == pytest.approx(0.83)
    assert metrics[0].headway_regularity_score <= 100.0


def test_headway_scheduled_from_median_start_time_gaps():
    """Scheduled headway comes from median gap of sorted non-canceled start_times."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(trip_id="T1", route_id="1", vehicle_id="V1", delay_seconds=0, start_time="08:00:00"),
        TripSnapshot(trip_id="T2", route_id="1", vehicle_id="V2", delay_seconds=0, start_time="08:10:00"),
        TripSnapshot(trip_id="T3", route_id="1", vehicle_id="V3", delay_seconds=0, start_time="08:30:00"),
        # Canceled trip at 08:05 must NOT skew the median gap (would give 5.0)
        TripSnapshot(trip_id="T4", route_id="1", is_canceled=True, delay_seconds=0, start_time="08:05:00"),
    ]
    metrics = analyzer.calculate_headway_metrics(trips)
    assert len(metrics) == 1
    # Sorted non-canceled starts 08:00, 08:10, 08:30 -> gaps 600s, 1200s -> median 900s
    assert metrics[0].scheduled_headway_min == pytest.approx(15.0)
    # Zero delay jitter -> perfect regularity and no excess wait
    assert metrics[0].excess_wait_time_min == pytest.approx(0.0)
    assert metrics[0].headway_regularity_score == pytest.approx(100.0)
    assert metrics[0].observed_headway_min == pytest.approx(15.0)


def test_headway_metrics_require_real_start_times():
    """Routes without parseable start_times produce no synthetic headway metric."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(trip_id="T1", route_id="1", vehicle_id="V1", delay_seconds=0),
        TripSnapshot(trip_id="T2", route_id="1", vehicle_id="V2", delay_seconds=600),
    ]
    metrics = analyzer.calculate_headway_metrics(trips)
    assert metrics == []


def test_tracked_vehicles_counts_unique_vehicles_per_route():
    """tracked_vehicles counts unique broadcasting vehicles, not trips."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        # Three trips on route 7, but only two physical buses (V1 serves T1 and T3)
        TripSnapshot(trip_id="T1", route_id="7", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=0),
        TripSnapshot(trip_id="T2", route_id="7", vehicle_id="V2", has_vehicle_assigned=True, delay_seconds=0),
        TripSnapshot(trip_id="T3", route_id="7", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=0),
    ]
    vehicles = [
        VehicleSnapshot(vehicle_id="V1", trip_id="T1", route_id="7"),
        VehicleSnapshot(vehicle_id="V2", trip_id="T2", route_id="7"),
    ]
    snapshot = analyzer.analyze(vehicles, trips)
    r7 = next(r for r in snapshot.route_metrics if r.route_id == "7")
    assert r7.total_trips == 3
    assert r7.tracked_vehicles == 2  # unique {V1, V2}, not 3


def test_canceled_trip_not_tracked_or_ghost_in_snapshot():
    """A canceled trip lands only in the canceled bucket of the snapshot."""
    analyzer = ReliabilityAnalyzer()
    trips = [
        TripSnapshot(trip_id="T1", route_id="5", vehicle_id="V1", has_vehicle_assigned=True, delay_seconds=100),
        TripSnapshot(trip_id="T2", route_id="5", schedule_relationship=ScheduleRelationship.CANCELED.value, is_canceled=True, delay_seconds=9999),
    ]
    vehicles = [VehicleSnapshot(vehicle_id="V1", trip_id="T1", route_id="5")]

    snapshot = analyzer.analyze(vehicles, trips)

    assert snapshot.total_ghost_trips == 0
    assert snapshot.delay_distribution.ghost == 0
    assert snapshot.delay_distribution.canceled == 1
    # Canceled trip's 9999s delay is excluded from delay stats
    assert snapshot.mean_delay_sec == pytest.approx(100.0)
    # Ghost rate and sample list reflect only true ghosts
    assert snapshot.ghost_bus_rate_pct == 0.0
    assert all(g["trip_id"] != "T2" for g in snapshot.sample_ghost_trips)

    r5 = next(r for r in snapshot.route_metrics if r.route_id == "5")
    assert r5.total_trips == 2
    assert r5.canceled_trips == 1
    assert r5.ghost_trips == 0
    assert r5.tracked_vehicles == 1
