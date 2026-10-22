# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:00:20.351000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `156` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `104` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `37` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 37 | 23.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 62 | 29 | 30 | **`48.39%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 9 | 6 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 535** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 6 | 6 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 6 | 5 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 16 | 16 | 2 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 594** | 6 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 5 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100511** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 6 | 9 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `LLR_2026-10-22_20261007_Link_RailMilling2JPS_Weekday_2LINE_4035` | Route 2LINE | `08:03:30` | `DUPLICATED` | Assigned vehicle 666.623779 is broadcasting off-schedule with no vehicle covering LLR_2026-10-22_20261007_Link_RailMilling2JPS_Weekday_2LINE_4035 |
| `560088821` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9661 is broadcasting off-schedule with no vehicle covering 560088821 |
| `298020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9215 is broadcasting off-schedule with no vehicle covering 298020 |
| `2630020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41517 is broadcasting off-schedule with no vehicle covering 2630020 |
| `3852020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41502 is broadcasting off-schedule with no vehicle covering 3852020 |
| `3495020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41503 is broadcasting off-schedule with no vehicle covering 3495020 |
| `2361020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41503 is broadcasting off-schedule with no vehicle covering 2361020 |
| `17069013__H:121:0:Weekday:3:26SEP:52038:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52038:12345 is missing from active GPS transponder fleet |
| `4401020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9713 is broadcasting off-schedule with no vehicle covering 4401020 |
| `3821020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9717 is broadcasting off-schedule with no vehicle covering 3821020 |
| `451020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9721 is broadcasting off-schedule with no vehicle covering 451020 |
| `17068790__H:121:0:Weekday:3:26SEP:52004:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52004:12345 is missing from active GPS transponder fleet |
| `17068724__H:121:0:Weekday:3:26SEP:52004:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52004:12345 is missing from active GPS transponder fleet |
| `17068791__H:121:0:Weekday:3:26SEP:52037:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52037:12345 is missing from active GPS transponder fleet |
| `17069082__H:121:0:Weekday:3:26SEP:52032:12345` | Route 535 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52032:12345 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:00:20` | `23.72%` | `0.0%` | 156 | 104 | `+0.0s` |
| `2026-10-22 18:30:35` | `23.23%` | `0.0%` | 155 | 105 | `+0.0s` |
| `2026-10-22 17:30:36` | `0.0%` | `0.0%` | 19 | 111 | `+0.0s` |
| `2026-10-22 16:01:15` | `19.46%` | `0.0%` | 149 | 98 | `+0.0s` |
| `2026-10-22 15:01:08` | `21.34%` | `0.0%` | 239 | 163 | `+0.0s` |
| `2026-10-22 14:00:42` | `23.35%` | `0.0%` | 227 | 150 | `+0.0s` |
| `2026-10-22 13:31:53` | `27.19%` | `0.0%` | 217 | 138 | `+0.0s` |
| `2026-10-22 12:30:36` | `29.87%` | `0.0%` | 154 | 100 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:00:20.351000+00:00`.*
