# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-09-26T05:12:57.322076+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.4%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.83%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `143` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `141` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+50.0s` (`0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+2.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 90 | 62.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 41 | 28.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 4.9% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 2.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 1.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 64** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.3m` |
| **Route 36** | 5 | 3 | 1 | **`20.0%`** | `100.0%` | `-23.2s` |
| **Route 10** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `-15.8s` |
| **Route 11** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.2m` |
| **Route 14** | 5 | 4 | 0 | **`0.0%`** | `75.0%` | `+2.5m` |
| **Route 17** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `-66.8s` |
| **Route 18** | 7 | 6 | 0 | **`0.0%`** | `100.0%` | `+1.6m` |
| **Route 2** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `-34.0s` |
| **Route 22** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `-76.4s` |
| **Route 3** | 7 | 6 | 0 | **`0.0%`** | `66.67%` | `+6.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+14.3 min (856.0s)` | `+28.4 min (1702s)` | 2 | `33.33%` |
| **Route 3** | `+6.3 min (379.0s)` | `+37.2 min (2230s)` | 6 | `66.67%` |
| **Route 94** | `+5.0 min (297.0s)` | `+6.9 min (416s)` | 2 | `50.0%` |
| **Route 925** | `+2.7 min (164.8s)` | `+4.8 min (288s)` | 3 | `100.0%` |
| **Route 14** | `+2.5 min (148.0s)` | `+16.9 min (1011s)` | 4 | `75.0%` |
| **Route 65** | `+2.4 min (145.0s)` | `+2.8 min (165s)` | 1 | `100.0%` |
| **Route 922** | `+2.2 min (133.7s)` | `+8.4 min (504s)` | 7 | `57.14%` |
| **Route 54** | `+1.8 min (110.5s)` | `+4.2 min (252s)` | 3 | `100.0%` |
| **Route 18** | `+1.6 min (97.1s)` | `+4.0 min (243s)` | 6 | `100.0%` |
| **Route 903** | `+1.5 min (90.0s)` | `+1.5 min (90s)` | 1 | `100.0%` |

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
| `1233208` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360805` | Route 64 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-26T05:12:57.322076+00:00`.*
