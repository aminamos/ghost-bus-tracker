# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-28T22:11:30.266426+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.27%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `997` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `854` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `108` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+53.1s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 472 | 47.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 279 | 28.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 92 | 9.2% |
| 🔴 **Severe Delay** | Over 15m late | 11 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 108 | 10.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 35 | 3.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+2.9m` |
| **Route 64** | 24 | 11 | 9 | **`37.5%`** | `100.0%` | `+0.6m` |
| **Route 223** | 8 | 2 | 3 | **`37.5%`** | `66.67%` | `+0.3m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `80.0%` | `+1.6m` |
| **Route 540** | 12 | 5 | 4 | **`33.33%`** | `80.0%` | `+1.1m` |
| **Route 850** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `-189.0s` |
| **Route 924** | 39 | 19 | 12 | **`30.77%`** | `86.67%` | `+0.1m` |
| **Route 32** | 14 | 6 | 4 | **`28.57%`** | `66.67%` | `+2.6m` |
| **Route 888** | 7 | 3 | 2 | **`28.57%`** | `100.0%` | `-17.8s` |
| **Route 18** | 33 | 17 | 9 | **`27.27%`** | `73.68%` | `+1.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 766** | `+31.9 min (1917.0s)` | `+61.0 min (3661s)` | 2 | `50.0%` |
| **Route 294** | `+15.4 min (922.0s)` | `+15.4 min (922s)` | 1 | `0.0%` |
| **Route 667** | `+6.8 min (405.0s)` | `+6.8 min (405s)` | 1 | `0.0%` |
| **Route 747** | `+5.8 min (350.0s)` | `+11.3 min (678s)` | 3 | `0.0%` |
| **Route 87** | `+5.0 min (299.9s)` | `+25.0 min (1500s)` | 5 | `66.67%` |
| **Route 25** | `+4.5 min (271.4s)` | `+12.5 min (748s)` | 4 | `25.0%` |
| **Route 363** | `+4.5 min (271.0s)` | `+9.4 min (567s)` | 2 | `50.0%` |
| **Route 763** | `+4.1 min (248.0s)` | `+4.1 min (248s)` | 1 | `100.0%` |
| **Route 805** | `+4.1 min (244.6s)` | `+17.9 min (1072s)` | 2 | `33.33%` |
| **Route 777** | `+3.7 min (219.7s)` | `+15.1 min (905s)` | 3 | `50.0%` |

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
| `1325105` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326039` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326327` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319348` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319860` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349007` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349633` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349784` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331972` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332794` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319138` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319436` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319938` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320030` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349871` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-28T22:11:30.266426+00:00`.*
