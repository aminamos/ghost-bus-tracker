# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-20T06:30:18.941000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.24%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `34` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `19` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+76.7s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 30 | 88.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 5.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `+0.2 min` |
| **Route 9899** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 77** | 7 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 20** | 10 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.8 min` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-75.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+2.8 min (+168.4s)` | `+11.7 min (+700s)` | 4 | `80.0%` |
| **Route 601** | `+1.9 min (+116.0s)` | `+1.9 min (+116s)` | 1 | `100.0%` |
| **Route 9899** | `+1.4 min (+84.5s)` | `+3.0 min (+180s)` | 4 | `100.0%` |
| **Route 77** | `+1.1 min (+64.4s)` | `+5.0 min (+298s)` | 4 | `100.0%` |
| **Route 107** | `+0.2 min (+11.3s)` | `+2.1 min (+129s)` | 2 | `83.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~1.0m | ~1.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 9899** | ~3.0m | ~3.0m | **`+0.0 min`** | `57.8 / 100` |
| **Route 107** | ~2.0m | ~2.0m | **`+0.0 min`** | `52.4 / 100` |
| **Route 77** | ~16.5m | ~16.5m | **`+0.0 min`** | `90.0 / 100` |
| **Route 1** | ~55.0m | ~55.0m | **`+0.0 min`** | `97.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 06:30:18` | `0.0%` | `88.24%` | 34 | 19 | `+76.7s` |
| `2026-11-20 06:00:20` | `2.22%` | `86.36%` | 45 | 29 | `+41.6s` |
| `2026-11-20 05:30:18` | `4.41%` | `84.62%` | 68 | 45 | `+64.6s` |
| `2026-11-20 05:00:20` | `5.21%` | `79.12%` | 96 | 63 | `+80.2s` |
| `2026-11-20 04:30:18` | `7.94%` | `84.48%` | 126 | 75 | `+79.1s` |
| `2026-11-20 04:00:18` | `10.46%` | `86.86%` | 153 | 87 | `+58.4s` |
| `2026-11-20 03:30:21` | `3.33%` | `89.66%` | 180 | 97 | `+74.4s` |
| `2026-11-20 03:00:19` | `6.28%` | `85.57%` | 207 | 112 | `+70.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:18.941000+00:00`.*
