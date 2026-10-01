# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-01T19:08:55.080195+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.36%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `951` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `777` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `145` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+44.8s` (`0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+8.0s` (`0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 469 | 49.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 237 | 24.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 66 | 6.9% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 145 | 15.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 29 | 3.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 275** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 760** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 766** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 850** | 6 | 1 | 5 | **`83.33%`** | `100.0%` | `+0.2m` |
| **Route 768** | 6 | 3 | 3 | **`50.0%`** | `100.0%` | `+0.1m` |
| **Route 827** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `-157.5s` |
| **Route 25** | 9 | 3 | 4 | **`44.44%`** | `0.0%` | `+4.6m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.3m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.1m` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-30.7s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 25** | `+4.6 min (277.6s)` | `+11.4 min (683s)` | 3 | `0.0%` |
| **Route 87** | `+4.4 min (265.7s)` | `+20.6 min (1237s)` | 5 | `60.0%` |
| **Route 801** | `+4.1 min (244.7s)` | `+11.5 min (688s)` | 2 | `66.67%` |
| **Route 645** | `+4.0 min (238.7s)` | `+13.4 min (804s)` | 7 | `75.0%` |
| **Route 65** | `+2.9 min (176.5s)` | `+8.1 min (484s)` | 4 | `40.0%` |
| **Route 94** | `+2.9 min (174.9s)` | `+8.0 min (482s)` | 5 | `88.89%` |
| **Route 921** | `+2.6 min (158.4s)` | `+8.0 min (477s)` | 11 | `88.24%` |
| **Route 777** | `+2.6 min (156.0s)` | `+2.6 min (156s)` | 1 | `100.0%` |
| **Route 30** | `+2.5 min (152.0s)` | `+9.7 min (583s)` | 3 | `80.0%` |
| **Route 18** | `+2.3 min (138.8s)` | `+17.4 min (1043s)` | 20 | `77.27%` |

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
| `1324976` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324998` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325058` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325282` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325432` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326345` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326896` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318988` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319645` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319664` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319758` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331028` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331451` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-01T19:08:55.080195+00:00`.*
