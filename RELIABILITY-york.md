# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-24T06:30:22.567000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.24%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `17` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+99.8s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+87.0s` (`+1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 88.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 11.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 107** | 5 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 9899** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 77** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+2.2 min` |
| **Route 20** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+2.9 min (+173.2s)` | `+6.0 min (+359s)` | 4 | `80.0%` |
| **Route 77** | `+2.2 min (+133.5s)` | `+7.2 min (+430s)` | 4 | `75.0%` |
| **Route 107** | `+0.7 min (+42.8s)` | `+1.8 min (+107s)` | 2 | `100.0%` |
| **Route 9899** | `+0.5 min (+27.3s)` | `+2.2 min (+130s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `70.8 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `81.4 / 100` |
| **Route 9899** | ~22.5m | ~22.5m | **`+0.0 min`** | `94.4 / 100` |
| **Route 107** | ~16.0m | ~16.0m | **`+0.0 min`** | `94.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `0.0%` | `88.24%` | 17 | 13 | `+99.8s` |
| `2026-10-24 05:30:21` | `0.0%` | `85.71%` | 35 | 21 | `+86.7s` |
| `2026-10-24 05:00:24` | `7.55%` | `77.55%` | 53 | 35 | `+51.6s` |
| `2026-10-24 04:30:22` | `7.41%` | `86.67%` | 81 | 53 | `+86.3s` |
| `2026-10-24 04:00:23` | `4.39%` | `86.24%` | 114 | 71 | `+72.4s` |
| `2026-10-24 03:00:21` | `10.17%` | `83.65%` | 177 | 94 | `+64.9s` |
| `2026-10-24 02:00:23` | `9.63%` | `85.79%` | 218 | 115 | `+83.5s` |
| `2026-10-24 01:30:23` | `10.59%` | `86.73%` | 236 | 123 | `+90.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.567000+00:00`.*
