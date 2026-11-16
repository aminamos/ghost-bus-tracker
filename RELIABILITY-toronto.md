# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-16T07:00:19.236000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.11%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `530` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `961` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `43` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 43 | 8.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 343** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 365** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 6 | 5 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
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
| `43959010` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7102 is broadcasting off-schedule with no vehicle covering 43959010 |
| `58294010` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 9213 is broadcasting off-schedule with no vehicle covering 58294010 |
| `84460010` | Route 504 | `N/A` | `SCHEDULED` | Assigned vehicle 8363 is broadcasting off-schedule with no vehicle covering 84460010 |
| `33228010` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3630 is broadcasting off-schedule with no vehicle covering 33228010 |
| `58717010` | Route 354 | `N/A` | `SCHEDULED` | Assigned vehicle 3123 is broadcasting off-schedule with no vehicle covering 58717010 |
| `72521010` | Route 305 | `N/A` | `SCHEDULED` | Assigned vehicle 4623 is broadcasting off-schedule with no vehicle covering 72521010 |
| `36551010` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3205 is broadcasting off-schedule with no vehicle covering 36551010 |
| `68223010` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7316 is broadcasting off-schedule with no vehicle covering 68223010 |
| `79716010` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3128 is broadcasting off-schedule with no vehicle covering 79716010 |
| `57033010` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4438 is broadcasting off-schedule with no vehicle covering 57033010 |
| `86593010` | Route 386 | `N/A` | `SCHEDULED` | Assigned vehicle 3529 is broadcasting off-schedule with no vehicle covering 86593010 |
| `92267010` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 7286 is broadcasting off-schedule with no vehicle covering 92267010 |
| `77342010` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 6606 is broadcasting off-schedule with no vehicle covering 77342010 |
| `91725010` | Route 352 | `N/A` | `SCHEDULED` | Assigned vehicle 8790 is broadcasting off-schedule with no vehicle covering 91725010 |
| `11075010` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 8888 is broadcasting off-schedule with no vehicle covering 11075010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:19` | `8.11%` | `0.0%` | 530 | 961 | `+0.0s` |
| `2026-11-16 06:30:20` | `7.3%` | `0.0%` | 699 | 1007 | `+0.0s` |
| `2026-11-16 06:00:18` | `10.21%` | `0.0%` | 940 | 1036 | `+0.0s` |
| `2026-11-16 05:30:18` | `10.49%` | `0.0%` | 1068 | 1073 | `+0.0s` |
| `2026-11-16 05:00:18` | `8.96%` | `0.0%` | 1082 | 1062 | `+0.0s` |
| `2026-11-16 04:30:18` | `8.43%` | `0.0%` | 1091 | 1028 | `+0.0s` |
| `2026-11-16 04:00:18` | `7.69%` | `0.0%` | 1105 | 1107 | `+0.0s` |
| `2026-11-16 03:30:17` | `7.86%` | `0.0%` | 1170 | 1192 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:19.236000+00:00`.*
