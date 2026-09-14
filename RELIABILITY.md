# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-14T00:41:35.799649+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.01%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.03%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `471` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `405` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `66` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+275.1s` (`4.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+21.0s` (`0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 291 | 61.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 0.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 70 | 14.9% |
| 🔴 **Severe Delay** | Over 15m late | 40 | 8.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 66 | 14.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 13 | 6 | 7 | **`53.85%`** | `66.67%` | `+4.1m` |
| **Route 921** | 22 | 11 | 11 | **`50.0%`** | `100.0%` | `+0.5m` |
| **Route 540** | 8 | 5 | 3 | **`37.5%`** | `100.0%` | `+1.4m` |
| **Route 64** | 12 | 8 | 4 | **`33.33%`** | `100.0%` | `+0.9m` |
| **Route 534** | 6 | 4 | 2 | **`33.33%`** | `100.0%` | `0.0s` |
| **Route 18** | 25 | 17 | 8 | **`32.0%`** | `64.71%` | `+5.8m` |
| **Route 922** | 26 | 18 | 8 | **`30.77%`** | `72.22%` | `+4.3m` |
| **Route 36** | 8 | 6 | 2 | **`25.0%`** | `100.0%` | `+0.6m` |
| **Route 9** | 8 | 6 | 2 | **`25.0%`** | `33.33%` | `+11.7m` |
| **Route 63** | 9 | 7 | 2 | **`22.22%`** | `71.43%` | `+2.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+19.9 min (1193.0s)` | `+19.9 min (1193s)` | 1 | `0.0%` |
| **Route 61** | `+14.6 min (878.0s)` | `+52.0 min (3121s)` | 4 | `50.0%` |
| **Route 14** | `+14.4 min (862.6s)` | `+35.5 min (2129s)` | 13 | `23.08%` |
| **Route 94** | `+13.7 min (819.6s)` | `+32.1 min (1929s)` | 7 | `28.57%` |
| **Route 9** | `+11.7 min (702.3s)` | `+29.0 min (1738s)` | 6 | `33.33%` |
| **Route 924** | `+11.4 min (685.9s)` | `+37.0 min (2217s)` | 21 | `47.62%` |
| **Route 22** | `+10.9 min (651.4s)` | `+46.1 min (2765s)` | 14 | `50.0%` |
| **Route 3** | `+10.0 min (599.8s)` | `+24.6 min (1477s)` | 8 | `62.5%` |
| **Route 923** | `+9.3 min (555.5s)` | `+27.8 min (1670s)` | 15 | `40.0%` |
| **Route 2** | `+7.6 min (455.6s)` | `+32.4 min (1946s)` | 8 | `75.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 61** | ~15.0m | ~29.6m | **`+10.87 min`** | `0.0 / 100` |
| **Route 22** | ~15.0m | ~25.9m | **`+6.79 min`** | `0.0 / 100` |
| **Route 14** | ~15.0m | ~29.4m | **`+6.08 min`** | `0.0 / 100` |
| **Route 924** | ~15.0m | ~26.4m | **`+5.73 min`** | `0.0 / 100` |
| **Route 2** | ~15.0m | ~22.6m | **`+5.35 min`** | `0.0 / 100` |
| **Route 7** | ~15.0m | ~22.5m | **`+5.35 min`** | `0.0 / 100` |
| **Route 94** | ~15.0m | ~28.7m | **`+5.12 min`** | `0.0 / 100` |
| **Route 3** | ~15.0m | ~25.0m | **`+5.04 min`** | `0.0 / 100` |
| **Route 9** | ~15.0m | ~26.7m | **`+4.94 min`** | `1.2 / 100` |
| **Route 923** | ~15.0m | ~24.3m | **`+4.25 min`** | `14.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1318499` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318987` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319247` | Route 11 | `N/A` | `CANCELED` | Scheduled trip marked CANCELED by agency |
| `1320057` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348882` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350458` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351187` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331237` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332555` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349603` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349662` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349866` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350055` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350396` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350414` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T00:41:35.799649+00:00`.*
