# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-14T07:00:19.465000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.89%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `37` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `23` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+88.4s` (`+1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 29.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 10.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 10.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 37.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+2.5 min` |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-240.0s` |
| **Route 19792** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19780** | `+12.0 min (+720.0s)` | `+12.0 min (+720s)` | 1 | `0.0%` |
| **Route 19775** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 1 | `0.0%` |
| **Route 19777** | `+7.0 min (+420.0s)` | `+7.0 min (+420s)` | 1 | `0.0%` |
| **Route 19749** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19778** | `+2.5 min (+150.0s)` | `+7.0 min (+420s)` | 2 | `0.0%` |
| **Route 19784** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19787** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19782** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19793** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `10.0 / 100` |
| **Route 19785** | ~15.0m | ~15.0m | **`+0.0 min`** | `90.0 / 100` |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `0.0%` | `57.89%` | 37 | 23 | `+88.4s` |
| `2026-11-14 06:30:22` | `0.0%` | `74.42%` | 68 | 54 | `+20.9s` |
| `2026-11-14 06:00:21` | `83.53%` | `0.0%` | 85 | 0 | `+0.0s` |
| `2026-11-14 05:30:19` | `0.0%` | `74.58%` | 90 | 73 | `+85.4s` |
| `2026-11-14 05:00:28` | `0.0%` | `62.5%` | 89 | 82 | `+86.2s` |
| `2026-11-14 04:30:18` | `0.0%` | `74.24%` | 89 | 80 | `+85.5s` |
| `2026-11-14 04:00:23` | `0.0%` | `76.92%` | 88 | 88 | `+91.5s` |
| `2026-11-14 03:30:18` | `0.0%` | `67.61%` | 97 | 88 | `+101.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.465000+00:00`.*
