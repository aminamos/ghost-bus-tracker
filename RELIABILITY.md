# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-15T02:26:54.133109+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.03%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.32%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `458` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `380` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `78` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+62.9s` (`1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 347 | 75.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 2.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 20 | 4.4% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 78 | 17.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 10 | 2.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 71** | 8 | 1 | 7 | **`87.5%`** | `0.0%` | `-101.0s` |
| **Route 725** | 4 | 1 | 3 | **`75.0%`** | `100.0%` | `-3.0s` |
| **Route 10** | 15 | 7 | 8 | **`53.33%`** | `100.0%` | `+1.4m` |
| **Route 18** | 25 | 13 | 12 | **`48.0%`** | `92.31%` | `+0.8m` |
| **Route 17** | 12 | 7 | 5 | **`41.67%`** | `100.0%` | `+1.6m` |
| **Route 11** | 11 | 7 | 4 | **`36.36%`** | `71.43%` | `+2.1m` |
| **Route 64** | 12 | 8 | 4 | **`33.33%`** | `85.71%` | `+1.1m` |
| **Route 14** | 9 | 6 | 3 | **`33.33%`** | `100.0%` | `+0.6m` |
| **Route 30** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+0.2m` |
| **Route 723** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+4.4 min (263.0s)` | `+4.4 min (263s)` | 1 | `100.0%` |
| **Route 4** | `+3.2 min (189.6s)` | `+16.4 min (984s)` | 8 | `87.5%` |
| **Route 22** | `+3.0 min (179.6s)` | `+16.1 min (968s)` | 9 | `77.78%` |
| **Route 72** | `+2.6 min (154.8s)` | `+7.4 min (442s)` | 5 | `60.0%` |
| **Route 68** | `+2.5 min (150.1s)` | `+14.4 min (866s)` | 8 | `87.5%` |
| **Route 827** | `+2.3 min (139.0s)` | `+2.3 min (139s)` | 1 | `100.0%` |
| **Route 9** | `+2.2 min (130.2s)` | `+7.5 min (449s)` | 6 | `66.67%` |
| **Route 11** | `+2.1 min (126.6s)` | `+7.2 min (434s)` | 7 | `71.43%` |
| **Route 54** | `+2.0 min (121.1s)` | `+11.8 min (710s)` | 15 | `86.67%` |
| **Route 61** | `+1.9 min (112.6s)` | `+5.5 min (329s)` | 8 | `87.5%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 4** | ~15.0m | ~18.2m | **`+2.67 min`** | `46.6 / 100` |
| **Route 22** | ~15.0m | ~18.0m | **`+2.48 min`** | `50.3 / 100` |
| **Route 68** | ~15.0m | ~17.5m | **`+2.29 min`** | `54.1 / 100` |
| **Route 72** | ~15.0m | ~17.6m | **`+1.73 min`** | `65.4 / 100` |
| **Route 724** | ~15.0m | ~16.6m | **`+1.67 min`** | `66.6 / 100` |
| **Route 11** | ~15.0m | ~17.1m | **`+1.58 min`** | `68.4 / 100` |
| **Route 54** | ~15.0m | ~17.0m | **`+1.53 min`** | `69.4 / 100` |
| **Route 9** | ~15.0m | ~17.2m | **`+1.53 min`** | `69.3 / 100` |
| **Route 38** | ~15.0m | ~15.1m | **`+1.47 min`** | `70.7 / 100` |
| **Route 219** | ~15.0m | ~16.5m | **`+1.38 min`** | `72.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1325266` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325371` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325738` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325888` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326807` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327003` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319546` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319569` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349623` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351646` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332593` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332889` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333220` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-15 02:26:54` | `17.03%` | `91.32%` | 458 | 380 | `+62.9s` |
| `2026-09-14 23:35:16` | `16.58%` | `81.7%` | 760 | 634 | `+110.4s` |
| `2026-09-14 20:46:08` | `17.07%` | `80.61%` | 1113 | 923 | `+111.2s` |
| `2026-09-14 16:59:54` | `19.2%` | `86.8%` | 901 | 728 | `+60.5s` |
| `2026-09-14 11:14:14` | `20.62%` | `92.93%` | 873 | 693 | `+40.3s` |
| `2026-09-14 05:33:56` | `2.25%` | `80.46%` | 89 | 87 | `+102.8s` |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-15T02:26:54.133109+00:00`.*
