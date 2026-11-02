# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-02T07:00:18.635000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.86%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `52` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `290` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+309.8s` (`+5.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+41.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 29 | 55.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 21.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 15.4% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 5.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-13.7s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.1 min` |
| **Route 29** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-56.7s` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 90** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 27** | 5 | 5 | 0 | **`0.0%`** | `20.0%` | `+20.5 min` |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.4 min` |
| **Route 35** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `+3.0 min` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+59.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 28** | `+59.5 min (+3572.5s)` | `+67.2 min (+4029s)` | 1 | `0.0%` |
| **Route 27** | `+20.5 min (+1228.0s)` | `+88.8 min (+5327s)` | 5 | `20.0%` |
| **Route 51** | `+7.6 min (+456.0s)` | `+7.6 min (+456s)` | 1 | `0.0%` |
| **Route 41** | `+6.2 min (+369.0s)` | `+6.2 min (+369s)` | 2 | `0.0%` |
| **Route 17** | `+4.1 min (+243.5s)` | `+6.2 min (+369s)` | 2 | `50.0%` |
| **Route 50** | `+3.9 min (+235.0s)` | `+9.4 min (+562s)` | 3 | `0.0%` |
| **Route 7** | `+3.4 min (+204.3s)` | `+9.2 min (+550s)` | 3 | `66.67%` |
| **Route 35** | `+3.0 min (+180.0s)` | `+6.4 min (+384s)` | 4 | `66.67%` |
| **Route 154** | `+1.6 min (+97.0s)` | `+1.6 min (+97s)` | 3 | `100.0%` |
| **Route 44** | `+1.4 min (+82.0s)` | `+1.4 min (+82s)` | 1 | `100.0%` |

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
| `2026-11-02 07:00:18` | `0.0%` | `56.86%` | 52 | 290 | `+309.8s` |
| `2026-11-02 06:30:18` | `0.0%` | `78.86%` | 124 | 321 | `+238.2s` |
| `2026-11-02 06:00:25` | `3.69%` | `75.96%` | 217 | 330 | `+185.9s` |
| `2026-11-02 05:30:24` | `3.53%` | `74.18%` | 255 | 327 | `+210.3s` |
| `2026-11-02 05:00:19` | `2.88%` | `73.23%` | 278 | 338 | `+211.4s` |
| `2026-11-02 04:30:20` | `4.04%` | `73.5%` | 297 | 343 | `+241.5s` |
| `2026-11-02 04:00:20` | `2.6%` | `76.85%` | 308 | 372 | `+242.6s` |
| `2026-11-02 03:30:25` | `5.2%` | `71.29%` | 327 | 398 | `+308.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.635000+00:00`.*
