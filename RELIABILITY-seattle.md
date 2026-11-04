# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:18.663000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.81%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `73` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `50` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 17.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 25 | 13 | 11 | **`44.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 11 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41517 is broadcasting off-schedule with no vehicle covering 79020 |
| `1956020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 1956020 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 3010020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9716 is broadcasting off-schedule with no vehicle covering 2295020 |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273975 is missing from active GPS transponder fleet |
| `560092511` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273974 is missing from active GPS transponder fleet |
| `851857171` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273948 is missing from active GPS transponder fleet |
| `559501081` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8273953 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273952 is missing from active GPS transponder fleet |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_4129` | Route 2LINE | `N/A` | `SCHEDULED` | Assigned vehicle 743.583267 is missing from active GPS transponder fleet |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51402 is broadcasting off-schedule with no vehicle covering 3660020 |
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9207 is broadcasting off-schedule with no vehicle covering 3912020 |
| `17068831__H:121:0:Weekday:3:26SEP:52057:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52057:12345 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:18` | `17.81%` | `0.0%` | 73 | 50 | `+0.0s` |
| `2026-11-04 06:30:20` | `19.51%` | `0.0%` | 82 | 60 | `+0.0s` |
| `2026-11-04 06:00:18` | `21.43%` | `0.0%` | 98 | 68 | `+0.0s` |
| `2026-11-04 05:30:17` | `20.95%` | `0.0%` | 105 | 72 | `+0.0s` |
| `2026-11-04 05:00:17` | `0.0%` | `0.0%` | 16 | 81 | `+0.0s` |
| `2026-11-04 04:30:17` | `22.31%` | `0.0%` | 121 | 87 | `+0.0s` |
| `2026-11-04 04:00:19` | `22.79%` | `0.0%` | 136 | 89 | `+0.0s` |
| `2026-11-04 03:30:19` | `17.02%` | `0.0%` | 141 | 102 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:18.663000+00:00`.*
