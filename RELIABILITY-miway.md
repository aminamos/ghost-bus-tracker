# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-03T07:00:18.759000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`83.76%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `394` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `330` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+27.5s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 6 | 1.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 330 | 83.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `100.0%` | `+0.1 min` |
| **Route 1** | 91 | 6 | 82 | **`90.11%`** | `75.0%` | `-42.0s` |
| **Route 7** | 58 | 4 | 52 | **`89.66%`** | `50.0%` | `+3.1 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7** | `+3.1 min (+185.5s)` | `+6.2 min (+371s)` | 4 | `50.0%` |
| **Route 17** | `+0.1 min (+8.5s)` | `+0.3 min (+17s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7** | ~25.0m | ~25.0m | **`+0.0 min`** | `87.6 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `91.3 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30740082` | Route 7 | `22:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740077` | Route 7 | `20:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740085` | Route 7 | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740081` | Route 7 | `22:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740076` | Route 7 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740084` | Route 7 | `24:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740080` | Route 7 | `21:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740075` | Route 7 | `19:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740078` | Route 7 | `20:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740072` | Route 7 | `18:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740066` | Route 7 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740061` | Route 7 | `12:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740069` | Route 7 | `16:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740063` | Route 7 | `13:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740058` | Route 7 | `10:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `83.76%` | `75.0%` | 394 | 57 | `+27.5s` |
| `2026-11-03 06:30:26` | `79.76%` | `56.25%` | 415 | 76 | `+67.4s` |
| `2026-11-03 06:00:19` | `76.55%` | `78.95%` | 435 | 91 | `-23.2s` |
| `2026-11-03 05:30:18` | `8.11%` | `62.5%` | 111 | 101 | `-87.0s` |
| `2026-11-03 05:00:26` | `9.23%` | `45.45%` | 130 | 115 | `-50.3s` |
| `2026-11-03 04:30:21` | `12.33%` | `33.33%` | 146 | 128 | `+62.6s` |
| `2026-11-03 04:00:20` | `13.58%` | `44.44%` | 162 | 138 | `-60.3s` |
| `2026-11-03 03:30:20` | `15.43%` | `40.0%` | 175 | 148 | `-125.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.759000+00:00`.*
