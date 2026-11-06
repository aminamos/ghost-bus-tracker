# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-06T07:00:18.245000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.63%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `69` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `36` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+14.5s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+11.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 58.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 10.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 14.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 009** | 11 | 4 | 4 | **`36.36%`** | `100.0%` | `-4.1s` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `87.5%` | `+2.2 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+0.8 min` |
| **Route 008** | 8 | 5 | 0 | **`0.0%`** | `85.71%` | `-132.4s` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `-42.6s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-54.0s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-96.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 715** | `+7.1 min (+425.0s)` | `+7.1 min (+425s)` | 1 | `0.0%` |
| **Route 052** | `+3.7 min (+224.0s)` | `+3.7 min (+224s)` | 1 | `100.0%` |
| **Route 002** | `+2.2 min (+134.8s)` | `+6.7 min (+399s)` | 8 | `87.5%` |
| **Route 903** | `+1.8 min (+108.0s)` | `+2.4 min (+142s)` | 2 | `100.0%` |
| **Route 004** | `+0.8 min (+47.2s)` | `+2.6 min (+158s)` | 7 | `100.0%` |
| **Route 918A** | `+0.3 min (+19.0s)` | `+0.3 min (+19s)` | 1 | `100.0%` |
| **Route 721** | `+0.3 min (+16.0s)` | `+0.3 min (+16s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~31.0m | ~31.0m | **`+0.0 min`** | `72.7 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `90.7 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.7 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.6 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760711` | Route 009 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `14.49%` | `81.63%` | 69 | 36 | `+14.5s` |
| `2026-11-06 06:30:19` | `13.68%` | `81.61%` | 117 | 71 | `+16.7s` |
| `2026-11-06 06:00:18` | `10.64%` | `90.91%` | 188 | 111 | `+68.4s` |
| `2026-11-06 05:30:22` | `11.79%` | `90.0%` | 246 | 122 | `+60.0s` |
| `2026-11-06 05:00:20` | `14.38%` | `92.21%` | 292 | 134 | `+83.2s` |
| `2026-11-06 04:30:20` | `18.13%` | `90.0%` | 331 | 148 | `+57.8s` |
| `2026-11-06 04:00:23` | `17.32%` | `86.76%` | 456 | 236 | `+40.6s` |
| `2026-11-06 03:30:21` | `18.39%` | `85.88%` | 560 | 262 | `+46.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.245000+00:00`.*
