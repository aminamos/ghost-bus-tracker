# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:22.134000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.11%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `79` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `17` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+118.1s` (`+2.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+46.0s` (`+0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 50.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 3.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 3.8% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 17 | 21.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 18 | 7 | 7 | **`38.89%`** | `90.0%` | `+2.0 min` |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 009** | 12 | 4 | 4 | **`33.33%`** | `85.71%` | `+2.3 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `83.33%` | `+3.0 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `87.5%` | `+0.0 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+0.5 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-44.0s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 709** | `+31.2 min (+1873.0s)` | `+31.2 min (+1873s)` | 1 | `0.0%` |
| **Route 052** | `+4.6 min (+274.0s)` | `+4.6 min (+274s)` | 1 | `100.0%` |
| **Route 002** | `+3.0 min (+177.5s)` | `+6.6 min (+394s)` | 8 | `83.33%` |
| **Route 009** | `+2.3 min (+137.3s)` | `+12.5 min (+748s)` | 4 | `85.71%` |
| **Route 004** | `+2.0 min (+120.1s)` | `+8.8 min (+530s)` | 7 | `90.0%` |
| **Route 903** | `+0.6 min (+34.0s)` | `+1.5 min (+92s)` | 2 | `100.0%` |
| **Route 005** | `+0.5 min (+28.2s)` | `+2.3 min (+136s)` | 5 | `80.0%` |
| **Route 721** | `+0.3 min (+17.0s)` | `+0.3 min (+17s)` | 1 | `100.0%` |
| **Route 507** | `+0.2 min (+15.0s)` | `+0.2 min (+15s)` | 1 | `100.0%` |
| **Route 901** | `+0.2 min (+12.5s)` | `+0.3 min (+20s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `82.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `89.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.1 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.5 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.8 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.9 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.3 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760605` | Route 009 | `25:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904552` | Route 004 | `26:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904550` | Route 004 | `25:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33106705` | Route 004 | `26:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904551` | Route 004 | `25:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:22` | `21.52%` | `85.11%` | 79 | 38 | `+118.1s` |
| `2026-11-28 06:30:18` | `19.23%` | `81.52%` | 130 | 75 | `+120.9s` |
| `2026-11-28 06:00:18` | `14.93%` | `87.18%` | 201 | 112 | `+100.6s` |
| `2026-11-28 05:30:20` | `16.14%` | `79.9%` | 254 | 121 | `+124.7s` |
| `2026-11-28 05:00:22` | `18.09%` | `83.4%` | 304 | 134 | `+129.7s` |
| `2026-11-28 04:30:18` | `19.76%` | `78.71%` | 339 | 150 | `+160.5s` |
| `2026-11-28 04:00:20` | `19.0%` | `79.14%` | 458 | 234 | `+114.5s` |
| `2026-11-28 03:30:20` | `18.43%` | `83.0%` | 559 | 263 | `+82.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:22.134000+00:00`.*
