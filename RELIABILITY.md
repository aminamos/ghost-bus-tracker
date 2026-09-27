# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-27T17:51:50.840325+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `667` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `583` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `82` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+185.9s` (`3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+154.0s` (`2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 412 | 61.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 38 | 5.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 128 | 19.2% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 82 | 12.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 888** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-47.0s` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `50.0%` | `+3.9m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.7m` |
| **Route 48** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 18** | 36 | 19 | 12 | **`33.33%`** | `80.95%` | `+2.7m` |
| **Route 64** | 18 | 8 | 6 | **`33.33%`** | `72.73%` | `+3.8m` |
| **Route 36** | 12 | 6 | 4 | **`33.33%`** | `75.0%` | `+3.7m` |
| **Route 67** | 9 | 4 | 3 | **`33.33%`** | `83.33%` | `+5.0m` |
| **Route 538** | 6 | 2 | 2 | **`33.33%`** | `25.0%` | `+5.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+8.4 min (501.2s)` | `+12.4 min (746s)` | 2 | `25.0%` |
| **Route 9** | `+6.2 min (372.2s)` | `+19.1 min (1147s)` | 7 | `60.0%` |
| **Route 925** | `+6.0 min (357.2s)` | `+12.1 min (728s)` | 13 | `45.45%` |
| **Route 94** | `+5.7 min (343.0s)` | `+15.7 min (944s)` | 3 | `60.0%` |
| **Route 992** | `+5.5 min (332.4s)` | `+11.3 min (681s)` | 10 | `25.0%` |
| **Route 22** | `+5.3 min (318.2s)` | `+17.6 min (1057s)` | 11 | `53.33%` |
| **Route 538** | `+5.1 min (308.8s)` | `+6.7 min (402s)` | 2 | `25.0%` |
| **Route 67** | `+5.0 min (299.2s)` | `+10.3 min (620s)` | 4 | `83.33%` |
| **Route 725** | `+5.0 min (299.0s)` | `+6.4 min (386s)` | 2 | `50.0%` |
| **Route 10** | `+4.7 min (282.3s)` | `+12.7 min (762s)` | 12 | `58.82%` |

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
| `1331575` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331639` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332411` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1219944` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1220540` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242317` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242949` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349245` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1353024` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356057` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356520` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361218` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361788` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362848` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363686` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |
| `2026-09-27 07:19:56` | `0.0%` | `100.0%` | 2 | 2 | `+129.5s` |
| `2026-09-27 01:36:17` | `12.6%` | `73.35%` | 500 | 409 | `+161.6s` |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-27T17:51:50.840325+00:00`.*
