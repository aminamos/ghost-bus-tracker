# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:17.894000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `69` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `51` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 15 | 21.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 512** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 23 | 11 | 11 | **`47.83%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 10 | 10 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `1956020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41511 is broadcasting off-schedule with no vehicle covering 1956020 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41511 is broadcasting off-schedule with no vehicle covering 3010020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9726 is broadcasting off-schedule with no vehicle covering 2295020 |
| `LLR_2026-11-05_20261007_Link_RailMilling2NGS_Weekday_100479_2055` | Route 100479 | `10:59:30` | `DUPLICATED` | Assigned vehicle 914.263668 is broadcasting off-schedule with no vehicle covering LLR_2026-11-05_20261007_Link_RailMilling2NGS_Weekday_100479_2055 |
| `TLINE_2026-08-31_TLink_Weekday_forGTFS_09162023_12mins_TLINE_149` | Route TLINE | `16:55:30` | `DUPLICATED` | Assigned vehicle 5 is broadcasting off-schedule with no vehicle covering TLINE_2026-08-31_TLink_Weekday_forGTFS_09162023_12mins_TLINE_149 |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 61404 is broadcasting off-schedule with no vehicle covering 3660020 |
| `17068761__H:121:0:Weekday:3:26SEP:52061:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52061:12345 is missing from active GPS transponder fleet |
| `17068832__H:121:0:Weekday:3:26SEP:52061:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52061:12345 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273975 is missing from active GPS transponder fleet |
| `560092381` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8273973 is missing from active GPS transponder fleet |
| `350247351` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273973 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273952 is missing from active GPS transponder fleet |
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9204 is broadcasting off-schedule with no vehicle covering 3912020 |
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9220 is broadcasting off-schedule with no vehicle covering 79020 |
| `17068831__H:121:0:Weekday:3:26SEP:52057:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52057:12345 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:17` | `21.74%` | `0.0%` | 69 | 51 | `+0.0s` |
| `2026-11-06 06:30:18` | `24.74%` | `0.0%` | 97 | 59 | `+0.0s` |
| `2026-11-06 06:00:18` | `19.23%` | `0.0%` | 104 | 67 | `+0.0s` |
| `2026-11-06 05:30:17` | `24.22%` | `0.0%` | 128 | 75 | `+0.0s` |
| `2026-11-06 04:30:18` | `19.35%` | `0.0%` | 155 | 91 | `+0.0s` |
| `2026-11-06 04:00:19` | `21.25%` | `0.0%` | 160 | 90 | `+0.0s` |
| `2026-11-06 03:30:18` | `20.0%` | `0.0%` | 175 | 102 | `+0.0s` |
| `2026-11-06 03:00:18` | `19.37%` | `0.0%` | 191 | 118 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:17.894000+00:00`.*
