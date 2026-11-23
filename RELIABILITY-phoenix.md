# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-23T07:00:19.324000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `52` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `286` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+340.9s` (`+5.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+101.5s` (`+1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 31 | 59.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 17.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 15.4% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 7.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+13.4 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+5.8 min` |
| **Route 29** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+15.5 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 27** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+23.9 min` |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.4 min` |
| **Route 35** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `+3.8 min` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-37.5s` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 50** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 27** | `+23.9 min (+1431.6s)` | `+87.9 min (+5272s)` | 5 | `40.0%` |
| **Route 29** | `+15.5 min (+928.7s)` | `+39.6 min (+2374s)` | 3 | `33.33%` |
| **Route 19** | `+13.4 min (+804.4s)` | `+60.5 min (+3627s)` | 5 | `60.0%` |
| **Route 51** | `+10.1 min (+603.0s)` | `+10.1 min (+603s)` | 1 | `0.0%` |
| **Route 17** | `+5.8 min (+345.5s)` | `+6.2 min (+374s)` | 2 | `0.0%` |
| **Route 7** | `+4.4 min (+263.3s)` | `+7.9 min (+472s)` | 3 | `66.67%` |
| **Route 35** | `+3.8 min (+230.3s)` | `+9.2 min (+550s)` | 4 | `66.67%` |
| **Route 50** | `+3.6 min (+217.7s)` | `+12.6 min (+757s)` | 3 | `66.67%` |
| **Route 41** | `+3.0 min (+181.0s)` | `+3.2 min (+192s)` | 2 | `100.0%` |
| **Route 90** | `+2.4 min (+145.0s)` | `+2.4 min (+145s)` | 1 | `100.0%` |

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
| `2026-11-23 07:00:19` | `0.0%` | `59.62%` | 52 | 286 | `+340.9s` |
| `2026-11-23 06:30:18` | `0.77%` | `73.44%` | 130 | 309 | `+243.7s` |
| `2026-11-23 06:00:23` | `2.39%` | `78.33%` | 209 | 324 | `+190.3s` |
| `2026-11-23 05:30:19` | `3.7%` | `75.11%` | 243 | 309 | `+172.7s` |
| `2026-11-23 05:00:21` | `2.55%` | `74.81%` | 275 | 329 | `+171.3s` |
| `2026-11-23 04:30:21` | `3.88%` | `70.65%` | 309 | 329 | `+232.1s` |
| `2026-11-23 04:00:19` | `3.51%` | `73.06%` | 313 | 349 | `+228.3s` |
| `2026-11-23 03:30:18` | `4.28%` | `70.23%` | 327 | 384 | `+221.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:19.324000+00:00`.*
