"""Unit tests for FeedFetcher module."""

from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
import requests

from src.fetcher import FeedFetcher
from src.models import ScheduleRelationship, TripSnapshot, VehicleSnapshot


def test_parse_vehicle_positions(mock_gtfs_rt_bytes):
    """Test parsing of mock vehicle positions protobuf."""
    vp_bytes, _ = mock_gtfs_rt_bytes
    fetcher = FeedFetcher()

    vehicles, timestamp = fetcher.parse_vehicle_positions(vp_bytes)
    assert timestamp == 1789345000
    assert len(vehicles) == 2

    v1 = vehicles[0]
    assert v1.vehicle_id == "bus_1001"
    assert v1.trip_id == "trip_101"
    assert v1.route_id == "1"
    assert v1.latitude == pytest.approx(44.9778)
    assert v1.longitude == pytest.approx(-93.2650)
    assert v1.bearing == 180.0
    assert v1.speed == 12.5


def test_parse_trip_updates(mock_gtfs_rt_bytes):
    """Test parsing of mock trip updates protobuf."""
    _, tu_bytes = mock_gtfs_rt_bytes
    fetcher = FeedFetcher()

    trips, timestamp = fetcher.parse_trip_updates(tu_bytes)
    assert timestamp == 1789345000
    assert len(trips) == 5

    # Check Trip 101
    t1 = next(t for t in trips if t.trip_id == "trip_101")
    assert t1.route_id == "1"
    assert t1.vehicle_id == "bus_1001"
    assert t1.has_vehicle_assigned is True
    assert t1.is_canceled is False
    assert t1.delay_seconds == 60

    # Check Trip 104 (canceled)
    t4 = next(t for t in trips if t.trip_id == "trip_104")
    assert t4.schedule_relationship == ScheduleRelationship.CANCELED.value
    assert t4.is_canceled is True

    # Check Trip 103 (unassigned)
    t3 = next(t for t in trips if t.trip_id == "trip_103")
    assert t3.vehicle_id is None
    assert t3.has_vehicle_assigned is False


def test_read_bytes_from_local_file(tmp_path):
    """Test reading raw bytes from a local file."""
    test_file = tmp_path / "test.bin"
    test_file.write_bytes(b"HELLO_TRANSIT")

    fetcher = FeedFetcher()
    data = fetcher._read_bytes(test_file)
    assert data == b"HELLO_TRANSIT"


def test_read_bytes_file_not_found():
    """Test error when file path does not exist."""
    fetcher = FeedFetcher()
    with pytest.raises(FileNotFoundError):
        fetcher._read_bytes("nonexistent_feed_file_123.pb")


def test_fetch_from_http_url():
    """Test fetching from HTTP URL using mocked requests session."""
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.content = b"MOCK_FEED_DATA"
    mock_response.status_code = 200
    mock_session.get.return_value = mock_response

    fetcher = FeedFetcher(session=mock_session)
    data = fetcher._read_bytes("https://fake-transit.org/feed.pb")
    assert data == b"MOCK_FEED_DATA"
    mock_session.get.assert_called_once()


def test_fetch_from_http_url_error():
    """Test handling of HTTP error when fetching feed."""
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
    mock_session.get.return_value = mock_response

    fetcher = FeedFetcher(session=mock_session)
    with pytest.raises(requests.HTTPError):
        fetcher._read_bytes("https://fake-transit.org/notfound.pb")


def test_load_sample_feeds(sample_data_dir):
    """Test loading real sample files stored in sample_data/."""
    vp_path = sample_data_dir / "vehiclepositions_sample.pb"
    tu_path = sample_data_dir / "tripupdates_sample.pb"

    if not vp_path.exists() or not tu_path.exists():
        pytest.skip("Sample feed files not present in sample_data/")

    fetcher = FeedFetcher()
    vehicles, trips, timestamp = fetcher.load_sample_feeds(vp_path, tu_path)

    assert len(vehicles) > 0
    assert len(trips) > 0
    assert timestamp is not None
    assert all(isinstance(v, VehicleSnapshot) for v in vehicles)
    assert all(isinstance(t, TripSnapshot) for t in trips)


def test_fetch_nextrip_routes():
    """Test fetching and parsing NextTrip routes JSON."""
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"route_id": "2", "agency_id": 0, "route_label": "Route 2 - Franklin Av"}
    ]
    mock_session.get.return_value = mock_response

    fetcher = FeedFetcher(session=mock_session)
    routes = fetcher.fetch_nextrip_routes("https://fake-transit.org/routes")
    assert len(routes) == 1
    assert routes[0]["route_id"] == "2"


def test_fetch_nextrip_departures():
    """Test fetching NextTrip departures JSON."""
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "stops": [{"stop_id": 1234, "description": "Hennepin & 7th"}],
        "departures": [{"actual": True, "trip_id": "999", "departure_text": "5 Min"}],
    }
    mock_session.get.return_value = mock_response

    fetcher = FeedFetcher(session=mock_session)
    deps = fetcher.fetch_nextrip_departures(1234, "https://fake-transit.org/nextrip/stops")
    assert len(deps) == 1
    assert deps[0]["trip_id"] == "999"
