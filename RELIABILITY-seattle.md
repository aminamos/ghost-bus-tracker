# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:18.678000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`20.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `69` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 14 | 20.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 21 | 11 | 8 | **`38.1%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 13 | 13 | 4 | **`30.77%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 3 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `881956891` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9669 is broadcasting off-schedule with no vehicle covering 881956891 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41502 is broadcasting off-schedule with no vehicle covering 3010020 |
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41503 is broadcasting off-schedule with no vehicle covering 3912020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9714 is broadcasting off-schedule with no vehicle covering 2295020 |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 61401 is broadcasting off-schedule with no vehicle covering 3660020 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_1052` | Route 100479 | `11:05:30` | `DUPLICATED` | Assigned vehicle 608.180716 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_1052 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2014` | Route 100479 | `05:35:30` | `DUPLICATED` | Assigned vehicle 604.480321 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2014 |
| `881956891` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298750 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298729 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298706 is missing from active GPS transponder fleet |
| `559501081` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8298707 is missing from active GPS transponder fleet |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_1052` | Route 100479 | `11:05:30` | `DUPLICATED` | Assigned vehicle 644.728746 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_1052 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_4128` | Route 2LINE | `21:27:30` | `DUPLICATED` | Assigned vehicle 610.254127 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_4128 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2014` | Route 100479 | `05:35:30` | `DUPLICATED` | Assigned vehicle 604.454102 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2014 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:18` | `20.29%` | `0.0%` | 69 | 57 | `+0.0s` |
| `2026-11-26 06:30:17` | `20.78%` | `0.0%` | 77 | 60 | `+0.0s` |
| `2026-11-26 06:00:17` | `20.93%` | `0.0%` | 86 | 63 | `+0.0s` |
| `2026-11-26 05:30:18` | `21.65%` | `0.0%` | 97 | 73 | `+0.0s` |
| `2026-11-26 05:00:17` | `29.0%` | `0.0%` | 100 | 80 | `+0.0s` |
| `2026-11-26 04:30:18` | `24.3%` | `0.0%` | 107 | 87 | `+0.0s` |
| `2026-11-26 04:00:17` | `19.3%` | `0.0%` | 114 | 89 | `+0.0s` |
| `2026-11-26 03:30:18` | `18.55%` | `0.0%` | 124 | 97 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:18.678000+00:00`.*
