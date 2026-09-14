# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-14T16:59:54.904717+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.2%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`86.8%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `901` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `728` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `173` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+60.5s` (`1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 631 | 70.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 49 | 5.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 38 | 4.2% |
| 🔴 **Severe Delay** | Over 15m late | 9 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 173 | 19.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 0.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 465** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 475** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 223** | 7 | 2 | 5 | **`71.43%`** | `100.0%` | `+0.8m` |
| **Route 18** | 38 | 21 | 17 | **`44.74%`** | `94.44%` | `+0.7m` |
| **Route 10** | 34 | 19 | 15 | **`44.12%`** | `87.5%` | `+0.5m` |
| **Route 11** | 24 | 14 | 10 | **`41.67%`** | `100.0%` | `-31.6s` |
| **Route 538** | 10 | 6 | 4 | **`40.0%`** | `100.0%` | `+1.2m` |
| **Route 215** | 5 | 3 | 2 | **`40.0%`** | `100.0%` | `+0.2m` |
| **Route 921** | 31 | 19 | 12 | **`38.71%`** | `100.0%` | `+0.1m` |
| **Route 25** | 8 | 5 | 3 | **`37.5%`** | `60.0%` | `+3.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 71** | `+8.5 min (512.9s)` | `+50.1 min (3006s)` | 9 | `75.0%` |
| **Route 542** | `+7.4 min (446.4s)` | `+29.8 min (1790s)` | 7 | `71.43%` |
| **Route 540** | `+6.5 min (390.6s)` | `+34.2 min (2053s)` | 7 | `85.71%` |
| **Route 925** | `+3.9 min (234.8s)` | `+38.7 min (2320s)` | 25 | `80.0%` |
| **Route 25** | `+3.0 min (178.4s)` | `+7.5 min (453s)` | 5 | `60.0%` |
| **Route 725** | `+2.9 min (172.7s)` | `+8.6 min (518s)` | 3 | `66.67%` |
| **Route 781** | `+2.7 min (164.5s)` | `+5.5 min (329s)` | 2 | `50.0%` |
| **Route 645** | `+2.2 min (134.2s)` | `+10.7 min (640s)` | 9 | `88.89%` |
| **Route 94** | `+2.2 min (129.5s)` | `+15.2 min (914s)` | 10 | `80.0%` |
| **Route 3** | `+2.0 min (122.9s)` | `+14.3 min (861s)` | 17 | `81.25%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 71** | ~15.0m | ~23.5m | **`+8.37 min`** | `0.0 / 100` |
| **Route 540** | ~15.0m | ~21.5m | **`+5.71 min`** | `0.0 / 100` |
| **Route 542** | ~15.0m | ~22.4m | **`+5.39 min`** | `0.0 / 100` |
| **Route 925** | ~15.0m | ~18.9m | **`+4.08 min`** | `18.3 / 100` |
| **Route 888** | ~15.0m | ~11.9m | **`+2.83 min`** | `43.4 / 100` |
| **Route 904** | ~15.0m | ~17.0m | **`+2.36 min`** | `52.8 / 100` |
| **Route 94** | ~15.0m | ~17.2m | **`+2.31 min`** | `53.9 / 100` |
| **Route 11** | ~15.0m | ~14.5m | **`+2.3 min`** | `54.1 / 100` |
| **Route 725** | ~15.0m | ~17.9m | **`+2.03 min`** | `59.3 / 100` |
| **Route 902** | ~15.0m | ~15.5m | **`+2.02 min`** | `59.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325697` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325814` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325819` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326195` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326229` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326353` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326410` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326415` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326587` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329942` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330840` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 16:59:54` | `19.2%` | `86.8%` | 901 | 728 | `+60.5s` |
| `2026-09-14 11:14:14` | `20.62%` | `92.93%` | 873 | 693 | `+40.3s` |
| `2026-09-14 05:33:56` | `2.25%` | `80.46%` | 89 | 87 | `+102.8s` |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:41:28` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:36:50` | `13.36%` | `73.73%` | 479 | 414 | `+257.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T16:59:54.904717+00:00`.*
