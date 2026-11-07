# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:19.014000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.49%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `74` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+57.0s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+39.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 43 | 58.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 2.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 16.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.9 min` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `85.71%` | `+1.8 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `80.0%` | `+2.9 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.5 min` |
| **Route 008** | 14 | 6 | 2 | **`14.29%`** | `100.0%` | `+0.5 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `-31.4s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-63.0s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-35.0s` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-2.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | `+2.9 min (+171.6s)` | `+5.4 min (+324s)` | 8 | `80.0%` |
| **Route 523** | `+2.6 min (+157.0s)` | `+2.6 min (+157s)` | 1 | `100.0%` |
| **Route 009** | `+1.8 min (+110.3s)` | `+8.3 min (+497s)` | 4 | `85.71%` |
| **Route 918A** | `+1.6 min (+96.0s)` | `+1.6 min (+96s)` | 1 | `100.0%` |
| **Route 004** | `+1.5 min (+88.3s)` | `+3.5 min (+209s)` | 7 | `100.0%` |
| **Route 721** | `+0.9 min (+52.0s)` | `+0.9 min (+52s)` | 1 | `100.0%` |
| **Route 507** | `+0.5 min (+30.0s)` | `+0.5 min (+30s)` | 1 | `100.0%` |
| **Route 008** | `+0.5 min (+27.8s)` | `+2.3 min (+139s)` | 6 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `90.1 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `90.6 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.9 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.4 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.0 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32763447` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 2631 is missing from active GPS transponder fleet |
| `32755341` | Route 008 | `25:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32755342` | Route 008 | `26:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:19` | `16.22%` | `91.49%` | 74 | 37 | `+57.0s` |
| `2026-11-07 06:30:21` | `16.0%` | `84.27%` | 125 | 75 | `+59.3s` |
| `2026-11-07 06:00:23` | `13.5%` | `82.61%` | 200 | 115 | `+105.1s` |
| `2026-11-07 05:30:21` | `13.73%` | `86.89%` | 255 | 123 | `+85.8s` |
| `2026-11-07 05:00:19` | `16.45%` | `87.95%` | 310 | 138 | `+156.2s` |
| `2026-11-07 04:30:18` | `20.34%` | `87.07%` | 349 | 152 | `+134.7s` |
| `2026-11-07 04:00:25` | `19.08%` | `82.55%` | 477 | 241 | `+73.6s` |
| `2026-11-07 03:30:25` | `20.2%` | `86.06%` | 589 | 267 | `+76.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:19.014000+00:00`.*
