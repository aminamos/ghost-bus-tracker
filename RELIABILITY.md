# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-27T20:35:38.244728+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.95%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.38%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `678` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `590` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `81` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+197.7s` (`3.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+158.0s` (`2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 391 | 57.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 50 | 7.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 138 | 20.4% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 81 | 11.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 1.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `50.0%` | `+4.7m` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `83.33%` | `+3.9m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+3.4m` |
| **Route 64** | 18 | 8 | 6 | **`33.33%`** | `90.91%` | `+2.4m` |
| **Route 48** | 6 | 4 | 2 | **`33.33%`** | `100.0%` | `+1.0m` |
| **Route 645** | 6 | 2 | 2 | **`33.33%`** | `75.0%` | `+6.1m` |
| **Route 18** | 37 | 20 | 12 | **`32.43%`** | `72.22%` | `+1.6m` |
| **Route 9** | 13 | 7 | 4 | **`30.77%`** | `37.5%` | `+7.9m` |
| **Route 723** | 4 | 1 | 1 | **`25.0%`** | `100.0%` | `+2.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9** | `+7.9 min (471.3s)` | `+26.4 min (1585s)` | 7 | `37.5%` |
| **Route 11** | `+7.0 min (422.6s)` | `+18.5 min (1111s)` | 10 | `37.5%` |
| **Route 992** | `+7.0 min (418.2s)` | `+19.4 min (1164s)` | 11 | `52.94%` |
| **Route 3** | `+6.9 min (413.3s)` | `+11.7 min (700s)` | 6 | `33.33%` |
| **Route 925** | `+6.7 min (402.5s)` | `+13.2 min (793s)` | 15 | `40.91%` |
| **Route 22** | `+6.2 min (373.3s)` | `+19.6 min (1179s)` | 12 | `50.0%` |
| **Route 94** | `+6.2 min (370.5s)` | `+17.2 min (1031s)` | 3 | `50.0%` |
| **Route 645** | `+6.1 min (365.2s)` | `+14.1 min (843s)` | 2 | `75.0%` |
| **Route 54** | `+5.2 min (309.6s)` | `+15.9 min (955s)` | 10 | `55.56%` |
| **Route 38** | `+5.2 min (309.5s)` | `+14.2 min (850s)` | 6 | `44.44%` |

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
| `1331492` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331511` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332617` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1220556` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1221553` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1240657` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349736` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350797` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355932` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356527` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361068` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361658` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361956` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362802` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363730` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |
| `2026-09-27 07:19:56` | `0.0%` | `100.0%` | 2 | 2 | `+129.5s` |
| `2026-09-27 01:36:17` | `12.6%` | `73.35%` | 500 | 409 | `+161.6s` |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-27T20:35:38.244728+00:00`.*
