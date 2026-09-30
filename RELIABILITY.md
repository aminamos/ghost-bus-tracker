# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-30T09:22:54.875686+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`35.85%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `265` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `170` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `95` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-36.8s` (`-0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-39.5s` (`-0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 102 | 38.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 66 | 24.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 95 | 35.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 223** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 645** | 4 | 1 | 3 | **`75.0%`** | `100.0%` | `+0.1m` |
| **Route 11** | 11 | 4 | 7 | **`63.64%`** | `100.0%` | `-43.2s` |
| **Route 64** | 13 | 5 | 8 | **`61.54%`** | `100.0%` | `+0.4m` |
| **Route 9** | 7 | 3 | 4 | **`57.14%`** | `100.0%` | `+2.6m` |
| **Route 68** | 9 | 4 | 5 | **`55.56%`** | `100.0%` | `-2.8s` |
| **Route 924** | 18 | 8 | 9 | **`50.0%`** | `100.0%` | `-49.8s` |
| **Route 18** | 16 | 7 | 8 | **`50.0%`** | `100.0%` | `-3.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 921** | `+3.0 min (182.3s)` | `+5.3 min (316s)` | 4 | `83.33%` |
| **Route 901** | `+2.8 min (165.0s)` | `+3.0 min (180s)` | 2 | `100.0%` |
| **Route 9** | `+2.6 min (154.7s)` | `+3.1 min (189s)` | 3 | `100.0%` |
| **Route 54** | `+1.3 min (78.0s)` | `+6.2 min (374s)` | 4 | `80.0%` |
| **Route 7** | `+1.0 min (61.7s)` | `+2.7 min (160s)` | 3 | `100.0%` |
| **Route 72** | `+0.7 min (39.5s)` | `+0.8 min (45s)` | 2 | `100.0%` |
| **Route 923** | `+0.6 min (34.0s)` | `+1.3 min (78s)` | 3 | `100.0%` |
| **Route 3** | `+0.5 min (32.2s)` | `+4.0 min (241s)` | 5 | `100.0%` |
| **Route 36** | `+0.4 min (25.5s)` | `+2.2 min (132s)` | 3 | `100.0%` |
| **Route 64** | `+0.4 min (23.6s)` | `+1.5 min (92s)` | 5 | `100.0%` |

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
| `1325662` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325896` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326087` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327208` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318375` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318754` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319244` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319651` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349089` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350071` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351377` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1305021` | Route 134 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331482` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331585` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332211` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-30T09:22:54.875686+00:00`.*
