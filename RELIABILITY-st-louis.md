# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-17T07:00:22.865000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `41` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `27` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+64.8s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 17 | 41.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 12.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 4.9% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 34.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-150.0s` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-300.0s` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+8.5 min` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 19792** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19788** | `+9.0 min (+540.0s)` | `+9.0 min (+540s)` | 1 | `0.0%` |
| **Route 19785** | `+8.5 min (+510.0s)` | `+18.0 min (+1080s)` | 2 | `50.0%` |
| **Route 19777** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 1 | `0.0%` |
| **Route 19763** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19800** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19793** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19792** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |
| **Route 19768** | `+1.0 min (+60.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 19782** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19798** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19785** | ~37.0m | ~37.0m | **`+0.0 min`** | `74.3 / 100` |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `83.3 / 100` |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `80.0 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `90.9 / 100` |
| **Route 19792** | ~30.0m | ~30.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:22` | `0.0%` | `68.0%` | 41 | 27 | `+64.8s` |
| `2026-11-17 06:30:19` | `0.0%` | `68.63%` | 75 | 58 | `+75.3s` |
| `2026-11-17 06:00:22` | `0.0%` | `79.63%` | 87 | 68 | `+82.2s` |
| `2026-11-17 05:30:21` | `0.0%` | `74.55%` | 84 | 75 | `+60.0s` |
| `2026-11-17 05:00:18` | `0.0%` | `77.94%` | 94 | 80 | `+135.0s` |
| `2026-11-17 04:30:20` | `0.0%` | `78.48%` | 97 | 85 | `+120.8s` |
| `2026-11-17 04:00:18` | `0.0%` | `84.21%` | 105 | 90 | `+107.4s` |
| `2026-11-17 03:30:24` | `0.0%` | `80.6%` | 96 | 84 | `+87.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:22.865000+00:00`.*
