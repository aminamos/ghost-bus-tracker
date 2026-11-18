# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-18T07:00:19.997000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.48%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `571` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1049` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `37` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 37 | 6.5% |
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
| **Route 84** | 6 | 5 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7007 is broadcasting off-schedule with no vehicle covering 33114020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 9207 is broadcasting off-schedule with no vehicle covering 36540020 |
| `52549020` | Route 305 | `N/A` | `SCHEDULED` | Assigned vehicle 4560 is broadcasting off-schedule with no vehicle covering 52549020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4512 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8420 is broadcasting off-schedule with no vehicle covering 27458020 |
| `21609020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7058 is broadcasting off-schedule with no vehicle covering 21609020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8865 is broadcasting off-schedule with no vehicle covering 32959020 |
| `59341020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8790 is broadcasting off-schedule with no vehicle covering 59341020 |
| `54511020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 7058 is broadcasting off-schedule with no vehicle covering 54511020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7254 is broadcasting off-schedule with no vehicle covering 32095020 |
| `96253020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 7292 is broadcasting off-schedule with no vehicle covering 96253020 |
| `24550020` | Route 24 | `N/A` | `SCHEDULED` | Assigned vehicle 8517 is missing from active GPS transponder fleet |
| `33781020` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 8954 is broadcasting off-schedule with no vehicle covering 33781020 |
| `43639020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 8384 is broadcasting off-schedule with no vehicle covering 43639020 |
| `101032020` | Route 27 | `N/A` | `SCHEDULED` | Assigned vehicle 7203 is broadcasting off-schedule with no vehicle covering 101032020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 07:00:19` | `6.48%` | `0.0%` | 571 | 1049 | `+0.0s` |
| `2026-11-18 06:30:18` | `9.27%` | `0.0%` | 766 | 1121 | `+0.0s` |
| `2026-11-18 06:00:19` | `10.27%` | `0.0%` | 983 | 1145 | `+0.0s` |
| `2026-11-18 05:30:20` | `6.83%` | `0.0%` | 1127 | 1139 | `+0.0s` |
| `2026-11-18 05:00:18` | `8.15%` | `0.0%` | 1153 | 1157 | `+0.0s` |
| `2026-11-18 04:30:18` | `7.56%` | `0.0%` | 1177 | 1203 | `+0.0s` |
| `2026-11-18 04:00:17` | `7.34%` | `0.0%` | 1199 | 1325 | `+0.0s` |
| `2026-11-18 03:30:18` | `6.68%` | `0.0%` | 1287 | 1450 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T07:00:19.997000+00:00`.*
