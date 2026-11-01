# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:17.862000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.53%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `47` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 25.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 16 | 5 | 10 | **`62.5%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `LLR_2026-10-31_20261007_Link_RailMilling2JPS_Saturday_100479_2099` | Route 100479 | `20:04:30` | `DUPLICATED` | Assigned vehicle 449.175046 is broadcasting off-schedule with no vehicle covering LLR_2026-10-31_20261007_Link_RailMilling2JPS_Saturday_100479_2099 |
| `4683070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9734 is broadcasting off-schedule with no vehicle covering 4683070 |
| `17066046__H:171:5:Saturday:3:26SEP:57012:6` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:171:5:Saturday:3:26SEP:57012:6 is missing from active GPS transponder fleet |
| `4061070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9218 is broadcasting off-schedule with no vehicle covering 4061070 |
| `661070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9212 is broadcasting off-schedule with no vehicle covering 661070 |
| `17066104__H:171:5:Saturday:3:26SEP:57013:6` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 22801 is broadcasting off-schedule with no vehicle covering 17066104__H:171:5:Saturday:3:26SEP:57013:6 |
| `872325001` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273726 is missing from active GPS transponder fleet |
| `849295191` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273689 is missing from active GPS transponder fleet |
| `849295181` | Route 102767 | `N/A` | `SCHEDULED` | Assigned vehicle 8273687 is missing from active GPS transponder fleet |
| `851768161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273683 is missing from active GPS transponder fleet |
| `851768181` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273681 is missing from active GPS transponder fleet |
| `17066045__H:171:5:Saturday:3:26SEP:57007:6` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:171:5:Saturday:3:26SEP:57007:6 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:17` | `25.53%` | `0.0%` | 47 | 37 | `+0.0s` |
| `2026-11-01 06:00:18` | `17.54%` | `0.0%` | 57 | 47 | `+0.0s` |
| `2026-11-01 05:30:18` | `13.89%` | `0.0%` | 72 | 58 | `+0.0s` |
| `2026-11-01 05:00:18` | `16.47%` | `0.0%` | 85 | 64 | `+0.0s` |
| `2026-11-01 04:00:17` | `16.3%` | `0.0%` | 92 | 71 | `+0.0s` |
| `2026-11-01 03:30:17` | `15.69%` | `0.0%` | 102 | 77 | `+0.0s` |
| `2026-11-01 02:30:18` | `16.67%` | `0.0%` | 108 | 82 | `+0.0s` |
| `2026-11-01 01:30:18` | `24.19%` | `0.0%` | 124 | 85 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:17.862000+00:00`.*
