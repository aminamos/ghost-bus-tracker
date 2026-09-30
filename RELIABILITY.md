# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-30T02:59:00.500370+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.84%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.85%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `437` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `367` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `43` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+52.5s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 238 | 54.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 95 | 21.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 29 | 6.6% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 43 | 9.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 26 | 5.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `75.0%` | `+0.3m` |
| **Route 11** | 12 | 6 | 4 | **`33.33%`** | `85.71%` | `+1.9m` |
| **Route 515** | 7 | 4 | 2 | **`28.57%`** | `100.0%` | `+0.3m` |
| **Route 7** | 7 | 3 | 2 | **`28.57%`** | `100.0%` | `-17.0s` |
| **Route 9** | 7 | 4 | 2 | **`28.57%`** | `66.67%` | `+1.3m` |
| **Route 18** | 22 | 12 | 6 | **`27.27%`** | `91.67%` | `+0.8m` |
| **Route 64** | 11 | 4 | 3 | **`27.27%`** | `83.33%` | `+0.6m` |
| **Route 68** | 12 | 5 | 3 | **`25.0%`** | `100.0%` | `-68.2s` |
| **Route 5** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.3m` |
| **Route 924** | 21 | 12 | 5 | **`23.81%`** | `90.0%` | `+0.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+8.1 min (483.0s)` | `+8.1 min (483s)` | 1 | `0.0%` |
| **Route 725** | `+5.3 min (315.5s)` | `+8.5 min (512s)` | 2 | `50.0%` |
| **Route 30** | `+5.2 min (314.0s)` | `+10.6 min (634s)` | 2 | `50.0%` |
| **Route 2** | `+4.6 min (274.0s)` | `+15.0 min (901s)` | 6 | `66.67%` |
| **Route 32** | `+3.6 min (216.0s)` | `+3.6 min (216s)` | 1 | `100.0%` |
| **Route 215** | `+3.3 min (197.0s)` | `+5.5 min (327s)` | 1 | `50.0%` |
| **Route 923** | `+3.2 min (190.8s)` | `+15.8 min (949s)` | 5 | `81.82%` |
| **Route 17** | `+3.1 min (188.3s)` | `+28.4 min (1705s)` | 7 | `85.71%` |
| **Route 925** | `+2.7 min (164.4s)` | `+12.1 min (728s)` | 10 | `73.33%` |
| **Route 921** | `+2.4 min (143.2s)` | `+4.8 min (287s)` | 6 | `100.0%` |

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
| `1327003` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319445` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319546` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349623` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362805` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331698` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332889` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317845` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320086` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357399` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357743` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361046` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361581` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361969` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363353` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-30T02:59:00.500370+00:00`.*
