# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-08T07:00:17.791000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.24%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `525` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `912` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `38` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 38 | 7.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 185** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 343** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 6 | 5 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 396** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
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
| `38605070` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3111 is broadcasting off-schedule with no vehicle covering 38605070 |
| `31985070` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3148 is broadcasting off-schedule with no vehicle covering 31985070 |
| `48957070` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 8715 is broadcasting off-schedule with no vehicle covering 48957070 |
| `12892070` | Route 70 | `N/A` | `SCHEDULED` | Assigned vehicle 8412 is broadcasting off-schedule with no vehicle covering 12892070 |
| `86858070` | Route 185 | `N/A` | `SCHEDULED` | Assigned vehicle 1656 is broadcasting off-schedule with no vehicle covering 86858070 |
| `71216070` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7109 is broadcasting off-schedule with no vehicle covering 71216070 |
| `77919070` | Route 304 | `N/A` | `SCHEDULED` | Assigned vehicle 4453 is broadcasting off-schedule with no vehicle covering 77919070 |
| `54732070` | Route 129 | `N/A` | `SCHEDULED` | Assigned vehicle 8625 is broadcasting off-schedule with no vehicle covering 54732070 |
| `58852070` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 3276 is broadcasting off-schedule with no vehicle covering 58852070 |
| `28383070` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3169 is broadcasting off-schedule with no vehicle covering 28383070 |
| `17528070` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 3603 is broadcasting off-schedule with no vehicle covering 17528070 |
| `56880070` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 9223 is broadcasting off-schedule with no vehicle covering 56880070 |
| `100425070` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3346 is broadcasting off-schedule with no vehicle covering 100425070 |
| `95859070` | Route 36 | `N/A` | `SCHEDULED` | Assigned vehicle 9205 is broadcasting off-schedule with no vehicle covering 95859070 |
| `80713070` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 7284 is broadcasting off-schedule with no vehicle covering 80713070 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:17` | `7.24%` | `0.0%` | 525 | 912 | `+0.0s` |
| `2026-11-08 06:30:18` | `7.03%` | `0.0%` | 725 | 1005 | `+0.0s` |
| `2026-11-08 06:00:17` | `7.92%` | `0.0%` | 960 | 1018 | `+0.0s` |
| `2026-11-08 05:30:18` | `9.1%` | `0.0%` | 1099 | 1019 | `+0.0s` |
| `2026-11-08 05:00:18` | `6.95%` | `0.0%` | 1123 | 1043 | `+0.0s` |
| `2026-11-08 04:30:20` | `6.88%` | `0.0%` | 1133 | 1118 | `+0.0s` |
| `2026-11-08 04:00:18` | `7.12%` | `0.0%` | 1152 | 1201 | `+0.0s` |
| `2026-11-08 03:30:18` | `7.64%` | `0.0%` | 1218 | 1269 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.791000+00:00`.*
