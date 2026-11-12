# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **WeGo Public Transit** in **Nashville, TN** (Nashville Metropolitan Area, Tennessee).
> **Transit System:** WeGo | **Location:** Nashville, TN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-12T07:00:22.664000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `48` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+76.4s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+10.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 9 | 36.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 52** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 3** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 50** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 4** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+4.6 min` |
| **Route 7** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 22** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.5 min` |
| **Route 55** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 56** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 4** | `+4.6 min (+275.0s)` | `+4.6 min (+275s)` | 1 | `100.0%` |
| **Route 56** | `+3.6 min (+219.0s)` | `+3.6 min (+219s)` | 2 | `100.0%` |
| **Route 23** | `+2.5 min (+150.0s)` | `+2.5 min (+150s)` | 2 | `100.0%` |
| **Route 55** | `+0.6 min (+34.0s)` | `+0.6 min (+34s)` | 2 | `100.0%` |
| **Route 50** | `+0.2 min (+10.0s)` | `+0.2 min (+10s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 52** | ~30.0m | ~30.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:22` | `0.0%` | `100.0%` | 25 | 48 | `+76.4s` |
| `2026-11-12 06:30:19` | `0.0%` | `100.0%` | 41 | 57 | `+49.0s` |
| `2026-11-12 06:00:19` | `0.0%` | `100.0%` | 53 | 74 | `+0.0s` |
| `2026-11-12 05:30:18` | `2.82%` | `100.0%` | 71 | 74 | `+0.0s` |
| `2026-11-12 05:00:18` | `0.0%` | `0.0%` | 86 | 81 | `+0.0s` |
| `2026-11-12 04:30:19` | `0.95%` | `0.0%` | 105 | 100 | `+0.0s` |
| `2026-11-12 04:00:19` | `0.0%` | `0.0%` | 120 | 115 | `+0.0s` |
| `2026-11-12 03:30:19` | `0.0%` | `0.0%` | 134 | 109 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:22.664000+00:00`.*
