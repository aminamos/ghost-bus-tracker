# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:19.085000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.63%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `73` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+26.1s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+6.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 35 | 47.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 14 | 19.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 15.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 005** | 3 | 2 | 1 | **`33.33%`** | `50.0%` | `-59.5s` |
| **Route 004** | 14 | 6 | 4 | **`28.57%`** | `100.0%` | `+1.2 min` |
| **Route 002** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.0 min` |
| **Route 009** | 9 | 6 | 0 | **`0.0%`** | `87.5%` | `+2.1 min` |
| **Route 008** | 10 | 7 | 0 | **`0.0%`** | `20.0%` | `-89.9s` |
| **Route 523** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-161.0s` |
| **Route 006** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.8 min` |
| **Route 703** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-142.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 709** | `+5.7 min (+339.0s)` | `+5.7 min (+339s)` | 1 | `0.0%` |
| **Route A16** | `+4.4 min (+263.0s)` | `+4.4 min (+263s)` | 1 | `100.0%` |
| **Route 006** | `+2.8 min (+167.0s)` | `+3.9 min (+236s)` | 2 | `100.0%` |
| **Route 722** | `+2.4 min (+142.0s)` | `+2.4 min (+142s)` | 1 | `100.0%` |
| **Route 009** | `+2.1 min (+124.4s)` | `+7.1 min (+427s)` | 6 | `87.5%` |
| **Route 004** | `+1.2 min (+70.2s)` | `+3.1 min (+188s)` | 6 | `100.0%` |
| **Route 002** | `+1.0 min (+58.1s)` | `+4.6 min (+274s)` | 7 | `100.0%` |
| **Route 901** | `+0.7 min (+42.0s)` | `+0.7 min (+42s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.7 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32765746` | Route 005 | `24:20:00` | `SCHEDULED` | Assigned vehicle 3401 is missing from active GPS transponder fleet |
| `32770894` | Route 511 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770895` | Route 511 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770893` | Route 511 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766776` | Route 002 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765275` | Route 004 | `26:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766771` | Route 002 | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765274` | Route 004 | `26:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765278` | Route 004 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766775` | Route 002 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765273` | Route 004 | `25:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:19` | `15.07%` | `68.63%` | 73 | 38 | `+26.1s` |
| `2026-11-15 06:30:18` | `10.17%` | `67.39%` | 118 | 74 | `+494.9s` |
| `2026-11-15 06:00:32` | `9.6%` | `77.7%` | 177 | 105 | `+299.6s` |
| `2026-11-15 05:30:19` | `11.69%` | `77.84%` | 231 | 114 | `+185.9s` |
| `2026-11-15 05:00:19` | `12.73%` | `76.61%` | 267 | 121 | `+171.6s` |
| `2026-11-15 04:30:23` | `14.85%` | `75.62%` | 303 | 138 | `+143.1s` |
| `2026-11-15 04:00:19` | `17.23%` | `76.07%` | 354 | 163 | `+147.4s` |
| `2026-11-15 03:30:18` | `19.08%` | `74.43%` | 393 | 172 | `+125.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.085000+00:00`.*
