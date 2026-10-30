# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-30T07:00:20.842000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.08%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `295` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `780` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `15` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 15 | 5.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 329** | 4 | 4 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 354** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 312** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 345** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 396** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 334** | 17 | 13 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |
| **Route 336** | 9 | 8 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route 300** | 28 | 23 | 2 | **`7.14%`** | `0.0%` | `+0.0s` |

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
| `134554020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4639 is broadcasting off-schedule with no vehicle covering 134554020 |
| `41875020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4566 is broadcasting off-schedule with no vehicle covering 41875020 |
| `20869020` | Route 345 | `N/A` | `SCHEDULED` | Assigned vehicle 7314 is broadcasting off-schedule with no vehicle covering 20869020 |
| `21329020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 3536 is broadcasting off-schedule with no vehicle covering 21329020 |
| `113451020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3336 is broadcasting off-schedule with no vehicle covering 113451020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 7305 is broadcasting off-schedule with no vehicle covering 18602020 |
| `69874020` | Route 354 | `N/A` | `SCHEDULED` | Assigned vehicle 8810 is broadcasting off-schedule with no vehicle covering 69874020 |
| `48196020` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 8866 is broadcasting off-schedule with no vehicle covering 48196020 |
| `105672020` | Route 354 | `N/A` | `SCHEDULED` | Assigned vehicle 8810 is broadcasting off-schedule with no vehicle covering 105672020 |
| `48547020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4636 is broadcasting off-schedule with no vehicle covering 48547020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8812 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 8626 is broadcasting off-schedule with no vehicle covering 46232020 |
| `119649020` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9463 is broadcasting off-schedule with no vehicle covering 119649020 |
| `55632020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8543 is broadcasting off-schedule with no vehicle covering 55632020 |
| `59431020` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 7231 is broadcasting off-schedule with no vehicle covering 59431020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 07:00:20` | `5.08%` | `0.0%` | 295 | 780 | `+0.0s` |
| `2026-10-30 06:30:19` | `4.16%` | `0.0%` | 385 | 891 | `+0.0s` |
| `2026-10-30 06:00:20` | `9.11%` | `0.0%` | 549 | 1015 | `+0.0s` |
| `2026-10-30 05:30:20` | `8.13%` | `0.0%` | 750 | 1082 | `+0.0s` |
| `2026-10-30 05:00:18` | `9.31%` | `0.0%` | 988 | 1100 | `+0.0s` |
| `2026-10-30 04:30:18` | `7.14%` | `0.0%` | 1106 | 1088 | `+0.0s` |
| `2026-10-30 04:00:18` | `7.47%` | `0.0%` | 1151 | 1155 | `+0.0s` |
| `2026-10-30 03:30:18` | `6.49%` | `0.0%` | 1187 | 1215 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:20.842000+00:00`.*
