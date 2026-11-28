# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-28T07:00:20.515000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `346` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+164.3s` (`+2.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+35.5s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 42 | 70.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 15.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 13.3% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `-184.3s` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+1.0 min` |
| **Route 16** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+24.5 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+4.2 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+8.5 min` |
| **Route 41** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.5 min` |
| **Route 70** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `-34.5s` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-5.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 27** | `+24.5 min (+1471.0s)` | `+89.6 min (+5378s)` | 4 | `50.0%` |
| **Route 51** | `+8.5 min (+507.5s)` | `+9.0 min (+541s)` | 2 | `0.0%` |
| **Route 16** | `+6.0 min (+357.5s)` | `+11.7 min (+699s)` | 3 | `50.0%` |
| **Route 77** | `+5.0 min (+303.0s)` | `+5.0 min (+303s)` | 1 | `0.0%` |
| **Route 3** | `+4.2 min (+252.3s)` | `+4.8 min (+291s)` | 3 | `100.0%` |
| **Route 17** | `+3.5 min (+211.5s)` | `+4.2 min (+250s)` | 2 | `100.0%` |
| **Route 61** | `+2.9 min (+172.0s)` | `+2.9 min (+172s)` | 1 | `100.0%` |
| **Route 44** | `+2.1 min (+124.0s)` | `+2.1 min (+124s)` | 1 | `100.0%` |
| **Route 7** | `+1.9 min (+114.0s)` | `+4.8 min (+287s)` | 4 | `100.0%` |
| **Route B** | `+1.8 min (+110.0s)` | `+7.0 min (+420s)` | 6 | `50.0%` |

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
| `2026-11-28 07:00:20` | `0.0%` | `70.0%` | 60 | 346 | `+164.3s` |
| `2026-11-28 06:30:18` | `0.63%` | `76.58%` | 159 | 373 | `+165.8s` |
| `2026-11-28 06:00:19` | `3.35%` | `77.52%` | 269 | 399 | `+146.6s` |
| `2026-11-28 05:30:20` | `5.05%` | `76.25%` | 317 | 419 | `+160.4s` |
| `2026-11-28 05:00:20` | `4.41%` | `78.39%` | 363 | 447 | `+170.0s` |
| `2026-11-28 04:30:18` | `4.31%` | `81.43%` | 394 | 464 | `+174.3s` |
| `2026-11-28 04:00:20` | `3.76%` | `80.49%` | 426 | 504 | `+135.5s` |
| `2026-11-28 03:30:20` | `4.05%` | `81.18%` | 444 | 553 | `+131.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:20.515000+00:00`.*
