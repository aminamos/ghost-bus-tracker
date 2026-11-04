# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:22.970000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.79%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`78.72%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `76` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+482.5s` (`+8.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+21.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 48.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 7.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 5.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 15.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 009** | 16 | 4 | 6 | **`37.5%`** | `66.67%` | `+0.1 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+1.6 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `87.5%` | `+1.3 min` |
| **Route 008** | 8 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-19.0s` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-32.0s` |
| **Route 506** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-60.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 719** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+137.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 719** | `+137.5 min (+8249.5s)` | `+137.6 min (+8254s)` | 1 | `0.0%` |
| **Route 519** | `+57.6 min (+3457.0s)` | `+57.6 min (+3457s)` | 1 | `0.0%` |
| **Route 509A** | `+17.6 min (+1055.0s)` | `+17.6 min (+1055s)` | 1 | `0.0%` |
| **Route 052** | `+4.2 min (+250.0s)` | `+4.2 min (+250s)` | 1 | `100.0%` |
| **Route 511** | `+3.2 min (+190.0s)` | `+3.2 min (+190s)` | 2 | `100.0%` |
| **Route 523** | `+3.1 min (+188.0s)` | `+3.1 min (+188s)` | 1 | `100.0%` |
| **Route 002** | `+1.6 min (+98.6s)` | `+4.5 min (+273s)` | 8 | `100.0%` |
| **Route 004** | `+1.3 min (+76.4s)` | `+3.9 min (+232s)` | 7 | `87.5%` |
| **Route 918A** | `+0.9 min (+53.0s)` | `+0.9 min (+53s)` | 1 | `100.0%` |
| **Route 903** | `+0.9 min (+52.0s)` | `+1.2 min (+72s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.0 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.8 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.1 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
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
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:22` | `15.79%` | `78.72%` | 76 | 38 | `+482.5s` |
| `2026-11-04 06:30:31` | `14.4%` | `76.92%` | 125 | 74 | `+247.0s` |
| `2026-11-04 06:00:18` | `13.37%` | `83.23%` | 202 | 113 | `+180.6s` |
| `2026-11-04 05:30:18` | `15.38%` | `85.37%` | 260 | 121 | `+155.1s` |
| `2026-11-04 05:00:18` | `18.01%` | `88.24%` | 311 | 137 | `+125.7s` |
| `2026-11-04 04:30:18` | `20.8%` | `85.66%` | 351 | 150 | `+72.9s` |
| `2026-11-04 04:00:29` | `19.37%` | `85.48%` | 475 | 235 | `+69.3s` |
| `2026-11-04 03:30:26` | `20.88%` | `83.45%` | 589 | 265 | `+37.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:22.970000+00:00`.*
