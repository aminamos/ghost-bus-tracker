# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-21T19:30:37.793000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `154` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `102` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `33` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 33 | 21.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 61 | 31 | 25 | **`40.98%`** | `0.0%` | `+0.0s` |
| **Route 512** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 9 | 6 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 535** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 16 | 16 | 2 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 17 | 17 | 1 | **`5.88%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 6 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 6 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2117` | Route 100479 | `19:29:30` | `DUPLICATED` | Assigned vehicle 587.595248 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2117 |
| `4288020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9222 is broadcasting off-schedule with no vehicle covering 4288020 |
| `17069062__H:121:0:Weekday:3:26SEP:52033:12345` | Route 535 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52033:12345 is missing from active GPS transponder fleet |
| `17069013__H:121:0:Weekday:3:26SEP:52038:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52038:12345 is missing from active GPS transponder fleet |
| `2567020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9714 is broadcasting off-schedule with no vehicle covering 2567020 |
| `1356020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9715 is broadcasting off-schedule with no vehicle covering 1356020 |
| `3852020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9723 is broadcasting off-schedule with no vehicle covering 3852020 |
| `3438020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9729 is broadcasting off-schedule with no vehicle covering 3438020 |
| `122020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9728 is broadcasting off-schedule with no vehicle covering 122020 |
| `682020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9731 is broadcasting off-schedule with no vehicle covering 682020 |
| `1402020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9308 is broadcasting off-schedule with no vehicle covering 1402020 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_3013` | Route 2LINE | `05:35:30` | `DUPLICATED` | Assigned vehicle 585.538539 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_3013 |
| `17068791__H:121:0:Weekday:3:26SEP:52037:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52037:12345 is missing from active GPS transponder fleet |
| `17068725__H:121:0:Weekday:3:26SEP:52037:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52037:12345 is missing from active GPS transponder fleet |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_4072` | Route 2LINE | `13:34:30` | `DUPLICATED` | Assigned vehicle 583.824603 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_4072 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 19:30:37` | `21.43%` | `0.0%` | 154 | 102 | `+0.0s` |
| `2026-10-21 19:00:49` | `23.9%` | `0.0%` | 159 | 102 | `+0.0s` |
| `2026-10-21 18:30:38` | `24.0%` | `0.0%` | 150 | 101 | `+0.0s` |
| `2026-10-21 18:00:36` | `0.0%` | `0.0%` | 19 | 108 | `+0.0s` |
| `2026-10-21 16:31:23` | `21.35%` | `0.0%` | 178 | 125 | `+0.0s` |
| `2026-10-21 15:30:36` | `20.29%` | `0.0%` | 207 | 153 | `+0.0s` |
| `2026-10-21 15:00:38` | `19.56%` | `0.0%` | 225 | 161 | `+0.0s` |
| `2026-10-21 14:31:08` | `20.43%` | `0.0%` | 230 | 157 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T19:30:37.793000+00:00`.*
