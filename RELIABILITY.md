# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-16T07:00:19.136000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`69.57%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `46` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+96.6s` (`+1.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+52.5s` (`+0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 32 | 69.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 19.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 8.7% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-29.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-10.7s` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.6 min` |
| **Route 22** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+14.3 min` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+3.3 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-330.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-182.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | `+14.3 min (+861.0s)` | `+43.1 min (+2586s)` | 3 | `66.67%` |
| **Route 36** | `+4.5 min (+271.0s)` | `+4.5 min (+271s)` | 1 | `100.0%` |
| **Route 18** | `+3.6 min (+214.7s)` | `+5.4 min (+322s)` | 3 | `66.67%` |
| **Route 3** | `+3.3 min (+199.5s)` | `+9.4 min (+563s)` | 4 | `75.0%` |
| **Route 923** | `+2.7 min (+164.0s)` | `+5.4 min (+322s)` | 3 | `66.67%` |
| **Route 68** | `+2.7 min (+160.0s)` | `+2.7 min (+160s)` | 1 | `100.0%` |
| **Route 64** | `+1.7 min (+104.5s)` | `+3.0 min (+179s)` | 1 | `100.0%` |
| **Route 10** | `+1.5 min (+90.0s)` | `+1.7 min (+100s)` | 2 | `100.0%` |
| **Route 924** | `+1.5 min (+88.5s)` | `+10.0 min (+601s)` | 4 | `50.0%` |
| **Route 62** | `+1.4 min (+86.5s)` | `+1.6 min (+98s)` | 1 | `100.0%` |

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
| `2026-11-16 07:00:19` | `0.0%` | `69.57%` | 46 | 46 | `+96.6s` |
| `2026-11-16 06:00:18` | `1.38%` | `67.86%` | 145 | 140 | `+48.8s` |
| `2026-11-16 05:30:18` | `3.8%` | `67.24%` | 184 | 174 | `+71.3s` |
| `2026-11-16 05:00:18` | `5.51%` | `70.0%` | 236 | 220 | `+54.7s` |
| `2026-11-16 04:30:18` | `5.11%` | `70.31%` | 274 | 256 | `+49.9s` |
| `2026-11-16 04:00:18` | `7.07%` | `73.87%` | 311 | 287 | `+58.8s` |
| `2026-11-16 03:30:18` | `8.71%` | `74.92%` | 333 | 304 | `+58.0s` |
| `2026-11-16 02:30:18` | `8.21%` | `74.79%` | 390 | 357 | `+75.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:19.136000+00:00`.*
