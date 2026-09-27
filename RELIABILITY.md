# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-27T01:36:17.741571+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.6%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.35%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `500` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `409` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `63` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+161.6s` (`2.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+103.0s` (`1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 300 | 60.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 34 | 6.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 67 | 13.4% |
| 🔴 **Severe Delay** | Over 15m late | 8 | 1.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 63 | 12.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 28 | 5.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 9** | 9 | 4 | 4 | **`44.44%`** | `40.0%` | `+6.5m` |
| **Route 17** | 12 | 6 | 4 | **`33.33%`** | `75.0%` | `+4.3m` |
| **Route 36** | 12 | 5 | 4 | **`33.33%`** | `80.0%` | `+1.4m` |
| **Route 10** | 16 | 6 | 5 | **`31.25%`** | `40.0%` | `+9.4m` |
| **Route 64** | 16 | 7 | 5 | **`31.25%`** | `60.0%` | `+3.0m` |
| **Route 11** | 13 | 6 | 4 | **`30.77%`** | `55.56%` | `+8.3m` |
| **Route 18** | 24 | 12 | 7 | **`29.17%`** | `82.35%` | `+2.0m` |
| **Route 63** | 10 | 5 | 2 | **`20.0%`** | `100.0%` | `+2.0m` |
| **Route 68** | 10 | 6 | 2 | **`20.0%`** | `85.71%` | `+1.4m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | `+9.4 min (563.9s)` | `+41.2 min (2470s)` | 6 | `40.0%` |
| **Route 67** | `+8.4 min (501.7s)` | `+13.3 min (799s)` | 3 | `33.33%` |
| **Route 11** | `+8.3 min (496.1s)` | `+25.9 min (1554s)` | 6 | `55.56%` |
| **Route 9** | `+6.5 min (389.0s)` | `+10.6 min (637s)` | 4 | `40.0%` |
| **Route 54** | `+4.8 min (285.7s)` | `+10.7 min (643s)` | 10 | `60.0%` |
| **Route 645** | `+4.6 min (275.0s)` | `+12.9 min (773s)` | 2 | `66.67%` |
| **Route 925** | `+4.4 min (265.8s)` | `+16.4 min (984s)` | 10 | `70.59%` |
| **Route 7** | `+4.4 min (265.5s)` | `+8.8 min (525s)` | 4 | `66.67%` |
| **Route 14** | `+4.4 min (261.9s)` | `+9.8 min (587s)` | 6 | `66.67%` |
| **Route 72** | `+4.3 min (257.0s)` | `+12.7 min (764s)` | 4 | `71.43%` |

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
| `1325468` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326967` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330580` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348749` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359692` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319404` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319737` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350258` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362608` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333730` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1335783` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319517` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1321974` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1322450` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1323540` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-27 01:36:17` | `12.6%` | `73.35%` | 500 | 409 | `+161.6s` |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-27T01:36:17.741571+00:00`.*
