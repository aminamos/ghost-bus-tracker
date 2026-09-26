# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-26T14:13:02.768548+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.12%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `688` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `560` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `125` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+121.0s` (`2.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+38.0s` (`0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 399 | 58.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 110 | 16.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 42 | 6.1% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 125 | 18.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 645** | 4 | 1 | 3 | **`75.0%`** | `100.0%` | `+3.9m` |
| **Route 10** | 24 | 8 | 13 | **`54.17%`** | `100.0%` | `+0.9m` |
| **Route 25** | 6 | 2 | 3 | **`50.0%`** | `66.67%` | `+3.0m` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.1m` |
| **Route 11** | 23 | 8 | 11 | **`47.83%`** | `81.82%` | `+1.7m` |
| **Route 30** | 11 | 3 | 5 | **`45.45%`** | `100.0%` | `+2.2m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.7m` |
| **Route 17** | 15 | 6 | 6 | **`40.0%`** | `100.0%` | `+1.6m` |
| **Route 18** | 27 | 12 | 10 | **`37.04%`** | `93.33%` | `+0.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+80.0 min (4800.3s)` | `+102.0 min (6119s)` | 2 | `0.0%` |
| **Route 27** | `+4.0 min (243.0s)` | `+12.1 min (726s)` | 3 | `75.0%` |
| **Route 645** | `+3.9 min (235.0s)` | `+3.9 min (235s)` | 1 | `100.0%` |
| **Route 9** | `+3.7 min (222.0s)` | `+6.9 min (416s)` | 6 | `70.0%` |
| **Route 725** | `+3.3 min (199.0s)` | `+5.5 min (332s)` | 2 | `50.0%` |
| **Route 3** | `+3.2 min (194.9s)` | `+18.1 min (1089s)` | 12 | `86.67%` |
| **Route 36** | `+3.2 min (193.3s)` | `+7.7 min (462s)` | 4 | `71.43%` |
| **Route 921** | `+3.2 min (191.1s)` | `+12.6 min (758s)` | 7 | `76.92%` |
| **Route 25** | `+3.0 min (178.0s)` | `+7.0 min (418s)` | 2 | `66.67%` |
| **Route 67** | `+2.7 min (164.5s)` | `+5.5 min (333s)` | 5 | `40.0%` |

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
| `1325057` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325118` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325132` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325181` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325513` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325736` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326196` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326235` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327150` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329200` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1339533` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344034` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362498` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317761` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319483` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-26T14:13:02.768548+00:00`.*
