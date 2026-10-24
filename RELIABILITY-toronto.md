# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-24T07:00:22.297000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`3.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `303` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `771` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 3.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 343** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 324** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 312** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 334** | 17 | 13 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |
| **Route 336** | 9 | 8 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route 306** | 14 | 11 | 1 | **`7.14%`** | `0.0%` | `+0.0s` |
| **Route 301** | 20 | 15 | 1 | **`5.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 25 | 21 | 1 | **`4.0%`** | `0.0%` | `+0.0s` |
| **Route 504** | 6 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `128376020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4481 is broadcasting off-schedule with no vehicle covering 128376020 |
| `112446020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3135 is broadcasting off-schedule with no vehicle covering 112446020 |
| `66115020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4488 is broadcasting off-schedule with no vehicle covering 66115020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 1358 is broadcasting off-schedule with no vehicle covering 18602020 |
| `77498020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 3580 is broadcasting off-schedule with no vehicle covering 77498020 |
| `62825020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 7295 is broadcasting off-schedule with no vehicle covering 62825020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8824 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3106 is broadcasting off-schedule with no vehicle covering 46232020 |
| `78404020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 8629 is broadcasting off-schedule with no vehicle covering 78404020 |
| `53557020` | Route 324 | `N/A` | `SCHEDULED` | Assigned vehicle 6687 is broadcasting off-schedule with no vehicle covering 53557020 |
| `4978020` | Route 301 | `N/A` | `SCHEDULED` | Assigned vehicle 3267 is broadcasting off-schedule with no vehicle covering 4978020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 07:00:22` | `3.63%` | `0.0%` | 303 | 771 | `+0.0s` |
| `2026-10-24 06:30:19` | `4.1%` | `0.0%` | 390 | 875 | `+0.0s` |
| `2026-10-24 06:00:20` | `8.56%` | `0.0%` | 549 | 966 | `+0.0s` |
| `2026-10-24 05:30:18` | `7.81%` | `0.0%` | 768 | 1051 | `+0.0s` |
| `2026-10-24 05:00:20` | `8.72%` | `0.0%` | 1009 | 1053 | `+0.0s` |
| `2026-10-24 04:30:18` | `7.07%` | `0.0%` | 1145 | 1075 | `+0.0s` |
| `2026-10-24 04:00:19` | `8.79%` | `0.0%` | 1172 | 1139 | `+0.0s` |
| `2026-10-24 03:30:20` | `5.76%` | `0.0%` | 1198 | 1199 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T07:00:22.297000+00:00`.*
