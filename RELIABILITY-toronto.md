# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-21T07:00:18.277000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.93%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `563` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `990` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 39 | 6.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 105** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 373** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7091 is broadcasting off-schedule with no vehicle covering 33114020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7243 is broadcasting off-schedule with no vehicle covering 67227020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3208 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8312 is broadcasting off-schedule with no vehicle covering 26944020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 8864 is broadcasting off-schedule with no vehicle covering 65345020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4495 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8579 is broadcasting off-schedule with no vehicle covering 27458020 |
| `56365020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8799 is broadcasting off-schedule with no vehicle covering 56365020 |
| `21609020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7005 is broadcasting off-schedule with no vehicle covering 21609020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 3624 is broadcasting off-schedule with no vehicle covering 32959020 |
| `54511020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7005 is broadcasting off-schedule with no vehicle covering 54511020 |
| `72823020` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 8799 is broadcasting off-schedule with no vehicle covering 72823020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7302 is broadcasting off-schedule with no vehicle covering 32095020 |
| `11040020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 8864 is broadcasting off-schedule with no vehicle covering 11040020 |
| `96253020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 7212 is broadcasting off-schedule with no vehicle covering 96253020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `6.93%` | `0.0%` | 563 | 990 | `+0.0s` |
| `2026-11-21 06:30:19` | `8.69%` | `0.0%` | 771 | 1031 | `+0.0s` |
| `2026-11-21 06:00:18` | `9.54%` | `0.0%` | 985 | 1052 | `+0.0s` |
| `2026-11-21 05:30:17` | `6.38%` | `0.0%` | 1129 | 1050 | `+0.0s` |
| `2026-11-21 05:00:19` | `8.26%` | `0.0%` | 1150 | 1088 | `+0.0s` |
| `2026-11-21 04:30:18` | `8.38%` | `0.0%` | 1169 | 1160 | `+0.0s` |
| `2026-11-21 04:00:17` | `7.03%` | `0.0%` | 1181 | 1262 | `+0.0s` |
| `2026-11-21 03:30:17` | `7.01%` | `0.0%` | 1269 | 1404 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.277000+00:00`.*
