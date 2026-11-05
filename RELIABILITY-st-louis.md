# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-05T07:00:18.177000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.43%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `39` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `25` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+57.1s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 38.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 12.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 35.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-60.0s` |
| **Route 19792** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+0.3 min` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19780** | `+11.0 min (+660.0s)` | `+11.0 min (+660s)` | 1 | `0.0%` |
| **Route 19762** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19798** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19759** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19784** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19787** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19781** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19793** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19775** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19750** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19792** | ~17.5m | ~17.5m | **`+0.0 min`** | `85.0 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `81.8 / 100` |
| **Route 19785** | ~15.0m | ~15.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:18` | `0.0%` | `71.43%` | 39 | 25 | `+57.1s` |
| `2026-11-05 06:30:18` | `0.0%` | `73.91%` | 71 | 57 | `+112.2s` |
| `2026-11-05 06:00:18` | `0.0%` | `79.03%` | 91 | 75 | `+98.7s` |
| `2026-11-05 05:30:19` | `0.0%` | `77.97%` | 80 | 72 | `+94.6s` |
| `2026-11-05 05:00:18` | `0.0%` | `81.54%` | 83 | 78 | `+74.8s` |
| `2026-11-05 04:30:18` | `0.0%` | `68.66%` | 83 | 83 | `+82.4s` |
| `2026-11-05 04:00:20` | `0.0%` | `88.46%` | 94 | 92 | `+93.8s` |
| `2026-11-05 03:30:19` | `0.0%` | `87.32%` | 93 | 81 | `+88.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.177000+00:00`.*
