# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-20T06:30:18.982000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`74.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `74` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `60` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+67.2s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 50.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 13.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 4.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 18.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19757** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route 19783** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route 19767** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 19754** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19755** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 19788** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 19778** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 19776** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19785** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 19780** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19793** | `+6.5 min (+390.0s)` | `+14.0 min (+840s)` | 2 | `50.0%` |
| **Route 19781** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19775** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19797** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19787** | `+4.5 min (+270.0s)` | `+5.0 min (+300s)` | 3 | `100.0%` |
| **Route 19792** | `+3.3 min (+200.0s)` | `+8.0 min (+480s)` | 4 | `66.67%` |
| **Route 19767** | `+3.0 min (+180.0s)` | `+4.0 min (+240s)` | 2 | `100.0%` |
| **Route 19785** | `+3.0 min (+180.0s)` | `+5.0 min (+300s)` | 3 | `100.0%` |
| **Route 19777** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19776** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19759** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19792** | ~5.0m | ~5.0m | **`+0.0 min`** | `26.4 / 100` |
| **Route 19798** | ~9.0m | ~9.0m | **`+0.0 min`** | `66.7 / 100` |
| **Route 19788** | ~4.0m | ~4.0m | **`+0.0 min`** | `62.5 / 100` |
| **Route 19780** | ~16.0m | ~16.0m | **`+0.0 min`** | `81.2 / 100` |
| **Route 19754** | ~710.0m | ~710.0m | **`+0.0 min`** | `99.2 / 100` |
| **Route 19793** | ~1424.0m | ~1424.0m | **`+0.0 min`** | `99.5 / 100` |
| **Route 19800** | ~10.0m | ~10.0m | **`+0.0 min`** | `95.0 / 100` |
| **Route 19783** | ~1430.0m | ~1430.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 19755** | ~1416.0m | ~1416.0m | **`+0.0 min`** | `99.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 06:30:18` | `0.0%` | `74.0%` | 74 | 60 | `+67.2s` |
| `2026-11-20 06:00:20` | `0.0%` | `77.05%` | 88 | 74 | `+70.8s` |
| `2026-11-20 05:30:18` | `0.0%` | `78.69%` | 77 | 75 | `+108.2s` |
| `2026-11-20 05:00:20` | `0.0%` | `71.23%` | 87 | 84 | `+132.3s` |
| `2026-11-20 04:30:18` | `0.0%` | `81.08%` | 84 | 84 | `+143.5s` |
| `2026-11-20 04:00:18` | `0.0%` | `70.67%` | 90 | 90 | `+92.0s` |
| `2026-11-20 03:30:20` | `0.0%` | `75.32%` | 90 | 90 | `+123.1s` |
| `2026-11-20 03:00:19` | `0.0%` | `74.67%` | 88 | 88 | `+140.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:18.982000+00:00`.*
