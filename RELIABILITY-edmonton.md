# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:18.081000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`87.23%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `78` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `15` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+41.5s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+20.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 41 | 52.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 5.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 15 | 19.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 009** | 16 | 4 | 6 | **`37.5%`** | `100.0%` | `+0.1 min` |
| **Route 004** | 12 | 6 | 3 | **`25.0%`** | `100.0%` | `+0.9 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `87.5%` | `+1.6 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `87.5%` | `+0.7 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 721** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-14.5s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-94.0s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 052** | `+4.6 min (+274.0s)` | `+4.6 min (+274s)` | 1 | `100.0%` |
| **Route 523** | `+2.3 min (+140.0s)` | `+2.3 min (+140s)` | 1 | `100.0%` |
| **Route 002** | `+1.6 min (+98.2s)` | `+5.1 min (+307s)` | 8 | `87.5%` |
| **Route 056** | `+1.5 min (+88.0s)` | `+3.0 min (+181s)` | 2 | `100.0%` |
| **Route 004** | `+0.9 min (+54.9s)` | `+2.5 min (+151s)` | 6 | `100.0%` |
| **Route 903** | `+0.8 min (+50.0s)` | `+1.3 min (+78s)` | 2 | `100.0%` |
| **Route 005** | `+0.7 min (+43.4s)` | `+1.8 min (+106s)` | 5 | `100.0%` |
| **Route 008** | `+0.7 min (+40.8s)` | `+6.8 min (+408s)` | 6 | `87.5%` |
| **Route 009** | `+0.1 min (+7.8s)` | `+1.9 min (+114s)` | 4 | `100.0%` |
| **Route 053** | `+0.1 min (+4.0s)` | `+0.1 min (+4s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `90.6 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.7 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.0 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.1 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.5 / 100` |
| **Route 721** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756145` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756146` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756144` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:18` | `19.23%` | `87.23%` | 78 | 38 | `+41.5s` |
| `2026-11-05 06:30:18` | `16.92%` | `82.42%` | 130 | 78 | `+17.4s` |
| `2026-11-05 06:00:18` | `16.26%` | `86.54%` | 203 | 109 | `+74.8s` |
| `2026-11-05 05:30:20` | `18.36%` | `85.93%` | 256 | 116 | `+61.2s` |
| `2026-11-05 05:00:18` | `18.41%` | `92.53%` | 315 | 133 | `+62.2s` |
| `2026-11-05 04:30:18` | `22.6%` | `88.14%` | 354 | 149 | `+55.7s` |
| `2026-11-05 04:00:24` | `22.08%` | `85.55%` | 480 | 233 | `+66.7s` |
| `2026-11-05 03:30:19` | `21.8%` | `81.45%` | 601 | 264 | `+66.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.081000+00:00`.*
