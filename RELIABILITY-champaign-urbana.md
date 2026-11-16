# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-16T07:00:19.546000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `41` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 14.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route TEAL LATE NIGHT SUNDAY** | 8 | 2 | 4 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING SUNDAY** | 17 | 7 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |
| **Route GREEN LATE NIGHT SUNDAY** | 4 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT SUNDAY** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER EVENING SUNDAY** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `[@124.0.92276155@][1484344792164]/79__T1_UISU_LATE` | Route TEAL LATE NIGHT SUNDAY | `01:36:00` | `SCHEDULED` | Assigned vehicle 1602 is broadcasting off-schedule with no vehicle covering [@124.0.92276155@][1484344792164]/79__T1_UISU_LATE |
| `[@124.0.92263401@][1484328944432]/264__I7_UISU` | Route ILLINI EVENING SUNDAY | `01:00:00` | `SCHEDULED` | Assigned vehicle 2018 is broadcasting off-schedule with no vehicle covering [@124.0.92263401@][1484328944432]/264__I7_UISU |
| `[@124.0.92276155@][1484344792164]/33__T1_UISU_LATE` | Route TEAL LATE NIGHT SUNDAY | `01:55:00` | `SCHEDULED` | Assigned vehicle 1602 is broadcasting off-schedule with no vehicle covering [@124.0.92276155@][1484344792164]/33__T1_UISU_LATE |
| `[@124.0.92276155@][1484344792164]/60__T1_UISU_LATE` | Route TEAL LATE NIGHT SUNDAY | `00:56:00` | `SCHEDULED` | Assigned vehicle 1602 is broadcasting off-schedule with no vehicle covering [@124.0.92276155@][1484344792164]/60__T1_UISU_LATE |
| `[@124.0.92263401@][1484328944432]/111__I7_UISU` | Route ILLINI EVENING SUNDAY | `01:35:00` | `SCHEDULED` | Assigned vehicle 2018 is broadcasting off-schedule with no vehicle covering [@124.0.92263401@][1484328944432]/111__I7_UISU |
| `[@124.0.92276155@][1484344792164]/34__T1_UISU_LATE` | Route TEAL LATE NIGHT SUNDAY | `01:15:00` | `SCHEDULED` | Assigned vehicle 1602 is broadcasting off-schedule with no vehicle covering [@124.0.92276155@][1484344792164]/34__T1_UISU_LATE |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:19` | `14.63%` | `0.0%` | 41 | 14 | `+0.0s` |
| `2026-11-16 06:30:20` | `4.55%` | `0.0%` | 44 | 14 | `+0.0s` |
| `2026-11-16 06:00:18` | `23.81%` | `0.0%` | 42 | 14 | `+0.0s` |
| `2026-11-16 04:30:18` | `11.63%` | `0.0%` | 43 | 15 | `+0.0s` |
| `2026-11-16 04:00:18` | `30.0%` | `0.0%` | 40 | 14 | `+0.0s` |
| `2026-11-16 03:30:18` | `4.88%` | `0.0%` | 41 | 14 | `+0.0s` |
| `2026-11-16 03:00:20` | `25.58%` | `0.0%` | 43 | 14 | `+0.0s` |
| `2026-11-16 02:30:18` | `9.09%` | `0.0%` | 44 | 14 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:19.546000+00:00`.*
