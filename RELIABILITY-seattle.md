# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T06:42:12.049020+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`31.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 31.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 100232** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 20 | 7 | 13 | **`65.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 5 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 8 | 8 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 512** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `LLR_2026-09-30_20260903_Link_MISFencing-PHActive_Weekday_2LINE_4061` | Route 2LINE | `11:54:30` | `DUPLICATED` | Assigned vehicle 205.959442 is broadcasting off-schedule with no vehicle covering LLR_2026-09-30_20260903_Link_MISFencing-PHActive_Weekday_2LINE_4061 |
| `1254020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41605 is broadcasting off-schedule with no vehicle covering 1254020 |
| `4351020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 61406 is broadcasting off-schedule with no vehicle covering 4351020 |
| `LLR_2026-09-30_20260903_Link_MISFencing-PHActive_Weekday_100479_1044` | Route 100479 | `09:45:30` | `DUPLICATED` | Assigned vehicle 264.269230 is broadcasting off-schedule with no vehicle covering LLR_2026-09-30_20260903_Link_MISFencing-PHActive_Weekday_100479_1044 |
| `872393961` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273996 is missing from active GPS transponder fleet |
| `560092511` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273974 is missing from active GPS transponder fleet |
| `851857171` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273948 is missing from active GPS transponder fleet |
| `851857211` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `851857141` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `848943401` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273953 is missing from active GPS transponder fleet |
| `851857221` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273952 is missing from active GPS transponder fleet |
| `1799020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9212 is broadcasting off-schedule with no vehicle covering 1799020 |
| `4389020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9212 is broadcasting off-schedule with no vehicle covering 4389020 |
| `3919020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9220 is broadcasting off-schedule with no vehicle covering 3919020 |
| `789020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9221 is broadcasting off-schedule with no vehicle covering 789020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 06:42:12` | `31.58%` | `0.0%` | 57 | 52 | `+0.0s` |
| `2026-10-06 00:28:47` | `21.83%` | `0.0%` | 229 | 164 | `+0.0s` |
| `2026-10-05 18:39:12` | `22.56%` | `0.0%` | 164 | 104 | `+0.0s` |
| `2026-10-05 18:02:19` | `21.43%` | `0.0%` | 168 | 113 | `+0.0s` |
| `2026-10-05 17:57:49` | `18.99%` | `0.0%` | 158 | 109 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T06:42:12.049020+00:00`.*
