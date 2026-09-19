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

# Built-in City and Transit Agency Presets
AGENCY_PRESETS = {
    "twin-cities": {
        "id": "twin-cities",
        "name": "Metro Transit",
        "agency": "Metro Transit (Twin Cities)",
        "city": "Minneapolis–Saint Paul, MN",
        "region": "Twin Cities Metropolitan Area, Minnesota",
        "state": "Minnesota",
        "country": "USA",
        "vp_url": "https://svc.metrotransit.org/mtgtfs/vehiclepositions.pb",
        "tu_url": "https://svc.metrotransit.org/mtgtfs/tripupdates.pb",
        "requires_key": False,
        "description": "Minneapolis–St. Paul bus network, METRO Light Rail (Blue & Green lines), and BRT.",
    },
    "chicago": {
        "id": "chicago",
        "name": "CTA",
        "agency": "Chicago Transit Authority",
        "city": "Chicago, IL",
        "region": "Chicagoland / Cook County, Illinois",
        "state": "Illinois",
        "country": "USA",
        "vp_url": "https://www.transitchicago.com/api/1.0/gtfs-realtime/vehiclepositions.pb",
        "tu_url": "https://www.transitchicago.com/api/1.0/gtfs-realtime/tripupdates.pb",
        "requires_key": True,
        "key_env_var": "CTA_API_KEY",
        "key_param": "key",
        "key_url": "https://www.transitchicago.com/developers/",
        "description": "Chicago 'L' rapid transit and urban bus fleet (origin of the 'ghost bus' phenomenon).",
    },
    "boston": {
        "id": "boston",
        "name": "MBTA",
        "agency": "Massachusetts Bay Transportation Authority",
        "city": "Boston, MA",
        "region": "Greater Boston, Massachusetts",
        "state": "Massachusetts",
        "country": "USA",
        "vp_url": "https://cdn.mbta.com/realtime/VehiclePositions.pb",
        "tu_url": "https://cdn.mbta.com/realtime/TripUpdates.pb",
        "requires_key": False,
        "description": "Greater Boston subway, light rail, trolley, and bus network.",
    },
    "nyc": {
        "id": "nyc",
        "name": "MTA",
        "agency": "Metropolitan Transportation Authority",
        "city": "New York, NY",
        "region": "New York Metropolitan Area",
        "state": "New York",
        "country": "USA",
        "vp_url": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
        "tu_url": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
        "requires_key": True,
        "key_env_var": "MTA_API_KEY",
        "key_header": "x-api-key",
        "key_url": "https://api.mta.info/",
        "description": "New York City Subway and regional bus network.",
    },
    "sf": {
        "id": "sf",
        "name": "SFMTA",
        "agency": "San Francisco Municipal Transportation Agency",
        "city": "San Francisco, CA",
        "region": "San Francisco Bay Area, California",
        "state": "California",
        "country": "USA",
        "vp_url": "https://api.511.org/transit/vehiclepositions?agency=SF",
        "tu_url": "https://api.511.org/transit/tripupdates?agency=SF",
        "requires_key": True,
        "key_env_var": "BAY_AREA_511_KEY",
        "key_param": "api_key",
        "key_url": "https://511.org/open-data/token",
        "description": "San Francisco Muni Metro, historic streetcars, cable cars, and urban bus fleet.",
    },
    "philly": {
        "id": "philly",
        "name": "SEPTA",
        "agency": "Southeastern Pennsylvania Transportation Authority",
        "city": "Philadelphia, PA",
        "region": "Greater Philadelphia / Delaware Valley, Pennsylvania",
        "state": "Pennsylvania",
        "country": "USA",
        "vp_url": "https://www3.septa.org/developer/gtfs-rt/vehiclepositions.pb",
        "tu_url": "https://www3.septa.org/developer/gtfs-rt/tripupdates.pb",
        "requires_key": False,
        "description": "Greater Philadelphia subway, trolley, Norristown High Speed Line, and 120+ bus routes.",
    },
    "dc": {
        "id": "dc",
        "name": "WMATA",
        "agency": "Washington Metropolitan Area Transit Authority",
        "city": "Washington, DC",
        "region": "Washington Metropolitan Area (DC, MD, VA)",
        "state": "District of Columbia",
        "country": "USA",
        "vp_url": "https://api.wmata.com/gtfs/bus-gtfs-rt/vehiclepositions.pb",
        "tu_url": "https://api.wmata.com/gtfs/bus-gtfs-rt/tripupdates.pb",
        "requires_key": True,
        "key_env_var": "WMATA_API_KEY",
        "key_header": "api_key",
        "key_url": "https://developer.wmata.com/",
        "description": "Washington Metrorail and extensive Metrobus network across DC, Maryland, and Northern Virginia.",
    },
    "la": {
        "id": "la",
        "name": "LA Metro",
        "agency": "Los Angeles County Metropolitan Transportation Authority",
        "city": "Los Angeles, CA",
        "region": "Los Angeles County, California",
        "state": "California",
        "country": "USA",
        "vp_url": "https://api.metro.net/agencies/lametro/vehicle_positions.pb",
        "tu_url": "https://api.metro.net/agencies/lametro/trip_updates.pb",
        "requires_key": False,
        "description": "Los Angeles County Metro Rail (A, B, C, D, E, K lines) and vast 2,200+ bus fleet.",
    },
    "seattle": {
        "id": "seattle",
        "name": "Sound Transit & KCM",
        "agency": "King County Metro / Sound Transit",
        "city": "Seattle, WA",
        "region": "Central Puget Sound Region, Washington",
        "state": "Washington",
        "country": "USA",
        "vp_url": "https://api.soundtransit.org/gtfs-rt/vehicle-positions.pb",
        "tu_url": "https://api.soundtransit.org/gtfs-rt/trip-updates.pb",
        "requires_key": False,
        "description": "Seattle and Puget Sound Link Light Rail, Sounder commuter trains, RapidRide, and King County bus network.",
    },
    "denver": {
        "id": "denver",
        "name": "RTD",
        "agency": "Regional Transportation District",
        "city": "Denver, CO",
        "region": "Denver Metropolitan Area, Colorado",
        "state": "Colorado",
        "country": "USA",
        "vp_url": "https://www.rtd-denver.com/files/gtfs-rt/VehiclePosition.pb",
        "tu_url": "https://www.rtd-denver.com/files/gtfs-rt/TripUpdate.pb",
        "requires_key": False,
        "description": "Denver Front Range commuter rail (A, B, G, N lines), light rail, and regional bus grid.",
    },
    "portland": {
        "id": "portland",
        "name": "TriMet",
        "agency": "Tri-County Metropolitan Transportation District of Oregon",
        "city": "Portland, OR",
        "region": "Portland Metropolitan Area, Oregon",
        "state": "Oregon",
        "country": "USA",
        "vp_url": "https://developer.trimet.org/ws/V1/VehiclePositions.pb",
        "tu_url": "https://developer.trimet.org/ws/V1/TripUpdates.pb",
        "requires_key": True,
        "key_env_var": "TRIMET_APP_ID",
        "key_param": "appID",
        "key_url": "https://developer.trimet.org/",
        "description": "Portland MAX light rail, WES commuter rail, Portland Streetcar, and frequent-service bus network (co-inventors of GTFS).",
    },
    "atlanta": {
        "id": "atlanta",
        "name": "MARTA",
        "agency": "Metropolitan Atlanta Rapid Transit Authority",
        "city": "Atlanta, GA",
        "region": "Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia",
        "state": "Georgia",
        "country": "USA",
        "vp_url": "https://gtfs-rt.itsmarta.com/TMGTFSRealTimeWebService/vehicle/vehiclepositions.pb",
        "tu_url": "https://gtfs-rt.itsmarta.com/TMGTFSRealTimeWebService/tripupdate/tripupdates.pb",
        "requires_key": False,
        "description": "Metro Atlanta heavy rail system (Red, Gold, Blue, Green lines), Atlanta Streetcar, and bus fleet.",
    },
    "toronto": {
        "id": "toronto",
        "name": "TTC",
        "agency": "Toronto Transit Commission",
        "city": "Toronto, ON",
        "region": "Greater Toronto Area, Ontario",
        "state": "Ontario",
        "country": "Canada",
        "vp_url": "https://opendata.toronto.ca/transportation/ttc/gtfs-rt/vehicle-positions.pb",
        "tu_url": "https://opendata.toronto.ca/transportation/ttc/gtfs-rt/trip-updates.pb",
        "requires_key": False,
        "description": "Third largest urban transit system in North America: Toronto Subway (Lines 1-4), iconic streetcar network, and extensive bus routes.",
    },
}

PRESET_ALIASES = {
    "minneapolis": "twin-cities",
    "mpls": "twin-cities",
    "st-paul": "twin-cities",
    "stpaul": "twin-cities",
    "msp": "twin-cities",
    "metro-transit": "twin-cities",
    "sf": "sf",
    "sfmta": "sf",
    "muni": "sf",
    "san-francisco": "sf",
    "sanfrancisco": "sf",
    "cta": "chicago",
    "chi": "chicago",
    "chicago-transit": "chicago",
    "mbta": "boston",
    "mta": "nyc",
    "new-york": "nyc",
    "new-york-city": "nyc",
    "nyct": "nyc",
    "septa": "philly",
    "philadelphia": "philly",
    "wmata": "dc",
    "washington": "dc",
    "washington-dc": "dc",
    "lametro": "la",
    "los-angeles": "la",
    "la-metro": "la",
    "sound-transit": "seattle",
    "soundtransit": "seattle",
    "kcm": "seattle",
    "king-county-metro": "seattle",
    "rtd": "denver",
    "trimet": "portland",
    "pdx": "portland",
    "marta": "atlanta",
    "atl": "atlanta",
    "ttc": "toronto",
    "gta": "toronto",
}


def get_preset(name: str):
    """Resolves an agency or city name to a preset dict, or None if not found."""
    key = str(name).lower().strip().replace(" ", "-").replace("_", "")
    target_id = PRESET_ALIASES.get(key, key)
    return AGENCY_PRESETS.get(target_id)

