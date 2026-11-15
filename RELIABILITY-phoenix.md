# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-15T07:00:19.697000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `292` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+293.9s` (`+4.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+159.5s` (`+2.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 55.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 15.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 14 | 23.3% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 6.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 35** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+14.2 min` |
| **Route 7** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+6.7 min` |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+0.2 min` |
| **Route 90** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+51.9 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.4 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.4 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.0 min` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+4.1 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 90** | `+51.9 min (+3112.0s)` | `+54.8 min (+3290s)` | 2 | `0.0%` |
| **Route 41** | `+14.2 min (+854.5s)` | `+24.4 min (+1467s)` | 2 | `50.0%` |
| **Route 138** | `+12.4 min (+745.0s)` | `+12.4 min (+745s)` | 1 | `0.0%` |
| **Route 7** | `+6.7 min (+404.5s)` | `+8.8 min (+531s)` | 3 | `50.0%` |
| **Route 154** | `+6.0 min (+357.0s)` | `+6.0 min (+357s)` | 1 | `0.0%` |
| **Route 8** | `+5.7 min (+343.0s)` | `+5.7 min (+343s)` | 2 | `0.0%` |
| **Route 0** | `+5.5 min (+331.0s)` | `+6.7 min (+402s)` | 3 | `50.0%` |
| **Route 17** | `+5.1 min (+304.7s)` | `+6.8 min (+408s)` | 3 | `33.33%` |
| **Route 70** | `+5.1 min (+304.0s)` | `+5.1 min (+304s)` | 1 | `0.0%` |
| **Route 51** | `+5.0 min (+300.0s)` | `+7.4 min (+445s)` | 2 | `50.0%` |

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
| `2026-11-15 07:00:19` | `0.0%` | `55.0%` | 60 | 292 | `+293.9s` |
| `2026-11-15 06:30:19` | `0.0%` | `68.18%` | 154 | 320 | `+208.2s` |
| `2026-11-15 06:00:32` | `3.73%` | `77.16%` | 241 | 353 | `+197.2s` |
| `2026-11-15 05:30:19` | `2.67%` | `68.84%` | 300 | 354 | `+235.0s` |
| `2026-11-15 05:00:22` | `2.37%` | `73.86%` | 337 | 377 | `+218.5s` |
| `2026-11-15 04:30:19` | `4.85%` | `70.82%` | 371 | 377 | `+205.5s` |
| `2026-11-15 04:00:19` | `2.31%` | `72.18%` | 390 | 397 | `+226.1s` |
| `2026-11-15 03:30:20` | `3.92%` | `76.79%` | 408 | 416 | `+222.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.697000+00:00`.*
