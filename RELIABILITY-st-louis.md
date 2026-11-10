# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-10T07:00:18.731000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`76.92%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `42` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `28` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+69.2s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+90.0s` (`+1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 20 | 47.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 11.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 33.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+7.5 min` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-90.0s` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19792** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.0s` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19768** | `+7.5 min (+450.0s)` | `+10.0 min (+600s)` | 2 | `50.0%` |
| **Route 19779** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19759** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19754** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19749** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19785** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |
| **Route 19781** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19793** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19778** | `+1.0 min (+60.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `60.0 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `81.8 / 100` |
| **Route 19750** | ~26.0m | ~26.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 19785** | ~15.0m | ~15.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:18` | `0.0%` | `76.92%` | 42 | 28 | `+69.2s` |
| `2026-11-10 06:30:19` | `0.0%` | `74.42%` | 70 | 55 | `+74.0s` |
| `2026-11-10 06:00:18` | `0.0%` | `75.93%` | 85 | 70 | `+85.6s` |
| `2026-11-10 05:30:21` | `0.0%` | `73.77%` | 79 | 76 | `+82.6s` |
| `2026-11-10 05:00:19` | `0.0%` | `79.71%` | 84 | 79 | `+74.8s` |
| `2026-11-10 04:30:20` | `0.0%` | `77.14%` | 86 | 81 | `+114.9s` |
| `2026-11-10 04:00:19` | `0.0%` | `79.17%` | 96 | 88 | `+121.7s` |
| `2026-11-10 03:30:18` | `0.0%` | `70.42%` | 93 | 85 | `+153.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:18.731000+00:00`.*
