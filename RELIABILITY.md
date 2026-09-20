# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-20T19:11:50.026588+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.57%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `694` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `555` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `137` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+169.7s` (`2.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+120.0s` (`2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 375 | 54.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 55 | 7.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 115 | 16.6% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 1.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 137 | 19.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 46** | 7 | 1 | 5 | **`71.43%`** | `100.0%` | `+2.0m` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.5m` |
| **Route 9** | 15 | 5 | 7 | **`46.67%`** | `42.86%` | `+6.8m` |
| **Route 17** | 23 | 10 | 10 | **`43.48%`** | `100.0%` | `-8.1s` |
| **Route 10** | 35 | 13 | 15 | **`42.86%`** | `83.33%` | `+2.7m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+2.0m` |
| **Route 921** | 33 | 11 | 14 | **`42.42%`** | `89.47%` | `+2.4m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `+1.1m` |
| **Route 11** | 24 | 11 | 9 | **`37.5%`** | `85.71%` | `+2.4m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `57.14%` | `+4.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 725** | `+7.2 min (433.5s)` | `+7.4 min (443s)` | 2 | `0.0%` |
| **Route 9** | `+6.8 min (409.5s)` | `+24.7 min (1483s)` | 5 | `42.86%` |
| **Route 74** | `+6.5 min (390.2s)` | `+26.4 min (1582s)` | 6 | `37.5%` |
| **Route 645** | `+6.2 min (369.5s)` | `+10.1 min (605s)` | 2 | `50.0%` |
| **Route 22** | `+6.1 min (368.8s)` | `+15.7 min (944s)` | 12 | `64.29%` |
| **Route 68** | `+5.9 min (352.5s)` | `+18.9 min (1136s)` | 8 | `69.23%` |
| **Route 27** | `+5.8 min (348.7s)` | `+6.0 min (362s)` | 2 | `0.0%` |
| **Route 67** | `+5.7 min (343.2s)` | `+11.9 min (716s)` | 4 | `33.33%` |
| **Route 54** | `+5.1 min (303.8s)` | `+15.2 min (909s)` | 10 | `50.0%` |
| **Route 904** | `+5.0 min (302.4s)` | `+10.4 min (622s)` | 10 | `46.15%` |

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
| `1325402` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325540` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325702` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325899` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325905` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325976` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326298` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326303` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326325` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326504` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326665` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326691` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326906` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326976` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327216` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |
| `2026-09-20 07:50:25` | `0.0%` | `100.0%` | 4 | 4 | `+68.2s` |
| `2026-09-20 02:21:35` | `16.33%` | `70.92%` | 447 | 368 | `+162.2s` |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-20T19:11:50.026588+00:00`.*
