# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-22T07:00:18.090000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.1%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `543` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `898` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `44` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 44 | 8.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 151** | 3 | 1 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 304** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 6 | 5 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 396** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `38605070` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 9239 is broadcasting off-schedule with no vehicle covering 38605070 |
| `97344070` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle 4471 is broadcasting off-schedule with no vehicle covering 97344070 |
| `31985070` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3125 is broadcasting off-schedule with no vehicle covering 31985070 |
| `48957070` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 8794 is broadcasting off-schedule with no vehicle covering 48957070 |
| `12892070` | Route 70 | `N/A` | `SCHEDULED` | Assigned vehicle 8499 is broadcasting off-schedule with no vehicle covering 12892070 |
| `48799070` | Route 151 | `N/A` | `SCHEDULED` | Assigned vehicle 9223 is broadcasting off-schedule with no vehicle covering 48799070 |
| `71216070` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7041 is broadcasting off-schedule with no vehicle covering 71216070 |
| `77919070` | Route 304 | `N/A` | `SCHEDULED` | Assigned vehicle 4639 is broadcasting off-schedule with no vehicle covering 77919070 |
| `54732070` | Route 129 | `N/A` | `SCHEDULED` | Assigned vehicle 8962 is broadcasting off-schedule with no vehicle covering 54732070 |
| `58852070` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 8871 is broadcasting off-schedule with no vehicle covering 58852070 |
| `72425070` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 9110 is broadcasting off-schedule with no vehicle covering 72425070 |
| `7915070` | Route 151 | `N/A` | `SCHEDULED` | Assigned vehicle 9223 is broadcasting off-schedule with no vehicle covering 7915070 |
| `17528070` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 3318 is broadcasting off-schedule with no vehicle covering 17528070 |
| `67504070` | Route 102 | `N/A` | `SCHEDULED` | Assigned vehicle 6094 is broadcasting off-schedule with no vehicle covering 67504070 |
| `44127070` | Route 504 | `N/A` | `SCHEDULED` | Assigned vehicle 4625 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `8.1%` | `0.0%` | 543 | 898 | `+0.0s` |
| `2026-11-22 06:30:18` | `6.94%` | `0.0%` | 735 | 968 | `+0.0s` |
| `2026-11-22 06:00:17` | `8.48%` | `0.0%` | 955 | 975 | `+0.0s` |
| `2026-11-22 05:30:20` | `6.84%` | `0.0%` | 1097 | 1002 | `+0.0s` |
| `2026-11-22 05:00:18` | `7.39%` | `0.0%` | 1109 | 1021 | `+0.0s` |
| `2026-11-22 04:30:17` | `5.3%` | `0.0%` | 1114 | 1091 | `+0.0s` |
| `2026-11-22 04:00:17` | `7.07%` | `0.0%` | 1132 | 1185 | `+0.0s` |
| `2026-11-22 03:30:19` | `6.56%` | `0.0%` | 1205 | 1256 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.090000+00:00`.*
