"""Fetcher module for GTFS-RT vehicle positions, trip updates, and REST feeds."""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import requests
from google.transit import gtfs_realtime_pb2

from src import config
from src.models import (
    ScheduleRelationship,
    StopTimeUpdateSnapshot,
    TripSnapshot,
    VehicleSnapshot,
)

logger = logging.getLogger(__name__)


class FeedFetcher:
    """Fetches and parses GTFS Realtime and NextTrip feeds."""

    def __init__(
        self,
        session: Optional[requests.Session] = None,
        timeout: int = config.REQUEST_TIMEOUT_SEC,
        user_agent: str = config.USER_AGENT,
    ):
        self.session = session or requests.Session()
        self.session.headers.update({"User-Agent": user_agent})
        self.timeout = timeout

    def _read_bytes(self, source: Union[str, Path, bytes]) -> bytes:
        """Reads raw bytes from a URL, local file path, or returns raw bytes."""
        if isinstance(source, bytes):
            return source

        path_or_url = str(source)
        if path_or_url.startswith(("http://", "https://")):
            response = self.session.get(path_or_url, timeout=self.timeout)
            response.raise_for_status()
            return response.content

        file_path = Path(path_or_url)
        if not file_path.is_file():
            raise FileNotFoundError(f"Feed file not found: {file_path}")
        return file_path.read_bytes()

    def parse_vehicle_positions(
        self, raw_bytes: bytes
    ) -> Tuple[List[VehicleSnapshot], Optional[int]]:
        """Parses GTFS-RT protobuf bytes into a list of VehicleSnapshot objects."""
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(raw_bytes)
        feed_timestamp = feed.header.timestamp if feed.header.HasField("timestamp") else None

        vehicles: List[VehicleSnapshot] = []
        for entity in feed.entity:
            if not entity.HasField("vehicle"):
                continue
            v = entity.vehicle
            v_id = v.vehicle.id if v.HasField("vehicle") and v.vehicle.id else entity.id
            trip_id = v.trip.trip_id if v.HasField("trip") and v.trip.trip_id else None
            route_id = v.trip.route_id if v.HasField("trip") and v.trip.route_id else None
            direction_id = (
                v.trip.direction_id
                if v.HasField("trip") and v.trip.HasField("direction_id")
                else None
            )
            lat = v.position.latitude if v.HasField("position") else 0.0
            lon = v.position.longitude if v.HasField("position") else 0.0
            bearing = (
                v.position.bearing
                if v.HasField("position") and v.position.HasField("bearing")
                else None
            )
            speed = (
                v.position.speed
                if v.HasField("position") and v.position.HasField("speed")
                else None
            )
            timestamp = v.timestamp if v.HasField("timestamp") else None

            vehicles.append(
                VehicleSnapshot(
                    vehicle_id=str(v_id),
                    trip_id=trip_id,
                    route_id=route_id,
                    direction_id=direction_id,
                    latitude=lat,
                    longitude=lon,
                    bearing=bearing,
                    speed=speed,
                    timestamp=timestamp,
                )
            )
        return vehicles, feed_timestamp

    def parse_trip_updates(
        self, raw_bytes: bytes
    ) -> Tuple[List[TripSnapshot], Optional[int]]:
        """Parses GTFS-RT protobuf bytes into a list of TripSnapshot objects."""
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(raw_bytes)
        feed_timestamp = feed.header.timestamp if feed.header.HasField("timestamp") else None

        trips: List[TripSnapshot] = []
        for entity in feed.entity:
            if not entity.HasField("trip_update"):
                continue
            tu = entity.trip_update
            trip_desc = tu.trip
            trip_id = trip_desc.trip_id if trip_desc.trip_id else entity.id
            route_id = trip_desc.route_id if trip_desc.route_id else "UNKNOWN"
            start_time = trip_desc.start_time if trip_desc.HasField("start_time") else None
            start_date = trip_desc.start_date if trip_desc.HasField("start_date") else None

            # Schedule relationship
            rel_int = trip_desc.schedule_relationship if trip_desc.HasField("schedule_relationship") else 0
            # GTFS RT spec: 0=SCHEDULED, 1=ADDED, 2=UNSCHEDULED, 3=CANCELED, 5=REPLACEMENT, 6=DUPLICATED
            rel_map = {
                0: ScheduleRelationship.SCHEDULED.value,
                1: ScheduleRelationship.ADDED.value,
                2: ScheduleRelationship.UNSCHEDULED.value,
                3: ScheduleRelationship.CANCELED.value,
                5: ScheduleRelationship.REPLACEMENT.value,
                6: ScheduleRelationship.DUPLICATED.value,
            }
            rel_name = rel_map.get(rel_int, ScheduleRelationship.SCHEDULED.value)

            vehicle_id = None
            if tu.HasField("vehicle") and tu.vehicle.id:
                vehicle_id = str(tu.vehicle.id)

            # Determine representative delay from stop time updates
            delays: List[int] = []
            stop_count = len(tu.stop_time_update)
            for stu in tu.stop_time_update:
                if stu.HasField("departure") and stu.departure.HasField("delay"):
                    delays.append(stu.departure.delay)
                elif stu.HasField("arrival") and stu.arrival.HasField("delay"):
                    delays.append(stu.arrival.delay)

            # Latest or first reported delay
            rep_delay = delays[0] if delays else None

            is_canceled = (rel_name == ScheduleRelationship.CANCELED.value)

            trips.append(
                TripSnapshot(
                    trip_id=str(trip_id),
                    route_id=str(route_id),
                    start_time=start_time,
                    start_date=start_date,
                    schedule_relationship=rel_name,
                    vehicle_id=vehicle_id,
                    delay_seconds=rep_delay,
                    stop_updates_count=stop_count,
                    is_canceled=is_canceled,
                    has_vehicle_assigned=(vehicle_id is not None and vehicle_id != ""),
                )
            )
        return trips, feed_timestamp

    def fetch_vehicle_positions(
        self, source: Optional[Union[str, Path, bytes]] = None
    ) -> Tuple[List[VehicleSnapshot], Optional[int]]:
        """Fetches vehicle positions from URL or file path."""
        src = source or config.VEHICLE_POSITIONS_URL
        raw = self._read_bytes(src)
        return self.parse_vehicle_positions(raw)

    def fetch_trip_updates(
        self, source: Optional[Union[str, Path, bytes]] = None
    ) -> Tuple[List[TripSnapshot], Optional[int]]:
        """Fetches trip updates from URL or file path."""
        src = source or config.TRIP_UPDATES_URL
        raw = self._read_bytes(src)
        return self.parse_trip_updates(raw)

    def fetch_nextrip_routes(
        self, url: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Fetches transit routes from NextTrip REST API."""
        endpoint = url or config.DEFAULT_NEXTRIP_ROUTES_URL
        response = self.session.get(endpoint, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def fetch_nextrip_departures(
        self, stop_id: Union[int, str], url: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Fetches stop departures from NextTrip REST API."""
        base = url or config.DEFAULT_NEXTRIP_STOPS_URL
        endpoint = f"{base.rstrip('/')}/{stop_id}"
        response = self.session.get(endpoint, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        return data.get("departures", []) if isinstance(data, dict) else data

    def load_sample_feeds(
        self,
        vp_path: Optional[Union[str, Path]] = None,
        tu_path: Optional[Union[str, Path]] = None,
    ) -> Tuple[List[VehicleSnapshot], List[TripSnapshot], Optional[int]]:
        """Loads offline sample feeds from sample_data directory."""
        v_path = vp_path or config.SAMPLE_VP_FILE
        t_path = tu_path or config.SAMPLE_TU_FILE
        vehicles, v_ts = self.fetch_vehicle_positions(v_path)
        trips, t_ts = self.fetch_trip_updates(t_path)
        return vehicles, trips, (t_ts or v_ts)
