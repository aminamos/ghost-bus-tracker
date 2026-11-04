# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T07:00:22.861000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.68%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `374` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+138.5s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+42.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 42 | 73.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 19.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.5% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+1.5 min` |
| **Route 35** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.4 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+13.1 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-2.0s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.3 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-23.5s` |
| **Route 50** | 2 | 4 | 0 | **`0.0%`** | `100.0%` | `-34.5s` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 170** | `+43.7 min (+2621.0s)` | `+43.7 min (+2621s)` | 1 | `0.0%` |
| **Route 3** | `+13.1 min (+785.0s)` | `+34.0 min (+2042s)` | 3 | `66.67%` |
| **Route S** | `+4.5 min (+270.0s)` | `+14.0 min (+840s)` | 2 | `0.0%` |
| **Route 17** | `+4.3 min (+259.0s)` | `+4.8 min (+285s)` | 2 | `100.0%` |
| **Route 138** | `+3.2 min (+194.0s)` | `+3.2 min (+194s)` | 1 | `100.0%` |
| **Route 7** | `+2.4 min (+146.3s)` | `+4.9 min (+294s)` | 3 | `66.67%` |
| **Route 32** | `+2.4 min (+141.0s)` | `+2.4 min (+141s)` | 1 | `100.0%` |
| **Route 51** | `+2.0 min (+118.0s)` | `+2.0 min (+118s)` | 2 | `100.0%` |
| **Route 27** | `+1.9 min (+116.7s)` | `+4.0 min (+243s)` | 3 | `100.0%` |
| **Route 0** | `+1.9 min (+116.5s)` | `+4.7 min (+281s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:22` | `0.0%` | `73.68%` | 57 | 374 | `+138.5s` |
| `2026-11-04 06:30:32` | `0.65%` | `73.86%` | 154 | 415 | `+136.2s` |
| `2026-11-04 06:00:19` | `3.76%` | `78.12%` | 266 | 437 | `+190.7s` |
| `2026-11-04 05:30:18` | `4.92%` | `78.62%` | 305 | 455 | `+178.9s` |
| `2026-11-04 05:00:19` | `3.63%` | `76.81%` | 358 | 489 | `+186.6s` |
| `2026-11-04 04:30:18` | `3.8%` | `76.05%` | 395 | 497 | `+197.0s` |
| `2026-11-04 04:00:26` | `4.44%` | `77.52%` | 405 | 549 | `+194.9s` |
| `2026-11-04 03:30:21` | `3.42%` | `76.89%` | 439 | 589 | `+183.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:22.861000+00:00`.*
