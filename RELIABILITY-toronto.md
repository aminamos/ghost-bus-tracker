# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-31T07:00:20.380000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`3.31%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `302` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `780` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 3.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 343** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 52** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 324** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 312** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 306** | 15 | 12 | 2 | **`13.33%`** | `0.0%` | `+0.0s` |
| **Route 335** | 8 | 6 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 334** | 17 | 13 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |
| **Route 336** | 9 | 8 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route 325** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 307** | 7 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `41875020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4502 is broadcasting off-schedule with no vehicle covering 41875020 |
| `128376020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4404 is broadcasting off-schedule with no vehicle covering 128376020 |
| `112446020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3149 is broadcasting off-schedule with no vehicle covering 112446020 |
| `59155020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 8877 is broadcasting off-schedule with no vehicle covering 59155020 |
| `66115020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4661 is broadcasting off-schedule with no vehicle covering 66115020 |
| `21329020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 3443 is broadcasting off-schedule with no vehicle covering 21329020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 7265 is broadcasting off-schedule with no vehicle covering 18602020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8691 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3246 is broadcasting off-schedule with no vehicle covering 46232020 |
| `53557020` | Route 324 | `N/A` | `SCHEDULED` | Assigned vehicle 8799 is broadcasting off-schedule with no vehicle covering 53557020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:20` | `3.31%` | `0.0%` | 302 | 780 | `+0.0s` |
| `2026-10-31 06:30:18` | `3.37%` | `0.0%` | 386 | 953 | `+0.0s` |
| `2026-10-31 06:00:19` | `9.07%` | `0.0%` | 540 | 1055 | `+0.0s` |
| `2026-10-31 05:30:18` | `7.53%` | `0.0%` | 757 | 1107 | `+0.0s` |
| `2026-10-31 05:00:21` | `7.61%` | `0.0%` | 972 | 1136 | `+0.0s` |
| `2026-10-31 04:30:20` | `6.26%` | `0.0%` | 1134 | 1176 | `+0.0s` |
| `2026-10-31 04:00:17` | `8.97%` | `0.0%` | 1159 | 1201 | `+0.0s` |
| `2026-10-31 03:30:17` | `5.58%` | `0.0%` | 1183 | 1219 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:20.380000+00:00`.*
