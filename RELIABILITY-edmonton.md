# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-18T07:00:32.385000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`78.72%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `77` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+16.9s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+8.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 48.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 10.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 15.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `66.67%` | `-14.3s` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+2.2 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+0.8 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+1.8 min` |
| **Route 903** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `70.0%` | `-83.8s` |
| **Route 901** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-68.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 007** | `+7.8 min (+468.0s)` | `+7.8 min (+468s)` | 1 | `0.0%` |
| **Route 002** | `+2.2 min (+130.2s)` | `+4.4 min (+262s)` | 8 | `100.0%` |
| **Route 005** | `+1.8 min (+105.8s)` | `+9.1 min (+543s)` | 5 | `80.0%` |
| **Route 918A** | `+1.3 min (+78.0s)` | `+1.3 min (+78s)` | 1 | `100.0%` |
| **Route 004** | `+0.8 min (+45.6s)` | `+3.2 min (+190s)` | 7 | `100.0%` |
| **Route 056** | `+0.5 min (+29.0s)` | `+1.1 min (+69s)` | 2 | `100.0%` |
| **Route 903** | `+0.4 min (+21.5s)` | `+0.6 min (+35s)` | 2 | `100.0%` |
| **Route 721** | `+0.1 min (+6.0s)` | `+0.1 min (+6s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `75.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `86.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.7 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 901** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.5 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 07:00:32` | `15.58%` | `78.72%` | 77 | 37 | `+16.9s` |
| `2026-11-18 06:30:20` | `17.46%` | `81.61%` | 126 | 73 | `+38.9s` |
| `2026-11-18 06:00:28` | `13.57%` | `87.97%` | 199 | 112 | `+54.8s` |
| `2026-11-18 05:30:29` | `14.96%` | `82.3%` | 254 | 120 | `+92.0s` |
| `2026-11-18 05:00:20` | `16.16%` | `91.7%` | 297 | 135 | `+62.7s` |
| `2026-11-18 04:30:19` | `18.37%` | `85.77%` | 332 | 146 | `+50.8s` |
| `2026-11-18 04:00:18` | `17.59%` | `84.94%` | 449 | 231 | `+41.1s` |
| `2026-11-18 03:30:18` | `18.02%` | `82.54%` | 555 | 262 | `+40.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T07:00:32.385000+00:00`.*
