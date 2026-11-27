# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-27T07:00:20.613000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+100.5s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+81.0s` (`+1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 88.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 12.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 0 | **`0.0%`** | `85.71%` | `+1.2 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+1.9 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+2.9 min (+176.2s)` | `+9.1 min (+546s)` | 4 | `80.0%` |
| **Route 1** | `+2.6 min (+159.0s)` | `+2.6 min (+159s)` | 1 | `100.0%` |
| **Route 77** | `+1.9 min (+117.0s)` | `+6.9 min (+412s)` | 4 | `83.33%` |
| **Route 20** | `+1.2 min (+74.7s)` | `+5.9 min (+354s)` | 4 | `85.71%` |
| **Route 107** | `+0.7 min (+41.3s)` | `+2.8 min (+167s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `81.8 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `76.7 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `81.8 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `82.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:20` | `0.0%` | `88.0%` | 25 | 15 | `+100.5s` |
| `2026-11-27 06:30:20` | `0.0%` | `85.29%` | 34 | 19 | `+76.6s` |
| `2026-11-27 06:00:18` | `4.44%` | `81.4%` | 45 | 28 | `+107.7s` |
| `2026-11-27 05:30:20` | `5.88%` | `85.94%` | 68 | 46 | `+117.5s` |
| `2026-11-27 05:00:17` | `11.46%` | `85.88%` | 96 | 61 | `+114.5s` |
| `2026-11-27 04:30:21` | `9.6%` | `83.19%` | 125 | 73 | `+109.7s` |
| `2026-11-27 04:00:17` | `5.84%` | `86.21%` | 154 | 86 | `+67.4s` |
| `2026-11-27 03:30:21` | `5.52%` | `87.13%` | 181 | 100 | `+82.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:20.613000+00:00`.*
