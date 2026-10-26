# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-26T07:00:18.626000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.14%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `280` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `744` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `20` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 20 | 7.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 343** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 354** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 312** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 340** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 306** | 12 | 10 | 3 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 315** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 316** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 304** | 15 | 11 | 3 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 345** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `52975010` | Route 315 | `N/A` | `SCHEDULED` | Assigned vehicle 3332 is broadcasting off-schedule with no vehicle covering 52975010 |
| `125447010` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3305 is broadcasting off-schedule with no vehicle covering 125447010 |
| `58643010` | Route 345 | `N/A` | `SCHEDULED` | Assigned vehicle 7283 is broadcasting off-schedule with no vehicle covering 58643010 |
| `68377010` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3326 is broadcasting off-schedule with no vehicle covering 68377010 |
| `82003010` | Route 316 | `N/A` | `SCHEDULED` | Assigned vehicle 3127 is broadcasting off-schedule with no vehicle covering 82003010 |
| `117396010` | Route 304 | `N/A` | `SCHEDULED` | Assigned vehicle 4413 is broadcasting off-schedule with no vehicle covering 117396010 |
| `89176010` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3605 is broadcasting off-schedule with no vehicle covering 89176010 |
| `34115010` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3340 is broadcasting off-schedule with no vehicle covering 34115010 |
| `96279010` | Route 340 | `N/A` | `SCHEDULED` | Assigned vehicle 3349 is broadcasting off-schedule with no vehicle covering 96279010 |
| `124238010` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 1358 is broadcasting off-schedule with no vehicle covering 124238010 |
| `96555010` | Route 304 | `N/A` | `SCHEDULED` | Assigned vehicle 4611 is broadcasting off-schedule with no vehicle covering 96555010 |
| `41893010` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4453 is broadcasting off-schedule with no vehicle covering 41893010 |
| `45032010` | Route 304 | `N/A` | `SCHEDULED` | Assigned vehicle 4629 is broadcasting off-schedule with no vehicle covering 45032010 |
| `98531010` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4419 is broadcasting off-schedule with no vehicle covering 98531010 |
| `40232010` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 6611 is broadcasting off-schedule with no vehicle covering 40232010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:18` | `7.14%` | `0.0%` | 280 | 744 | `+0.0s` |
| `2026-10-26 06:30:35` | `6.93%` | `0.0%` | 361 | 836 | `+0.0s` |
| `2026-10-26 06:00:28` | `8.33%` | `0.0%` | 516 | 959 | `+0.0s` |
| `2026-10-26 05:30:19` | `9.14%` | `0.0%` | 689 | 1005 | `+0.0s` |
| `2026-10-26 05:00:22` | `8.86%` | `0.0%` | 937 | 1046 | `+0.0s` |
| `2026-10-26 04:30:29` | `10.79%` | `0.0%` | 1075 | 1053 | `+0.0s` |
| `2026-10-26 04:00:18` | `8.88%` | `0.0%` | 1092 | 1057 | `+0.0s` |
| `2026-10-26 03:30:33` | `8.4%` | `0.0%` | 1095 | 1083 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:18.626000+00:00`.*
