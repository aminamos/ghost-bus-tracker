-- Durable time-series store for Ghost Bus Tracker scans.
-- One row per market per scan; Twin Cities rows predate the market_id
-- column and were backfilled to 'twin-cities'.
CREATE TABLE IF NOT EXISTS scans (
  market_id TEXT NOT NULL DEFAULT 'twin-cities',
  scan_time TEXT NOT NULL,
  ghost_bus_rate_pct REAL NOT NULL,
  overall_on_time_pct REAL NOT NULL,
  total_scheduled_trips INTEGER NOT NULL,
  total_tracked_vehicles INTEGER NOT NULL,
  total_ghost_trips INTEGER NOT NULL,
  mean_delay_sec REAL,
  agency TEXT,
  city TEXT,
  transit_system TEXT,
  source TEXT NOT NULL DEFAULT 'live',
  PRIMARY KEY (market_id, scan_time)
);
CREATE INDEX IF NOT EXISTS idx_scans_time ON scans (scan_time);
