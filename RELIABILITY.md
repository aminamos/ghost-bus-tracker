# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T13:37:58.942548+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.4%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `675` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `514` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `160` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+83.2s` (`1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+36.5s` (`0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 367 | 54.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 96 | 14.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 47 | 7.0% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 160 | 23.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 36** | 10 | 4 | 6 | **`60.0%`** | `100.0%` | `+0.2m` |
| **Route 7** | 12 | 3 | 7 | **`58.33%`** | `100.0%` | `+1.0m` |
| **Route 17** | 14 | 5 | 8 | **`57.14%`** | `100.0%` | `-7.0s` |
| **Route 18** | 25 | 9 | 13 | **`52.0%`** | `90.91%` | `+1.5m` |
| **Route 10** | 24 | 8 | 12 | **`50.0%`** | `100.0%` | `+0.8m` |
| **Route 64** | 20 | 7 | 9 | **`45.0%`** | `90.0%` | `+0.8m` |
| **Route 14** | 14 | 6 | 6 | **`42.86%`** | `100.0%` | `+2.1m` |
| **Route 538** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.5m` |
| **Route 11** | 20 | 9 | 8 | **`40.0%`** | `81.82%` | `+2.0m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+0.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+27.5 min (1649.4s)` | `+56.6 min (3394s)` | 2 | `40.0%` |
| **Route 94** | `+6.6 min (396.7s)` | `+20.9 min (1251s)` | 4 | `66.67%` |
| **Route 645** | `+5.7 min (340.8s)` | `+15.0 min (899s)` | 2 | `75.0%` |
| **Route 725** | `+5.4 min (322.2s)` | `+11.9 min (712s)` | 2 | `50.0%` |
| **Route 921** | `+4.4 min (264.3s)` | `+11.3 min (680s)` | 6 | `61.54%` |
| **Route 904** | `+3.7 min (223.9s)` | `+8.0 min (482s)` | 7 | `50.0%` |
| **Route 3** | `+3.1 min (186.6s)` | `+8.7 min (520s)` | 11 | `75.0%` |
| **Route 54** | `+3.0 min (181.3s)` | `+6.3 min (378s)` | 9 | `66.67%` |
| **Route 9** | `+3.0 min (177.8s)` | `+6.1 min (364s)` | 6 | `87.5%` |
| **Route 72** | `+2.9 min (173.8s)` | `+5.6 min (337s)` | 3 | `83.33%` |

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
| `1325132` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325181` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325513` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325561` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326094` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326234` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326595` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329200` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1335977` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344512` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1345684` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359085` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317761` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319483` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319883` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T13:37:58.942548+00:00`.*
