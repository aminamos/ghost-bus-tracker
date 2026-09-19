# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T13:33:11.244805+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`24.19%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.29%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `682` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `516` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `165` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+82.7s` (`1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+37.5s` (`0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 373 | 54.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 91 | 13.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 46 | 6.7% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 165 | 24.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 1 | 4 | **`66.67%`** | `50.0%` | `+3.8m` |
| **Route 17** | 15 | 4 | 9 | **`60.0%`** | `83.33%` | `+1.4m` |
| **Route 36** | 10 | 4 | 6 | **`60.0%`** | `100.0%` | `+0.2m` |
| **Route 18** | 25 | 9 | 13 | **`52.0%`** | `90.0%` | `+1.1m` |
| **Route 64** | 20 | 6 | 10 | **`50.0%`** | `100.0%` | `+0.5m` |
| **Route 10** | 23 | 8 | 11 | **`47.83%`** | `100.0%` | `+0.1m` |
| **Route 11** | 20 | 8 | 9 | **`45.0%`** | `81.82%` | `+2.2m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+2.0m` |
| **Route 61** | 12 | 5 | 5 | **`41.67%`** | `100.0%` | `-100.1s` |
| **Route 7** | 12 | 4 | 5 | **`41.67%`** | `66.67%` | `+4.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+24.1 min (1448.4s)` | `+51.4 min (3086s)` | 2 | `40.0%` |
| **Route 94** | `+5.5 min (332.2s)` | `+18.0 min (1078s)` | 4 | `83.33%` |
| **Route 725** | `+5.3 min (316.0s)` | `+13.2 min (792s)` | 2 | `50.0%` |
| **Route 645** | `+5.2 min (314.2s)` | `+13.5 min (812s)` | 2 | `75.0%` |
| **Route 9** | `+5.2 min (311.6s)` | `+18.5 min (1109s)` | 6 | `55.56%` |
| **Route 7** | `+4.8 min (288.1s)` | `+18.8 min (1128s)` | 4 | `66.67%` |
| **Route 921** | `+4.4 min (265.2s)` | `+9.6 min (574s)` | 6 | `66.67%` |
| **Route 25** | `+3.8 min (230.5s)` | `+6.4 min (384s)` | 1 | `50.0%` |
| **Route 3** | `+3.7 min (219.7s)` | `+8.6 min (516s)` | 10 | `58.33%` |
| **Route 904** | `+3.5 min (210.5s)` | `+8.2 min (490s)` | 7 | `53.85%` |

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
| `1325181` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325513` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325561` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326094` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326234` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326451` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326595` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329200` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1335977` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344512` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359085` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317761` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318806` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319483` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319883` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T13:33:11.244805+00:00`.*
