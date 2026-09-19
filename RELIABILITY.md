# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T21:56:09.594602+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.13%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.68%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `759` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `622` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `130` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+110.3s` (`1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+68.5s` (`1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 421 | 55.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 103 | 13.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 94 | 12.4% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 130 | 17.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 0.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 30 | 14 | 13 | **`43.33%`** | `78.57%` | `+2.6m` |
| **Route 11** | 21 | 8 | 9 | **`42.86%`** | `81.82%` | `+2.3m` |
| **Route 38** | 14 | 5 | 6 | **`42.86%`** | `83.33%` | `+0.3m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.4m` |
| **Route 25** | 7 | 3 | 3 | **`42.86%`** | `100.0%` | `-22.8s` |
| **Route 538** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.8m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+2.0m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-63.0s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.5m` |
| **Route 64** | 23 | 11 | 9 | **`39.13%`** | `69.23%` | `+3.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+7.4 min (442.9s)` | `+16.9 min (1012s)` | 8 | `28.57%` |
| **Route 645** | `+5.7 min (341.5s)` | `+9.5 min (570s)` | 2 | `50.0%` |
| **Route 94** | `+4.9 min (296.1s)` | `+8.2 min (489s)` | 3 | `57.14%` |
| **Route 22** | `+4.6 min (278.2s)` | `+27.5 min (1652s)` | 10 | `58.33%` |
| **Route 9** | `+4.6 min (277.6s)` | `+15.7 min (943s)` | 7 | `66.67%` |
| **Route 30** | `+4.4 min (266.2s)` | `+7.5 min (450s)` | 3 | `50.0%` |
| **Route 64** | `+3.9 min (234.1s)` | `+13.8 min (829s)` | 11 | `69.23%` |
| **Route 721** | `+3.6 min (218.7s)` | `+8.6 min (516s)` | 2 | `66.67%` |
| **Route 54** | `+3.6 min (216.3s)` | `+11.4 min (684s)` | 12 | `62.5%` |
| **Route 61** | `+3.5 min (207.3s)` | `+11.7 min (699s)` | 8 | `50.0%` |

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
| `1325437` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325638` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326308` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326843` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329474` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330314` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1334407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318514` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318745` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349128` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349791` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352033` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352289` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354092` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T21:56:09.594602+00:00`.*
