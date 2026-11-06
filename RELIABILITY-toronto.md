# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-06T07:00:17.916000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.99%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `558` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `993` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `39` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 39 | 7.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 365** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 3586 is broadcasting off-schedule with no vehicle covering 33114020 |
| `83352020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8558 is broadcasting off-schedule with no vehicle covering 83352020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7319 is broadcasting off-schedule with no vehicle covering 67227020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 9238 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8126 is broadcasting off-schedule with no vehicle covering 26944020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4410 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8918 is broadcasting off-schedule with no vehicle covering 27458020 |
| `18967020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8558 is broadcasting off-schedule with no vehicle covering 18967020 |
| `56365020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8824 is broadcasting off-schedule with no vehicle covering 56365020 |
| `21609020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 3590 is broadcasting off-schedule with no vehicle covering 21609020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8851 is broadcasting off-schedule with no vehicle covering 32959020 |
| `59341020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8685 is broadcasting off-schedule with no vehicle covering 59341020 |
| `54511020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 3590 is broadcasting off-schedule with no vehicle covering 54511020 |
| `72823020` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 8824 is broadcasting off-schedule with no vehicle covering 72823020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7290 is broadcasting off-schedule with no vehicle covering 32095020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:17` | `6.99%` | `0.0%` | 558 | 993 | `+0.0s` |
| `2026-11-06 06:30:18` | `9.51%` | `0.0%` | 768 | 1054 | `+0.0s` |
| `2026-11-06 06:00:18` | `9.2%` | `0.0%` | 1000 | 1070 | `+0.0s` |
| `2026-11-06 05:30:18` | `7.58%` | `0.0%` | 1135 | 1098 | `+0.0s` |
| `2026-11-06 05:00:18` | `7.29%` | `0.0%` | 1166 | 1131 | `+0.0s` |
| `2026-11-06 04:30:19` | `8.14%` | `0.0%` | 1180 | 1185 | `+0.0s` |
| `2026-11-06 04:00:20` | `5.96%` | `0.0%` | 1208 | 1302 | `+0.0s` |
| `2026-11-06 03:30:19` | `6.96%` | `0.0%` | 1279 | 1413 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:17.916000+00:00`.*
