# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:18.023000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.57%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `42` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `45` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 28.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 12 | 3 | 7 | **`58.33%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 11 | 11 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2079` | Route 100479 | `14:29:30` | `DUPLICATED` | Assigned vehicle 221.989449 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2079 |
| `17068832__H:121:0:Weekday:3:26SEP:52061:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52061:12345 is missing from active GPS transponder fleet |
| `17068834__H:121:0:Weekday:3:26SEP:52061:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52061:12345 is missing from active GPS transponder fleet |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2079` | Route 100479 | `14:29:30` | `DUPLICATED` | Assigned vehicle 189.351184 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2079 |
| `867255671` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273973 is missing from active GPS transponder fleet |
| `851857241` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273948 is missing from active GPS transponder fleet |
| `851857141` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273949 is missing from active GPS transponder fleet |
| `848943401` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273953 is missing from active GPS transponder fleet |
| `17068833__H:121:0:Weekday:3:26SEP:52062:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52062:12345 is missing from active GPS transponder fleet |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2079` | Route 100479 | `14:29:30` | `DUPLICATED` | Assigned vehicle 188.564707 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2079 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_3010` | Route 2LINE | `05:11:30` | `DUPLICATED` | Assigned vehicle 223.618834 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_2LINE_3010 |
| `872392081` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8274000 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `28.57%` | `0.0%` | 42 | 45 | `+0.0s` |
| `2026-10-29 06:30:18` | `20.97%` | `0.0%` | 62 | 48 | `+0.0s` |
| `2026-10-29 06:00:18` | `16.22%` | `0.0%` | 74 | 55 | `+0.0s` |
| `2026-10-29 05:30:18` | `21.43%` | `0.0%` | 84 | 63 | `+0.0s` |
| `2026-10-29 05:00:17` | `19.79%` | `0.0%` | 96 | 70 | `+0.0s` |
| `2026-10-29 04:30:18` | `22.12%` | `0.0%` | 104 | 76 | `+0.0s` |
| `2026-10-29 04:00:18` | `24.17%` | `0.0%` | 120 | 87 | `+0.0s` |
| `2026-10-29 03:30:18` | `25.6%` | `0.0%` | 125 | 87 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.023000+00:00`.*
