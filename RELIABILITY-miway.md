# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:18.223000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`83.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `408` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `55` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `348` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-41.7s` (`-0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 5 | 1.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 348 | 85.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `50.0%` | `-147.0s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `100.0%` | `+0.3 min` |
| **Route 1** | 89 | 4 | 83 | **`93.26%`** | `100.0%` | `+0.1 min` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+0.3 min (+19.0s)` | `+0.6 min (+38s)` | 3 | `100.0%` |
| **Route 1** | `+0.1 min (+3.0s)` | `+0.1 min (+6s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `83.7 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.4 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `99.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30726702` | Route 1 | `18:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726711` | Route 1 | `21:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726718` | Route 1 | `23:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726724` | Route 1 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726668` | Route 1 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726678` | Route 1 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726689` | Route 1 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726659` | Route 1 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726669` | Route 1 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726679` | Route 1 | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726690` | Route 1 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726701` | Route 1 | `18:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726710` | Route 1 | `20:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726661` | Route 1 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726671` | Route 1 | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:18` | `85.29%` | `83.33%` | 408 | 55 | `-41.7s` |
| `2026-11-05 06:30:18` | `80.0%` | `71.43%` | 435 | 80 | `-43.6s` |
| `2026-11-05 06:00:18` | `77.61%` | `72.22%` | 451 | 91 | `-23.3s` |
| `2026-11-05 05:30:19` | `8.26%` | `55.56%` | 109 | 99 | `+7.0s` |
| `2026-11-05 05:00:18` | `9.92%` | `100.0%` | 131 | 116 | `+61.1s` |
| `2026-11-05 04:30:18` | `12.33%` | `77.78%` | 146 | 128 | `+28.3s` |
| `2026-11-05 04:00:20` | `13.5%` | `41.67%` | 163 | 139 | `-85.2s` |
| `2026-11-05 03:30:19` | `15.22%` | `54.55%` | 184 | 157 | `-12.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.223000+00:00`.*
