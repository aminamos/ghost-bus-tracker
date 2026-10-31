# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-31T06:30:18.361000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.71%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `34` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `34` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+271.8s` (`+4.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+172.0s` (`+2.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 64.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 8.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 17.6% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 8.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.0 min` |
| **Route 17** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `+0.7 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.3 min` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+11.8 min` |
| **Route 4** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.8 min` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+11.8 min` |
| **Route 922** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.7 min` |
| **Route 924** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 2** | `+12.1 min (+728.0s)` | `+12.1 min (+728s)` | 1 | `0.0%` |
| **Route 63** | `+11.8 min (+711.0s)` | `+23.3 min (+1396s)` | 2 | `50.0%` |
| **Route 3** | `+11.8 min (+705.2s)` | `+24.9 min (+1495s)` | 4 | `25.0%` |
| **Route 64** | `+8.6 min (+514.0s)` | `+8.6 min (+514s)` | 1 | `0.0%` |
| **Route 925** | `+8.4 min (+505.5s)` | `+8.6 min (+513s)` | 2 | `0.0%` |
| **Route 14** | `+5.0 min (+300.5s)` | `+6.7 min (+400s)` | 2 | `50.0%` |
| **Route 74** | `+3.5 min (+208.0s)` | `+3.5 min (+208s)` | 1 | `100.0%` |
| **Route 18** | `+2.9 min (+172.0s)` | `+2.9 min (+172s)` | 1 | `100.0%` |
| **Route 923** | `+2.9 min (+172.0s)` | `+2.9 min (+172s)` | 1 | `100.0%` |
| **Route 4** | `+2.8 min (+166.0s)` | `+4.1 min (+248s)` | 2 | `100.0%` |

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
| `2026-10-31 06:30:18` | `0.0%` | `64.71%` | 34 | 34 | `+271.8s` |
| `2026-10-31 06:00:19` | `0.0%` | `57.89%` | 57 | 57 | `+145.5s` |
| `2026-10-31 05:30:18` | `0.0%` | `56.3%` | 120 | 119 | `+119.0s` |
| `2026-10-31 04:30:20` | `3.16%` | `61.99%` | 253 | 221 | `+78.4s` |
| `2026-10-31 04:00:17` | `3.99%` | `60.53%` | 301 | 266 | `+98.7s` |
| `2026-10-31 03:30:17` | `4.92%` | `59.38%` | 366 | 325 | `+103.2s` |
| `2026-10-31 03:00:17` | `6.31%` | `60.61%` | 412 | 363 | `+82.1s` |
| `2026-10-31 02:30:18` | `7.11%` | `62.53%` | 450 | 395 | `+55.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T06:30:18.361000+00:00`.*
