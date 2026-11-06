# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-06T07:00:18.255000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `88` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `85` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+145.5s` (`+2.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+120.0s` (`+2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 60 | 68.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 8.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 12 | 13.6% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 3.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19761** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 19754** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 19759** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |
| **Route 19778** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+5.8 min` |
| **Route 19788** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-60.0s` |
| **Route 19772** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 19753** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |
| **Route 19757** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 19762** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-90.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19775** | `+19.0 min (+1140.0s)` | `+19.0 min (+1140s)` | 1 | `0.0%` |
| **Route 19803** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 1 | `0.0%` |
| **Route 19780** | `+7.0 min (+420.0s)` | `+9.0 min (+540s)` | 3 | `50.0%` |
| **Route 19779** | `+7.0 min (+420.0s)` | `+7.0 min (+420s)` | 2 | `0.0%` |
| **Route 19759** | `+6.0 min (+360.0s)` | `+7.0 min (+420s)` | 2 | `50.0%` |
| **Route 19753** | `+6.0 min (+360.0s)` | `+8.0 min (+480s)` | 2 | `50.0%` |
| **Route 19778** | `+5.8 min (+345.0s)` | `+9.0 min (+540s)` | 4 | `50.0%` |
| **Route 19766** | `+4.5 min (+270.0s)` | `+9.0 min (+540s)` | 2 | `50.0%` |
| **Route 19749** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19781** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19750** | ~1.0m | ~1.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 19784** | ~2.0m | ~2.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19766** | ~8.0m | ~8.0m | **`+0.0 min`** | `43.8 / 100` |
| **Route 19759** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19767** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19761** | ~3.0m | ~3.0m | **`+0.0 min`** | `50.0 / 100` |
| **Route 19778** | ~12.0m | ~12.0m | **`+0.0 min`** | `76.9 / 100` |
| **Route 19772** | ~2.0m | ~2.0m | **`+0.0 min`** | `50.0 / 100` |
| **Route 19770** | ~20.0m | ~20.0m | **`+0.0 min`** | `85.9 / 100` |
| **Route 19787** | ~15.0m | ~15.0m | **`+0.0 min`** | `85.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 06:30:19` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 06:00:18` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 05:30:20` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 05:00:19` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 04:30:19` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 04:00:23` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |
| `2026-11-06 03:30:21` | `0.0%` | `75.0%` | 88 | 85 | `+145.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.255000+00:00`.*
