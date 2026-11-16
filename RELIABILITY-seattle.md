# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-16T07:00:18.606000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`38.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `52` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `47` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `20` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 20 | 38.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 17 | 5 | 12 | **`70.59%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 6 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 4 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `LLR_2026-11-15_20260924_Link_OctoberCLCclosure_Sunday_100479_2097` | Route 100479 | `17:28:30` | `DUPLICATED` | Assigned vehicle 792.876979 is broadcasting off-schedule with no vehicle covering LLR_2026-11-15_20260924_Link_OctoberCLCclosure_Sunday_100479_2097 |
| `849295741` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298561 is missing from active GPS transponder fleet |
| `867187601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298557 is missing from active GPS transponder fleet |
| `851805191` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298548 is missing from active GPS transponder fleet |
| `851805201` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298548 is missing from active GPS transponder fleet |
| `851804811` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298549 is missing from active GPS transponder fleet |
| `851804801` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298549 is missing from active GPS transponder fleet |
| `3275010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41604 is broadcasting off-schedule with no vehicle covering 3275010 |
| `3292010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41602 is broadcasting off-schedule with no vehicle covering 3292010 |
| `LLR_2026-11-15_20260924_Link_OctoberCLCclosure_Sunday_100479_1062` | Route 100479 | `12:34:30` | `DUPLICATED` | Assigned vehicle 763.176400 is broadcasting off-schedule with no vehicle covering LLR_2026-11-15_20260924_Link_OctoberCLCclosure_Sunday_100479_1062 |
| `3875010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41507 is broadcasting off-schedule with no vehicle covering 3875010 |
| `1065010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9734 is broadcasting off-schedule with no vehicle covering 1065010 |
| `3936010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9738 is broadcasting off-schedule with no vehicle covering 3936010 |
| `LLR_2026-11-15_20260924_Link_OctoberCLCclosure_Sunday_100479_1062` | Route 100479 | `12:34:30` | `DUPLICATED` | Assigned vehicle 767.749087 is broadcasting off-schedule with no vehicle covering LLR_2026-11-15_20260924_Link_OctoberCLCclosure_Sunday_100479_1062 |
| `17071742__H:111:6:Sunday:3:26SEP:51012:1234567` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:111:6:Sunday:3:26SEP:51012:1234567 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:18` | `38.46%` | `0.0%` | 52 | 47 | `+0.0s` |
| `2026-11-16 06:30:19` | `32.76%` | `0.0%` | 58 | 51 | `+0.0s` |
| `2026-11-16 05:30:18` | `29.17%` | `0.0%` | 72 | 52 | `+0.0s` |
| `2026-11-16 05:00:17` | `34.72%` | `0.0%` | 72 | 54 | `+0.0s` |
| `2026-11-16 04:30:17` | `22.89%` | `0.0%` | 83 | 58 | `+0.0s` |
| `2026-11-16 04:00:18` | `31.4%` | `0.0%` | 86 | 54 | `+0.0s` |
| `2026-11-16 03:30:17` | `27.96%` | `0.0%` | 93 | 63 | `+0.0s` |
| `2026-11-16 03:00:19` | `40.0%` | `0.0%` | 90 | 67 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:18.606000+00:00`.*
