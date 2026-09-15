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

            # Condition 1: Explicitly marked CANCELED in GTFS-RT.
            # Canceled trips are their own category: NOT ghosts, NOT tracked,
            # and excluded from delay stats. No ghost_reason applies.
            if updated_trip.is_canceled:
                updated_trip.is_ghost = False
                updated_trip.ghost_reason = None
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

    @staticmethod
    def _parse_start_time_seconds(start_time: str) -> Optional[int]:
        """Parses a GTFS 'HH:MM:SS' start time into seconds after midnight.

        GTFS times may exceed 24:00:00 for after-midnight service, so plain
        time parsing is intentionally avoided. Returns None if unparseable.
        """
        try:
            parts = start_time.strip().split(":")
            if len(parts) != 3:
                return None
            hours, minutes, seconds = (int(p) for p in parts)
            if hours < 0 or not (0 <= minutes < 60) or not (0 <= seconds < 60):
                return None
            return hours * 3600 + minutes * 60 + seconds
        except (ValueError, AttributeError):
            return None

    def calculate_headway_metrics(
        self, trips: List[TripSnapshot]
    ) -> List[HeadwayMetric]:
        """Calculates headway regularity and Excess Wait Time (EWT) for routes with multiple runs."""
        route_delays: Dict[str, List[int]] = {}
        route_start_times: Dict[str, List[int]] = {}

        for trip in trips:
            # Canceled trips never ran: they contribute neither delay samples
            # nor scheduled start times to headway analysis.
            if trip.is_canceled:
                continue

            # Scheduled start times come from all non-canceled trips, including
            # ghosts — a ghost run was still scheduled to depart at start_time.
            if trip.start_time:
                start_sec = self._parse_start_time_seconds(trip.start_time)
                if start_sec is not None:
                    route_start_times.setdefault(trip.route_id, []).append(start_sec)

            # Delay samples only from verified tracked (non-ghost) trips.
            if not trip.is_ghost and trip.delay_seconds is not None:
                route_delays.setdefault(trip.route_id, []).append(trip.delay_seconds)

        metrics: List[HeadwayMetric] = []
        for route_id, delays in route_delays.items():
            if len(delays) < 2:
                continue

            # Real scheduled headway: median gap between sorted start times of
            # non-canceled trips on the route. Zero/negative gaps (simultaneous
            # departures, e.g. opposite directions) are not meaningful headways.
            starts = sorted(route_start_times.get(route_id, []))
            gaps = [b - a for a, b in zip(starts, starts[1:]) if b - a > 0]
            if not gaps:
                continue  # no real headway measurable for this route
            scheduled_headway_sec = statistics.median(gaps)
            scheduled_headway_min = round(scheduled_headway_sec / 60.0, 1)

            # Standard deviation of delays indicates bunching vs steady headway
            delay_std = statistics.pstdev(delays)
            avg_delay = statistics.mean(delays)

            # Documented approximation: observed headway ≈ scheduled headway
            # shifted by the average delay of tracked trips on the route.
            observed_headway_min = round(scheduled_headway_min + (avg_delay / 60.0), 1)

            # Standard EWT formula: EWT = Var(headway) / (2 * E[headway]).
            # True per-departure headway variance is not observable here, so it
            # is estimated from the variance of delays (delay jitter is what
            # produces bunching), and E[headway] is the real scheduled headway.
            headway_var_sec2 = delay_std ** 2
            ewt_min = round(headway_var_sec2 / (2.0 * scheduled_headway_sec) / 60.0, 2)

            # Regularity score: 100 when observed headway jitter is zero,
            # degrading toward 0 as the delay stddev approaches one full
            # scheduled headway (coefficient of variation of the headway).
            regularity_score = max(
                0.0, round(100.0 * (1.0 - delay_std / scheduled_headway_sec), 1)
            )

            metrics.append(
                HeadwayMetric(
                    route_id=route_id,
                    scheduled_headway_min=scheduled_headway_min,
                    observed_headway_min=observed_headway_min,
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

        total_canceled = len([t for t in annotated_trips if t.is_canceled])
        # Tracked = verified-running trips only: canceled trips are neither
        # ghosts nor tracked, so ghost% + tracked% + canceled% partitions 100%.
        tracked_trips_count = total_scheduled_trips - total_ghosts - total_canceled
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

        # Unique vehicles observed per route. A vehicle is attributed to a
        # route via its own broadcast route_id, falling back to the route of
        # the trip it is broadcasting (vehicle positions sometimes lack
        # route_id). tracked_vehicles counts UNIQUE vehicle_ids, not trips.
        active_vehicle_ids: Set[str] = {v.vehicle_id for v in vehicles if v.vehicle_id}
        trip_route_by_id: Dict[str, Optional[str]] = {
            t.trip_id: t.route_id for t in annotated_trips if t.trip_id
        }
        route_vehicle_ids: Dict[str, Set[str]] = {}
        for v in vehicles:
            if not v.vehicle_id:
                continue
            v_route = v.route_id or trip_route_by_id.get(v.trip_id)
            if v_route:
                route_vehicle_ids.setdefault(v_route, set()).add(v.vehicle_id)

        for trip in annotated_trips:
            r_id = trip.route_id or "UNKNOWN"
            if r_id not in route_map:
                route_map[r_id] = {
                    "route_id": r_id,
                    "total_trips": 0,
                    "ghost_trips": 0,
                    "canceled_trips": 0,
                    "on_time_trips": 0,
                    "delayed_trips": 0,
                    "delays": [],
                }

            rm = route_map[r_id]
            rm["total_trips"] += 1

            if trip.is_canceled:
                # Canceled trips are their own bucket: not ghosts, not
                # tracked, and excluded from delay statistics.
                rm["canceled_trips"] += 1
            elif trip.is_ghost:
                rm["ghost_trips"] += 1
            else:
                # Tracked trip: record its assigned vehicle if that vehicle is
                # actually broadcasting GPS.
                if trip.vehicle_id and trip.vehicle_id in active_vehicle_ids:
                    route_vehicle_ids.setdefault(r_id, set()).add(trip.vehicle_id)

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
                    tracked_vehicles=len(route_vehicle_ids.get(r_id, set())),
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
