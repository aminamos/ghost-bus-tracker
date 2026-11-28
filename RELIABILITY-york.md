# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-28T07:00:20.557000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.3%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+83.4s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 21 | 84.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 8.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 8.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 2 | **`28.57%`** | `100.0%` | `+0.8 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `66.67%` | `+4.2 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | `+4.2 min (+251.5s)` | `+13.8 min (+826s)` | 4 | `66.67%` |
| **Route 20** | `+0.8 min (+48.0s)` | `+4.1 min (+245s)` | 4 | `100.0%` |
| **Route 9899** | `+0.3 min (+20.8s)` | `+1.8 min (+105s)` | 4 | `100.0%` |
| **Route 107** | `+0.3 min (+19.0s)` | `+2.8 min (+165s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `52.0 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `85.1 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `81.1 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `95.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024940` | Route 20 | `02:47:00` | `SCHEDULED` | Assigned vehicle C2017 is broadcasting off-schedule with no vehicle covering 2024940 |
| `2025027` | Route 20 | `02:04:00` | `SCHEDULED` | Assigned vehicle C2017 is broadcasting off-schedule with no vehicle covering 2025027 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:20` | `8.0%` | `91.3%` | 25 | 15 | `+83.4s` |
| `2026-11-28 06:30:17` | `0.0%` | `79.41%` | 34 | 19 | `+86.7s` |
| `2026-11-28 06:00:18` | `4.44%` | `88.37%` | 45 | 28 | `+95.3s` |
| `2026-11-28 05:30:20` | `8.82%` | `82.26%` | 68 | 46 | `+125.3s` |
| `2026-11-28 05:00:20` | `7.29%` | `78.65%` | 96 | 63 | `+123.6s` |
| `2026-11-28 04:30:17` | `11.2%` | `81.98%` | 125 | 74 | `+114.3s` |
| `2026-11-28 04:00:20` | `10.53%` | `83.82%` | 152 | 86 | `+104.8s` |
| `2026-11-28 03:30:20` | `7.91%` | `85.89%` | 177 | 98 | `+115.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:20.557000+00:00`.*
