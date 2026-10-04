# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-04T23:20:57.739301+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.8%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `562` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `501` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `53` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+251.0s` (`4.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+180.0s` (`3.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 309 | 55.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 27 | 4.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 147 | 26.2% |
| 🔴 **Severe Delay** | Over 15m late | 17 | 3.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 53 | 9.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 1.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `66.67%` | `+3.0m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+3.8m` |
| **Route 18** | 27 | 13 | 10 | **`37.04%`** | `50.0%` | `+5.4m` |
| **Route 36** | 12 | 5 | 4 | **`33.33%`** | `87.5%` | `+2.9m` |
| **Route 68** | 14 | 8 | 4 | **`28.57%`** | `66.67%` | `+3.7m` |
| **Route 67** | 11 | 5 | 3 | **`27.27%`** | `71.43%` | `+4.7m` |
| **Route 924** | 32 | 16 | 8 | **`25.0%`** | `54.17%` | `+6.3m` |
| **Route 38** | 10 | 6 | 2 | **`20.0%`** | `50.0%` | `+5.1m` |
| **Route 9** | 10 | 6 | 2 | **`20.0%`** | `37.5%` | `+5.3m` |
| **Route 5** | 5 | 4 | 1 | **`20.0%`** | `75.0%` | `+3.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 14** | `+12.3 min (735.5s)` | `+30.0 min (1802s)` | 8 | `23.08%` |
| **Route 94** | `+7.7 min (462.3s)` | `+16.0 min (958s)` | 5 | `28.57%` |
| **Route 645** | `+7.6 min (458.8s)` | `+20.1 min (1207s)` | 2 | `50.0%` |
| **Route 921** | `+6.8 min (408.6s)` | `+25.2 min (1510s)` | 9 | `46.67%` |
| **Route 3** | `+6.7 min (404.2s)` | `+15.1 min (908s)` | 7 | `25.0%` |
| **Route 10** | `+6.4 min (386.7s)` | `+18.8 min (1127s)` | 9 | `50.0%` |
| **Route 22** | `+6.4 min (385.1s)` | `+13.8 min (828s)` | 11 | `42.86%` |
| **Route 924** | `+6.3 min (375.6s)` | `+17.2 min (1033s)` | 16 | `54.17%` |
| **Route 923** | `+6.2 min (374.2s)` | `+18.1 min (1083s)` | 9 | `41.18%` |
| **Route 17** | `+6.2 min (373.0s)` | `+12.7 min (764s)` | 6 | `37.5%` |

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
| `1331432` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333050` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361382` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361658` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361678` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361727` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364332` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365234` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365609` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366671` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366731` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368709` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1281236` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1282829` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365032` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-04 23:20:57` | `9.43%` | `61.8%` | 562 | 501 | `+251.0s` |
| `2026-10-04 20:16:15` | `11.44%` | `60.24%` | 673 | 591 | `+290.1s` |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-04T23:20:57.739301+00:00`.*
