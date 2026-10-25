# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-25T06:15:47.614000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.21%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `140` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `90` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `14` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+40.2s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+8.5s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 82 | 58.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 22 | 15.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 4.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 1.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 14 | 10.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 518** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-62.0s` |
| **Route 004** | 19 | 11 | 6 | **`31.58%`** | `69.23%` | `+4.0 min` |
| **Route 002** | 14 | 8 | 4 | **`28.57%`** | `66.67%` | `+2.3 min` |
| **Route 007** | 6 | 6 | 0 | **`0.0%`** | `80.0%` | `+0.4 min` |
| **Route 009** | 9 | 7 | 0 | **`0.0%`** | `80.0%` | `+1.6 min` |
| **Route 121** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 103** | 4 | 3 | 0 | **`0.0%`** | `75.0%` | `-56.8s` |
| **Route 722** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 107** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `40.0%` | `-60.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 004** | `+4.0 min (+238.5s)` | `+21.6 min (+1294s)` | 11 | `69.23%` |
| **Route 901** | `+3.4 min (+203.0s)` | `+5.7 min (+342s)` | 2 | `66.67%` |
| **Route 056** | `+3.3 min (+197.2s)` | `+18.8 min (+1125s)` | 5 | `60.0%` |
| **Route 721** | `+3.2 min (+190.0s)` | `+4.0 min (+243s)` | 1 | `100.0%` |
| **Route 495** | `+2.8 min (+168.0s)` | `+2.8 min (+168s)` | 1 | `100.0%` |
| **Route 716** | `+2.4 min (+143.0s)` | `+2.4 min (+143s)` | 1 | `100.0%` |
| **Route 002** | `+2.3 min (+135.2s)` | `+13.8 min (+827s)` | 8 | `66.67%` |
| **Route 915** | `+2.2 min (+130.0s)` | `+2.2 min (+130s)` | 1 | `100.0%` |
| **Route 107** | `+1.6 min (+98.0s)` | `+2.3 min (+138s)` | 2 | `100.0%` |
| **Route 009** | `+1.6 min (+93.8s)` | `+6.4 min (+384s)` | 7 | `80.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 056** | ~30.0m | ~30.0m | **`+0.0 min`** | `70.7 / 100` |
| **Route 004** | ~25.0m | ~25.0m | **`+0.0 min`** | `72.1 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `79.9 / 100` |
| **Route 009** | ~21.0m | ~21.0m | **`+0.0 min`** | `86.8 / 100` |
| **Route 103** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.7 / 100` |
| **Route 901** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.1 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `92.8 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.4 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.9 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32767214` | Route 902 | `23:54:00` | `SCHEDULED` | Assigned vehicle 3145 is missing from active GPS transponder fleet |
| `32769170` | Route 003 | `24:00:00` | `SCHEDULED` | Assigned vehicle 3317 is missing from active GPS transponder fleet |
| `32768953` | Route 518 | `24:16:00` | `SCHEDULED` | Assigned vehicle 3351 is broadcasting off-schedule with no vehicle covering 32768953 |
| `32766776` | Route 002 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32768953` | Route 518 | `24:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766774` | Route 002 | `25:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765271` | Route 004 | `24:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765275` | Route 004 | `26:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766771` | Route 002 | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765274` | Route 004 | `26:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765272` | Route 004 | `24:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765278` | Route 004 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766775` | Route 002 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765273` | Route 004 | `25:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:47` | `10.0%` | `73.21%` | 140 | 90 | `+40.2s` |
| `2026-10-25 06:00:58` | `9.44%` | `79.86%` | 180 | 104 | `+61.7s` |
| `2026-10-25 05:30:24` | `13.42%` | `76.44%` | 231 | 111 | `+58.0s` |
| `2026-10-25 04:33:57` | `18.09%` | `82.98%` | 304 | 135 | `+51.1s` |
| `2026-10-25 03:30:20` | `21.87%` | `82.47%` | 407 | 173 | `+158.1s` |
| `2026-10-25 03:00:22` | `24.34%` | `81.21%` | 452 | 176 | `+168.3s` |
| `2026-10-25 02:30:20` | `27.18%` | `80.9%` | 482 | 180 | `+172.9s` |
| `2026-10-25 01:30:20` | `31.23%` | `77.21%` | 570 | 219 | `+147.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:47.614000+00:00`.*
