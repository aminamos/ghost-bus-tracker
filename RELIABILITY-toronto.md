# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-23T07:01:22.190000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.04%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `297` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `801` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 4.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 343** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 324** | 5 | 2 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 334** | 16 | 13 | 2 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 336** | 8 | 8 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 306** | 14 | 11 | 1 | **`7.14%`** | `0.0%` | `+0.0s` |
| **Route 300** | 31 | 24 | 2 | **`6.45%`** | `0.0%` | `+0.0s` |
| **Route 320** | 25 | 21 | 1 | **`4.0%`** | `0.0%` | `+0.0s` |
| **Route 325** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `68181020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8556 is broadcasting off-schedule with no vehicle covering 68181020 |
| `128376020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4617 is broadcasting off-schedule with no vehicle covering 128376020 |
| `112446020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3325 is broadcasting off-schedule with no vehicle covering 112446020 |
| `21329020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 3548 is broadcasting off-schedule with no vehicle covering 21329020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 7314 is broadcasting off-schedule with no vehicle covering 18602020 |
| `77498020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7090 is broadcasting off-schedule with no vehicle covering 77498020 |
| `48547020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4515 is broadcasting off-schedule with no vehicle covering 48547020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8700 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3215 is broadcasting off-schedule with no vehicle covering 46232020 |
| `53557020` | Route 324 | `N/A` | `SCHEDULED` | Assigned vehicle 6689 is broadcasting off-schedule with no vehicle covering 53557020 |
| `55632020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8612 is broadcasting off-schedule with no vehicle covering 55632020 |
| `22563020` | Route 882 | `N/A` | `SCHEDULED` | Assigned vehicle 9042 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:22` | `4.04%` | `0.0%` | 297 | 801 | `+0.0s` |
| `2026-10-23 06:30:20` | `4.13%` | `0.0%` | 387 | 902 | `+0.0s` |
| `2026-10-23 06:00:19` | `7.93%` | `0.0%` | 555 | 1008 | `+0.0s` |
| `2026-10-23 05:30:19` | `7.29%` | `0.0%` | 768 | 1092 | `+0.0s` |
| `2026-10-23 05:15:26` | `5.94%` | `0.0%` | 893 | 1119 | `+0.0s` |
| `2026-10-23 05:00:36` | `8.28%` | `0.0%` | 1014 | 1142 | `+0.0s` |
| `2026-10-23 04:30:33` | `7.31%` | `0.0%` | 1163 | 1150 | `+0.0s` |
| `2026-10-23 04:00:38` | `8.11%` | `0.0%` | 1183 | 1201 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:22.190000+00:00`.*
