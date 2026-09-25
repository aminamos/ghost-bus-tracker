# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-25T21:43:01.460691+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.61%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.06%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1037` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `892` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `110` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+58.8s` (`1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 509 | 49.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 266 | 25.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 102 | 9.8% |
| 🔴 **Severe Delay** | Over 15m late | 15 | 1.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 110 | 10.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 35 | 3.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 223** | 7 | 1 | 5 | **`71.43%`** | `100.0%` | `-3.5s` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+1.0m` |
| **Route 760** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-42.0s` |
| **Route 766** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+2.7m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `75.0%` | `+0.9m` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `85.71%` | `+1.9m` |
| **Route 827** | 6 | 3 | 2 | **`33.33%`** | `100.0%` | `-167.0s` |
| **Route 645** | 10 | 7 | 3 | **`30.0%`** | `85.71%` | `+1.6m` |
| **Route 64** | 24 | 12 | 7 | **`29.17%`** | `76.92%` | `+1.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 860** | `+25.1 min (1504.0s)` | `+25.1 min (1504s)` | 1 | `0.0%` |
| **Route 467** | `+15.0 min (900.0s)` | `+38.3 min (2296s)` | 2 | `33.33%` |
| **Route 9** | `+6.9 min (411.2s)` | `+20.0 min (1202s)` | 7 | `25.0%` |
| **Route 777** | `+5.6 min (333.3s)` | `+15.7 min (944s)` | 3 | `50.0%` |
| **Route 764** | `+5.1 min (305.0s)` | `+5.1 min (305s)` | 1 | `0.0%` |
| **Route 5** | `+4.8 min (290.0s)` | `+16.6 min (995s)` | 3 | `0.0%` |
| **Route 747** | `+4.7 min (279.5s)` | `+13.3 min (801s)` | 4 | `50.0%` |
| **Route 7** | `+4.2 min (254.5s)` | `+19.0 min (1139s)` | 8 | `66.67%` |
| **Route 992** | `+3.9 min (234.2s)` | `+16.5 min (991s)` | 11 | `70.59%` |
| **Route 904** | `+3.5 min (211.5s)` | `+14.6 min (875s)` | 14 | `66.67%` |

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
| `1331506` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331972` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332865` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349017` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349721` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350710` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350941` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351168` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356889` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357233` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1280384` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1282048` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355996` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356237` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357217` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-25T21:43:01.460691+00:00`.*
