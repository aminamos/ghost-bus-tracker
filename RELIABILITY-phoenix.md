# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-26T07:00:24.403000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `356` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+126.3s` (`+2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+35.5s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 66.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 15.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 9 | 15.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+3.9 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.4 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.6 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.8 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-39.5s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.3 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-22.0s` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.8 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 29** | `+7.2 min (+431.3s)` | `+21.0 min (+1260s)` | 3 | `66.67%` |
| **Route 27** | `+5.6 min (+336.3s)` | `+14.2 min (+851s)` | 3 | `66.67%` |
| **Route 16** | `+5.4 min (+323.0s)` | `+8.6 min (+518s)` | 2 | `50.0%` |
| **Route 43** | `+4.0 min (+238.5s)` | `+8.1 min (+486s)` | 3 | `50.0%` |
| **Route 35** | `+3.9 min (+235.2s)` | `+18.3 min (+1100s)` | 5 | `60.0%` |
| **Route 44** | `+3.8 min (+225.5s)` | `+7.0 min (+422s)` | 2 | `50.0%` |
| **Route 17** | `+3.3 min (+196.0s)` | `+5.7 min (+343s)` | 2 | `50.0%` |
| **Route 8** | `+3.3 min (+196.0s)` | `+3.3 min (+196s)` | 1 | `100.0%` |
| **Route 72** | `+3.1 min (+186.0s)` | `+3.1 min (+186s)` | 1 | `100.0%` |
| **Route 3** | `+2.8 min (+169.3s)` | `+7.5 min (+451s)` | 3 | `66.67%` |

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
| `2026-11-26 07:00:24` | `0.0%` | `66.67%` | 60 | 356 | `+126.3s` |
| `2026-11-26 06:30:20` | `0.0%` | `74.67%` | 150 | 388 | `+144.9s` |
| `2026-11-26 06:00:19` | `4.71%` | `75.67%` | 276 | 419 | `+187.9s` |
| `2026-11-26 05:30:25` | `3.06%` | `77.29%` | 327 | 456 | `+182.5s` |
| `2026-11-26 05:00:19` | `4.1%` | `78.06%` | 366 | 500 | `+137.5s` |
| `2026-11-26 04:30:21` | `4.94%` | `80.78%` | 405 | 524 | `+121.0s` |
| `2026-11-26 04:00:20` | `3.78%` | `84.52%` | 423 | 571 | `+103.2s` |
| `2026-11-26 03:30:20` | `3.82%` | `78.97%` | 445 | 613 | `+127.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:24.403000+00:00`.*
