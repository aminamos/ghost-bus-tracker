# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.824000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`84.44%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `74` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+34.2s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+16.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 38 | 51.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 5.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 4.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 16.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 009** | 11 | 4 | 3 | **`27.27%`** | `100.0%` | `-11.8s` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `80.0%` | `+2.6 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+0.5 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `88.89%` | `+0.4 min` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 721** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-136.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 523** | `+10.2 min (+613.0s)` | `+10.2 min (+613s)` | 1 | `0.0%` |
| **Route 002** | `+2.6 min (+156.0s)` | `+5.2 min (+309s)` | 8 | `80.0%` |
| **Route 715** | `+0.8 min (+48.0s)` | `+0.8 min (+48s)` | 1 | `100.0%` |
| **Route 721** | `+0.5 min (+30.5s)` | `+1.2 min (+73s)` | 2 | `100.0%` |
| **Route 005** | `+0.5 min (+29.8s)` | `+1.9 min (+115s)` | 4 | `100.0%` |
| **Route 004** | `+0.5 min (+27.3s)` | `+2.0 min (+123s)` | 7 | `100.0%` |
| **Route 918A** | `+0.5 min (+27.0s)` | `+0.5 min (+27s)` | 1 | `100.0%` |
| **Route 008** | `+0.4 min (+25.6s)` | `+5.5 min (+327s)` | 6 | `88.89%` |
| **Route 903** | `+0.4 min (+25.0s)` | `+0.8 min (+49s)` | 2 | `100.0%` |
| **Route 056** | `+0.1 min (+7.5s)` | `+1.5 min (+88s)` | 2 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.9 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 721** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.8 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `16.22%` | `84.44%` | 74 | 38 | `+34.2s` |
| `2026-11-25 06:30:19` | `16.13%` | `75.0%` | 124 | 73 | `+13.6s` |
| `2026-11-25 06:00:20` | `11.68%` | `92.36%` | 197 | 112 | `+43.6s` |
| `2026-11-25 05:30:18` | `12.75%` | `84.95%` | 251 | 122 | `+33.4s` |
| `2026-11-25 05:00:19` | `15.2%` | `88.38%` | 296 | 134 | `+67.4s` |
| `2026-11-25 04:30:18` | `16.11%` | `86.31%` | 329 | 149 | `+92.0s` |
| `2026-11-25 04:00:19` | `17.92%` | `83.62%` | 452 | 231 | `+62.0s` |
| `2026-11-25 03:00:27` | `18.83%` | `79.8%` | 632 | 267 | `+42.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.824000+00:00`.*
