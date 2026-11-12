# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-12T07:00:18.434000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.34%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `58` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+25.8s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-12.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 35 | 60.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 19 | 32.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 6.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-6.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.3 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-47.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-8.0s` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-61.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-26.0s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-41.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-6.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.5 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-92.7s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9** | `+12.0 min (+721.0s)` | `+12.0 min (+721s)` | 1 | `0.0%` |
| **Route 54** | `+10.9 min (+654.0s)` | `+10.9 min (+654s)` | 1 | `0.0%` |
| **Route 924** | `+4.2 min (+251.5s)` | `+11.7 min (+700s)` | 4 | `75.0%` |
| **Route 36** | `+2.5 min (+148.5s)` | `+5.5 min (+333s)` | 2 | `50.0%` |
| **Route 921** | `+2.0 min (+122.0s)` | `+3.6 min (+218s)` | 2 | `100.0%` |
| **Route 925** | `+1.8 min (+109.0s)` | `+2.4 min (+144s)` | 2 | `100.0%` |
| **Route 923** | `+1.4 min (+86.0s)` | `+2.3 min (+136s)` | 2 | `100.0%` |
| **Route 922** | `+0.4 min (+25.8s)` | `+2.7 min (+164s)` | 4 | `75.0%` |
| **Route 11** | `+0.3 min (+20.5s)` | `+1.8 min (+106s)` | 2 | `50.0%` |
| **Route 515** | `+0.3 min (+20.0s)` | `+0.3 min (+20s)` | 1 | `100.0%` |

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
| `2026-11-12 07:00:18` | `0.0%` | `60.34%` | 58 | 58 | `+25.8s` |
| `2026-11-12 06:30:18` | `0.0%` | `64.22%` | 109 | 109 | `+32.7s` |
| `2026-11-12 05:30:17` | `4.41%` | `58.06%` | 227 | 217 | `+17.8s` |
| `2026-11-12 05:00:18` | `4.44%` | `58.53%` | 270 | 258 | `+15.4s` |
| `2026-11-12 04:30:18` | `5.42%` | `59.24%` | 332 | 314 | `+11.4s` |
| `2026-11-12 04:00:18` | `5.74%` | `58.45%` | 383 | 361 | `+26.7s` |
| `2026-11-12 03:30:18` | `7.11%` | `61.22%` | 422 | 391 | `+13.8s` |
| `2026-11-12 03:00:18` | `7.33%` | `60.0%` | 464 | 430 | `+25.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:18.434000+00:00`.*
