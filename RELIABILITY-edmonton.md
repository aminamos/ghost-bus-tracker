# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-10T07:00:18.945000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`84.78%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `65` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+53.6s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+19.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 60.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 7.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.5% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 9.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+2.2 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.2 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-2.0s` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.9 min` |
| **Route 009** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 056** | 3 | 3 | 0 | **`0.0%`** | `50.0%` | `-98.0s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-115.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 509A** | `+18.2 min (+1095.0s)` | `+18.2 min (+1095s)` | 1 | `0.0%` |
| **Route 715** | `+7.3 min (+441.0s)` | `+7.3 min (+441s)` | 1 | `0.0%` |
| **Route 511** | `+3.9 min (+234.0s)` | `+3.9 min (+234s)` | 2 | `100.0%` |
| **Route 523** | `+2.2 min (+132.0s)` | `+2.2 min (+132s)` | 1 | `100.0%` |
| **Route 002** | `+2.2 min (+131.4s)` | `+5.0 min (+300s)` | 8 | `100.0%` |
| **Route 004** | `+1.2 min (+69.8s)` | `+2.0 min (+121s)` | 7 | `100.0%` |
| **Route 918A** | `+0.8 min (+47.0s)` | `+0.8 min (+47s)` | 1 | `100.0%` |
| **Route 005** | `+0.7 min (+44.5s)` | `+2.1 min (+129s)` | 4 | `100.0%` |
| **Route 009** | `+0.3 min (+16.0s)` | `+0.3 min (+16s)` | 3 | `100.0%` |
| **Route 008** | `+0.1 min (+8.9s)` | `+2.0 min (+123s)` | 6 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.7 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.9 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.7 / 100` |
| **Route 009** | ~45.0m | ~45.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33276367` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33276366` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33270793` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33270791` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33276365` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33270792` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:18` | `9.23%` | `84.78%` | 65 | 37 | `+53.6s` |
| `2026-11-10 06:30:19` | `9.91%` | `78.82%` | 111 | 71 | `+24.2s` |
| `2026-11-10 06:00:18` | `7.1%` | `86.45%` | 183 | 111 | `+48.6s` |
| `2026-11-10 05:30:21` | `8.51%` | `87.94%` | 235 | 119 | `+54.5s` |
| `2026-11-10 05:00:19` | `11.11%` | `86.97%` | 279 | 133 | `+68.5s` |
| `2026-11-10 04:30:23` | `15.0%` | `86.77%` | 320 | 150 | `+72.5s` |
| `2026-11-10 04:00:20` | `14.06%` | `81.09%` | 434 | 234 | `+47.1s` |
| `2026-11-10 03:30:18` | `15.03%` | `79.73%` | 539 | 262 | `+33.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:18.945000+00:00`.*
