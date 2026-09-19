# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T17:35:31.586616+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.71%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `787` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `617` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `167` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+125.3s` (`2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+85.0s` (`1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 441 | 56.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 79 | 10.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 89 | 11.3% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 167 | 21.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 46** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `+7.5m` |
| **Route 36** | 10 | 4 | 5 | **`50.0%`** | `100.0%` | `+1.6m` |
| **Route 888** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+1.3m` |
| **Route 10** | 36 | 13 | 16 | **`44.44%`** | `84.62%` | `+0.5m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+2.1m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.2m` |
| **Route 11** | 24 | 9 | 10 | **`41.67%`** | `58.33%` | `+3.6m` |
| **Route 7** | 12 | 6 | 5 | **`41.67%`** | `100.0%` | `+1.4m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+1.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 25** | `+7.5 min (451.0s)` | `+17.9 min (1074s)` | 2 | `0.0%` |
| **Route 9** | `+6.9 min (411.4s)` | `+11.5 min (689s)` | 6 | `37.5%` |
| **Route 904** | `+6.1 min (364.6s)` | `+15.4 min (924s)` | 8 | `42.86%` |
| **Route 645** | `+4.3 min (261.0s)` | `+8.4 min (504s)` | 2 | `50.0%` |
| **Route 925** | `+4.1 min (248.2s)` | `+12.8 min (770s)` | 15 | `52.63%` |
| **Route 225** | `+3.8 min (229.8s)` | `+17.2 min (1035s)` | 2 | `66.67%` |
| **Route 94** | `+3.7 min (223.5s)` | `+5.4 min (324s)` | 5 | `83.33%` |
| **Route 11** | `+3.6 min (218.6s)` | `+10.6 min (637s)` | 9 | `58.33%` |
| **Route 38** | `+3.5 min (209.5s)` | `+10.4 min (624s)` | 6 | `55.56%` |
| **Route 14** | `+3.5 min (207.4s)` | `+7.9 min (472s)` | 7 | `58.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1325188` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325625` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325975` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326209` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326212` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326342` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327194` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329777` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329938` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330214` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1345502` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352070` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355655` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1358259` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359447` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T17:35:31.586616+00:00`.*
