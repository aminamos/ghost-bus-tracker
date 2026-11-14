# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-14T07:00:18.316000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.93%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `56` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `56` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+62.3s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+14.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 58.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 16 | 28.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 10.7% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-10.0s` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-40.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.4 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.1 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-85.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+1.2 min` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.0 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-26.3s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 2** | `+5.1 min (+307.7s)` | `+15.6 min (+935s)` | 3 | `66.67%` |
| **Route 36** | `+4.0 min (+241.0s)` | `+8.6 min (+516s)` | 2 | `50.0%` |
| **Route 925** | `+3.6 min (+218.5s)` | `+6.1 min (+364s)` | 2 | `50.0%` |
| **Route 922** | `+2.5 min (+151.0s)` | `+5.2 min (+312s)` | 4 | `75.0%` |
| **Route 17** | `+2.4 min (+144.0s)` | `+8.0 min (+481s)` | 3 | `66.67%` |
| **Route 62** | `+2.1 min (+128.0s)` | `+4.9 min (+292s)` | 1 | `100.0%` |
| **Route 61** | `+2.0 min (+119.0s)` | `+2.0 min (+119s)` | 1 | `100.0%` |
| **Route 63** | `+1.9 min (+113.0s)` | `+5.2 min (+314s)` | 2 | `0.0%` |
| **Route 3** | `+1.2 min (+75.0s)` | `+6.0 min (+357s)` | 5 | `40.0%` |
| **Route 923** | `+1.1 min (+65.0s)` | `+3.8 min (+225s)` | 2 | `100.0%` |

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
| `2026-11-14 07:00:18` | `0.0%` | `58.93%` | 56 | 56 | `+62.3s` |
| `2026-11-14 05:30:18` | `4.13%` | `62.98%` | 218 | 208 | `+39.8s` |
| `2026-11-14 05:00:19` | `4.91%` | `61.2%` | 285 | 250 | `+26.0s` |
| `2026-11-14 04:30:18` | `5.07%` | `59.37%` | 355 | 315 | `+33.7s` |
| `2026-11-14 04:00:19` | `5.79%` | `61.36%` | 397 | 352 | `+29.3s` |
| `2026-11-14 03:30:18` | `7.16%` | `57.36%` | 447 | 394 | `+29.4s` |
| `2026-11-14 03:00:18` | `7.53%` | `66.82%` | 478 | 422 | `+26.7s` |
| `2026-11-14 02:00:19` | `7.42%` | `64.21%` | 566 | 503 | `+41.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:18.316000+00:00`.*
