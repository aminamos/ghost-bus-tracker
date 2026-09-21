# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-21T20:03:32.275000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.78%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.44%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1108` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `864` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `197` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+35.0s` (`0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.5s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 510 | 46.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 261 | 23.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 81 | 7.3% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 197 | 17.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 49 | 4.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 9 | 3 | 6 | **`66.67%`** | `100.0%` | `+1.2m` |
| **Route 760** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-72.0s` |
| **Route 766** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+2.0m` |
| **Route 882** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+1.0m` |
| **Route 768** | 8 | 3 | 5 | **`62.5%`** | `100.0%` | `+0.0m` |
| **Route 275** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `-28.5s` |
| **Route 763** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-74.0s` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-75.0s` |
| **Route 860** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-52.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+5.8 min (348.9s)` | `+19.0 min (1138s)` | 11 | `33.33%` |
| **Route 113** | `+4.8 min (288.0s)` | `+4.8 min (288s)` | 2 | `100.0%` |
| **Route 65** | `+4.2 min (249.3s)` | `+17.1 min (1024s)` | 4 | `0.0%` |
| **Route 67** | `+3.4 min (206.5s)` | `+7.3 min (436s)` | 6 | `62.5%` |
| **Route 673** | `+3.3 min (198.0s)` | `+6.4 min (384s)` | 3 | `75.0%` |
| **Route 777** | `+3.3 min (197.0s)` | `+3.3 min (197s)` | 1 | `100.0%` |
| **Route 5** | `+3.2 min (194.4s)` | `+21.6 min (1299s)` | 7 | `87.5%` |
| **Route 645** | `+3.2 min (193.7s)` | `+10.3 min (618s)` | 4 | `66.67%` |
| **Route 75** | `+3.2 min (190.8s)` | `+13.5 min (810s)` | 2 | `66.67%` |
| **Route 363** | `+3.1 min (184.0s)` | `+3.1 min (184s)` | 1 | `100.0%` |

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
| `1325041` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325282` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325699` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325853` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326040` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326160` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326419` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326803` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326896` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327099` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327148` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |
| `2026-09-21 08:05:04` | `0.0%` | `53.85%` | 13 | 13 | `+-52.1s` |
| `2026-09-20 23:42:26` | `14.52%` | `62.89%` | 544 | 450 | `+204.9s` |
| `2026-09-20 21:42:01` | `16.79%` | `67.44%` | 679 | 563 | `+174.9s` |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-21T20:03:32.275000+00:00`.*
