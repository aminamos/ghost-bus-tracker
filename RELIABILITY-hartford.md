# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Connecticut Transit** in **Hartford, CT** (Hartford Metropolitan Area, Connecticut).
> **Transit System:** Hartford | **Location:** Hartford, CT | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:50.067000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.41%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`99.69%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `343` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `322` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `22` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-1.4s` (`-0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 320 | 93.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 22 | 6.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16479** | 13 | 2 | 11 | **`84.62%`** | `100.0%` | `+0.0s` |
| **Route 16221** | 14 | 3 | 11 | **`78.57%`** | `100.0%` | `+0.0s` |
| **Route 16470** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16469** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16467** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16464** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16465** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16466** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16462** | 6 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 16366** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-18.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 16471** | `+0.5 min (+32.0s)` | `+1.1 min (+64s)` | 2 | `100.0%` |
| **Route 16450** | `+0.3 min (+17.0s)` | `+0.3 min (+17s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 16203** | ~9.0m | ~9.0m | **`+0.0 min`** | `95.3 / 100` |
| **Route 16470** | ~20.0m | ~20.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16469** | ~40.0m | ~40.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16467** | ~40.0m | ~40.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16464** | ~45.0m | ~45.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16465** | ~31.5m | ~31.5m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16467** | ~30.0m | ~30.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16466** | ~40.0m | ~40.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16462** | ~10.0m | ~10.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 16462** | ~12.0m | ~12.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1924176` | Route 16221 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924154` | Route 16221 | `15:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924171` | Route 16221 | `17:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924177` | Route 16221 | `20:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924172` | Route 16221 | `22:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924180` | Route 16221 | `00:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924178` | Route 16221 | `16:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924170` | Route 16221 | `18:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924179` | Route 16221 | `23:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924174` | Route 16221 | `16:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924173` | Route 16221 | `17:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1954346` | Route 16479 | `15:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1954351` | Route 16479 | `18:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1954354` | Route 16479 | `20:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1954355` | Route 16479 | `23:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:50.067000+00:00`.*
