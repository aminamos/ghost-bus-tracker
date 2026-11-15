# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-15T07:00:19.164000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.54%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `40` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `19` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+133.8s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+120.0s` (`+2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 20.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 7.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 5.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 21 | 52.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19780** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+7.0 min` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+7.0 min` |
| **Route 19792** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route UNKNOWN** | 21 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19780** | `+7.0 min (+420.0s)` | `+7.0 min (+420s)` | 2 | `0.0%` |
| **Route 19778** | `+7.0 min (+420.0s)` | `+10.0 min (+600s)` | 2 | `50.0%` |
| **Route 19749** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19787** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19781** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19777** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~4.0m | ~4.0m | **`+0.0 min`** | `25.0 / 100` |
| **Route 19792** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:19` | `0.0%` | `61.54%` | 40 | 19 | `+133.8s` |
| `2026-11-15 06:30:19` | `0.0%` | `82.86%` | 65 | 44 | `+149.1s` |
| `2026-11-15 05:30:19` | `0.0%` | `83.33%` | 67 | 60 | `+85.6s` |
| `2026-11-15 05:00:19` | `1.23%` | `74.58%` | 81 | 67 | `+122.0s` |
| `2026-11-15 04:30:19` | `0.0%` | `76.47%` | 78 | 65 | `+145.9s` |
| `2026-11-15 04:00:20` | `0.0%` | `75.71%` | 78 | 78 | `+96.9s` |
| `2026-11-15 03:30:19` | `0.0%` | `80.7%` | 82 | 75 | `+181.1s` |
| `2026-11-15 03:00:20` | `0.0%` | `83.78%` | 84 | 84 | `+176.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.164000+00:00`.*
