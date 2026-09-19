# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T13:42:25.721933+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.87%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`74.32%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `683` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `518` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `163` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+82.8s` (`1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+40.0s` (`0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 385 | 56.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 87 | 12.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 41 | 6.0% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 163 | 23.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 7** | 12 | 3 | 7 | **`58.33%`** | `75.0%` | `+1.2m` |
| **Route 17** | 14 | 5 | 8 | **`57.14%`** | `100.0%` | `+0.2m` |
| **Route 36** | 11 | 4 | 6 | **`54.55%`** | `100.0%` | `+0.1m` |
| **Route 10** | 24 | 7 | 13 | **`54.17%`** | `100.0%` | `+1.1m` |
| **Route 11** | 20 | 8 | 10 | **`50.0%`** | `100.0%` | `+1.2m` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.5m` |
| **Route 18** | 24 | 10 | 11 | **`45.83%`** | `91.67%` | `+1.5m` |
| **Route 14** | 14 | 6 | 6 | **`42.86%`** | `100.0%` | `+2.1m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.9m` |
| **Route 538** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+30.1 min (1805.6s)` | `+60.7 min (3640s)` | 2 | `40.0%` |
| **Route 94** | `+7.1 min (428.5s)` | `+22.7 min (1362s)` | 4 | `66.67%` |
| **Route 645** | `+6.2 min (369.0s)` | `+15.5 min (930s)` | 2 | `75.0%` |
| **Route 725** | `+5.2 min (309.8s)` | `+11.2 min (675s)` | 2 | `50.0%` |
| **Route 904** | `+3.9 min (233.9s)` | `+10.2 min (615s)` | 7 | `53.85%` |
| **Route 921** | `+3.8 min (226.4s)` | `+12.2 min (730s)` | 6 | `71.43%` |
| **Route 72** | `+3.2 min (194.8s)` | `+7.2 min (430s)` | 3 | `80.0%` |
| **Route 54** | `+3.0 min (182.5s)` | `+6.9 min (415s)` | 9 | `69.23%` |
| **Route 25** | `+3.0 min (179.0s)` | `+6.5 min (388s)` | 3 | `75.0%` |
| **Route 9** | `+3.0 min (177.0s)` | `+6.2 min (375s)` | 6 | `75.0%` |

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
| `1325118` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325132` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325181` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325513` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325561` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326234` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326595` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326911` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329200` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1335977` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344512` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1345684` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359085` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317761` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319483` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T13:42:25.721933+00:00`.*
