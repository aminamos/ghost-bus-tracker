# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-05T18:39:12.510075+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`22.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `164` | Total runs operating in current transit schedule window |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 37 | 22.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 100511** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 66 | 32 | 32 | **`48.48%`** | `0.0%` | `+0.0s` |
| **Route 512** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 17 | 17 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 18 | 18 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 7 | 9 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 6 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 8 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 6 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `482020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51403 is broadcasting off-schedule with no vehicle covering 482020 |
| `3270020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9215 is broadcasting off-schedule with no vehicle covering 3270020 |
| `3852020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9713 is broadcasting off-schedule with no vehicle covering 3852020 |
| `16687589__H:121:0:Weekday:1:26SEP:52035:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 15806 is broadcasting off-schedule with no vehicle covering 16687589__H:121:0:Weekday:1:26SEP:52035:12345 |
| `16687255__H:121:0:Weekday:1:26SEP:52010:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 15805 is broadcasting off-schedule with no vehicle covering 16687255__H:121:0:Weekday:1:26SEP:52010:12345 |
| `4517020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9738 is broadcasting off-schedule with no vehicle covering 4517020 |
| `16687325__H:121:0:Weekday:1:26SEP:52004:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:1:26SEP:52004:12345 is missing from active GPS transponder fleet |
| `851843111` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8248836 is missing from active GPS transponder fleet |
| `851839411` | Route 100511 | `N/A` | `SCHEDULED` | Assigned vehicle 8248834 is missing from active GPS transponder fleet |
| `851839401` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248834 is missing from active GPS transponder fleet |
| `851839751` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248833 is missing from active GPS transponder fleet |
| `851843491` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248838 is missing from active GPS transponder fleet |
| `851843501` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248838 is missing from active GPS transponder fleet |
| `851844281` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248839 is missing from active GPS transponder fleet |
| `851839621` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248820 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:39:12.510075+00:00`.*
