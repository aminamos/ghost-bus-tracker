# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-28T07:00:18.066000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.68%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `299` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `819` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `14` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 14 | 4.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 312** | 3 | 3 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 343** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 324** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 329** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 396** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 336** | 8 | 8 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 334** | 17 | 13 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |
| **Route 306** | 15 | 11 | 1 | **`6.67%`** | `0.0%` | `+0.0s` |
| **Route 300** | 31 | 24 | 2 | **`6.45%`** | `0.0%` | `+0.0s` |

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
| `134554020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4418 is broadcasting off-schedule with no vehicle covering 134554020 |
| `41875020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4435 is broadcasting off-schedule with no vehicle covering 41875020 |
| `21329020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8830 is broadcasting off-schedule with no vehicle covering 21329020 |
| `93411020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4654 is broadcasting off-schedule with no vehicle covering 93411020 |
| `113451020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3338 is broadcasting off-schedule with no vehicle covering 113451020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 7282 is missing from active GPS transponder fleet |
| `48196020` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3611 is broadcasting off-schedule with no vehicle covering 48196020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8701 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3179 is broadcasting off-schedule with no vehicle covering 46232020 |
| `78404020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 9210 is broadcasting off-schedule with no vehicle covering 78404020 |
| `53557020` | Route 324 | `N/A` | `SCHEDULED` | Assigned vehicle 6677 is broadcasting off-schedule with no vehicle covering 53557020 |
| `55632020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8497 is broadcasting off-schedule with no vehicle covering 55632020 |
| `4978020` | Route 301 | `N/A` | `SCHEDULED` | Assigned vehicle 3259 is broadcasting off-schedule with no vehicle covering 4978020 |
| `59431020` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9454 is broadcasting off-schedule with no vehicle covering 59431020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `4.68%` | `0.0%` | 299 | 819 | `+0.0s` |
| `2026-10-28 06:30:18` | `3.25%` | `0.0%` | 400 | 904 | `+0.0s` |
| `2026-10-28 06:00:18` | `7.81%` | `0.0%` | 576 | 1032 | `+0.0s` |
| `2026-10-28 05:30:21` | `6.89%` | `0.0%` | 769 | 1090 | `+0.0s` |
| `2026-10-28 05:00:21` | `8.07%` | `0.0%` | 991 | 1107 | `+0.0s` |
| `2026-10-28 04:30:20` | `6.54%` | `0.0%` | 1132 | 1120 | `+0.0s` |
| `2026-10-28 04:00:20` | `8.03%` | `0.0%` | 1170 | 1163 | `+0.0s` |
| `2026-10-28 03:30:18` | `6.42%` | `0.0%` | 1200 | 1223 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.066000+00:00`.*
