# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.727000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.21%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `68` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `34` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+362.8s` (`+6.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+4.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 48.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 11.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 7.4% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 16.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 15 | 7 | 4 | **`26.67%`** | `90.0%` | `-8.4s` |
| **Route 009** | 13 | 6 | 3 | **`23.08%`** | `100.0%` | `+1.5 min` |
| **Route 002** | 14 | 7 | 3 | **`21.43%`** | `85.71%` | `+2.3 min` |
| **Route 005** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-35.5s` |
| **Route 008** | 9 | 6 | 0 | **`0.0%`** | `25.0%` | `-26.1s` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+6.0 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-105.0s` |
| **Route 006** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 003** | `+240.4 min (+14426.0s)` | `+240.4 min (+14426s)` | 1 | `0.0%` |
| **Route 511** | `+6.0 min (+357.0s)` | `+6.7 min (+402s)` | 2 | `0.0%` |
| **Route 006** | `+6.0 min (+357.0s)` | `+9.5 min (+569s)` | 2 | `50.0%` |
| **Route 002** | `+2.3 min (+138.6s)` | `+9.1 min (+546s)` | 7 | `85.71%` |
| **Route 901** | `+1.7 min (+104.0s)` | `+1.7 min (+104s)` | 1 | `100.0%` |
| **Route 903** | `+1.6 min (+95.0s)` | `+1.6 min (+95s)` | 1 | `100.0%` |
| **Route 009** | `+1.5 min (+90.5s)` | `+3.8 min (+230s)` | 6 | `100.0%` |
| **Route 103** | `+0.8 min (+49.0s)` | `+0.8 min (+49s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `88.0 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `90.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32767755` | Route 722 | `24:42:00` | `SCHEDULED` | Assigned vehicle 2690 is missing from active GPS transponder fleet |
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
| `2026-11-08 07:00:18` | `16.18%` | `70.21%` | 68 | 34 | `+362.8s` |
| `2026-11-08 06:30:22` | `15.52%` | `74.71%` | 116 | 73 | `+171.1s` |
| `2026-11-08 06:00:18` | `10.4%` | `74.44%` | 173 | 105 | `+105.1s` |
| `2026-11-08 05:30:23` | `14.98%` | `80.77%` | 227 | 111 | `+67.9s` |
| `2026-11-08 05:00:18` | `15.79%` | `78.2%` | 266 | 121 | `+62.7s` |
| `2026-11-08 04:30:29` | `17.97%` | `81.62%` | 306 | 138 | `+88.1s` |
| `2026-11-08 04:00:19` | `20.67%` | `76.49%` | 358 | 161 | `+103.1s` |
| `2026-11-08 03:30:18` | `23.02%` | `78.86%` | 404 | 172 | `+107.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.727000+00:00`.*
