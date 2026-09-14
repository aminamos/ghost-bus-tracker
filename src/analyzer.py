"""Analyzer module for transit reliability, ghost bus rates, and headway adherence."""

from datetime import datetime, timezone
import statistics
from typing import Any, Dict, List, Optional, Set
from src import config
from src.models import (
    DelayCategoryBreakdown,
    HeadwayMetric,
    ReliabilitySnapshot,
    RouteReliability,
    TripSnapshot,
    VehicleSnapshot,
)


class ReliabilityAnalyzer:
    """Analyzes vehicle positions and trip updates to identify ghost buses and reliability trends."""

    def __init__(
        self,
        early_threshold_sec: int = config.EARLY_THRESHOLD_SEC,
        on_time_threshold_sec: int = config.ON_TIME_THRESHOLD_SEC,
        minor_delay_threshold_sec: int = config.MINOR_DELAY_THRESHOLD_SEC,
        agency_name: str = config.AGENCY_NAME,
    ):
        self.early_threshold_sec = early_threshold_sec
        self.on_time_threshold_sec = on_time_threshold_sec
        self.minor_delay_threshold_sec = minor_delay_threshold_sec
        self.agency_name = agency_name

    def identify_ghost_trips(
        self, trips: List[TripSnapshot], vehicles: List[VehicleSnapshot]
    ) -> List[TripSnapshot]:
        """Correlates trips with active vehicle positions to flag ghost buses."""
        # Active vehicle trip IDs and vehicle IDs broadcasting GPS
        active_trip_ids: Set[str] = {v.trip_id for v in vehicles if v.trip_id}
        active_vehicle_ids: Set[str] = {v.vehicle_id for v in vehicles if v.vehicle_id}

        analyzed_trips: List[TripSnapshot] = []

        for trip in trips:
            updated_trip = trip.model_copy()

            # Condition 1: Explicitly marked CANCELED in GTFS-RT
            if updated_trip.is_canceled:
                updated_trip.is_ghost = True
                updated_trip.ghost_reason = "Scheduled trip marked CANCELED by agency"
            # Condition 2: Trip update exists but no vehicle assigned and no GPS broadcast for trip_id
            elif not updated_trip.has_vehicle_assigned and updated_trip.trip_id not in active_trip_ids:
                updated_trip.is_ghost = True
                updated_trip.ghost_reason = "No vehicle assigned and no active GPS broadcast"
            # Condition 3: Trip update has vehicle_id assigned, but that vehicle is NOT broadcasting in vehicle positions
            elif updated_trip.vehicle_id and updated_trip.vehicle_id not in active_vehicle_ids and updated_trip.trip_id not in active_trip_ids:
                updated_trip.is_ghost = True
                updated_trip.ghost_reason = f"Assigned vehicle {updated_trip.vehicle_id} is missing from active GPS transponder fleet"
            else:
                updated_trip.is_ghost = False
                updated_trip.ghost_reason = None

            analyzed_trips.append(updated_trip)

        return analyzed_trips

    def calculate_headway_metrics(
        self, trips: List[TripSnapshot]
    ) -> List[HeadwayMetric]:
        """Calculates headway regularity and Excess Wait Time (EWT) for routes with multiple runs."""
        route_delays: Dict[str, List[int]] = {}
        for trip in trips:
            if not trip.is_ghost and trip.delay_seconds is not None:
                route_delays.setdefault(trip.route_id, []).append(trip.delay_seconds)

        metrics: List[HeadwayMetric] = []
        for route_id, delays in route_delays.items():
            if len(delays) < 2:
                continue

            # Standard deviation of delays indicates bunching vs steady headway
            delay_std = statistics.pstdev(delays) if len(delays) > 1 else 0.0
            avg_delay = statistics.mean(delays)

            # Excess wait time estimate: variance / (2 * mean_headway_estimate)
            # Typically urban headway is ~15-20 min (900-1200s); delay jitter translates directly to excess wait
            ewt_min = round(delay_std / 60.0 * 0.5, 2)
            regularity_score = max(0.0, round(100.0 - (delay_std / 60.0 * 10.0), 1))

            metrics.append(
                HeadwayMetric(
                    route_id=route_id,
                    scheduled_headway_min=15.0,  # nominal standard headway
                    observed_headway_min=round(15.0 + (avg_delay / 60.0), 1),
                    excess_wait_time_min=ewt_min,
                    headway_regularity_score=min(100.0, regularity_score),
                )
            )

        metrics.sort(key=lambda m: m.excess_wait_time_min or 0.0, reverse=True)
        return metrics

    def analyze(
        self,
        vehicles: List[VehicleSnapshot],
        trips: List[TripSnapshot],
        feed_timestamp: Optional[int] = None,
        scan_time: Optional[str] = None,
    ) -> ReliabilitySnapshot:
        """Performs full reliability, ghost bus, and delay distribution analysis."""
        now_iso = scan_time or datetime.now(timezone.utc).isoformat()

        # Flag ghost trips
        annotated_trips = self.identify_ghost_trips(trips, vehicles)

        total_scheduled_trips = len(annotated_trips)
        total_tracked_vehicles = len(vehicles)
        ghost_trips = [t for t in annotated_trips if t.is_ghost]
        total_ghosts = len(ghost_trips)

        ghost_rate = (
            round((total_ghosts / total_scheduled_trips) * 100, 2)
            if total_scheduled_trips > 0
            else 0.0
        )

        tracked_trips_count = total_scheduled_trips - total_ghosts
        tracking_rate = (
            round((tracked_trips_count / total_scheduled_trips) * 100, 2)
            if total_scheduled_trips > 0
            else 0.0
        )

        # Delay categorization
        breakdown = DelayCategoryBreakdown(
            ghost=total_ghosts,
            canceled=len([t for t in annotated_trips if t.is_canceled]),
        )

        valid_delays: List[int] = []
        route_map: Dict[str, Dict[str, Any]] = {}

        for trip in annotated_trips:
            r_id = trip.route_id or "UNKNOWN"
            if r_id not in route_map:
                route_map[r_id] = {
                    "route_id": r_id,
                    "total_trips": 0,
                    "tracked_vehicles": 0,
                    "ghost_trips": 0,
                    "canceled_trips": 0,
                    "on_time_trips": 0,
                    "delayed_trips": 0,
                    "delays": [],
                }

            rm = route_map[r_id]
            rm["total_trips"] += 1

            if trip.is_canceled:
                rm["canceled_trips"] += 1

            if trip.is_ghost:
                rm["ghost_trips"] += 1
            else:
                rm["tracked_vehicles"] += 1
                if trip.delay_seconds is not None:
                    valid_delays.append(trip.delay_seconds)
                    rm["delays"].append(trip.delay_seconds)

                    if trip.delay_seconds < self.early_threshold_sec:
                        breakdown.early += 1
                    elif trip.delay_seconds <= self.on_time_threshold_sec:
                        breakdown.on_time += 1
                        rm["on_time_trips"] += 1
                    elif trip.delay_seconds <= self.minor_delay_threshold_sec:
                        breakdown.minor_delay += 1
                        rm["delayed_trips"] += 1
                    else:
                        breakdown.severe_delay += 1
                        rm["delayed_trips"] += 1

        # Mean and median delays
        if valid_delays:
            mean_delay = round(statistics.mean(valid_delays), 1)
            median_delay = round(statistics.median(valid_delays), 1)
        else:
            mean_delay = 0.0
            median_delay = 0.0

        # Overall on-time % of tracked vehicles with delay info
        total_delay_tracked = breakdown.early + breakdown.on_time + breakdown.minor_delay + breakdown.severe_delay
        overall_on_time_pct = (
            round((breakdown.on_time / total_delay_tracked) * 100, 2)
            if total_delay_tracked > 0
            else 0.0
        )

        # Build route reliability summaries
        route_metrics: List[RouteReliability] = []
        for r_id, stats in route_map.items():
            tot = stats["total_trips"]
            ghosts = stats["ghost_trips"]
            g_rate = round((ghosts / tot) * 100, 2) if tot > 0 else 0.0
            
            d_list = stats["delays"]
            avg_d = round(statistics.mean(d_list), 1) if d_list else 0.0
            max_d = max(d_list) if d_list else 0
            
            delay_reported_count = stats["on_time_trips"] + stats["delayed_trips"]
            ot_rate = (
                round((stats["on_time_trips"] / delay_reported_count) * 100, 2)
                if delay_reported_count > 0
                else 0.0
            )

            route_metrics.append(
                RouteReliability(
                    route_id=r_id,
                    route_name=f"Route {r_id}",
                    total_trips=tot,
                    tracked_vehicles=stats["tracked_vehicles"],
                    ghost_trips=ghosts,
                    canceled_trips=stats["canceled_trips"],
                    on_time_trips=stats["on_time_trips"],
                    delayed_trips=stats["delayed_trips"],
                    ghost_rate_pct=g_rate,
                    on_time_pct=ot_rate,
                    avg_delay_sec=avg_d,
                    max_delay_sec=max_d,
                )
            )

        # Sort worst routes: highest ghost rate, then most ghost trips
        worst_routes = sorted(
            [r for r in route_metrics if r.total_trips >= 2],
            key=lambda x: (x.ghost_rate_pct, x.ghost_trips),
            reverse=True,
        )[:10]

        # Most delayed routes
        most_delayed = sorted(
            [r for r in route_metrics if r.avg_delay_sec > 0],
            key=lambda x: x.avg_delay_sec,
            reverse=True,
        )[:10]

        # Sample ghost trips for the report
        sample_ghosts = [
            {
                "trip_id": g.trip_id,
                "route_id": g.route_id,
                "start_time": g.start_time or "N/A",
                "start_date": g.start_date or "N/A",
                "status": g.schedule_relationship,
                "reason": g.ghost_reason,
            }
            for g in ghost_trips[:15]
        ]

        # Headway adherence
        headway_metrics = self.calculate_headway_metrics(annotated_trips)

        return ReliabilitySnapshot(
            scan_time=now_iso,
            feed_timestamp=feed_timestamp,
            agency=self.agency_name,
            total_scheduled_trips=total_scheduled_trips,
            total_tracked_vehicles=total_tracked_vehicles,
            total_ghost_trips=total_ghosts,
            ghost_bus_rate_pct=ghost_rate,
            vehicle_tracking_rate_pct=tracking_rate,
            overall_on_time_pct=overall_on_time_pct,
            delay_distribution=breakdown,
            mean_delay_sec=mean_delay,
            median_delay_sec=median_delay,
            worst_routes_by_ghost=worst_routes,
            most_delayed_routes=most_delayed,
            route_metrics=route_metrics,
            sample_ghost_trips=sample_ghosts,
            headway_metrics=headway_metrics[:10],
        )
