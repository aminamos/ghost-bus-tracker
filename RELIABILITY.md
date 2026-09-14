# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-14T11:14:14.332197+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`20.62%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`92.93%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `873` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `693` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `180` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+40.3s` (`0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 644 | 73.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 27 | 3.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 18 | 2.1% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 180 | 20.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 490** | 8 | 0 | 8 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 465** | 6 | 0 | 6 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 475** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 538** | 8 | 2 | 6 | **`75.0%`** | `100.0%` | `0.0s` |
| **Route 578** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `0.0s` |
| **Route 888** | 6 | 3 | 3 | **`50.0%`** | `100.0%` | `-5.3s` |
| **Route 215** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `0.0s` |
| **Route 615** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `0.0s` |
| **Route 540** | 9 | 5 | 4 | **`44.44%`** | `100.0%` | `+0.8m` |
| **Route 67** | 9 | 5 | 4 | **`44.44%`** | `100.0%` | `0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 27** | `+5.6 min (336.0s)` | `+16.8 min (1008s)` | 3 | `66.67%` |
| **Route 645** | `+5.2 min (313.9s)` | `+20.3 min (1218s)` | 8 | `75.0%` |
| **Route 36** | `+4.3 min (259.0s)` | `+28.3 min (1696s)` | 8 | `87.5%` |
| **Route 805** | `+3.0 min (178.0s)` | `+10.4 min (623s)` | 4 | `75.0%` |
| **Route 25** | `+2.5 min (148.4s)` | `+9.1 min (545s)` | 5 | `80.0%` |
| **Route 902** | `+2.1 min (126.7s)` | `+6.0 min (360s)` | 9 | `88.89%` |
| **Route 10** | `+2.1 min (126.1s)` | `+11.5 min (688s)` | 14 | `85.71%` |
| **Route 824** | `+1.8 min (109.0s)` | `+3.6 min (218s)` | 2 | `100.0%` |
| **Route 901** | `+1.8 min (105.0s)` | `+5.0 min (300s)` | 8 | `100.0%` |
| **Route 467** | `+1.5 min (89.0s)` | `+3.0 min (178s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 36** | ~15.0m | ~19.3m | **`+4.56 min`** | `8.9 / 100` |
| **Route 645** | ~15.0m | ~20.2m | **`+4.29 min`** | `14.3 / 100` |
| **Route 27** | ~15.0m | ~20.6m | **`+3.96 min`** | `20.8 / 100` |
| **Route 790** | ~15.0m | ~12.3m | **`+2.84 min`** | `43.3 / 100` |
| **Route 776** | ~15.0m | ~12.3m | **`+2.32 min`** | `53.7 / 100` |
| **Route 805** | ~15.0m | ~18.0m | **`+2.16 min`** | `56.8 / 100` |
| **Route 673** | ~15.0m | ~13.4m | **`+1.93 min`** | `61.3 / 100` |
| **Route 10** | ~15.0m | ~17.1m | **`+1.89 min`** | `62.1 / 100` |
| **Route 25** | ~15.0m | ~17.5m | **`+1.77 min`** | `64.6 / 100` |
| **Route 3** | ~15.0m | ~16.3m | **`+1.33 min`** | `73.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1325972` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326014` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326163` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326264` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326441` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326937` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326961` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327017` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1219476` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317864` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318128` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318262` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318573` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348808` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349275` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 11:14:14` | `20.62%` | `92.93%` | 873 | 693 | `+40.3s` |
| `2026-09-14 05:33:56` | `2.25%` | `80.46%` | 89 | 87 | `+102.8s` |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:41:28` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:36:50` | `13.36%` | `73.73%` | 479 | 414 | `+257.4s` |
| `2026-09-14 00:36:42` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T11:14:14.332197+00:00`.*
