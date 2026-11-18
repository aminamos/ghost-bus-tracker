# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-18T06:30:19.194000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.24%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `34` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `19` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+57.4s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 30 | 88.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 8.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 77** | 7 | 4 | 0 | **`0.0%`** | `85.71%` | `+1.2 min` |
| **Route 20** | 10 | 4 | 0 | **`0.0%`** | `90.0%` | `+0.5 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `-4.7s` |
| **Route 9899** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 601** | `+5.4 min (+326.0s)` | `+5.4 min (+326s)` | 1 | `0.0%` |
| **Route 605** | `+2.7 min (+161.0s)` | `+2.7 min (+161s)` | 1 | `100.0%` |
| **Route 9899** | `+1.6 min (+94.3s)` | `+4.6 min (+275s)` | 4 | `100.0%` |
| **Route 77** | `+1.2 min (+70.9s)` | `+4.9 min (+295s)` | 4 | `85.71%` |
| **Route 1** | `+0.8 min (+46.5s)` | `+1.6 min (+93s)` | 2 | `100.0%` |
| **Route 20** | `+0.5 min (+32.8s)` | `+4.7 min (+280s)` | 4 | `90.0%` |
| **Route 6** | `+0.1 min (+9.0s)` | `+0.1 min (+9s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 9899** | ~3.0m | ~3.0m | **`+0.0 min`** | `43.0 / 100` |
| **Route 77** | ~16.5m | ~16.5m | **`+0.0 min`** | `85.7 / 100` |
| **Route 107** | ~2.0m | ~2.0m | **`+0.0 min`** | `73.9 / 100` |
| **Route 1** | ~55.0m | ~55.0m | **`+0.0 min`** | `98.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 06:30:19` | `0.0%` | `88.24%` | 34 | 19 | `+57.4s` |
| `2026-11-18 06:00:27` | `2.22%` | `97.73%` | 45 | 28 | `+45.4s` |
| `2026-11-18 05:30:30` | `7.35%` | `93.65%` | 68 | 45 | `+57.8s` |
| `2026-11-18 05:00:18` | `5.21%` | `86.81%` | 96 | 61 | `+53.3s` |
| `2026-11-18 04:30:19` | `6.35%` | `83.9%` | 126 | 75 | `+52.8s` |
| `2026-11-18 04:00:18` | `7.79%` | `84.51%` | 154 | 87 | `+45.4s` |
| `2026-11-18 03:30:18` | `6.63%` | `85.8%` | 181 | 97 | `+67.1s` |
| `2026-11-18 03:00:20` | `5.31%` | `88.27%` | 207 | 114 | `+50.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:19.194000+00:00`.*
