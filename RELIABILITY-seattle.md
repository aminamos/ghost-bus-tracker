# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:18.137000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`62.86%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `35` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `17` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `22` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 22 | 62.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 597** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 11 | 1 | 10 | **`90.91%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 8 | 8 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 102767** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `3422010` | Route 594 | `N/A` | `SCHEDULED` | Assigned vehicle 51402 is missing from active GPS transponder fleet |
| `3292010` | Route 578 | `N/A` | `SCHEDULED` | Assigned vehicle 9206 is missing from active GPS transponder fleet |
| `3275010` | Route 560 | `N/A` | `SCHEDULED` | Assigned vehicle 41511 is missing from active GPS transponder fleet |
| `3875010` | Route 597 | `N/A` | `SCHEDULED` | Assigned vehicle 41507 is missing from active GPS transponder fleet |
| `17071744__H:111:6:Sunday:3:26SEP:51008:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:111:6:Sunday:3:26SEP:51008:1234567 is missing from active GPS transponder fleet |
| `3936010` | Route 574 | `N/A` | `SCHEDULED` | Assigned vehicle 9717 is missing from active GPS transponder fleet |
| `2619010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9717 is missing from active GPS transponder fleet |
| `1589010` | Route 597 | `N/A` | `SCHEDULED` | Assigned vehicle 9729 is missing from active GPS transponder fleet |
| `4434010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9728 is missing from active GPS transponder fleet |
| `196010` | Route 597 | `N/A` | `SCHEDULED` | Assigned vehicle 9737 is missing from active GPS transponder fleet |
| `1640010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9733 is missing from active GPS transponder fleet |
| `867187611` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273804 is missing from active GPS transponder fleet |
| `849295751` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273801 is missing from active GPS transponder fleet |
| `849295761` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273802 is missing from active GPS transponder fleet |
| `1274010` | Route 594 | `N/A` | `SCHEDULED` | Assigned vehicle 9304 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:18` | `62.86%` | `0.0%` | 35 | 17 | `+0.0s` |
| `2026-10-26 06:00:27` | `36.76%` | `0.0%` | 68 | 53 | `+0.0s` |
| `2026-10-26 05:30:19` | `36.23%` | `0.0%` | 69 | 61 | `+0.0s` |
| `2026-10-26 05:00:21` | `24.1%` | `0.0%` | 83 | 63 | `+0.0s` |
| `2026-10-26 04:30:29` | `23.26%` | `0.0%` | 86 | 68 | `+0.0s` |
| `2026-10-26 04:00:18` | `25.88%` | `0.0%` | 85 | 67 | `+0.0s` |
| `2026-10-26 03:30:33` | `22.22%` | `0.0%` | 90 | 73 | `+0.0s` |
| `2026-10-26 03:00:35` | `22.94%` | `0.0%` | 109 | 73 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:18.137000+00:00`.*
