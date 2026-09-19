# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T13:13:58.637521+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`24.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.97%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `667` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `503` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `163` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+73.2s` (`1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+32.0s` (`0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 362 | 54.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 92 | 13.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 45 | 6.7% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 163 | 24.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 223** | 7 | 1 | 5 | **`71.43%`** | `50.0%` | `+4.1m` |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `+1.8m` |
| **Route 11** | 18 | 6 | 10 | **`55.56%`** | `100.0%` | `+1.9m` |
| **Route 36** | 11 | 3 | 6 | **`54.55%`** | `80.0%` | `+1.3m` |
| **Route 10** | 21 | 8 | 11 | **`52.38%`** | `88.89%` | `+1.2m` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.4m` |
| **Route 827** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+1.5m` |
| **Route 17** | 13 | 5 | 6 | **`46.15%`** | `100.0%` | `-37.3s` |
| **Route 18** | 24 | 9 | 11 | **`45.83%`** | `81.82%` | `+0.7m` |
| **Route 64** | 22 | 6 | 10 | **`45.45%`** | `100.0%` | `-5.9s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+15.2 min (913.8s)` | `+32.5 min (1949s)` | 2 | `50.0%` |
| **Route 645** | `+8.0 min (477.0s)` | `+12.7 min (763s)` | 2 | `25.0%` |
| **Route 94** | `+6.4 min (384.6s)` | `+23.4 min (1402s)` | 3 | `62.5%` |
| **Route 921** | `+5.1 min (303.7s)` | `+18.7 min (1124s)` | 6 | `69.23%` |
| **Route 223** | `+4.1 min (248.5s)` | `+6.2 min (369s)` | 1 | `50.0%` |
| **Route 725** | `+3.6 min (218.5s)` | `+3.9 min (232s)` | 2 | `100.0%` |
| **Route 904** | `+3.5 min (208.5s)` | `+6.8 min (409s)` | 7 | `61.54%` |
| **Route 3** | `+3.3 min (197.6s)` | `+8.6 min (516s)` | 9 | `81.82%` |
| **Route 9** | `+3.0 min (179.5s)` | `+5.9 min (356s)` | 6 | `70.0%` |
| **Route 903** | `+2.9 min (174.0s)` | `+13.6 min (813s)` | 2 | `80.0%` |

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
| `1325561` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326094` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326234` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326451` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326595` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326652` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326736` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327908` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344512` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359085` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318806` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319883` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351611` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351873` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T13:13:58.637521+00:00`.*
