# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-03T07:00:18.417000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`47.37%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+58.3s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-2.0s` (`-0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 27 | 47.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 22 | 38.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 12.3% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-57.5s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+0.1 min` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.8 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-57.5s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `-74.0s` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-196.3s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 323** | `+8.8 min (+526.0s)` | `+8.8 min (+526s)` | 1 | `0.0%` |
| **Route 54** | `+8.4 min (+504.0s)` | `+8.4 min (+504s)` | 1 | `0.0%` |
| **Route 924** | `+8.2 min (+491.3s)` | `+17.4 min (+1043s)` | 3 | `33.33%` |
| **Route 923** | `+6.5 min (+389.0s)` | `+9.3 min (+556s)` | 2 | `33.33%` |
| **Route 921** | `+5.0 min (+298.5s)` | `+9.4 min (+565s)` | 2 | `50.0%` |
| **Route 7** | `+5.0 min (+297.0s)` | `+5.0 min (+297s)` | 1 | `100.0%` |
| **Route 18** | `+3.8 min (+225.3s)` | `+6.3 min (+378s)` | 3 | `66.67%` |
| **Route 925** | `+2.7 min (+164.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 5** | `+0.5 min (+28.0s)` | `+2.8 min (+165s)` | 2 | `50.0%` |
| **Route 22** | `+0.4 min (+25.0s)` | `+1.3 min (+76s)` | 2 | `100.0%` |

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
| `2026-11-03 07:00:18` | `0.0%` | `47.37%` | 57 | 57 | `+58.3s` |
| `2026-11-03 06:00:18` | `2.38%` | `56.71%` | 168 | 164 | `+14.7s` |
| `2026-11-03 05:30:18` | `3.18%` | `62.44%` | 220 | 213 | `+13.5s` |
| `2026-11-03 04:30:18` | `4.5%` | `61.32%` | 333 | 318 | `+22.7s` |
| `2026-11-03 04:00:18` | `6.38%` | `64.58%` | 392 | 367 | `+24.9s` |
| `2026-11-03 03:30:19` | `7.66%` | `63.07%` | 431 | 398 | `+27.3s` |
| `2026-11-03 03:00:18` | `7.34%` | `63.64%` | 463 | 429 | `+23.8s` |
| `2026-11-03 02:00:18` | `7.54%` | `68.46%` | 544 | 501 | `+38.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.417000+00:00`.*
