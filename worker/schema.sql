-- Durable time-series store for Ghost Bus Tracker scans.
-- One row per scan; scan_time is unique across the pipeline's 30-minute cadence.
CREATE TABLE IF NOT EXISTS scans (
  scan_time TEXT PRIMARY KEY,
  ghost_bus_rate_pct REAL NOT NULL,
  overall_on_time_pct REAL NOT NULL,
  total_scheduled_trips INTEGER NOT NULL,
  total_tracked_vehicles INTEGER NOT NULL,
  total_ghost_trips INTEGER NOT NULL,
  mean_delay_sec REAL,
  agency TEXT,
  city TEXT,
  transit_system TEXT,
  source TEXT NOT NULL DEFAULT 'live'
);
CREATE INDEX IF NOT EXISTS idx_scans_time ON scans (scan_time);
