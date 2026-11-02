# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-02T07:00:18.031000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.82%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `524` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `897` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `41` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 41 | 7.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 365** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 396** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 373** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `43959010` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7128 is broadcasting off-schedule with no vehicle covering 43959010 |
| `58294010` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 9227 is broadcasting off-schedule with no vehicle covering 58294010 |
| `84460010` | Route 504 | `N/A` | `SCHEDULED` | Assigned vehicle 3277 is broadcasting off-schedule with no vehicle covering 84460010 |
| `33228010` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3646 is broadcasting off-schedule with no vehicle covering 33228010 |
| `58717010` | Route 354 | `N/A` | `SCHEDULED` | Assigned vehicle 9231 is broadcasting off-schedule with no vehicle covering 58717010 |
| `72521010` | Route 305 | `N/A` | `SCHEDULED` | Assigned vehicle 4646 is broadcasting off-schedule with no vehicle covering 72521010 |
| `36551010` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3229 is broadcasting off-schedule with no vehicle covering 36551010 |
| `68223010` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7299 is broadcasting off-schedule with no vehicle covering 68223010 |
| `79716010` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3108 is broadcasting off-schedule with no vehicle covering 79716010 |
| `17141010` | Route 504 | `N/A` | `SCHEDULED` | Assigned vehicle 8457 is broadcasting off-schedule with no vehicle covering 17141010 |
| `86593010` | Route 386 | `N/A` | `SCHEDULED` | Assigned vehicle 3491 is broadcasting off-schedule with no vehicle covering 86593010 |
| `92267010` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 7218 is broadcasting off-schedule with no vehicle covering 92267010 |
| `77342010` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8795 is broadcasting off-schedule with no vehicle covering 77342010 |
| `91725010` | Route 352 | `N/A` | `SCHEDULED` | Assigned vehicle 8800 is broadcasting off-schedule with no vehicle covering 91725010 |
| `11075010` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 3198 is broadcasting off-schedule with no vehicle covering 11075010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `7.82%` | `0.0%` | 524 | 897 | `+0.0s` |
| `2026-11-02 06:30:17` | `8.43%` | `0.0%` | 688 | 963 | `+0.0s` |
| `2026-11-02 06:00:20` | `8.58%` | `0.0%` | 921 | 997 | `+0.0s` |
| `2026-11-02 05:30:19` | `9.0%` | `0.0%` | 1045 | 993 | `+0.0s` |
| `2026-11-02 05:00:18` | `9.25%` | `0.0%` | 1059 | 968 | `+0.0s` |
| `2026-11-02 04:30:18` | `8.2%` | `0.0%` | 1073 | 992 | `+0.0s` |
| `2026-11-02 04:00:18` | `8.14%` | `0.0%` | 1094 | 1057 | `+0.0s` |
| `2026-11-02 03:30:19` | `7.17%` | `0.0%` | 1158 | 1138 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.031000+00:00`.*
