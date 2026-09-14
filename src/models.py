"""Data models for Ghost Bus Tracker."""

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class ScheduleRelationship(str, Enum):
    SCHEDULED = "SCHEDULED"
    ADDED = "ADDED"
    UNSCHEDULED = "UNSCHEDULED"
    CANCELED = "CANCELED"
    REPLACEMENT = "REPLACEMENT"
    DUPLICATED = "DUPLICATED"


class VehicleSnapshot(BaseModel):
    vehicle_id: str
    trip_id: Optional[str] = None
    route_id: Optional[str] = None
    direction_id: Optional[int] = None
    latitude: float = 0.0
    longitude: float = 0.0
    bearing: Optional[float] = None
    speed: Optional[float] = None
    timestamp: Optional[int] = None


class StopTimeUpdateSnapshot(BaseModel):
    stop_sequence: Optional[int] = None
    stop_id: Optional[str] = None
    arrival_delay: Optional[int] = None
    arrival_time: Optional[int] = None
    departure_delay: Optional[int] = None
    departure_time: Optional[int] = None
    schedule_relationship: str = "SCHEDULED"


class TripSnapshot(BaseModel):
    trip_id: str
    route_id: str
    start_time: Optional[str] = None
    start_date: Optional[str] = None
    schedule_relationship: str = "SCHEDULED"
    vehicle_id: Optional[str] = None
    delay_seconds: Optional[int] = None
    stop_updates_count: int = 0
    is_canceled: bool = False
    has_vehicle_assigned: bool = False
    is_ghost: bool = False
    ghost_reason: Optional[str] = None


class DelayCategoryBreakdown(BaseModel):
    early: int = 0
    on_time: int = 0
    minor_delay: int = 0
    severe_delay: int = 0
    ghost: int = 0
    canceled: int = 0


class RouteReliability(BaseModel):
    route_id: str
    route_name: Optional[str] = None
    total_trips: int = 0
    tracked_vehicles: int = 0
    ghost_trips: int = 0
    canceled_trips: int = 0
    on_time_trips: int = 0
    delayed_trips: int = 0
    ghost_rate_pct: float = 0.0
    on_time_pct: float = 0.0
    avg_delay_sec: float = 0.0
    max_delay_sec: int = 0


class HeadwayMetric(BaseModel):
    route_id: str
    scheduled_headway_min: Optional[float] = None
    observed_headway_min: Optional[float] = None
    excess_wait_time_min: Optional[float] = None
    headway_regularity_score: Optional[float] = None


class ReliabilitySnapshot(BaseModel):
    scan_time: str
    feed_timestamp: Optional[int] = None
    agency: str
    total_scheduled_trips: int = 0
    total_tracked_vehicles: int = 0
    total_ghost_trips: int = 0
    ghost_bus_rate_pct: float = 0.0
    vehicle_tracking_rate_pct: float = 0.0
    overall_on_time_pct: float = 0.0
    delay_distribution: DelayCategoryBreakdown = Field(default_factory=DelayCategoryBreakdown)
    mean_delay_sec: float = 0.0
    median_delay_sec: float = 0.0
    worst_routes_by_ghost: List[RouteReliability] = Field(default_factory=list)
    most_delayed_routes: List[RouteReliability] = Field(default_factory=list)
    route_metrics: List[RouteReliability] = Field(default_factory=list)
    sample_ghost_trips: List[Dict[str, Any]] = Field(default_factory=list)
    headway_metrics: List[HeadwayMetric] = Field(default_factory=list)


class HistoryEntry(BaseModel):
    scan_time: str
    ghost_bus_rate_pct: float
    overall_on_time_pct: float
    total_scheduled_trips: int
    total_tracked_vehicles: int
    total_ghost_trips: int
    mean_delay_sec: float
