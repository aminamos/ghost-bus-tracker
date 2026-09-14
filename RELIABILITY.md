# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-14T23:35:16.321773+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.7%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `760` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `634` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `126` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+110.4s` (`1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 518 | 68.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 56 | 7.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 44 | 5.8% |
| 🔴 **Severe Delay** | Over 15m late | 16 | 2.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 126 | 16.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 15 | 2.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 71** | 19 | 8 | 11 | **`57.89%`** | `14.29%` | `+44.0m` |
| **Route 540** | 11 | 5 | 6 | **`54.55%`** | `80.0%` | `+2.2m` |
| **Route 921** | 22 | 11 | 11 | **`50.0%`** | `100.0%` | `+0.8m` |
| **Route 5** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `-41.5s` |
| **Route 10** | 23 | 12 | 11 | **`47.83%`** | `100.0%` | `+0.4m` |
| **Route 219** | 10 | 6 | 4 | **`40.0%`** | `100.0%` | `+0.9m` |
| **Route 215** | 5 | 3 | 2 | **`40.0%`** | `100.0%` | `+1.4m` |
| **Route 18** | 26 | 16 | 10 | **`38.46%`** | `84.62%` | `+1.1m` |
| **Route 30** | 8 | 5 | 3 | **`37.5%`** | `100.0%` | `-77.6s` |
| **Route 538** | 11 | 7 | 4 | **`36.36%`** | `100.0%` | `-3.9s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 71** | `+44.0 min (2638.4s)` | `+86.6 min (5196s)` | 8 | `14.29%` |
| **Route 65** | `+8.6 min (516.2s)` | `+24.1 min (1449s)` | 5 | `60.0%` |
| **Route 54** | `+6.3 min (378.5s)` | `+26.2 min (1570s)` | 17 | `58.82%` |
| **Route 904** | `+6.2 min (373.7s)` | `+24.7 min (1482s)` | 17 | `58.82%` |
| **Route 9** | `+5.2 min (310.8s)` | `+23.8 min (1427s)` | 9 | `66.67%` |
| **Route 790** | `+4.5 min (269.0s)` | `+4.5 min (269s)` | 1 | `100.0%` |
| **Route 645** | `+4.2 min (250.7s)` | `+18.1 min (1085s)` | 6 | `60.0%` |
| **Route 542** | `+3.3 min (199.2s)` | `+9.7 min (581s)` | 4 | `75.0%` |
| **Route 673** | `+2.9 min (174.0s)` | `+2.9 min (174s)` | 1 | `100.0%` |
| **Route 902** | `+2.8 min (166.7s)` | `+7.0 min (420s)` | 9 | `88.89%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 71** | ~15.0m | ~59.0m | **`+15.56 min`** | `0.0 / 100` |
| **Route 65** | ~15.0m | ~23.6m | **`+5.33 min`** | `0.0 / 100` |
| **Route 54** | ~15.0m | ~21.3m | **`+3.85 min`** | `23.1 / 100` |
| **Route 9** | ~15.0m | ~20.2m | **`+3.75 min`** | `25.0 / 100` |
| **Route 904** | ~15.0m | ~21.2m | **`+3.61 min`** | `27.7 / 100` |
| **Route 645** | ~15.0m | ~19.2m | **`+3.35 min`** | `32.9 / 100` |
| **Route 61** | ~15.0m | ~17.5m | **`+3.12 min`** | `37.7 / 100` |
| **Route 30** | ~15.0m | ~13.7m | **`+2.47 min`** | `50.6 / 100` |
| **Route 11** | ~15.0m | ~13.1m | **`+2.37 min`** | `52.5 / 100` |
| **Route 615** | ~15.0m | ~15.8m | **`+2.33 min`** | `53.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1325105` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325715` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326039` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326050` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319876` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349744` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350049` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 23:35:16` | `16.58%` | `81.7%` | 760 | 634 | `+110.4s` |
| `2026-09-14 20:46:08` | `17.07%` | `80.61%` | 1113 | 923 | `+111.2s` |
| `2026-09-14 16:59:54` | `19.2%` | `86.8%` | 901 | 728 | `+60.5s` |
| `2026-09-14 11:14:14` | `20.62%` | `92.93%` | 873 | 693 | `+40.3s` |
| `2026-09-14 05:33:56` | `2.25%` | `80.46%` | 89 | 87 | `+102.8s` |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T23:35:16.321773+00:00`.*
