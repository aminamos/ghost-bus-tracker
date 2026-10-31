# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-31T06:30:19.835000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`83.51%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `126` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `79` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `16` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+98.4s` (`+1.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+64.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 81 | 64.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 7.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 16 | 12.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 916** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-157.0s` |
| **Route 002** | 11 | 6 | 5 | **`45.45%`** | `75.0%` | `+11.6 min` |
| **Route 009** | 15 | 7 | 5 | **`33.33%`** | `71.43%` | `+4.1 min` |
| **Route 004** | 16 | 9 | 4 | **`25.0%`** | `90.0%` | `+2.9 min` |
| **Route 005** | 7 | 6 | 0 | **`0.0%`** | `85.71%` | `-2.4s` |
| **Route 008** | 10 | 7 | 0 | **`0.0%`** | `88.89%` | `+1.6 min` |
| **Route 107** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 007** | 6 | 5 | 0 | **`0.0%`** | `100.0%` | `+2.3 min` |
| **Route 519** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 903** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | `+11.6 min (+693.5s)` | `+38.9 min (+2332s)` | 6 | `75.0%` |
| **Route 909** | `+6.6 min (+394.0s)` | `+6.6 min (+394s)` | 1 | `0.0%` |
| **Route 114** | `+5.5 min (+328.0s)` | `+5.5 min (+328s)` | 1 | `0.0%` |
| **Route 119** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 917** | `+4.6 min (+276.0s)` | `+4.6 min (+276s)` | 1 | `100.0%` |
| **Route 009** | `+4.1 min (+246.3s)` | `+14.7 min (+882s)` | 7 | `71.43%` |
| **Route 004** | `+2.9 min (+172.8s)` | `+7.9 min (+474s)` | 9 | `90.0%` |
| **Route 523** | `+2.5 min (+147.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 007** | `+2.3 min (+140.6s)` | `+4.1 min (+244s)` | 5 | `100.0%` |
| **Route 719** | `+2.3 min (+137.0s)` | `+2.3 min (+137s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.1 min`** | `44.9 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `82.6 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `88.9 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `88.5 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.4 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `91.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.5 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.4 / 100` |
| **Route 903** | ~60.0m | ~60.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 008** | ~29.5m | ~29.5m | **`+0.0 min`** | `95.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32762449` | Route 518 | `23:38:00` | `SCHEDULED` | Assigned vehicle 2977 is broadcasting off-schedule with no vehicle covering 32762449 |
| `32763923` | Route 916 | `23:59:00` | `SCHEDULED` | Assigned vehicle 3312 is missing from active GPS transponder fleet |
| `32760708` | Route 009 | `23:37:00` | `SCHEDULED` | Assigned vehicle 3364 is broadcasting off-schedule with no vehicle covering 32760708 |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904643` | Route 004 | `25:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760711` | Route 009 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760328` | Route 002 | `24:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760329` | Route 002 | `25:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 06:30:19` | `12.7%` | `83.51%` | 126 | 79 | `+98.4s` |
| `2026-10-31 06:00:20` | `11.56%` | `85.8%` | 199 | 115 | `+107.1s` |
| `2026-10-31 05:30:23` | `13.55%` | `83.01%` | 251 | 121 | `+139.0s` |
| `2026-10-31 04:30:22` | `17.75%` | `82.06%` | 338 | 151 | `+305.8s` |
| `2026-10-31 04:00:20` | `17.03%` | `83.01%` | 458 | 234 | `+225.8s` |
| `2026-10-31 03:30:18` | `17.94%` | `82.54%` | 563 | 264 | `+176.5s` |
| `2026-10-31 03:00:18` | `20.5%` | `83.13%` | 644 | 268 | `+153.0s` |
| `2026-10-31 02:30:18` | `23.28%` | `78.9%` | 696 | 276 | `+188.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T06:30:19.835000+00:00`.*
