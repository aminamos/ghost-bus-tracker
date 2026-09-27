# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-27T13:10:06.252259+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.59%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `508` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `433` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `72` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+124.5s` (`2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+105.0s` (`1.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 347 | 68.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 35 | 6.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 52 | 10.2% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 72 | 14.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 645** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+8.2m` |
| **Route 723** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+1.6m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.3m` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `+2.6m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.6m` |
| **Route 64** | 11 | 4 | 4 | **`36.36%`** | `66.67%` | `+3.4m` |
| **Route 67** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+2.4m` |
| **Route 18** | 25 | 11 | 8 | **`32.0%`** | `81.25%` | `+2.6m` |
| **Route 9** | 13 | 6 | 4 | **`30.77%`** | `55.56%` | `+5.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+8.2 min (492.0s)` | `+8.2 min (492s)` | 1 | `0.0%` |
| **Route 9** | `+5.1 min (307.1s)` | `+11.9 min (716s)` | 6 | `55.56%` |
| **Route 10** | `+5.0 min (301.1s)` | `+13.7 min (822s)` | 5 | `50.0%` |
| **Route 72** | `+4.7 min (281.3s)` | `+14.2 min (853s)` | 4 | `71.43%` |
| **Route 925** | `+4.2 min (250.7s)` | `+15.6 min (937s)` | 12 | `75.0%` |
| **Route 805** | `+3.5 min (207.7s)` | `+4.0 min (239s)` | 2 | `100.0%` |
| **Route 64** | `+3.4 min (202.4s)` | `+9.7 min (580s)` | 4 | `66.67%` |
| **Route 27** | `+3.3 min (198.7s)` | `+4.7 min (283s)` | 2 | `100.0%` |
| **Route 534** | `+3.3 min (197.0s)` | `+6.2 min (372s)` | 2 | `75.0%` |
| **Route 61** | `+3.2 min (193.4s)` | `+14.5 min (869s)` | 3 | `75.0%` |

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
| `1332022` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332148` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332333` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350293` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355771` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356407` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361391` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361405` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361536` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361548` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363500` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1279334` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1281659` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356295` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356406` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |
| `2026-09-27 07:19:56` | `0.0%` | `100.0%` | 2 | 2 | `+129.5s` |
| `2026-09-27 01:36:17` | `12.6%` | `73.35%` | 500 | 409 | `+161.6s` |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-27T13:10:06.252259+00:00`.*
