# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-25T07:00:18.264000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.16%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+28.9s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+16.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 63.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 18 | 31.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.5% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-8.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-2.0s` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-45.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.6 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.0 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-106.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.3 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-288.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+8.7 min (+521.0s)` | `+8.7 min (+521s)` | 1 | `0.0%` |
| **Route 922** | `+5.4 min (+321.8s)` | `+26.6 min (+1598s)` | 4 | `40.0%` |
| **Route 74** | `+4.3 min (+259.0s)` | `+4.3 min (+259s)` | 1 | `100.0%` |
| **Route 2** | `+3.0 min (+180.0s)` | `+5.3 min (+320s)` | 2 | `50.0%` |
| **Route 18** | `+2.6 min (+156.0s)` | `+3.9 min (+234s)` | 2 | `100.0%` |
| **Route 921** | `+2.1 min (+124.0s)` | `+2.3 min (+140s)` | 2 | `100.0%` |
| **Route 61** | `+1.6 min (+98.0s)` | `+1.6 min (+98s)` | 1 | `100.0%` |
| **Route 17** | `+0.7 min (+41.3s)` | `+1.6 min (+96s)` | 3 | `100.0%` |
| **Route 5** | `+0.6 min (+35.0s)` | `+0.9 min (+54s)` | 2 | `100.0%` |
| **Route 515** | `+0.4 min (+24.0s)` | `+0.4 min (+24s)` | 1 | `100.0%` |

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
| `2026-11-25 07:00:18` | `0.0%` | `63.16%` | 57 | 57 | `+28.9s` |
| `2026-11-25 06:30:18` | `0.0%` | `60.75%` | 107 | 107 | `+5.1s` |
| `2026-11-25 05:30:18` | `4.42%` | `62.79%` | 226 | 215 | `+5.8s` |
| `2026-11-25 05:00:17` | `5.28%` | `62.16%` | 284 | 259 | `-20.8s` |
| `2026-11-25 04:30:17` | `5.75%` | `62.26%` | 348 | 318 | `-4.0s` |
| `2026-11-25 04:00:18` | `7.14%` | `62.54%` | 392 | 355 | `+2.6s` |
| `2026-11-25 03:00:20` | `9.17%` | `65.57%` | 480 | 427 | `+7.4s` |
| `2026-11-25 02:30:18` | `8.94%` | `65.73%` | 526 | 464 | `+6.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.264000+00:00`.*
