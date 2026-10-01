# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-01T06:13:46.566455+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.52%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `61` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `46` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+167.1s` (`2.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+29.0s` (`0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 26 | 42.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 14 | 23.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 4.9% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 4.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 23.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+34.6m` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8m` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-74.0s` |
| **Route 17** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `-16.2s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6m` |
| **Route 22** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `-46.5s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `66.67%` | `+2.5m` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `-19.3s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-48.5s` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-94.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 18** | `+34.6 min (2078.0s)` | `+41.8 min (2508s)` | 2 | `0.0%` |
| **Route 54** | `+28.0 min (1679.0s)` | `+28.0 min (1679s)` | 1 | `0.0%` |
| **Route 924** | `+4.8 min (289.3s)` | `+14.3 min (857s)` | 3 | `66.67%` |
| **Route 921** | `+3.2 min (191.5s)` | `+3.4 min (203s)` | 2 | `100.0%` |
| **Route 922** | `+3.0 min (178.0s)` | `+5.5 min (331s)` | 2 | `50.0%` |
| **Route 64** | `+2.9 min (175.0s)` | `+2.9 min (175s)` | 1 | `100.0%` |
| **Route 3** | `+2.5 min (151.0s)` | `+7.3 min (441s)` | 4 | `66.67%` |
| **Route 74** | `+2.3 min (140.0s)` | `+2.3 min (140s)` | 1 | `100.0%` |
| **Route 923** | `+2.2 min (132.0s)` | `+2.2 min (132s)` | 1 | `100.0%` |
| **Route 925** | `+1.1 min (63.5s)` | `+1.6 min (95s)` | 2 | `100.0%` |

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
| `1357973` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-01T06:13:46.566455+00:00`.*
