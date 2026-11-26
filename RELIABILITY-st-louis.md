# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-26T07:00:24.667000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`51.61%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `55` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `33` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+371.6s` (`+6.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+240.0s` (`+4.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 29.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 7.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 14.5% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 5.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 22 | 40.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.5 min` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-150.0s` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19792** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+8.5 min` |
| **Route 19800** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+8.5 min` |
| **Route 19775** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+24.0 min` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.5 min` |
| **Route UNKNOWN** | 22 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19785** | `+28.0 min (+1680.0s)` | `+28.0 min (+1680s)` | 1 | `0.0%` |
| **Route 19775** | `+24.0 min (+1440.0s)` | `+45.0 min (+2700s)` | 2 | `50.0%` |
| **Route 19783** | `+23.0 min (+1380.0s)` | `+23.0 min (+1380s)` | 1 | `0.0%` |
| **Route 19759** | `+11.0 min (+660.0s)` | `+11.0 min (+660s)` | 1 | `0.0%` |
| **Route 19792** | `+8.5 min (+510.0s)` | `+10.0 min (+600s)` | 3 | `0.0%` |
| **Route 19800** | `+8.5 min (+510.0s)` | `+9.0 min (+540s)` | 2 | `0.0%` |
| **Route 19784** | `+7.0 min (+420.0s)` | `+7.0 min (+420s)` | 1 | `0.0%` |
| **Route 19778** | `+6.5 min (+390.0s)` | `+11.0 min (+660s)` | 2 | `50.0%` |
| **Route 19757** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19755** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `10.0 / 100` |
| **Route 19775** | ~1380.0m | ~1380.0m | **`+0.0 min`** | `98.5 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `86.4 / 100` |
| **Route 19792** | ~17.5m | ~17.5m | **`+0.0 min`** | `91.4 / 100` |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `92.9 / 100` |
| **Route 19800** | ~10.0m | ~10.0m | **`+0.0 min`** | `95.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:24` | `0.0%` | `51.61%` | 55 | 33 | `+371.6s` |
| `2026-11-26 06:30:20` | `0.0%` | `60.0%` | 91 | 68 | `+373.0s` |
| `2026-11-26 06:00:18` | `0.0%` | `60.32%` | 94 | 72 | `+387.6s` |
| `2026-11-26 05:30:25` | `0.0%` | `60.27%` | 91 | 81 | `+443.8s` |
| `2026-11-26 05:00:18` | `0.0%` | `57.33%` | 91 | 83 | `+372.0s` |
| `2026-11-26 04:30:21` | `0.0%` | `57.89%` | 93 | 85 | `+397.9s` |
| `2026-11-26 04:00:20` | `0.0%` | `64.37%` | 105 | 94 | `+317.2s` |
| `2026-11-26 03:30:20` | `0.0%` | `54.55%` | 102 | 94 | `+382.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:24.667000+00:00`.*
