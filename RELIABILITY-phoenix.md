# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-25T07:00:19.363000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.07%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `58` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `362` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+101.6s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+32.0s` (`+0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 62.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 22.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 13.8% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+5.0 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+0.2 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+6.6 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 51** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+6.5 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+5.9 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.5 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.7 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 170** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+1.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 27** | `+6.6 min (+395.7s)` | `+10.4 min (+624s)` | 3 | `33.33%` |
| **Route 51** | `+6.5 min (+391.0s)` | `+8.2 min (+494s)` | 3 | `50.0%` |
| **Route 41** | `+5.9 min (+355.3s)` | `+18.9 min (+1135s)` | 3 | `33.33%` |
| **Route 19** | `+5.0 min (+302.8s)` | `+12.0 min (+722s)` | 4 | `50.0%` |
| **Route 17** | `+2.5 min (+152.5s)` | `+3.5 min (+209s)` | 2 | `100.0%` |
| **Route 0** | `+2.1 min (+127.5s)` | `+3.5 min (+209s)` | 2 | `100.0%` |
| **Route 7** | `+2.1 min (+127.0s)` | `+7.7 min (+464s)` | 4 | `33.33%` |
| **Route 29** | `+1.9 min (+114.0s)` | `+3.7 min (+224s)` | 2 | `100.0%` |
| **Route 170** | `+1.8 min (+108.0s)` | `+5.2 min (+315s)` | 2 | `0.0%` |
| **Route A** | `+1.4 min (+84.0s)` | `+7.0 min (+420s)` | 5 | `60.0%` |

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
| `2026-11-25 07:00:19` | `0.0%` | `62.07%` | 58 | 362 | `+101.6s` |
| `2026-11-25 06:30:19` | `0.0%` | `65.81%` | 155 | 411 | `+163.7s` |
| `2026-11-25 06:00:20` | `3.28%` | `75.09%` | 274 | 441 | `+181.1s` |
| `2026-11-25 05:30:19` | `3.17%` | `76.07%` | 315 | 463 | `+201.3s` |
| `2026-11-25 05:00:18` | `3.55%` | `73.94%` | 366 | 504 | `+180.9s` |
| `2026-11-25 04:30:18` | `2.99%` | `74.29%` | 401 | 528 | `+187.8s` |
| `2026-11-25 04:00:19` | `3.54%` | `77.02%` | 424 | 594 | `+188.2s` |
| `2026-11-25 03:30:25` | `3.86%` | `79.91%` | 440 | 627 | `+185.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:19.363000+00:00`.*
