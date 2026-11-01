# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-01T07:00:19.045000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `75` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `41` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+395.5s` (`+6.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+126.5s` (`+2.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 26 | 34.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 9.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 9 | 12.0% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 13.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 13.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 16 | 8 | 4 | **`25.0%`** | `33.33%` | `+11.2 min` |
| **Route 009** | 13 | 6 | 3 | **`23.08%`** | `100.0%` | `+0.9 min` |
| **Route 002** | 14 | 7 | 3 | **`21.43%`** | `85.71%` | `+1.7 min` |
| **Route 008** | 10 | 7 | 0 | **`0.0%`** | `40.0%` | `+15.5 min` |
| **Route 056** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-99.7s` |
| **Route 006** | 3 | 2 | 0 | **`0.0%`** | `33.33%` | `+7.8 min` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.9 min` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+6.1 min` |
| **Route 007** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+19.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 007** | `+19.0 min (+1138.0s)` | `+21.0 min (+1258s)` | 2 | `0.0%` |
| **Route 008** | `+15.5 min (+930.0s)` | `+49.6 min (+2976s)` | 7 | `40.0%` |
| **Route 004** | `+11.2 min (+674.7s)` | `+31.0 min (+1859s)` | 8 | `33.33%` |
| **Route 006** | `+7.8 min (+468.7s)` | `+13.8 min (+828s)` | 2 | `33.33%` |
| **Route 511** | `+6.1 min (+365.0s)` | `+6.8 min (+410s)` | 2 | `0.0%` |
| **Route 002** | `+1.7 min (+99.6s)` | `+6.7 min (+400s)` | 7 | `85.71%` |
| **Route 722** | `+1.4 min (+81.0s)` | `+1.4 min (+81s)` | 1 | `100.0%` |
| **Route 009** | `+0.9 min (+54.7s)` | `+4.0 min (+242s)` | 6 | `100.0%` |
| **Route 005** | `+0.9 min (+52.2s)` | `+9.2 min (+553s)` | 4 | `0.0%` |
| **Route 901** | `+0.7 min (+40.0s)` | `+0.7 min (+40s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.1 min`** | `37.6 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.1 min`** | `53.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `61.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `76.3 / 100` |
| **Route 006** | ~20.0m | ~20.0m | **`+0.0 min`** | `72.0 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `73.2 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.0 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `90.0 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32766776` | Route 002 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770182` | Route 009 | `25:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770183` | Route 009 | `26:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770184` | Route 009 | `26:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765275` | Route 004 | `26:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765274` | Route 004 | `26:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766771` | Route 002 | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765278` | Route 004 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766775` | Route 002 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765273` | Route 004 | `25:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:19` | `13.33%` | `50.0%` | 75 | 41 | `+395.5s` |
| `2026-11-01 06:30:19` | `12.1%` | `64.89%` | 124 | 79 | `+316.1s` |
| `2026-11-01 06:00:23` | `12.15%` | `74.64%` | 181 | 104 | `+198.4s` |
| `2026-11-01 05:30:19` | `15.29%` | `72.4%` | 242 | 115 | `+142.5s` |
| `2026-11-01 05:00:24` | `16.91%` | `74.29%` | 278 | 124 | `+238.8s` |
| `2026-11-01 04:30:20` | `17.5%` | `72.18%` | 320 | 143 | `+177.8s` |
| `2026-11-01 04:00:20` | `21.08%` | `71.06%` | 370 | 165 | `+158.4s` |
| `2026-11-01 03:30:18` | `22.46%` | `73.62%` | 414 | 174 | `+226.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:19.045000+00:00`.*
