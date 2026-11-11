# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-11T07:00:18.243000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.16%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+31.2s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+10.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 63.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 18 | 31.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 5.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.5s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-159.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 18** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+3.2 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.4 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-83.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.3 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-201.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-8.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 64** | `+5.7 min (+341.5s)` | `+7.8 min (+465s)` | 1 | `50.0%` |
| **Route 74** | `+3.5 min (+211.0s)` | `+3.5 min (+211s)` | 1 | `100.0%` |
| **Route 925** | `+3.5 min (+208.5s)` | `+3.9 min (+233s)` | 2 | `100.0%` |
| **Route 18** | `+3.2 min (+193.8s)` | `+7.9 min (+474s)` | 4 | `75.0%` |
| **Route 922** | `+2.9 min (+171.0s)` | `+5.4 min (+324s)` | 4 | `75.0%` |
| **Route 923** | `+2.3 min (+137.3s)` | `+4.8 min (+288s)` | 2 | `100.0%` |
| **Route 921** | `+2.0 min (+121.0s)` | `+3.5 min (+211s)` | 2 | `100.0%` |
| **Route 61** | `+1.6 min (+93.0s)` | `+1.6 min (+93s)` | 1 | `100.0%` |
| **Route 2** | `+1.4 min (+84.5s)` | `+4.6 min (+274s)` | 2 | `50.0%` |
| **Route 3** | `+0.3 min (+16.2s)` | `+3.6 min (+214s)` | 5 | `60.0%` |

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
| `2026-11-11 07:00:18` | `0.0%` | `63.16%` | 57 | 57 | `+31.2s` |
| `2026-11-11 06:30:17` | `1.83%` | `52.34%` | 109 | 107 | `+2.0s` |
| `2026-11-11 05:30:18` | `5.38%` | `63.03%` | 223 | 211 | `+39.2s` |
| `2026-11-11 05:00:18` | `5.82%` | `60.62%` | 275 | 259 | `+6.3s` |
| `2026-11-11 04:30:18` | `6.88%` | `60.82%` | 349 | 319 | `+21.2s` |
| `2026-11-11 04:00:18` | `7.77%` | `63.03%` | 399 | 357 | `+21.8s` |
| `2026-11-11 03:00:19` | `8.66%` | `65.51%` | 485 | 432 | `+20.3s` |
| `2026-11-11 02:30:18` | `8.77%` | `65.43%` | 513 | 458 | `+31.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:18.243000+00:00`.*
