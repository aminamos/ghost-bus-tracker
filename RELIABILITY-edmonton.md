# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-12T07:00:19.362000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `67` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+20.2s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+1.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 30 | 44.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 14 | 20.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 6.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 10.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 15 | 7 | 4 | **`26.67%`** | `90.0%` | `+0.4 min` |
| **Route 002** | 15 | 7 | 3 | **`20.0%`** | `88.89%` | `+1.6 min` |
| **Route 009** | 9 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 008** | 10 | 7 | 0 | **`0.0%`** | `0.0%` | `-93.0s` |
| **Route 007** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-184.0s` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+6.1 min` |
| **Route 006** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-5.0s` |
| **Route 005** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-128.7s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 511** | `+6.1 min (+368.0s)` | `+6.9 min (+413s)` | 2 | `0.0%` |
| **Route 518** | `+5.9 min (+352.0s)` | `+5.9 min (+352s)` | 1 | `0.0%` |
| **Route 002** | `+1.6 min (+93.3s)` | `+5.3 min (+317s)` | 7 | `88.89%` |
| **Route 722** | `+1.4 min (+84.0s)` | `+1.4 min (+84s)` | 1 | `100.0%` |
| **Route 009** | `+0.5 min (+31.3s)` | `+2.6 min (+155s)` | 6 | `100.0%` |
| **Route 004** | `+0.4 min (+26.6s)` | `+3.5 min (+207s)` | 7 | `90.0%` |
| **Route 509A** | `+0.4 min (+22.0s)` | `+0.4 min (+22s)` | 1 | `100.0%` |
| **Route 103** | `+0.1 min (+5.0s)` | `+0.1 min (+5s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.0 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.8 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.1 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32766776` | Route 002 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
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
| `2026-11-12 07:00:19` | `10.45%` | `62.5%` | 67 | 37 | `+20.2s` |
| `2026-11-12 06:30:18` | `11.01%` | `75.0%` | 109 | 70 | `+0.1s` |
| `2026-11-12 06:00:19` | `7.41%` | `78.79%` | 162 | 100 | `+7.9s` |
| `2026-11-12 05:30:18` | `8.96%` | `78.49%` | 212 | 108 | `+10.5s` |
| `2026-11-12 05:00:18` | `9.5%` | `76.3%` | 242 | 116 | `+9.0s` |
| `2026-11-12 04:30:20` | `11.55%` | `75.42%` | 277 | 132 | `+16.9s` |
| `2026-11-12 04:00:20` | `13.12%` | `72.39%` | 320 | 157 | `+43.4s` |
| `2026-11-12 03:30:19` | `13.93%` | `77.18%` | 359 | 168 | `+18.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:19.362000+00:00`.*
