# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:18.916000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.42%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `67` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `49` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 16.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 22 | 13 | 9 | **`40.91%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 9 | 9 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 13 | 13 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41603 is broadcasting off-schedule with no vehicle covering 3912020 |
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41513 is broadcasting off-schedule with no vehicle covering 79020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9718 is broadcasting off-schedule with no vehicle covering 2295020 |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 61404 is broadcasting off-schedule with no vehicle covering 3660020 |
| `1956020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9222 is broadcasting off-schedule with no vehicle covering 1956020 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9222 is broadcasting off-schedule with no vehicle covering 3010020 |
| `17068831__H:121:0:Weekday:3:26SEP:52057:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52057:12345 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298729 is missing from active GPS transponder fleet |
| `851857151` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298706 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298706 is missing from active GPS transponder fleet |
| `559501081` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8298707 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:18` | `16.42%` | `0.0%` | 67 | 49 | `+0.0s` |
| `2026-11-17 06:30:18` | `18.75%` | `0.0%` | 80 | 58 | `+0.0s` |
| `2026-11-17 06:00:18` | `22.45%` | `0.0%` | 98 | 64 | `+0.0s` |
| `2026-11-17 05:30:18` | `24.07%` | `0.0%` | 108 | 73 | `+0.0s` |
| `2026-11-17 05:00:17` | `25.0%` | `0.0%` | 112 | 78 | `+0.0s` |
| `2026-11-17 04:30:18` | `25.78%` | `0.0%` | 128 | 90 | `+0.0s` |
| `2026-11-17 04:00:18` | `24.43%` | `0.0%` | 131 | 89 | `+0.0s` |
| `2026-11-17 03:30:18` | `20.0%` | `0.0%` | 140 | 101 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:18.916000+00:00`.*
