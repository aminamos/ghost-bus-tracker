# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-20T06:30:19.762000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`69.18%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `146` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `407` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+191.4s` (`+3.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+94.0s` (`+1.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 101 | 69.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 19 | 13.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 22 | 15.1% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 2.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 7 | 7 | 0 | **`0.0%`** | `71.43%` | `+4.8 min` |
| **Route 106** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-58.5s` |
| **Route 35** | 7 | 7 | 0 | **`0.0%`** | `71.43%` | `+1.5 min` |
| **Route 28** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.6 min` |
| **Route 16** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+2.7 min` |
| **Route EART** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.3 min` |
| **Route 27** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+6.2 min` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 3** | 4 | 5 | 0 | **`0.0%`** | `100.0%` | `+2.8 min` |
| **Route 51** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+5.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 59** | `+73.5 min (+4407.5s)` | `+84.2 min (+5049s)` | 1 | `0.0%` |
| **Route 45** | `+9.1 min (+548.3s)` | `+20.9 min (+1251s)` | 3 | `66.67%` |
| **Route 28** | `+6.6 min (+394.0s)` | `+11.3 min (+676s)` | 2 | `50.0%` |
| **Route 27** | `+6.2 min (+369.4s)` | `+21.4 min (+1284s)` | 5 | `60.0%` |
| **Route 8** | `+5.8 min (+350.0s)` | `+7.6 min (+455s)` | 4 | `50.0%` |
| **Route 51** | `+5.4 min (+321.6s)` | `+9.4 min (+566s)` | 5 | `40.0%` |
| **Route 0** | `+5.0 min (+301.3s)` | `+5.6 min (+338s)` | 4 | `66.67%` |
| **Route 19** | `+4.8 min (+290.1s)` | `+14.7 min (+882s)` | 7 | `71.43%` |
| **Route 17** | `+4.6 min (+275.3s)` | `+9.2 min (+550s)` | 3 | `66.67%` |
| **Route 29** | `+4.1 min (+248.8s)` | `+5.3 min (+316s)` | 4 | `75.0%` |

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
| `2026-11-20 06:30:19` | `0.0%` | `69.18%` | 146 | 407 | `+191.4s` |
| `2026-11-20 06:00:23` | `4.2%` | `81.67%` | 262 | 440 | `+131.0s` |
| `2026-11-20 05:30:19` | `3.49%` | `79.93%` | 315 | 455 | `+172.3s` |
| `2026-11-20 05:00:20` | `4.07%` | `73.73%` | 369 | 487 | `+202.2s` |
| `2026-11-20 04:30:19` | `5.06%` | `76.27%` | 395 | 500 | `+191.0s` |
| `2026-11-20 04:00:19` | `4.01%` | `76.41%` | 424 | 568 | `+201.5s` |
| `2026-11-20 03:30:20` | `3.33%` | `77.06%` | 451 | 625 | `+205.2s` |
| `2026-11-20 03:00:20` | `4.62%` | `76.16%` | 476 | 636 | `+227.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:19.762000+00:00`.*
