# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-29T08:47:30.373175+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`52.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.09%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `138` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `66` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `72` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-52.2s` (`-0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-43.0s` (`-0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 28.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 26 | 18.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 72 | 52.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 645** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 68** | 5 | 1 | 4 | **`80.0%`** | `100.0%` | `+2.1m` |
| **Route 9** | 5 | 1 | 4 | **`80.0%`** | `100.0%` | `+0.1m` |
| **Route 64** | 9 | 1 | 7 | **`77.78%`** | `100.0%` | `-41.0s` |
| **Route 10** | 7 | 2 | 5 | **`71.43%`** | `100.0%` | `-27.5s` |
| **Route 11** | 7 | 2 | 5 | **`71.43%`** | `100.0%` | `-61.0s` |
| **Route 924** | 12 | 4 | 8 | **`66.67%`** | `100.0%` | `-101.2s` |
| **Route 14** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-72.5s` |
| **Route 36** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-43.5s` |
| **Route 17** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-207.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 921** | `+3.0 min (182.0s)` | `+5.3 min (316s)` | 3 | `75.0%` |
| **Route 68** | `+2.1 min (127.0s)` | `+2.1 min (127s)` | 1 | `100.0%` |
| **Route 72** | `+0.7 min (43.0s)` | `+0.7 min (43s)` | 1 | `100.0%` |
| **Route 7** | `+0.7 min (40.5s)` | `+2.3 min (136s)` | 2 | `100.0%` |
| **Route 904** | `+0.3 min (19.0s)` | `+0.7 min (42s)` | 2 | `100.0%` |
| **Route 9** | `+0.1 min (8.0s)` | `+0.1 min (8s)` | 1 | `100.0%` |
| **Route 923** | `+0.1 min (8.0s)` | `+0.1 min (8s)` | 1 | `100.0%` |
| **Route 515** | `+0.1 min (5.0s)` | `+0.1 min (5s)` | 1 | `100.0%` |

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
| `1325896` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326087` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326286` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326575` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326914` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318375` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318435` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319651` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349019` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350071` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331213` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331482` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331947` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333184` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1291665` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-29T08:47:30.373175+00:00`.*
