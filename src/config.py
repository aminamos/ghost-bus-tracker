"""Configuration settings and constants for Ghost Bus Tracker."""

import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("GBT_DATA_DIR", str(BASE_DIR / "data")))
SAMPLE_DIR = BASE_DIR / "sample_data"

LATEST_FILE = DATA_DIR / "latest.json"
HISTORY_FILE = DATA_DIR / "history.json"
REPORT_FILE = Path(os.getenv("GBT_REPORT_PATH", str(BASE_DIR / "RELIABILITY.md")))

SAMPLE_VP_FILE = SAMPLE_DIR / "vehiclepositions_sample.pb"
SAMPLE_TU_FILE = SAMPLE_DIR / "tripupdates_sample.pb"
SAMPLE_SCHEDULES_FILE = SAMPLE_DIR / "schedules_sample.json"

# Feed URLs (Twin Cities Metro Transit by default)
DEFAULT_VP_URL = "https://svc.metrotransit.org/mtgtfs/vehiclepositions.pb"
DEFAULT_TU_URL = "https://svc.metrotransit.org/mtgtfs/tripupdates.pb"
DEFAULT_NEXTRIP_ROUTES_URL = "https://svc.metrotransit.org/nextrip/routes"
DEFAULT_NEXTRIP_STOPS_URL = "https://svc.metrotransit.org/nextrip/stops"

VEHICLE_POSITIONS_URL = os.getenv("GBT_VP_URL", DEFAULT_VP_URL)
TRIP_UPDATES_URL = os.getenv("GBT_TU_URL", DEFAULT_TU_URL)
AGENCY_NAME = os.getenv("GBT_AGENCY_NAME", "Metro Transit (Twin Cities)")
CITY_NAME = os.getenv("GBT_CITY_NAME", "Minneapolis–Saint Paul, MN")
TRANSIT_SYSTEM = os.getenv("GBT_TRANSIT_SYSTEM", "Metro Transit")
REGION_NAME = os.getenv("GBT_REGION_NAME", "Twin Cities Metropolitan Area, Minnesota")
STATE_NAME = os.getenv("GBT_STATE_NAME", "Minnesota")
COUNTRY_NAME = os.getenv("GBT_COUNTRY_NAME", "USA")

# Reliability Thresholds (seconds)
# Early: departure is more than 60s ahead of schedule (causes riders to miss the bus!)
EARLY_THRESHOLD_SEC = int(os.getenv("GBT_EARLY_SEC", "-60"))

# On-time: from 60s early up to 300s (5 minutes) late
ON_TIME_THRESHOLD_SEC = int(os.getenv("GBT_ON_TIME_SEC", "300"))

# Minor delay: between 300s (5m) and 900s (15m) late
MINOR_DELAY_THRESHOLD_SEC = int(os.getenv("GBT_MINOR_DELAY_SEC", "900"))

# Max historical snapshots to retain in history.json
MAX_HISTORY_SNAPSHOTS = int(os.getenv("GBT_MAX_HISTORY", "100"))

# HTTP Request Timeout (seconds)
REQUEST_TIMEOUT_SEC = int(os.getenv("GBT_REQUEST_TIMEOUT", "15"))
USER_AGENT = "GhostBusTracker/0.1.0 (+https://github.com/aminamos/ghost-bus-tracker)"
