# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-03T07:00:18.755000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`52.17%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `29` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+78.3s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-60.0s` (`-1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 12 | 27.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 18.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 4.5% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 15 | 34.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-120.0s` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+12.5 min` |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.5 min` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-120.0s` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 19792** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route UNKNOWN** | 15 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19768** | `+12.5 min (+750.0s)` | `+21.0 min (+1260s)` | 2 | `50.0%` |
| **Route 19788** | `+10.0 min (+600.0s)` | `+10.0 min (+600s)` | 1 | `0.0%` |
| **Route 19777** | `+9.0 min (+540.0s)` | `+9.0 min (+540s)` | 1 | `0.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19784** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19749** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19793** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19798** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19778** | `+0.5 min (+30.0s)` | `+3.0 min (+180s)` | 2 | `50.0%` |
| **Route 19785** | `+0.5 min (+30.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `50.0 / 100` |
| **Route 19785** | ~15.0m | ~15.0m | **`+0.0 min`** | `90.0 / 100` |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `95.2 / 100` |
| **Route 19750** | ~26.0m | ~26.0m | **`+0.0 min`** | `96.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `0.0%` | `52.17%` | 44 | 29 | `+78.3s` |
| `2026-11-03 06:30:26` | `0.0%` | `71.74%` | 73 | 59 | `+54.8s` |
| `2026-11-03 06:00:19` | `0.0%` | `86.0%` | 84 | 68 | `+55.2s` |
| `2026-11-03 05:30:18` | `0.0%` | `78.33%` | 86 | 76 | `+60.0s` |
| `2026-11-03 05:00:25` | `0.0%` | `83.58%` | 85 | 80 | `+37.6s` |
| `2026-11-03 04:30:21` | `0.0%` | `79.1%` | 84 | 81 | `+83.3s` |
| `2026-11-03 04:00:19` | `0.0%` | `78.08%` | 100 | 91 | `+54.2s` |
| `2026-11-03 03:30:20` | `0.0%` | `84.29%` | 100 | 89 | `+110.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.755000+00:00`.*
