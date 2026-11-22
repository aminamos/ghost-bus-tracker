# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-22T07:00:19.383000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`54.24%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `59` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `301` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+140.3s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+37.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 32 | 54.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 15 | 25.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 11 | 18.6% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 35** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+0.1 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+26.3 min` |
| **Route 50** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-21.7s` |
| **Route 7** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+6.4 min` |
| **Route 170** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 19** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.5 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-9.0s` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.1 min` |
| **Route 27** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.2 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | `+26.3 min (+1575.5s)` | `+48.7 min (+2920s)` | 2 | `50.0%` |
| **Route 138** | `+9.4 min (+567.0s)` | `+9.4 min (+567s)` | 1 | `0.0%` |
| **Route 12** | `+8.9 min (+536.0s)` | `+8.9 min (+536s)` | 1 | `0.0%` |
| **Route 106** | `+7.2 min (+432.0s)` | `+7.2 min (+432s)` | 1 | `0.0%` |
| **Route 7** | `+6.4 min (+386.5s)` | `+10.8 min (+647s)` | 3 | `50.0%` |
| **Route 72** | `+5.1 min (+305.0s)` | `+5.1 min (+305s)` | 1 | `0.0%` |
| **Route 0** | `+4.7 min (+282.0s)` | `+4.7 min (+282s)` | 1 | `100.0%` |
| **Route 17** | `+4.6 min (+273.7s)` | `+6.1 min (+366s)` | 3 | `66.67%` |
| **Route 19** | `+4.5 min (+269.5s)` | `+9.1 min (+548s)` | 2 | `50.0%` |
| **Route 43** | `+3.2 min (+193.0s)` | `+3.2 min (+193s)` | 1 | `100.0%` |

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
| `2026-11-22 07:00:19` | `0.0%` | `54.24%` | 59 | 301 | `+140.3s` |
| `2026-11-22 06:30:19` | `0.0%` | `66.67%` | 144 | 320 | `+188.1s` |
| `2026-11-22 06:00:19` | `3.27%` | `78.06%` | 245 | 338 | `+185.0s` |
| `2026-11-22 05:30:32` | `4.03%` | `70.98%` | 298 | 348 | `+256.1s` |
| `2026-11-22 05:00:19` | `2.35%` | `68.67%` | 340 | 363 | `+277.3s` |
| `2026-11-22 04:30:18` | `2.75%` | `66.29%` | 363 | 366 | `+285.8s` |
| `2026-11-22 04:00:19` | `2.88%` | `63.07%` | 382 | 405 | `+279.9s` |
| `2026-11-22 03:30:20` | `3.71%` | `66.07%` | 404 | 428 | `+265.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:19.383000+00:00`.*
