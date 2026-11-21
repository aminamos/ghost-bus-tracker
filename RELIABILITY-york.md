# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-21T07:00:18.864000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`95.45%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+63.0s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 21 | 84.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 12.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 3 | **`42.86%`** | `100.0%` | `+1.3 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+1.4 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+1.8 min (+107.0s)` | `+4.2 min (+250s)` | 4 | `100.0%` |
| **Route 77** | `+1.4 min (+84.2s)` | `+4.1 min (+246s)` | 4 | `83.33%` |
| **Route 20** | `+1.3 min (+80.2s)` | `+4.0 min (+238s)` | 4 | `100.0%` |
| **Route 107** | `+0.1 min (+7.2s)` | `+0.8 min (+48s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `79.3 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `85.3 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `90.5 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `94.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2646 is broadcasting off-schedule with no vehicle covering 2024938 |
| `2024940` | Route 20 | `02:47:00` | `SCHEDULED` | Assigned vehicle C2006 is broadcasting off-schedule with no vehicle covering 2024940 |
| `2025027` | Route 20 | `02:04:00` | `SCHEDULED` | Assigned vehicle C2006 is broadcasting off-schedule with no vehicle covering 2025027 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `12.0%` | `95.45%` | 25 | 15 | `+63.0s` |
| `2026-11-21 06:00:18` | `2.22%` | `81.82%` | 45 | 28 | `+74.0s` |
| `2026-11-21 05:30:18` | `4.41%` | `80.0%` | 68 | 45 | `+88.2s` |
| `2026-11-21 05:00:21` | `9.38%` | `80.46%` | 96 | 63 | `+86.4s` |
| `2026-11-21 04:30:18` | `8.8%` | `85.09%` | 125 | 75 | `+98.5s` |
| `2026-11-21 04:00:18` | `9.09%` | `89.93%` | 154 | 86 | `+92.3s` |
| `2026-11-21 03:30:18` | `6.11%` | `83.23%` | 180 | 99 | `+93.7s` |
| `2026-11-21 03:00:18` | `8.25%` | `85.03%` | 206 | 112 | `+106.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.864000+00:00`.*
