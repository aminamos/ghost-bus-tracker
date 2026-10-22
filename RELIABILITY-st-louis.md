# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** St. Louis | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:53.537000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.2%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `128` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `125` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+115.7s` (`+1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 99 | 77.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 15 | 11.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 9 | 7.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 1.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 2.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19779** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `-12.0s` |
| **Route 19757** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 19788** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+0.0s` |
| **Route 19770** | 6 | 6 | 0 | **`0.0%`** | `83.33%` | `+2.2 min` |
| **Route 19773** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 19778** | 9 | 9 | 0 | **`0.0%`** | `77.78%` | `+3.3 min` |
| **Route 19754** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `-105.0s` |
| **Route 19775** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.5 min` |
| **Route 19790** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-60.0s` |
| **Route 19772** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+3.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19767** | `+11.5 min (+690.0s)` | `+49.0 min (+2940s)` | 4 | `50.0%` |
| **Route 19793** | `+8.7 min (+520.0s)` | `+21.0 min (+1260s)` | 3 | `66.67%` |
| **Route 19763** | `+6.0 min (+360.0s)` | `+12.0 min (+720s)` | 2 | `50.0%` |
| **Route 19796** | `+6.0 min (+360.0s)` | `+6.0 min (+360s)` | 1 | `0.0%` |
| **Route 19789** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19795** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19764** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19772** | `+3.8 min (+225.0s)` | `+12.0 min (+720s)` | 4 | `50.0%` |
| **Route 19775** | `+3.5 min (+210.0s)` | `+5.0 min (+300s)` | 2 | `100.0%` |
| **Route 19784** | `+3.5 min (+210.0s)` | `+8.0 min (+480s)` | 2 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19767** | ~24.0m | ~24.0m | **`+0.2 min`** | `9.4 / 100` |
| **Route 19763** | ~3.0m | ~3.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 19772** | ~4.0m | ~4.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 19750** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19793** | ~20.0m | ~20.0m | **`+0.0 min`** | `56.3 / 100` |
| **Route 19787** | ~4.0m | ~4.0m | **`+0.0 min`** | `17.1 / 100` |
| **Route 19790** | ~2.0m | ~2.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19784** | ~15.0m | ~15.0m | **`+0.0 min`** | `70.0 / 100` |
| **Route 19778** | ~6.0m | ~6.0m | **`+0.0 min`** | `53.5 / 100` |
| **Route 19780** | ~10.0m | ~10.0m | **`+0.0 min`** | `73.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:53.537000+00:00`.*
