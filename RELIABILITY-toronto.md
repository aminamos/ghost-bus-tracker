# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-27T07:00:20.085000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.12%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `294` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `798` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `18` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 6.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 365** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 343** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 329** | 4 | 4 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 336** | 8 | 8 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 324** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 312** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 396** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 334** | 17 | 13 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |

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
| `22313020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8608 is broadcasting off-schedule with no vehicle covering 22313020 |
| `112446020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3154 is broadcasting off-schedule with no vehicle covering 112446020 |
| `105934020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3128 is broadcasting off-schedule with no vehicle covering 105934020 |
| `66115020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4504 is broadcasting off-schedule with no vehicle covering 66115020 |
| `103645020` | Route 365 | `N/A` | `SCHEDULED` | Assigned vehicle 8608 is broadcasting off-schedule with no vehicle covering 103645020 |
| `21329020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 3446 is broadcasting off-schedule with no vehicle covering 21329020 |
| `113451020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3338 is broadcasting off-schedule with no vehicle covering 113451020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 7275 is broadcasting off-schedule with no vehicle covering 18602020 |
| `48196020` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 8873 is broadcasting off-schedule with no vehicle covering 48196020 |
| `48547020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4497 is broadcasting off-schedule with no vehicle covering 48547020 |
| `132415020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4657 is broadcasting off-schedule with no vehicle covering 132415020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8661 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3149 is broadcasting off-schedule with no vehicle covering 46232020 |
| `119649020` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9444 is broadcasting off-schedule with no vehicle covering 119649020 |
| `78404020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 9227 is broadcasting off-schedule with no vehicle covering 78404020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 07:00:20` | `6.12%` | `0.0%` | 294 | 798 | `+0.0s` |
| `2026-10-27 06:30:19` | `3.11%` | `0.0%` | 386 | 936 | `+0.0s` |
| `2026-10-27 06:00:24` | `8.9%` | `0.0%` | 562 | 1015 | `+0.0s` |
| `2026-10-27 05:30:20` | `8.16%` | `0.0%` | 760 | 1085 | `+0.0s` |
| `2026-10-27 05:00:18` | `8.92%` | `0.0%` | 998 | 1108 | `+0.0s` |
| `2026-10-27 04:30:18` | `7.27%` | `0.0%` | 1141 | 1133 | `+0.0s` |
| `2026-10-27 04:00:19` | `7.63%` | `0.0%` | 1166 | 1149 | `+0.0s` |
| `2026-10-27 03:30:19` | `8.24%` | `0.0%` | 1177 | 1198 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T07:00:20.085000+00:00`.*
