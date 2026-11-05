# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-05T07:00:18.743000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.14%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `49` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `342` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+292.4s` (`+4.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+98.0s` (`+1.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 28 | 57.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 18.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 10 | 20.4% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 4.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 5 | 6 | 0 | **`0.0%`** | `60.0%` | `+3.2 min` |
| **Route 35** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `-69.5s` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-9.5s` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+24.6 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.2 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.2 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+3.7 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.2 min` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 29** | `+28.8 min (+1729.0s)` | `+56.0 min (+3363s)` | 2 | `50.0%` |
| **Route 27** | `+24.6 min (+1475.2s)` | `+76.6 min (+4598s)` | 4 | `25.0%` |
| **Route 51** | `+11.2 min (+672.0s)` | `+11.2 min (+672s)` | 1 | `0.0%` |
| **Route FBUZ** | `+7.5 min (+449.0s)` | `+7.5 min (+449s)` | 1 | `0.0%` |
| **Route 41** | `+5.2 min (+311.5s)` | `+5.7 min (+341s)` | 2 | `50.0%` |
| **Route 43** | `+4.8 min (+288.0s)` | `+4.8 min (+288s)` | 1 | `100.0%` |
| **Route 50** | `+4.2 min (+250.0s)` | `+5.9 min (+355s)` | 2 | `50.0%` |
| **Route 70** | `+3.7 min (+220.0s)` | `+8.7 min (+522s)` | 2 | `0.0%` |
| **Route 7** | `+3.4 min (+206.2s)` | `+6.4 min (+382s)` | 4 | `75.0%` |
| **Route 17** | `+3.2 min (+192.0s)` | `+4.4 min (+262s)` | 2 | `100.0%` |

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
| `2026-11-05 07:00:18` | `0.0%` | `57.14%` | 49 | 342 | `+292.4s` |
| `2026-11-05 06:30:19` | `0.0%` | `67.35%` | 147 | 388 | `+169.5s` |
| `2026-11-05 06:00:18` | `3.77%` | `76.47%` | 265 | 425 | `+163.5s` |
| `2026-11-05 05:30:19` | `2.88%` | `75.0%` | 313 | 461 | `+213.3s` |
| `2026-11-05 05:00:21` | `4.4%` | `72.99%` | 364 | 494 | `+206.6s` |
| `2026-11-05 04:30:19` | `2.98%` | `72.12%` | 403 | 523 | `+215.7s` |
| `2026-11-05 04:00:20` | `3.54%` | `70.66%` | 424 | 588 | `+201.0s` |
| `2026-11-05 03:30:19` | `3.82%` | `70.56%` | 445 | 607 | `+227.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.743000+00:00`.*
