# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-02T07:00:18.019000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`30.91%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `55` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `47` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `17` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 17 | 30.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 19 | 5 | 14 | **`73.68%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 6 | 6 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 13 | 13 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 4 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `17071742__H:111:6:Sunday:3:26SEP:51012:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:111:6:Sunday:3:26SEP:51012:1234567 is missing from active GPS transponder fleet |
| `3875010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41603 is broadcasting off-schedule with no vehicle covering 3875010 |
| `3275010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9206 is broadcasting off-schedule with no vehicle covering 3275010 |
| `3292010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41506 is broadcasting off-schedule with no vehicle covering 3292010 |
| `1065010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9717 is broadcasting off-schedule with no vehicle covering 1065010 |
| `3936010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9731 is broadcasting off-schedule with no vehicle covering 3936010 |
| `867187601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273803 is missing from active GPS transponder fleet |
| `851804231` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273804 is missing from active GPS transponder fleet |
| `1274010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9303 is broadcasting off-schedule with no vehicle covering 1274010 |
| `851804801` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273795 is missing from active GPS transponder fleet |
| `851804721` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273796 is missing from active GPS transponder fleet |
| `851804791` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273796 is missing from active GPS transponder fleet |
| `17071804__H:111:6:Sunday:3:26SEP:51010:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 16803 is broadcasting off-schedule with no vehicle covering 17071804__H:111:6:Sunday:3:26SEP:51010:1234567 |
| `17071743__H:111:6:Sunday:3:26SEP:51010:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 16803 is broadcasting off-schedule with no vehicle covering 17071743__H:111:6:Sunday:3:26SEP:51010:1234567 |
| `17071742__H:111:6:Sunday:3:26SEP:51012:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 16802 is broadcasting off-schedule with no vehicle covering 17071742__H:111:6:Sunday:3:26SEP:51012:1234567 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `30.91%` | `0.0%` | 55 | 47 | `+0.0s` |
| `2026-11-02 06:30:17` | `16.42%` | `0.0%` | 67 | 54 | `+0.0s` |
| `2026-11-02 06:00:19` | `16.22%` | `0.0%` | 74 | 57 | `+0.0s` |
| `2026-11-02 05:00:18` | `16.67%` | `0.0%` | 72 | 55 | `+0.0s` |
| `2026-11-02 04:30:18` | `13.58%` | `0.0%` | 81 | 61 | `+0.0s` |
| `2026-11-02 04:00:18` | `15.38%` | `0.0%` | 78 | 63 | `+0.0s` |
| `2026-11-02 03:30:19` | `13.79%` | `0.0%` | 87 | 68 | `+0.0s` |
| `2026-11-02 03:00:18` | `0.0%` | `0.0%` | 18 | 67 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.019000+00:00`.*
