# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-10T07:00:20.616000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.41%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `354` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+271.7s` (`+4.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+46.0s` (`+0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 38 | 63.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 18.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 6.7% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 10.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+7.9 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `-25.2s` |
| **Route 16** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+4.5 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+9.1 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.3 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+10.6 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.4 min` |
| **Route 70** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+42.9 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.5 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 70** | `+42.9 min (+2572.3s)` | `+73.0 min (+4381s)` | 3 | `0.0%` |
| **Route 80** | `+32.9 min (+1972.0s)` | `+32.9 min (+1972s)` | 1 | `0.0%` |
| **Route 51** | `+10.6 min (+635.5s)` | `+18.1 min (+1086s)` | 2 | `50.0%` |
| **Route 27** | `+9.1 min (+545.7s)` | `+24.6 min (+1476s)` | 3 | `66.67%` |
| **Route 19** | `+7.9 min (+475.5s)` | `+21.4 min (+1287s)` | 4 | `25.0%` |
| **Route 32** | `+6.9 min (+415.0s)` | `+6.9 min (+415s)` | 1 | `0.0%` |
| **Route 16** | `+4.5 min (+268.5s)` | `+8.0 min (+478s)` | 3 | `50.0%` |
| **Route 44** | `+3.5 min (+207.5s)` | `+7.0 min (+419s)` | 2 | `50.0%` |
| **Route 17** | `+3.4 min (+203.0s)` | `+4.4 min (+264s)` | 2 | `100.0%` |
| **Route 3** | `+3.3 min (+195.5s)` | `+3.5 min (+211s)` | 2 | `100.0%` |

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
| `24784259` | Route 28 | `N/A` | `SCHEDULED` | Assigned vehicle 5253 is broadcasting off-schedule with no vehicle covering 24784259 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:20` | `1.67%` | `64.41%` | 60 | 354 | `+271.7s` |
| `2026-11-10 06:30:19` | `0.0%` | `72.67%` | 150 | 388 | `+171.8s` |
| `2026-11-10 06:00:19` | `4.51%` | `78.35%` | 266 | 416 | `+132.8s` |
| `2026-11-10 05:30:21` | `3.17%` | `78.36%` | 315 | 441 | `+190.6s` |
| `2026-11-10 05:00:19` | `3.01%` | `75.42%` | 365 | 478 | `+199.6s` |
| `2026-11-10 04:30:20` | `4.6%` | `76.14%` | 391 | 496 | `+192.7s` |
| `2026-11-10 04:00:21` | `4.05%` | `78.91%` | 420 | 561 | `+189.1s` |
| `2026-11-10 03:30:18` | `4.11%` | `80.24%` | 438 | 584 | `+183.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:20.616000+00:00`.*
