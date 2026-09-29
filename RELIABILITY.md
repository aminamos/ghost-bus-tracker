# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-29T02:07:24.812743+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.2%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.25%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `500` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `423` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `56` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+53.5s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+10.0s` (`0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 276 | 55.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 106 | 21.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 36 | 7.2% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 56 | 11.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 21 | 4.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 9** | 7 | 3 | 3 | **`42.86%`** | `50.0%` | `+1.7m` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-39.8s` |
| **Route 11** | 12 | 6 | 4 | **`33.33%`** | `100.0%` | `+0.3m` |
| **Route 64** | 12 | 4 | 4 | **`33.33%`** | `71.43%` | `+1.9m` |
| **Route 18** | 23 | 11 | 7 | **`30.43%`** | `90.91%` | `+0.0m` |
| **Route 10** | 14 | 6 | 4 | **`28.57%`** | `85.71%` | `-29.8s` |
| **Route 68** | 11 | 6 | 3 | **`27.27%`** | `85.71%` | `+1.4m` |
| **Route 215** | 4 | 1 | 1 | **`25.0%`** | `100.0%` | `+1.2m` |
| **Route 723** | 4 | 2 | 1 | **`25.0%`** | `100.0%` | `-11.3s` |
| **Route 924** | 25 | 12 | 6 | **`24.0%`** | `40.0%` | `+1.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+6.8 min (410.3s)` | `+15.5 min (928s)` | 2 | `0.0%` |
| **Route 923** | `+4.2 min (250.5s)` | `+23.4 min (1404s)` | 6 | `63.64%` |
| **Route 30** | `+3.9 min (232.5s)` | `+9.0 min (539s)` | 2 | `66.67%` |
| **Route 87** | `+3.5 min (210.8s)` | `+15.5 min (929s)` | 3 | `66.67%` |
| **Route 22** | `+3.3 min (198.4s)` | `+19.8 min (1186s)` | 8 | `75.0%` |
| **Route 75** | `+3.1 min (184.0s)` | `+3.1 min (184s)` | 1 | `100.0%` |
| **Route 54** | `+3.0 min (181.1s)` | `+23.5 min (1409s)` | 10 | `73.33%` |
| **Route 94** | `+3.0 min (179.0s)` | `+13.0 min (780s)` | 3 | `83.33%` |
| **Route 921** | `+2.5 min (149.4s)` | `+7.8 min (467s)` | 7 | `91.67%` |
| **Route 2** | `+2.3 min (140.4s)` | `+12.2 min (730s)` | 6 | `80.0%` |

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
| `1325324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325371` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327003` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327097` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319546` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319569` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351263` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351646` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332889` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333220` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318826` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318967` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356538` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356654` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356938` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-29T02:07:24.812743+00:00`.*
