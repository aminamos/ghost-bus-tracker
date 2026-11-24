# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-24T07:00:19.158000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`86.96%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `73` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `36` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+7.5s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+24.0s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 54.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 8.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 16.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `100.0%` | `-14.3s` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.8 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+2.1 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `87.5%` | `-140.8s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-122.5s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-8.8s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-174.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 523** | `+2.8 min (+167.0s)` | `+2.8 min (+167s)` | 1 | `100.0%` |
| **Route 002** | `+2.1 min (+126.9s)` | `+4.6 min (+275s)` | 8 | `100.0%` |
| **Route 004** | `+1.8 min (+110.7s)` | `+4.5 min (+271s)` | 7 | `100.0%` |
| **Route 903** | `+1.7 min (+104.0s)` | `+2.7 min (+160s)` | 2 | `100.0%` |
| **Route 918A** | `+1.1 min (+64.0s)` | `+1.1 min (+64s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `67.5 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.9 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.6 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.8 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:19` | `16.44%` | `86.96%` | 73 | 36 | `+7.5s` |
| `2026-11-24 06:30:23` | `15.45%` | `79.31%` | 123 | 74 | `+26.0s` |
| `2026-11-24 06:00:18` | `12.18%` | `87.97%` | 197 | 111 | `+69.4s` |
| `2026-11-24 05:30:19` | `13.6%` | `87.75%` | 250 | 121 | `+57.2s` |
| `2026-11-24 05:00:19` | `15.15%` | `88.21%` | 297 | 136 | `+62.8s` |
| `2026-11-24 04:30:23` | `18.1%` | `87.45%` | 326 | 147 | `+56.9s` |
| `2026-11-24 04:00:19` | `16.0%` | `82.68%` | 450 | 234 | `+80.5s` |
| `2026-11-24 03:30:30` | `15.86%` | `79.51%` | 555 | 265 | `+42.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:19.158000+00:00`.*
