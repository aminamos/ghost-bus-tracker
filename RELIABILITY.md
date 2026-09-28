# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-28T16:23:26.267318+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.55%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.91%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `873` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `739` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `127` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+7.1s` (`0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-22.0s` (`-0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 420 | 48.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 271 | 31.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 42 | 4.8% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 127 | 14.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 0.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 25 | 10 | 10 | **`40.0%`** | `84.62%` | `+1.1m` |
| **Route 32** | 15 | 5 | 6 | **`40.0%`** | `100.0%` | `-50.1s` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-67.5s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-5.0s` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.4m` |
| **Route 64** | 24 | 10 | 9 | **`37.5%`** | `90.0%` | `-10.9s` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `+0.9m` |
| **Route 18** | 36 | 18 | 12 | **`33.33%`** | `93.75%` | `-8.0s` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+0.0m` |
| **Route 850** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-68.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9** | `+4.8 min (286.7s)` | `+28.7 min (1724s)` | 7 | `62.5%` |
| **Route 902** | `+3.4 min (201.0s)` | `+12.5 min (750s)` | 10 | `80.0%` |
| **Route 717** | `+2.9 min (171.7s)` | `+8.4 min (502s)` | 1 | `50.0%` |
| **Route 923** | `+1.9 min (112.4s)` | `+18.7 min (1120s)` | 11 | `93.33%` |
| **Route 25** | `+1.8 min (106.3s)` | `+5.5 min (329s)` | 3 | `50.0%` |
| **Route 645** | `+1.7 min (99.8s)` | `+10.6 min (636s)` | 6 | `85.71%` |
| **Route 10** | `+1.5 min (91.8s)` | `+17.9 min (1071s)` | 16 | `76.47%` |
| **Route 54** | `+1.5 min (91.1s)` | `+15.6 min (933s)` | 15 | `88.24%` |
| **Route 921** | `+1.5 min (88.5s)` | `+5.8 min (351s)` | 11 | `92.86%` |
| **Route 537** | `+1.4 min (83.3s)` | `+3.8 min (229s)` | 1 | `100.0%` |

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
| `1325219` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325814` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326056` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326238` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326353` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326410` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317828` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318029` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318093` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319476` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319548` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348961` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350134` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350603` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350654` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |
| `2026-09-27 07:19:56` | `0.0%` | `100.0%` | 2 | 2 | `+129.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-28T16:23:26.267318+00:00`.*
