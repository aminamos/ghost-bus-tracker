# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-02T07:00:18.034000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.45%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `44` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+142.8s` (`+2.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+102.5s` (`+1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 31 | 70.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 13.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 13.6% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 18** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+8.2 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-23.5s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+4.9 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `50.0%` | `-79.0s` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-18.0s` |
| **Route 64** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+12.6 min (+754.0s)` | `+12.6 min (+754s)` | 1 | `0.0%` |
| **Route 323** | `+8.7 min (+521.0s)` | `+8.7 min (+521s)` | 1 | `0.0%` |
| **Route 18** | `+8.2 min (+489.5s)` | `+30.5 min (+1830s)` | 4 | `50.0%` |
| **Route 3** | `+4.9 min (+294.5s)` | `+7.3 min (+436s)` | 4 | `50.0%` |
| **Route 923** | `+3.3 min (+198.3s)` | `+6.0 min (+358s)` | 3 | `66.67%` |
| **Route 922** | `+2.8 min (+165.5s)` | `+3.6 min (+217s)` | 2 | `100.0%` |
| **Route 925** | `+2.1 min (+128.5s)` | `+6.6 min (+397s)` | 2 | `0.0%` |
| **Route 17** | `+1.9 min (+113.7s)` | `+4.9 min (+294s)` | 3 | `100.0%` |
| **Route 64** | `+1.8 min (+106.0s)` | `+2.5 min (+147s)` | 1 | `100.0%` |
| **Route 10** | `+1.6 min (+97.0s)` | `+1.6 min (+97s)` | 1 | `100.0%` |

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
| `2026-11-02 07:00:18` | `0.0%` | `70.45%` | 44 | 44 | `+142.8s` |
| `2026-11-02 06:30:17` | `0.0%` | `73.68%` | 95 | 95 | `+59.5s` |
| `2026-11-02 06:00:19` | `3.33%` | `74.14%` | 120 | 116 | `+50.9s` |
| `2026-11-02 05:30:19` | `4.26%` | `72.0%` | 235 | 225 | `+98.5s` |
| `2026-11-02 05:00:18` | `4.24%` | `71.24%` | 236 | 226 | `+97.6s` |
| `2026-11-02 04:30:18` | `4.8%` | `76.26%` | 271 | 258 | `+94.9s` |
| `2026-11-02 04:00:18` | `6.09%` | `77.4%` | 312 | 292 | `+98.2s` |
| `2026-11-02 03:00:18` | `6.81%` | `74.27%` | 367 | 342 | `+95.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.034000+00:00`.*
