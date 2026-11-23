# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-23T07:00:18.848000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.89%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `20` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+67.4s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 80.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 10.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 10.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 9899** | 5 | 3 | 2 | **`40.0%`** | `66.67%` | `+3.1 min` |
| **Route 77** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 20** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+1.2 min` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+3.1 min (+188.0s)` | `+9.7 min (+580s)` | 3 | `66.67%` |
| **Route 107** | `+1.3 min (+77.8s)` | `+3.3 min (+199s)` | 2 | `100.0%` |
| **Route 20** | `+1.2 min (+69.8s)` | `+6.1 min (+365s)` | 4 | `80.0%` |
| **Route 77** | `+0.2 min (+9.4s)` | `+0.6 min (+36s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | ~23.0m | ~23.0m | **`+0.0 min`** | `79.9 / 100` |
| **Route 20** | ~23.0m | ~23.0m | **`+0.0 min`** | `89.3 / 100` |
| **Route 107** | ~10.0m | ~10.0m | **`+0.0 min`** | `87.7 / 100` |
| **Route 77** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024034` | Route 9899 | `01:54:00` | `SCHEDULED` | Assigned vehicle M1414 is broadcasting off-schedule with no vehicle covering 2024034 |
| `2024028` | Route 9899 | `03:00:00` | `SCHEDULED` | Assigned vehicle M1414 is broadcasting off-schedule with no vehicle covering 2024028 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:18` | `10.0%` | `88.89%` | 20 | 13 | `+67.4s` |
| `2026-11-23 06:30:18` | `16.0%` | `76.19%` | 25 | 14 | `+52.6s` |
| `2026-11-23 06:00:21` | `2.86%` | `88.24%` | 35 | 21 | `+43.5s` |
| `2026-11-23 05:30:18` | `3.92%` | `81.63%` | 51 | 34 | `+68.9s` |
| `2026-11-23 05:00:22` | `4.69%` | `78.69%` | 64 | 40 | `+69.2s` |
| `2026-11-23 04:30:22` | `8.86%` | `81.94%` | 79 | 40 | `+90.2s` |
| `2026-11-23 04:00:20` | `2.33%` | `89.29%` | 86 | 45 | `+85.5s` |
| `2026-11-23 03:30:18` | `5.43%` | `89.66%` | 92 | 52 | `+85.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:18.848000+00:00`.*
