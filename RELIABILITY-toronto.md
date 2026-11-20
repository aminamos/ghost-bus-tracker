# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-20T07:00:19.907000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.93%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `560` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `991` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `50` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 50 | 8.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 185** | 3 | 1 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 365** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 343** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7108 is broadcasting off-schedule with no vehicle covering 33114020 |
| `83352020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8483 is broadcasting off-schedule with no vehicle covering 83352020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7271 is broadcasting off-schedule with no vehicle covering 67227020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 9230 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8333 is broadcasting off-schedule with no vehicle covering 26944020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 8758 is broadcasting off-schedule with no vehicle covering 65345020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4622 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8606 is broadcasting off-schedule with no vehicle covering 27458020 |
| `18967020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8483 is broadcasting off-schedule with no vehicle covering 18967020 |
| `56365020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8673 is broadcasting off-schedule with no vehicle covering 56365020 |
| `21609020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7056 is broadcasting off-schedule with no vehicle covering 21609020 |
| `75378020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7026 is broadcasting off-schedule with no vehicle covering 75378020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 3614 is broadcasting off-schedule with no vehicle covering 32959020 |
| `96065020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8524 is broadcasting off-schedule with no vehicle covering 96065020 |
| `54511020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7056 is broadcasting off-schedule with no vehicle covering 54511020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:19` | `8.93%` | `0.0%` | 560 | 991 | `+0.0s` |
| `2026-11-20 06:30:18` | `8.78%` | `0.0%` | 763 | 1048 | `+0.0s` |
| `2026-11-20 06:00:19` | `9.79%` | `0.0%` | 981 | 1071 | `+0.0s` |
| `2026-11-20 05:30:18` | `7.6%` | `0.0%` | 1119 | 1064 | `+0.0s` |
| `2026-11-20 05:00:18` | `8.49%` | `0.0%` | 1143 | 1111 | `+0.0s` |
| `2026-11-20 04:30:17` | `7.22%` | `0.0%` | 1177 | 1170 | `+0.0s` |
| `2026-11-20 04:00:18` | `7.35%` | `0.0%` | 1197 | 1277 | `+0.0s` |
| `2026-11-20 03:30:18` | `6.69%` | `0.0%` | 1285 | 1378 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:19.907000+00:00`.*
