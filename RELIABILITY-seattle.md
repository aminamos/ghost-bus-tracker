# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-10T06:30:17.728000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.92%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `83` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `63` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `24` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 24 | 28.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 28 | 13 | 14 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 512** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 11 | 11 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 17 | 17 | 4 | **`23.53%`** | `0.0%` | `+0.0s` |
| **Route 100511** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `LLR_2026-11-09_20261007_Link_RailMilling2NGS_Weekday_100479_1101` | Route 100479 | `18:15:30` | `DUPLICATED` | Assigned vehicle 262.106214 is broadcasting off-schedule with no vehicle covering LLR_2026-11-09_20261007_Link_RailMilling2NGS_Weekday_100479_1101 |
| `3568020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9722 is broadcasting off-schedule with no vehicle covering 3568020 |
| `2226020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9731 is broadcasting off-schedule with no vehicle covering 2226020 |
| `17068829__H:121:0:Weekday:3:26SEP:52061:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52061:12345 is missing from active GPS transponder fleet |
| `17068761__H:121:0:Weekday:3:26SEP:52061:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52061:12345 is missing from active GPS transponder fleet |
| `851839341` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273874 is missing from active GPS transponder fleet |
| `LLR_2026-11-09_20261007_Link_RailMilling2NGS_Weekday_100479_2106` | Route 100479 | `17:57:30` | `DUPLICATED` | Assigned vehicle 267.061936 is broadcasting off-schedule with no vehicle covering LLR_2026-11-09_20261007_Link_RailMilling2NGS_Weekday_100479_2106 |
| `350247351` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273973 is missing from active GPS transponder fleet |
| `851857181` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `851857211` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `559501081` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273953 is missing from active GPS transponder fleet |
| `851857151` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273952 is missing from active GPS transponder fleet |
| `560092311` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8273931 is missing from active GPS transponder fleet |
| `1799020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9221 is broadcasting off-schedule with no vehicle covering 1799020 |
| `567020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9221 is broadcasting off-schedule with no vehicle covering 567020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 06:30:17` | `28.92%` | `0.0%` | 83 | 63 | `+0.0s` |
| `2026-11-10 06:00:17` | `26.53%` | `0.0%` | 98 | 66 | `+0.0s` |
| `2026-11-10 05:30:18` | `33.65%` | `0.0%` | 104 | 73 | `+0.0s` |
| `2026-11-10 05:00:17` | `29.73%` | `0.0%` | 111 | 84 | `+0.0s` |
| `2026-11-10 04:30:17` | `30.89%` | `0.0%` | 123 | 87 | `+0.0s` |
| `2026-11-10 04:00:18` | `23.53%` | `0.0%` | 136 | 92 | `+0.0s` |
| `2026-11-10 03:30:18` | `22.7%` | `0.0%` | 141 | 97 | `+0.0s` |
| `2026-11-10 03:00:18` | `24.84%` | `0.0%` | 161 | 115 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T06:30:17.728000+00:00`.*
