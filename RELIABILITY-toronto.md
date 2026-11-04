# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-04T07:00:19.307000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.02%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `561` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1004` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `45` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 45 | 8.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 365** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 185** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 385** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `83352020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8570 is broadcasting off-schedule with no vehicle covering 83352020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7246 is broadcasting off-schedule with no vehicle covering 67227020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3154 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3360 is broadcasting off-schedule with no vehicle covering 26944020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 8923 is broadcasting off-schedule with no vehicle covering 65345020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8520 is broadcasting off-schedule with no vehicle covering 27458020 |
| `18967020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8570 is broadcasting off-schedule with no vehicle covering 18967020 |
| `21609020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7037 is broadcasting off-schedule with no vehicle covering 21609020 |
| `75378020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7010 is broadcasting off-schedule with no vehicle covering 75378020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8844 is broadcasting off-schedule with no vehicle covering 32959020 |
| `85429020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3210 is broadcasting off-schedule with no vehicle covering 85429020 |
| `59341020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8637 is broadcasting off-schedule with no vehicle covering 59341020 |
| `54511020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7037 is broadcasting off-schedule with no vehicle covering 54511020 |
| `91595020` | Route 60 | `N/A` | `SCHEDULED` | Assigned vehicle 7007 is broadcasting off-schedule with no vehicle covering 91595020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7307 is broadcasting off-schedule with no vehicle covering 32095020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:19` | `8.02%` | `0.0%` | 561 | 1004 | `+0.0s` |
| `2026-11-04 06:30:21` | `8.31%` | `0.0%` | 770 | 1066 | `+0.0s` |
| `2026-11-04 06:00:18` | `9.18%` | `0.0%` | 991 | 1088 | `+0.0s` |
| `2026-11-04 05:30:17` | `7.61%` | `0.0%` | 1117 | 1082 | `+0.0s` |
| `2026-11-04 05:00:17` | `8.65%` | `0.0%` | 1156 | 1153 | `+0.0s` |
| `2026-11-04 04:30:17` | `8.5%` | `0.0%` | 1165 | 1196 | `+0.0s` |
| `2026-11-04 04:00:20` | `6.56%` | `0.0%` | 1205 | 1309 | `+0.0s` |
| `2026-11-04 03:30:19` | `5.77%` | `0.0%` | 1299 | 1428 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:19.307000+00:00`.*
