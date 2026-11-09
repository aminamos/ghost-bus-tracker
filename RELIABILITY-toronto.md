# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-09T07:00:18.510000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `524` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `953` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `40` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 40 | 7.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 365** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 325** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 5 | 5 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
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
| `43959010` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 3579 is broadcasting off-schedule with no vehicle covering 43959010 |
| `58294010` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3213 is broadcasting off-schedule with no vehicle covering 58294010 |
| `84460010` | Route 504 | `N/A` | `SCHEDULED` | Assigned vehicle 8371 is broadcasting off-schedule with no vehicle covering 84460010 |
| `33228010` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3275 is broadcasting off-schedule with no vehicle covering 33228010 |
| `72521010` | Route 305 | `N/A` | `SCHEDULED` | Assigned vehicle 4418 is broadcasting off-schedule with no vehicle covering 72521010 |
| `36551010` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3164 is broadcasting off-schedule with no vehicle covering 36551010 |
| `65319010` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle 4405 is broadcasting off-schedule with no vehicle covering 65319010 |
| `79716010` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3221 is broadcasting off-schedule with no vehicle covering 79716010 |
| `86593010` | Route 386 | `N/A` | `SCHEDULED` | Assigned vehicle 3454 is broadcasting off-schedule with no vehicle covering 86593010 |
| `92267010` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 7217 is broadcasting off-schedule with no vehicle covering 92267010 |
| `28487010` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 6621 is broadcasting off-schedule with no vehicle covering 28487010 |
| `77342010` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8669 is broadcasting off-schedule with no vehicle covering 77342010 |
| `91725010` | Route 352 | `N/A` | `SCHEDULED` | Assigned vehicle 8761 is broadcasting off-schedule with no vehicle covering 91725010 |
| `88767010` | Route 129 | `N/A` | `SCHEDULED` | Assigned vehicle 3256 is broadcasting off-schedule with no vehicle covering 88767010 |
| `65448010` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 3186 is broadcasting off-schedule with no vehicle covering 65448010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:18` | `7.63%` | `0.0%` | 524 | 953 | `+0.0s` |
| `2026-11-09 06:30:18` | `7.34%` | `0.0%` | 695 | 1006 | `+0.0s` |
| `2026-11-09 06:00:18` | `9.01%` | `0.0%` | 932 | 1025 | `+0.0s` |
| `2026-11-09 05:30:18` | `8.09%` | `0.0%` | 1063 | 1054 | `+0.0s` |
| `2026-11-09 05:00:17` | `8.76%` | `0.0%` | 1084 | 1033 | `+0.0s` |
| `2026-11-09 04:30:18` | `7.12%` | `0.0%` | 1096 | 1049 | `+0.0s` |
| `2026-11-09 04:00:18` | `7.2%` | `0.0%` | 1111 | 1139 | `+0.0s` |
| `2026-11-09 03:30:17` | `8.0%` | `0.0%` | 1162 | 1219 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:18.510000+00:00`.*
