# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-24T07:00:18.298000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.96%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `54` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+26.4s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-5.5s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 63.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 17 | 31.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.7% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-108.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+0.2 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.2 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.0 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-335.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-13.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+13.4 min (+802.0s)` | `+13.4 min (+802s)` | 1 | `0.0%` |
| **Route 922** | `+11.1 min (+664.0s)` | `+33.9 min (+2031s)` | 3 | `33.33%` |
| **Route 18** | `+3.2 min (+193.0s)` | `+5.0 min (+302s)` | 2 | `50.0%` |
| **Route 923** | `+2.5 min (+152.7s)` | `+4.8 min (+291s)` | 2 | `100.0%` |
| **Route 921** | `+1.8 min (+107.5s)` | `+3.2 min (+190s)` | 2 | `100.0%` |
| **Route 2** | `+1.5 min (+92.5s)` | `+1.9 min (+117s)` | 2 | `100.0%` |
| **Route 11** | `+1.4 min (+84.0s)` | `+2.1 min (+128s)` | 2 | `100.0%` |
| **Route 925** | `+1.3 min (+80.5s)` | `+1.5 min (+89s)` | 2 | `100.0%` |
| **Route 22** | `+0.5 min (+30.5s)` | `+0.6 min (+37s)` | 2 | `100.0%` |
| **Route 17** | `+0.2 min (+12.0s)` | `+1.9 min (+116s)` | 3 | `66.67%` |

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
| `2026-11-24 07:00:18` | `0.0%` | `62.96%` | 54 | 54 | `+26.4s` |
| `2026-11-24 05:30:17` | `4.29%` | `59.2%` | 210 | 201 | `+12.1s` |
| `2026-11-24 05:00:18` | `4.98%` | `56.5%` | 281 | 246 | `-7.0s` |
| `2026-11-24 04:30:18` | `5.25%` | `61.51%` | 343 | 304 | `-1.2s` |
| `2026-11-24 04:00:18` | `6.36%` | `61.67%` | 393 | 347 | `+7.3s` |
| `2026-11-24 03:00:18` | `7.79%` | `64.66%` | 475 | 416 | `+0.2s` |
| `2026-11-24 02:30:18` | `8.11%` | `66.45%` | 518 | 453 | `+8.3s` |
| `2026-11-24 02:00:19` | `7.89%` | `64.26%` | 570 | 498 | `+10.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:18.298000+00:00`.*
