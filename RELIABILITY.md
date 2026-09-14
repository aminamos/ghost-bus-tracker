# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-14T20:46:08.479584+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.61%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1113` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `923` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `190` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+111.2s` (`1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 744 | 66.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 42 | 3.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 124 | 11.1% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 1.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 190 | 17.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 21 | 1.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 465** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 71** | 19 | 8 | 11 | **`57.89%`** | `62.5%` | `+7.8m` |
| **Route 540** | 10 | 5 | 5 | **`50.0%`** | `60.0%` | `+4.1m` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+1.9m` |
| **Route 10** | 38 | 21 | 17 | **`44.74%`** | `90.0%` | `+1.8m` |
| **Route 768** | 9 | 5 | 4 | **`44.44%`** | `60.0%` | `+4.9m` |
| **Route 223** | 7 | 4 | 3 | **`42.86%`** | `75.0%` | `+1.6m` |
| **Route 11** | 26 | 15 | 11 | **`42.31%`** | `83.33%` | `+1.2m` |
| **Route 219** | 10 | 6 | 4 | **`40.0%`** | `100.0%` | `+0.9m` |
| **Route 538** | 10 | 6 | 4 | **`40.0%`** | `100.0%` | `+0.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 860** | `+12.4 min (746.5s)` | `+24.9 min (1493s)` | 2 | `50.0%` |
| **Route 71** | `+7.8 min (470.0s)` | `+37.4 min (2246s)` | 8 | `62.5%` |
| **Route 615** | `+6.2 min (373.7s)` | `+15.2 min (910s)` | 3 | `66.67%` |
| **Route 763** | `+5.7 min (339.0s)` | `+11.3 min (678s)` | 2 | `50.0%` |
| **Route 768** | `+4.9 min (291.8s)` | `+18.2 min (1090s)` | 5 | `60.0%` |
| **Route 902** | `+4.3 min (256.4s)` | `+9.0 min (540s)` | 11 | `63.64%` |
| **Route 904** | `+4.2 min (251.6s)` | `+16.2 min (975s)` | 22 | `59.09%` |
| **Route 540** | `+4.1 min (248.4s)` | `+8.0 min (481s)` | 5 | `60.0%` |
| **Route 46** | `+4.1 min (247.2s)` | `+11.5 min (692s)` | 6 | `66.67%` |
| **Route 65** | `+4.1 min (246.2s)` | `+24.8 min (1486s)` | 6 | `83.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 860** | ~15.0m | ~27.4m | **`+6.22 min`** | `0.0 / 100` |
| **Route 71** | ~15.0m | ~22.8m | **`+5.96 min`** | `0.0 / 100` |
| **Route 36** | ~15.0m | ~19.0m | **`+4.7 min`** | `6.0 / 100` |
| **Route 65** | ~15.0m | ~19.1m | **`+4.62 min`** | `7.6 / 100` |
| **Route 768** | ~15.0m | ~19.9m | **`+3.53 min`** | `29.3 / 100` |
| **Route 850** | ~15.0m | ~17.9m | **`+3.4 min`** | `32.1 / 100` |
| **Route 615** | ~15.0m | ~21.2m | **`+3.24 min`** | `35.2 / 100` |
| **Route 467** | ~15.0m | ~18.4m | **`+3.21 min`** | `35.7 / 100` |
| **Route 763** | ~15.0m | ~20.6m | **`+2.83 min`** | `43.5 / 100` |
| **Route 904** | ~15.0m | ~19.2m | **`+2.75 min`** | `45.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1324976` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324998` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325186` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325924` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326050` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326221` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326592` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 20:46:08` | `17.07%` | `80.61%` | 1113 | 923 | `+111.2s` |
| `2026-09-14 16:59:54` | `19.2%` | `86.8%` | 901 | 728 | `+60.5s` |
| `2026-09-14 11:14:14` | `20.62%` | `92.93%` | 873 | 693 | `+40.3s` |
| `2026-09-14 05:33:56` | `2.25%` | `80.46%` | 89 | 87 | `+102.8s` |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:41:28` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T20:46:08.479584+00:00`.*
