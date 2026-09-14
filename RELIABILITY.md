# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-09-14T05:33:56.193205+00:00`

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.46%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `89` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `87` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+102.8s` (`1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+40.0s` (`0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 70 | 78.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 6.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 11 | 12.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 2.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 22** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-52.0s` |
| **Route 10** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.5m` |
| **Route 11** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.9m` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-17.0s` |
| **Route 17** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.2m` |
| **Route 18** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+1.1m` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1m` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+1.6m` |
| **Route 323** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.3m` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9** | `+8.5 min (510.0s)` | `+8.5 min (510s)` | 1 | `0.0%` |
| **Route 38** | `+8.0 min (482.0s)` | `+8.0 min (482s)` | 1 | `0.0%` |
| **Route 64** | `+5.8 min (346.0s)` | `+7.4 min (443s)` | 3 | `33.33%` |
| **Route 724** | `+5.5 min (333.0s)` | `+11.1 min (666s)` | 2 | `50.0%` |
| **Route 922** | `+4.4 min (263.8s)` | `+12.2 min (731s)` | 4 | `66.67%` |
| **Route 36** | `+4.3 min (261.0s)` | `+7.4 min (446s)` | 2 | `50.0%` |
| **Route 323** | `+4.3 min (257.7s)` | `+5.4 min (325s)` | 3 | `66.67%` |
| **Route 11** | `+2.9 min (173.7s)` | `+7.1 min (425s)` | 3 | `66.67%` |
| **Route 54** | `+2.4 min (141.5s)` | `+3.4 min (203s)` | 2 | `100.0%` |
| **Route 925** | `+2.2 min (130.0s)` | `+6.5 min (393s)` | 4 | `75.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 724** | ~15.0m | ~20.6m | **`+2.77 min`** | `44.5 / 100` |
| **Route 922** | ~15.0m | ~19.4m | **`+2.53 min`** | `49.5 / 100` |
| **Route 36** | ~15.0m | ~19.4m | **`+1.54 min`** | `69.2 / 100` |
| **Route 11** | ~15.0m | ~17.9m | **`+1.52 min`** | `69.7 / 100` |
| **Route 925** | ~15.0m | ~17.2m | **`+1.34 min`** | `73.3 / 100` |
| **Route 14** | ~15.0m | ~14.7m | **`+1.32 min`** | `73.7 / 100` |
| **Route 3** | ~15.0m | ~16.6m | **`+1.22 min`** | `75.6 / 100` |
| **Route 10** | ~15.0m | ~16.5m | **`+1.07 min`** | `78.6 / 100` |
| **Route 5** | ~15.0m | ~16.5m | **`+1.03 min`** | `79.4 / 100` |
| **Route 2** | ~15.0m | ~16.1m | **`+0.86 min`** | `82.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1351591` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351604` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-14 05:33:56` | `2.25%` | `80.46%` | 89 | 87 | `+102.8s` |
| `2026-09-14 01:09:20` | `14.1%` | `66.41%` | 454 | 390 | `+284.0s` |
| `2026-09-14 00:42:36` | `13.63%` | `73.3%` | 477 | 412 | `+242.2s` |
| `2026-09-14 00:41:35` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:41:28` | `14.01%` | `72.03%` | 471 | 405 | `+275.1s` |
| `2026-09-14 00:36:50` | `13.36%` | `73.73%` | 479 | 414 | `+257.4s` |
| `2026-09-14 00:36:42` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |
| `2026-09-14 00:36:37` | `13.36%` | `73.73%` | 479 | 415 | `+257.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-14T05:33:56.193205+00:00`.*
