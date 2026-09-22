# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-22T01:41:09.840023+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.51%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `530` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `430` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `86` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+65.0s` (`1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+11.0s` (`0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 286 | 54.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 99 | 18.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 40 | 7.5% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 86 | 16.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 2.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 65** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+10.7m` |
| **Route 17** | 13 | 5 | 6 | **`46.15%`** | `100.0%` | `-56.0s` |
| **Route 10** | 20 | 7 | 8 | **`40.0%`** | `100.0%` | `-19.6s` |
| **Route 540** | 11 | 4 | 4 | **`36.36%`** | `80.0%` | `+1.1m` |
| **Route 18** | 25 | 12 | 9 | **`36.0%`** | `71.43%` | `+0.3m` |
| **Route 921** | 23 | 7 | 8 | **`34.78%`** | `85.71%` | `+2.2m` |
| **Route 11** | 12 | 6 | 4 | **`33.33%`** | `100.0%` | `-57.0s` |
| **Route 64** | 12 | 5 | 4 | **`33.33%`** | `100.0%` | `+0.8m` |
| **Route 68** | 12 | 6 | 4 | **`33.33%`** | `71.43%` | `+2.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 65** | `+10.7 min (643.0s)` | `+12.6 min (757s)` | 1 | `0.0%` |
| **Route 9** | `+4.6 min (275.7s)` | `+11.2 min (671s)` | 4 | `40.0%` |
| **Route 904** | `+4.3 min (260.1s)` | `+8.7 min (520s)` | 7 | `53.85%` |
| **Route 924** | `+4.2 min (249.9s)` | `+22.2 min (1335s)` | 12 | `57.14%` |
| **Route 802** | `+3.8 min (229.0s)` | `+15.8 min (945s)` | 2 | `0.0%` |
| **Route 5** | `+3.1 min (187.8s)` | `+14.7 min (882s)` | 3 | `66.67%` |
| **Route 725** | `+3.1 min (183.5s)` | `+3.9 min (233s)` | 1 | `100.0%` |
| **Route 68** | `+2.6 min (158.1s)` | `+9.4 min (565s)` | 6 | `71.43%` |
| **Route 87** | `+2.6 min (157.8s)` | `+12.2 min (731s)` | 3 | `66.67%` |
| **Route 54** | `+2.4 min (146.0s)` | `+15.9 min (955s)` | 11 | `93.75%` |

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
| `1325266` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325968` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326479` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326807` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319569` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319879` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351263` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351646` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332519` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332593` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333220` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-22 01:41:09` | `16.23%` | `66.51%` | 530 | 430 | `+65.0s` |
| `2026-09-21 23:25:41` | `15.03%` | `53.0%` | 825 | 666 | `+13.2s` |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |
| `2026-09-21 08:05:04` | `0.0%` | `53.85%` | 13 | 13 | `+-52.1s` |
| `2026-09-20 23:42:26` | `14.52%` | `62.89%` | 544 | 450 | `+204.9s` |
| `2026-09-20 21:42:01` | `16.79%` | `67.44%` | 679 | 563 | `+174.9s` |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-22T01:41:09.840023+00:00`.*
