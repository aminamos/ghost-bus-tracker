# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-05T07:00:17.748000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`45.61%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+54.1s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+10.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 26 | 45.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 23 | 40.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 12.3% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-66.5s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-129.0s` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-95.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 18** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+5.7 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-92.0s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-90.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+0.6 min` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-5.3s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+12.7 min (+761.0s)` | `+12.7 min (+761s)` | 1 | `0.0%` |
| **Route 925** | `+6.0 min (+360.5s)` | `+7.1 min (+428s)` | 2 | `50.0%` |
| **Route 18** | `+5.7 min (+340.5s)` | `+16.6 min (+997s)` | 4 | `75.0%` |
| **Route 924** | `+3.4 min (+201.7s)` | `+9.5 min (+571s)` | 3 | `66.67%` |
| **Route 922** | `+3.3 min (+197.0s)` | `+6.8 min (+409s)` | 4 | `50.0%` |
| **Route 921** | `+2.8 min (+170.5s)` | `+5.0 min (+302s)` | 2 | `50.0%` |
| **Route 923** | `+2.5 min (+147.3s)` | `+3.8 min (+230s)` | 2 | `100.0%` |
| **Route 36** | `+1.9 min (+117.0s)` | `+3.9 min (+234s)` | 2 | `100.0%` |
| **Route 724** | `+0.7 min (+39.0s)` | `+2.5 min (+152s)` | 1 | `50.0%` |
| **Route 3** | `+0.6 min (+37.8s)` | `+5.8 min (+348s)` | 5 | `40.0%` |

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
| `2026-11-05 07:00:17` | `0.0%` | `45.61%` | 57 | 57 | `+54.1s` |
| `2026-11-05 06:30:17` | `0.0%` | `54.21%` | 107 | 107 | `+50.4s` |
| `2026-11-05 05:30:18` | `4.87%` | `63.64%` | 226 | 209 | `+13.1s` |
| `2026-11-05 05:00:17` | `5.73%` | `61.48%` | 279 | 257 | `+29.9s` |
| `2026-11-05 04:30:18` | `6.86%` | `61.15%` | 350 | 314 | `+29.6s` |
| `2026-11-05 04:00:18` | `8.46%` | `62.36%` | 402 | 356 | `+40.8s` |
| `2026-11-05 03:30:18` | `9.37%` | `63.78%` | 459 | 392 | `+46.6s` |
| `2026-11-05 03:00:17` | `9.02%` | `61.4%` | 499 | 430 | `+45.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.748000+00:00`.*
