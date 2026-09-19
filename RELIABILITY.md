# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T11:16:01.074324+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.05%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `479` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `343` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `135` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+48.3s` (`0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+33.5s` (`0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 243 | 50.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 78 | 16.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 19 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 135 | 28.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 94** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 67** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 10** | 15 | 4 | 9 | **`60.0%`** | `100.0%` | `+0.5m` |
| **Route 25** | 5 | 2 | 3 | **`60.0%`** | `0.0%` | `+1.9m` |
| **Route 538** | 5 | 2 | 3 | **`60.0%`** | `100.0%` | `+1.3m` |
| **Route 540** | 5 | 1 | 3 | **`60.0%`** | `100.0%` | `-26.0s` |
| **Route 64** | 13 | 3 | 7 | **`53.85%`** | `100.0%` | `-82.3s` |
| **Route 17** | 12 | 4 | 6 | **`50.0%`** | `83.33%` | `+1.2m` |
| **Route 68** | 12 | 4 | 6 | **`50.0%`** | `100.0%` | `-5.3s` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+3.6 min (218.0s)` | `+8.1 min (487s)` | 7 | `66.67%` |
| **Route 725** | `+3.4 min (201.3s)` | `+6.8 min (408s)` | 2 | `66.67%` |
| **Route 921** | `+3.1 min (184.8s)` | `+16.2 min (970s)` | 6 | `84.62%` |
| **Route 54** | `+2.7 min (159.7s)` | `+8.0 min (480s)` | 5 | `85.71%` |
| **Route 18** | `+2.5 min (148.6s)` | `+15.3 min (916s)` | 9 | `81.82%` |
| **Route 901** | `+2.4 min (146.2s)` | `+5.0 min (300s)` | 8 | `100.0%` |
| **Route 923** | `+2.4 min (145.9s)` | `+8.2 min (489s)` | 5 | `77.78%` |
| **Route 645** | `+2.3 min (138.0s)` | `+2.3 min (138s)` | 1 | `100.0%` |
| **Route 36** | `+2.3 min (136.7s)` | `+8.1 min (484s)` | 3 | `80.0%` |
| **Route 9** | `+2.1 min (125.1s)` | `+5.4 min (325s)` | 7 | `85.71%` |

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
| `1325424` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325586` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325685` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325831` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326094` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326155` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327171` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1328129` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329456` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333584` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351873` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352185` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1353062` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331025` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332360` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T11:16:01.074324+00:00`.*
