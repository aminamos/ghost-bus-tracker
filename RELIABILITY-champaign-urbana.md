# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-14T07:00:18.466000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 13.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GREEN LATE NIGHT** | 6 | 2 | 6 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT** | 6 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING** | 17 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER LATE NIGHT** | 7 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `8GN531__GR3_UI` | Route GREEN LATE NIGHT | `01:20:00` | `SCHEDULED` | Assigned vehicle 2429 is broadcasting off-schedule with no vehicle covering 8GN531__GR3_UI |
| `[@7.0.38112640@][4][1219153573468]/9__GR3_UI` | Route GREEN LATE NIGHT | `01:43:00` | `SCHEDULED` | Assigned vehicle 2429 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][4][1219153573468]/9__GR3_UI |
| `[@7.0.38112640@][3][1219153533843]/3__GN7_UIF` | Route GREEN LATE NIGHT | `01:40:00` | `SCHEDULED` | Assigned vehicle 1604 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153533843]/3__GN7_UIF |
| `3GR788__GR3_UI` | Route GREEN LATE NIGHT | `01:03:00` | `SCHEDULED` | Assigned vehicle 2429 is broadcasting off-schedule with no vehicle covering 3GR788__GR3_UI |
| `[@7.0.38112640@][3][1219153533843]/2__GN7_UIF` | Route GREEN LATE NIGHT | `01:00:00` | `SCHEDULED` | Assigned vehicle 1604 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153533843]/2__GN7_UIF |
| `[@7.0.38112640@][4][1219153573468]/8__GN7_UIF` | Route GREEN LATE NIGHT | `01:23:00` | `SCHEDULED` | Assigned vehicle 1604 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][4][1219153573468]/8__GN7_UIF |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:18` | `13.64%` | `0.0%` | 44 | 15 | `+0.0s` |
| `2026-11-14 06:30:18` | `10.42%` | `0.0%` | 48 | 14 | `+0.0s` |
| `2026-11-14 06:00:18` | `20.0%` | `0.0%` | 45 | 16 | `+0.0s` |
| `2026-11-14 05:30:18` | `7.14%` | `0.0%` | 56 | 25 | `+0.0s` |
| `2026-11-14 05:00:19` | `11.67%` | `0.0%` | 60 | 29 | `+0.0s` |
| `2026-11-14 04:30:18` | `13.43%` | `0.0%` | 67 | 30 | `+0.0s` |
| `2026-11-14 04:00:19` | `21.13%` | `0.0%` | 71 | 30 | `+0.0s` |
| `2026-11-14 03:30:18` | `8.96%` | `0.0%` | 67 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:18.466000+00:00`.*
