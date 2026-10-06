# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T00:28:47.444828+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `229` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `164` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `50` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 50 | 21.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 82 | 37 | 44 | **`53.66%`** | `0.0%` | `+0.0s` |
| **Route 102734** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 512** | 6 | 4 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 535** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 11 | 11 | 1 | **`9.09%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 22 | 22 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 21 | 21 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 6 | 9 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 7 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `16687547__H:121:0:Weekday:1:26SEP:52057:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:1:26SEP:52057:12345 is missing from active GPS transponder fleet |
| `2711020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51403 is broadcasting off-schedule with no vehicle covering 2711020 |
| `1254020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41605 is broadcasting off-schedule with no vehicle covering 1254020 |
| `2504020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41602 is broadcasting off-schedule with no vehicle covering 2504020 |
| `560087391` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9677 is broadcasting off-schedule with no vehicle covering 560087391 |
| `389020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9201 is broadcasting off-schedule with no vehicle covering 389020 |
| `16687345__H:121:0:Weekday:1:26SEP:52043:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:1:26SEP:52043:12345 is missing from active GPS transponder fleet |
| `4536020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9213 is broadcasting off-schedule with no vehicle covering 4536020 |
| `3645020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9222 is broadcasting off-schedule with no vehicle covering 3645020 |
| `3737020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9222 is broadcasting off-schedule with no vehicle covering 3737020 |
| `16687109__H:121:0:Weekday:1:26SEP:52040:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:1:26SEP:52040:12345 is missing from active GPS transponder fleet |
| `4550020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9723 is broadcasting off-schedule with no vehicle covering 4550020 |
| `2949020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9722 is broadcasting off-schedule with no vehicle covering 2949020 |
| `3416020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9306 is broadcasting off-schedule with no vehicle covering 3416020 |
| `3620020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9304 is broadcasting off-schedule with no vehicle covering 3620020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T00:28:47.444828+00:00`.*
