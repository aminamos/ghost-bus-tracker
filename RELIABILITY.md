# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-28T01:53:47.156381+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.89%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `396` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `347` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `45` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+171.9s` (`2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+128.0s` (`2.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 246 | 62.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 27 | 6.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 69 | 17.4% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 1.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 45 | 11.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 4 | 1.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+1.7m` |
| **Route 64** | 12 | 5 | 4 | **`33.33%`** | `71.43%` | `+2.8m` |
| **Route 18** | 25 | 12 | 7 | **`28.0%`** | `81.25%` | `+1.8m` |
| **Route 68** | 9 | 5 | 2 | **`22.22%`** | `83.33%` | `+4.3m` |
| **Route 925** | 20 | 10 | 4 | **`20.0%`** | `68.75%` | `+3.9m` |
| **Route 14** | 10 | 6 | 2 | **`20.0%`** | `62.5%` | `+6.1m` |
| **Route 5** | 5 | 3 | 1 | **`20.0%`** | `50.0%` | `+6.6m` |
| **Route 9** | 5 | 3 | 1 | **`20.0%`** | `75.0%` | `+4.2m` |
| **Route 924** | 22 | 12 | 4 | **`18.18%`** | `80.0%` | `+2.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 67** | `+8.4 min (506.0s)` | `+8.4 min (506s)` | 1 | `0.0%` |
| **Route 10** | `+6.6 min (396.8s)` | `+16.9 min (1011s)` | 4 | `33.33%` |
| **Route 5** | `+6.6 min (396.0s)` | `+11.4 min (684s)` | 3 | `50.0%` |
| **Route 14** | `+6.1 min (363.8s)` | `+17.0 min (1018s)` | 6 | `62.5%` |
| **Route 3** | `+5.7 min (343.8s)` | `+10.4 min (624s)` | 6 | `25.0%` |
| **Route 54** | `+5.1 min (303.1s)` | `+13.5 min (811s)` | 8 | `63.64%` |
| **Route 2** | `+4.4 min (265.9s)` | `+7.9 min (475s)` | 4 | `57.14%` |
| **Route 68** | `+4.3 min (256.9s)` | `+15.7 min (941s)` | 5 | `83.33%` |
| **Route 9** | `+4.2 min (254.8s)` | `+5.2 min (310s)` | 3 | `75.0%` |
| **Route 11** | `+4.1 min (247.0s)` | `+7.5 min (447s)` | 4 | `66.67%` |

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
| `1331871` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332641` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357293` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357299` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357359` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357875` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360855` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361516` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363098` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356256` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359942` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1177347` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1183032` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1185379` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1186463` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |
| `2026-09-27 07:19:56` | `0.0%` | `100.0%` | 2 | 2 | `+129.5s` |
| `2026-09-27 01:36:17` | `12.6%` | `73.35%` | 500 | 409 | `+161.6s` |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-28T01:53:47.156381+00:00`.*
