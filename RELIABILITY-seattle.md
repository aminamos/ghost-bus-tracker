# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:17.723000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `71` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `53` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 15.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 512** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 22 | 13 | 8 | **`36.36%`** | `0.0%` | `+0.0s` |
| **Route 574** | 3 | 4 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 594** | 6 | 6 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 13 | 13 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 11 | 11 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `1956020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 1956020 |
| `3010020` | Route 594 | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 3010020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9731 is broadcasting off-schedule with no vehicle covering 2295020 |
| `3660020` | Route 574 | `N/A` | `SCHEDULED` | Assigned vehicle 61406 is broadcasting off-schedule with no vehicle covering 3660020 |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273975 is missing from active GPS transponder fleet |
| `851857211` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273952 is missing from active GPS transponder fleet |
| `17068831__H:121:0:Weekday:3:26SEP:52057:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 19122 is broadcasting off-schedule with no vehicle covering 17068831__H:121:0:Weekday:3:26SEP:52057:12345 |
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9207 is broadcasting off-schedule with no vehicle covering 79020 |
| `17068830__H:121:0:Weekday:3:26SEP:52062:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52062:12345 is missing from active GPS transponder fleet |
| `17068762__H:121:0:Weekday:3:26SEP:52062:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52062:12345 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:17` | `15.49%` | `0.0%` | 71 | 53 | `+0.0s` |
| `2026-11-05 06:30:17` | `14.29%` | `0.0%` | 84 | 63 | `+0.0s` |
| `2026-11-05 06:00:17` | `15.79%` | `0.0%` | 95 | 66 | `+0.0s` |
| `2026-11-05 05:30:18` | `24.04%` | `0.0%` | 104 | 73 | `+0.0s` |
| `2026-11-05 05:00:17` | `24.11%` | `0.0%` | 112 | 81 | `+0.0s` |
| `2026-11-05 04:30:17` | `24.37%` | `0.0%` | 119 | 85 | `+0.0s` |
| `2026-11-05 04:00:18` | `19.23%` | `0.0%` | 130 | 91 | `+0.0s` |
| `2026-11-05 03:30:18` | `17.14%` | `0.0%` | 140 | 102 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.723000+00:00`.*
