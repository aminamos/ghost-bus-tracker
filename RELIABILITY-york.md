# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-16T07:00:21.137000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `20` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+126.9s` (`+2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 17 | 85.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 10.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 5.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 77** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 9899** | 5 | 3 | 0 | **`0.0%`** | `60.0%` | `+4.2 min` |
| **Route 20** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+4.2 min (+253.8s)` | `+15.2 min (+914s)` | 3 | `60.0%` |
| **Route 20** | `+2.5 min (+149.6s)` | `+10.0 min (+602s)` | 4 | `80.0%` |
| **Route 77** | `+1.2 min (+72.6s)` | `+3.9 min (+234s)` | 3 | `100.0%` |
| **Route 107** | `+0.7 min (+40.2s)` | `+1.2 min (+75s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | ~23.0m | ~23.0m | **`+0.0 min`** | `74.0 / 100` |
| **Route 20** | ~23.0m | ~23.0m | **`+0.0 min`** | `83.1 / 100` |
| **Route 77** | ~20.0m | ~20.0m | **`+0.0 min`** | `92.1 / 100` |
| **Route 107** | ~10.0m | ~10.0m | **`+0.0 min`** | `95.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:21` | `0.0%` | `85.0%` | 20 | 13 | `+126.9s` |
| `2026-11-16 06:00:19` | `0.0%` | `72.22%` | 36 | 22 | `+83.2s` |
| `2026-11-16 05:30:20` | `3.92%` | `89.8%` | 51 | 33 | `+68.0s` |
| `2026-11-16 05:00:21` | `0.0%` | `85.94%` | 64 | 39 | `+69.9s` |
| `2026-11-16 04:30:20` | `8.86%` | `87.5%` | 79 | 42 | `+42.7s` |
| `2026-11-16 04:00:20` | `2.33%` | `84.52%` | 86 | 45 | `+99.9s` |
| `2026-11-16 03:30:18` | `4.35%` | `87.5%` | 92 | 51 | `+53.7s` |
| `2026-11-16 02:30:18` | `5.71%` | `87.12%` | 140 | 77 | `+75.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:21.137000+00:00`.*
