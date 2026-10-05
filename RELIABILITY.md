# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-05T09:18:29.366305+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`33.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.79%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `231` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `154` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `77` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-42.7s` (`-0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-43.5s` (`-0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 89 | 38.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 65 | 28.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 77 | 33.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 223** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 67** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 645** | 4 | 1 | 3 | **`75.0%`** | `100.0%` | `+0.1m` |
| **Route 9** | 7 | 2 | 5 | **`71.43%`** | `100.0%` | `+1.8m` |
| **Route 63** | 9 | 4 | 5 | **`55.56%`** | `100.0%` | `-58.0s` |
| **Route 68** | 9 | 4 | 5 | **`55.56%`** | `100.0%` | `-4.0s` |
| **Route 925** | 9 | 4 | 5 | **`55.56%`** | `100.0%` | `-33.0s` |
| **Route 18** | 15 | 7 | 8 | **`53.33%`** | `100.0%` | `-14.6s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+2.9 min (171.5s)` | `+4.8 min (287s)` | 5 | `100.0%` |
| **Route 921** | `+1.9 min (115.2s)` | `+3.3 min (200s)` | 3 | `100.0%` |
| **Route 9** | `+1.8 min (107.5s)` | `+3.1 min (189s)` | 2 | `100.0%` |
| **Route 7** | `+1.3 min (79.7s)` | `+3.6 min (216s)` | 3 | `100.0%` |
| **Route 901** | `+1.0 min (60.0s)` | `+1.0 min (60s)` | 1 | `100.0%` |
| **Route 3** | `+0.7 min (43.6s)` | `+4.5 min (272s)` | 5 | `100.0%` |
| **Route 72** | `+0.7 min (39.0s)` | `+0.7 min (44s)` | 2 | `100.0%` |
| **Route 923** | `+0.6 min (34.0s)` | `+1.3 min (78s)` | 3 | `100.0%` |
| **Route 36** | `+0.5 min (28.5s)` | `+2.4 min (144s)` | 3 | `100.0%` |
| **Route 64** | `+0.3 min (20.0s)` | `+1.5 min (92s)` | 4 | `100.0%` |

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
| `1305021` | Route 134 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331482` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332211` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333184` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1141528` | Route 156 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361093` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361681` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361789` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361795` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364927` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365944` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366412` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366852` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1277834` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1278473` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 09:18:29` | `33.33%` | `57.79%` | 231 | 154 | `+-42.7s` |
| `2026-10-05 02:10:28` | `11.4%` | `67.17%` | 386 | 332 | `+204.7s` |
| `2026-10-04 23:20:57` | `9.43%` | `61.8%` | 562 | 501 | `+251.0s` |
| `2026-10-04 20:16:15` | `11.44%` | `60.24%` | 673 | 591 | `+290.1s` |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T09:18:29.366305+00:00`.*
