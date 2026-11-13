# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-13T07:00:27.763000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `359` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+177.4s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+41.5s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 43 | 71.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 13.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 11.7% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 5 | 0 | **`0.0%`** | `75.0%` | `+2.3 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-42.8s` |
| **Route 16** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+1.7 min` |
| **Route 27** | 3 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+3.8 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-36.5s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.9 min` |
| **Route 70** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+15.3 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route S** | `+54.0 min (+3240.0s)` | `+54.0 min (+3240s)` | 1 | `0.0%` |
| **Route 70** | `+15.3 min (+920.0s)` | `+31.5 min (+1892s)` | 3 | `50.0%` |
| **Route 75** | `+14.9 min (+892.0s)` | `+14.9 min (+892s)` | 1 | `0.0%` |
| **Route 61** | `+6.0 min (+363.0s)` | `+13.6 min (+813s)` | 2 | `0.0%` |
| **Route 51** | `+6.0 min (+359.5s)` | `+8.8 min (+531s)` | 2 | `50.0%` |
| **Route 77** | `+5.3 min (+318.0s)` | `+5.3 min (+318s)` | 1 | `0.0%` |
| **Route 8** | `+4.5 min (+271.0s)` | `+4.5 min (+271s)` | 1 | `100.0%` |
| **Route 72** | `+4.3 min (+260.0s)` | `+4.3 min (+260s)` | 1 | `100.0%` |
| **Route 3** | `+3.8 min (+227.0s)` | `+4.7 min (+282s)` | 3 | `100.0%` |
| **Route 17** | `+2.9 min (+171.0s)` | `+4.0 min (+241s)` | 2 | `100.0%` |

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
| `2026-11-13 07:00:27` | `0.0%` | `71.67%` | 60 | 359 | `+177.4s` |
| `2026-11-13 06:30:19` | `0.0%` | `75.68%` | 148 | 398 | `+186.2s` |
| `2026-11-13 06:00:32` | `2.68%` | `79.92%` | 261 | 434 | `+148.6s` |
| `2026-11-13 05:30:19` | `3.49%` | `79.54%` | 315 | 455 | `+203.5s` |
| `2026-11-13 05:00:22` | `3.36%` | `76.52%` | 357 | 490 | `+177.9s` |
| `2026-11-13 04:30:20` | `3.84%` | `75.53%` | 391 | 510 | `+203.2s` |
| `2026-11-13 04:00:21` | `4.55%` | `73.18%` | 418 | 587 | `+210.4s` |
| `2026-11-13 03:30:19` | `3.78%` | `77.83%` | 423 | 596 | `+191.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:27.763000+00:00`.*
