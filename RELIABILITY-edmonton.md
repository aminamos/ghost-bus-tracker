# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:22.335000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`22.37%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `76` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `17` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+13.3s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+7.5s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 47.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 11.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 3.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 17 | 22.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 004** | 18 | 7 | 7 | **`38.89%`** | `90.0%` | `+0.8 min` |
| **Route 009** | 13 | 5 | 4 | **`30.77%`** | `66.67%` | `-11.8s` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `75.0%` | `+3.2 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+0.7 min` |
| **Route 008** | 9 | 5 | 0 | **`0.0%`** | `88.89%` | `-91.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-206.0s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-108.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | `+3.2 min (+189.4s)` | `+7.8 min (+467s)` | 8 | `75.0%` |
| **Route 523** | `+1.4 min (+85.0s)` | `+1.4 min (+85s)` | 1 | `100.0%` |
| **Route 903** | `+1.2 min (+69.5s)` | `+1.7 min (+103s)` | 2 | `100.0%` |
| **Route 004** | `+0.8 min (+45.0s)` | `+2.1 min (+128s)` | 7 | `90.0%` |
| **Route 005** | `+0.7 min (+42.0s)` | `+6.3 min (+376s)` | 5 | `40.0%` |
| **Route 721** | `+0.2 min (+10.0s)` | `+0.2 min (+10s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.5m | ~30.5m | **`+0.0 min`** | `74.9 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `84.9 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.8 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.9 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760603` | Route 009 | `24:10:00` | `SCHEDULED` | Assigned vehicle 2253 is broadcasting off-schedule with no vehicle covering 32760603 |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904552` | Route 004 | `26:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904550` | Route 004 | `25:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33106705` | Route 004 | `26:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904551` | Route 004 | `25:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:22` | `22.37%` | `75.0%` | 76 | 37 | `+13.3s` |
| `2026-11-26 06:30:19` | `19.2%` | `80.0%` | 125 | 72 | `+37.9s` |
| `2026-11-26 06:00:18` | `16.0%` | `90.97%` | 200 | 110 | `+58.3s` |
| `2026-11-26 05:30:28` | `16.47%` | `86.73%` | 249 | 117 | `+62.4s` |
| `2026-11-26 05:00:18` | `18.6%` | `90.6%` | 301 | 132 | `+64.8s` |
| `2026-11-26 04:30:22` | `19.71%` | `87.6%` | 340 | 147 | `+128.5s` |
| `2026-11-26 04:00:25` | `18.18%` | `84.36%` | 462 | 233 | `+122.2s` |
| `2026-11-26 03:30:24` | `18.89%` | `85.13%` | 561 | 259 | `+72.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:22.335000+00:00`.*
