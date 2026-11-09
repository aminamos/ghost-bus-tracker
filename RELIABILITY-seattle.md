# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:18.122000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `55` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `46` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 23.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 16 | 6 | 10 | **`62.5%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 10 | 10 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 11 | 11 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `849295741` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9632 is broadcasting off-schedule with no vehicle covering 849295741 |
| `1065010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9722 is broadcasting off-schedule with no vehicle covering 1065010 |
| `3936010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9737 is broadcasting off-schedule with no vehicle covering 3936010 |
| `17071803__H:111:6:Sunday:3:26SEP:51008:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:111:6:Sunday:3:26SEP:51008:1234567 is missing from active GPS transponder fleet |
| `3292010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41603 is broadcasting off-schedule with no vehicle covering 3292010 |
| `3275010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41513 is broadcasting off-schedule with no vehicle covering 3275010 |
| `3875010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 3875010 |
| `17071742__H:111:6:Sunday:3:26SEP:51012:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:111:6:Sunday:3:26SEP:51012:1234567 is missing from active GPS transponder fleet |
| `867187601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273803 is missing from active GPS transponder fleet |
| `851804231` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273804 is missing from active GPS transponder fleet |
| `347632051` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8273801 is missing from active GPS transponder fleet |
| `851804811` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273795 is missing from active GPS transponder fleet |
| `851804801` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273795 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:18` | `23.64%` | `0.0%` | 55 | 46 | `+0.0s` |
| `2026-11-09 06:30:18` | `13.04%` | `0.0%` | 69 | 56 | `+0.0s` |
| `2026-11-09 05:00:17` | `18.6%` | `0.0%` | 86 | 66 | `+0.0s` |
| `2026-11-09 04:30:17` | `16.5%` | `0.0%` | 103 | 71 | `+0.0s` |
| `2026-11-09 04:00:18` | `18.81%` | `0.0%` | 101 | 70 | `+0.0s` |
| `2026-11-09 03:30:17` | `16.82%` | `0.0%` | 107 | 78 | `+0.0s` |
| `2026-11-09 03:00:18` | `23.15%` | `0.0%` | 108 | 80 | `+0.0s` |
| `2026-11-09 02:30:18` | `16.24%` | `0.0%` | 117 | 84 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:18.122000+00:00`.*
