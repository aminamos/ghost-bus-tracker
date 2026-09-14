# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-14T00:42:36.543175+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.3%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `477` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `412` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `65` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+242.2s` (`4.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+33.5s` (`0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 302 | 63.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 1.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 69 | 14.5% |
| 🔴 **Severe Delay** | Over 15m late | 34 | 7.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 65 | 13.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 13 | 5 | 8 | **`61.54%`** | `60.0%` | `+4.0m` |
| **Route 921** | 20 | 10 | 10 | **`50.0%`** | `100.0%` | `+0.0m` |
| **Route 540** | 7 | 4 | 3 | **`42.86%`** | `75.0%` | `+2.3m` |
| **Route 18** | 24 | 16 | 8 | **`33.33%`** | `62.5%` | `+5.1m` |
| **Route 64** | 12 | 8 | 4 | **`33.33%`** | `87.5%` | `+1.9m` |
| **Route 922** | 26 | 18 | 8 | **`30.77%`** | `64.71%` | `+3.1m` |
| **Route 36** | 8 | 6 | 2 | **`25.0%`** | `100.0%` | `+0.6m` |
| **Route 534** | 8 | 6 | 2 | **`25.0%`** | `100.0%` | `+0.4m` |
| **Route 9** | 8 | 6 | 2 | **`25.0%`** | `16.67%` | `+10.4m` |
| **Route 61** | 4 | 3 | 1 | **`25.0%`** | `66.67%` | `+18.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+22.5 min (1351.0s)` | `+30.5 min (1831s)` | 2 | `0.0%` |
| **Route 61** | `+18.6 min (1115.7s)` | `+52.0 min (3121s)` | 3 | `66.67%` |
| **Route 14** | `+12.4 min (742.9s)` | `+34.7 min (2084s)` | 12 | `41.67%` |
| **Route 94** | `+11.9 min (711.2s)` | `+30.9 min (1851s)` | 8 | `37.5%` |
| **Route 9** | `+10.4 min (625.3s)` | `+21.6 min (1299s)` | 6 | `16.67%` |
| **Route 924** | `+10.0 min (599.0s)` | `+35.2 min (2113s)` | 21 | `47.62%` |
| **Route 3** | `+9.8 min (586.7s)` | `+24.3 min (1457s)` | 9 | `55.56%` |
| **Route 22** | `+8.2 min (493.1s)` | `+41.9 min (2514s)` | 14 | `53.85%` |
| **Route 923** | `+7.7 min (464.7s)` | `+23.3 min (1397s)` | 14 | `50.0%` |
| **Route 2** | `+7.7 min (460.3s)` | `+30.7 min (1844s)` | 7 | `57.14%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 61** | ~15.0m | ~33.6m | **`+11.84 min`** | `0.0 / 100` |
| **Route 14** | ~15.0m | ~27.4m | **`+6.13 min`** | `0.0 / 100` |
| **Route 22** | ~15.0m | ~23.2m | **`+6.09 min`** | `0.0 / 100` |
| **Route 924** | ~15.0m | ~25.0m | **`+5.39 min`** | `0.0 / 100` |
| **Route 3** | ~15.0m | ~24.8m | **`+5.27 min`** | `0.0 / 100` |
| **Route 2** | ~15.0m | ~22.7m | **`+5.26 min`** | `0.0 / 100` |
| **Route 94** | ~15.0m | ~26.9m | **`+4.95 min`** | `0.9 / 100` |
| **Route 7** | ~15.0m | ~21.6m | **`+4.85 min`** | `3.0 / 100` |
| **Route 645** | ~15.0m | ~37.5m | **`+4.0 min`** | `20.0 / 100` |
| **Route 923** | ~15.0m | ~22.7m | **`+3.85 min`** | `23.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1318499` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318987` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319247` | Route 11 | `N/A` | `CANCELED` | Scheduled trip marked CANCELED by agency |
| `1320057` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348882` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349363` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351187` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352622` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331237` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332555` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349603` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349662` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350055` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350082` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350414` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:41:28` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:36:50` | `13.36%` | `73.73%` | 479 | 414 | `+257.4s` |
| `2026-09-14 00:36:42` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |
| `2026-09-14 00:36:37` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |
| `2026-09-14 00:35:23` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:35:12` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T00:42:36.543175+00:00`.*
