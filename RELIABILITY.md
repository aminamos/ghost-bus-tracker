# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-14T01:09:20.106229+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.1%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.41%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `454` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `390` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `64` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+284.0s` (`4.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+57.0s` (`0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 259 | 57.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 14 | 3.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 79 | 17.4% |
| 🔴 **Severe Delay** | Over 15m late | 38 | 8.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 64 | 14.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 14 | 7 | 7 | **`50.0%`** | `42.86%` | `+6.6m` |
| **Route 921** | 22 | 12 | 10 | **`45.45%`** | `91.67%` | `+1.1m` |
| **Route 64** | 12 | 8 | 4 | **`33.33%`** | `87.5%` | `+2.2m` |
| **Route 540** | 6 | 4 | 2 | **`33.33%`** | `75.0%` | `+3.4m` |
| **Route 922** | 25 | 17 | 8 | **`32.0%`** | `76.47%` | `+3.1m` |
| **Route 18** | 27 | 19 | 8 | **`29.63%`** | `57.89%` | `+7.2m` |
| **Route 534** | 7 | 5 | 2 | **`28.57%`** | `80.0%` | `+1.2m` |
| **Route 3** | 11 | 8 | 3 | **`27.27%`** | `50.0%` | `+13.0m` |
| **Route 36** | 8 | 6 | 2 | **`25.0%`** | `100.0%` | `+1.3m` |
| **Route 9** | 8 | 6 | 2 | **`25.0%`** | `33.33%` | `+11.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+22.4 min (1344.0s)` | `+22.4 min (1344s)` | 1 | `0.0%` |
| **Route 22** | `+17.8 min (1067.2s)` | `+44.8 min (2689s)` | 13 | `15.38%` |
| **Route 14** | `+13.4 min (802.0s)` | `+32.2 min (1932s)` | 12 | `25.0%` |
| **Route 3** | `+13.0 min (778.2s)` | `+39.0 min (2343s)` | 8 | `50.0%` |
| **Route 9** | `+11.8 min (705.7s)` | `+33.2 min (1992s)` | 6 | `33.33%` |
| **Route 924** | `+9.9 min (594.5s)` | `+32.1 min (1925s)` | 21 | `38.1%` |
| **Route 7** | `+9.1 min (543.6s)` | `+34.5 min (2073s)` | 7 | `57.14%` |
| **Route 923** | `+8.9 min (533.0s)` | `+32.7 min (1964s)` | 16 | `43.75%` |
| **Route 2** | `+8.9 min (532.5s)` | `+38.1 min (2284s)` | 8 | `50.0%` |
| **Route 18** | `+7.2 min (430.8s)` | `+26.8 min (1607s)` | 19 | `57.89%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | ~15.0m | ~32.8m | **`+7.46 min`** | `0.0 / 100` |
| **Route 3** | ~15.0m | ~28.0m | **`+7.15 min`** | `0.0 / 100` |
| **Route 2** | ~15.0m | ~23.9m | **`+5.96 min`** | `0.0 / 100` |
| **Route 7** | ~15.0m | ~24.1m | **`+5.95 min`** | `0.0 / 100` |
| **Route 9** | ~15.0m | ~26.8m | **`+5.71 min`** | `0.0 / 100` |
| **Route 14** | ~15.0m | ~28.4m | **`+4.93 min`** | `1.4 / 100` |
| **Route 924** | ~15.0m | ~24.9m | **`+4.81 min`** | `3.8 / 100` |
| **Route 923** | ~15.0m | ~23.9m | **`+4.51 min`** | `9.8 / 100` |
| **Route 18** | ~15.0m | ~22.2m | **`+4.43 min`** | `11.4 / 100` |
| **Route 5** | ~15.0m | ~21.0m | **`+4.2 min`** | `16.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1318039` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318499` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318987` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319247` | Route 11 | `N/A` | `CANCELED` | Scheduled trip marked CANCELED by agency |
| `1348882` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350458` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351187` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332555` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332641` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349612` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349698` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349866` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350396` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350414` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350502` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:41:28` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:36:50` | `13.36%` | `73.73%` | 479 | 414 | `+257.4s` |
| `2026-09-14 00:36:42` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |
| `2026-09-14 00:36:37` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |
| `2026-09-14 00:35:23` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T01:09:20.106229+00:00`.*
