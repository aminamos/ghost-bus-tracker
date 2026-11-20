# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:19.088000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.4%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `67` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `49` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 19.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 22 | 11 | 10 | **`45.45%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 2 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `1956020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41604 is broadcasting off-schedule with no vehicle covering 1956020 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41604 is broadcasting off-schedule with no vehicle covering 3010020 |
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41513 is broadcasting off-schedule with no vehicle covering 3912020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9722 is broadcasting off-schedule with no vehicle covering 2295020 |
| `LLR_2026-11-19_20261007_Link_RailMilling2NGS_Weekday_2LINE_3055` | Route 2LINE | `11:50:30` | `DUPLICATED` | Assigned vehicle 130.494644 is broadcasting off-schedule with no vehicle covering LLR_2026-11-19_20261007_Link_RailMilling2NGS_Weekday_2LINE_3055 |
| `LLR_2026-11-19_20261007_Link_RailMilling2NGS_Weekday_2LINE_4125` | Route 2LINE | `20:54:30` | `DUPLICATED` | Assigned vehicle 91.877834 is broadcasting off-schedule with no vehicle covering LLR_2026-11-19_20261007_Link_RailMilling2NGS_Weekday_2LINE_4125 |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51402 is broadcasting off-schedule with no vehicle covering 3660020 |
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9212 is broadcasting off-schedule with no vehicle covering 79020 |
| `350247561` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8298728 is missing from active GPS transponder fleet |
| `560092511` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298728 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298729 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298706 is missing from active GPS transponder fleet |
| `851857211` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298703 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:19` | `19.4%` | `0.0%` | 67 | 49 | `+0.0s` |
| `2026-11-20 06:30:18` | `21.13%` | `0.0%` | 71 | 55 | `+0.0s` |
| `2026-11-20 05:30:18` | `18.28%` | `0.0%` | 93 | 66 | `+0.0s` |
| `2026-11-20 05:00:18` | `25.25%` | `0.0%` | 99 | 73 | `+0.0s` |
| `2026-11-20 04:30:17` | `19.81%` | `0.0%` | 106 | 79 | `+0.0s` |
| `2026-11-20 04:00:17` | `17.7%` | `0.0%` | 113 | 81 | `+0.0s` |
| `2026-11-20 03:30:18` | `17.6%` | `0.0%` | 125 | 95 | `+0.0s` |
| `2026-11-20 03:00:18` | `20.86%` | `0.0%` | 139 | 101 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:19.088000+00:00`.*
