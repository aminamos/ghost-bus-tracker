# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T07:00:21.047000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `41` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `29` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 17.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 10 | 5 | 5 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 8 | 8 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `17068833__H:121:0:Weekday:3:26SEP:52062:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52062:12345 is missing from active GPS transponder fleet |
| `LLR_2026-10-23_20261007_Link_RailMilling2NGS_Weekday_2LINE_4059` | Route 2LINE | `11:34:30` | `DUPLICATED` | Assigned vehicle 755.247874 is broadcasting off-schedule with no vehicle covering LLR_2026-10-23_20261007_Link_RailMilling2NGS_Weekday_2LINE_4059 |
| `872393291` | Route 100451 | `N/A` | `SCHEDULED` | Assigned vehicle 8274001 is missing from active GPS transponder fleet |
| `872393961` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273996 is missing from active GPS transponder fleet |
| `851857241` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273948 is missing from active GPS transponder fleet |
| `851857141` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `848943401` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273953 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 07:00:21` | `17.07%` | `0.0%` | 41 | 29 | `+0.0s` |
| `2026-10-24 06:30:19` | `18.33%` | `0.0%` | 60 | 48 | `+0.0s` |
| `2026-10-24 06:00:19` | `20.27%` | `0.0%` | 74 | 52 | `+0.0s` |
| `2026-10-24 05:30:18` | `21.95%` | `0.0%` | 82 | 61 | `+0.0s` |
| `2026-10-24 05:00:20` | `19.59%` | `0.0%` | 97 | 66 | `+0.0s` |
| `2026-10-24 04:30:18` | `24.07%` | `0.0%` | 108 | 76 | `+0.0s` |
| `2026-10-24 04:00:18` | `26.09%` | `0.0%` | 115 | 85 | `+0.0s` |
| `2026-10-24 03:30:19` | `25.41%` | `0.0%` | 122 | 91 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T07:00:21.047000+00:00`.*
