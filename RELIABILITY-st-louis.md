# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-12T07:00:20.041000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`69.57%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `43` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `28` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-31.3s` (`-0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-60.0s` (`-1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 37.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 16.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 15 | 34.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-240.0s` |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route 19780** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-180.0s` |
| **Route 19792** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route UNKNOWN** | 15 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19780** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19778** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |
| **Route 19787** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19792** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 3 | `100.0%` |
| **Route 19798** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19777** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19800** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19797** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 2 | `100.0%` |
| **Route 19793** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `90.5 / 100` |
| **Route 19750** | ~26.0m | ~26.0m | **`+0.0 min`** | `92.3 / 100` |
| **Route 19792** | ~17.5m | ~17.5m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:20` | `0.0%` | `69.57%` | 43 | 28 | `-31.3s` |
| `2026-11-12 06:30:19` | `0.0%` | `72.92%` | 73 | 58 | `+28.8s` |
| `2026-11-12 06:00:19` | `0.0%` | `0.0%` | 16 | 0 | `+0.0s` |
| `2026-11-12 05:30:18` | `0.0%` | `68.42%` | 79 | 79 | `+85.3s` |
| `2026-11-12 05:00:19` | `0.0%` | `78.46%` | 82 | 82 | `+73.8s` |
| `2026-11-12 04:30:19` | `0.0%` | `75.0%` | 87 | 81 | `+108.5s` |
| `2026-11-12 04:00:20` | `0.0%` | `73.53%` | 92 | 90 | `+107.6s` |
| `2026-11-12 03:30:19` | `0.0%` | `76.47%` | 94 | 88 | `+172.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:20.041000+00:00`.*
