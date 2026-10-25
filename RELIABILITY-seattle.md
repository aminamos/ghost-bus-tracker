# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T07:00:19.664000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`38.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `47` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `40` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `18` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 38.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 14 | 3 | 11 | **`78.57%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 10 | 10 | 3 | **`30.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 9 | 9 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `4061070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 4061070 |
| `LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_100479_1019` | Route 100479 | `06:50:30` | `DUPLICATED` | Assigned vehicle 843.036759 is broadcasting off-schedule with no vehicle covering LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_100479_1019 |
| `849295191` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273689 is missing from active GPS transponder fleet |
| `849295181` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273687 is missing from active GPS transponder fleet |
| `851768161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273683 is missing from active GPS transponder fleet |
| `851768141` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273681 is missing from active GPS transponder fleet |
| `851768181` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273681 is missing from active GPS transponder fleet |
| `851768101` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273682 is missing from active GPS transponder fleet |
| `851768171` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273682 is missing from active GPS transponder fleet |
| `LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_100479_1019` | Route 100479 | `06:50:30` | `DUPLICATED` | Assigned vehicle 841.846500 is broadcasting off-schedule with no vehicle covering LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_100479_1019 |
| `LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_2LINE_3110` | Route 2LINE | `23:18:30` | `DUPLICATED` | Assigned vehicle 843.679764 is broadcasting off-schedule with no vehicle covering LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_2LINE_3110 |
| `LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_100479_1019` | Route 100479 | `06:50:30` | `DUPLICATED` | Assigned vehicle 836.931579 is broadcasting off-schedule with no vehicle covering LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_100479_1019 |
| `872325001` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273726 is missing from active GPS transponder fleet |
| `LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_2LINE_3110` | Route 2LINE | `23:18:30` | `DUPLICATED` | Assigned vehicle 881.567684 is broadcasting off-schedule with no vehicle covering LLR_2026-10-24_20261007_Link_RailMilling2NGS_Saturday_2LINE_3110 |
| `17066045__H:171:5:Saturday:3:26SEP:57007:6` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:171:5:Saturday:3:26SEP:57007:6 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 07:00:19` | `38.3%` | `0.0%` | 47 | 40 | `+0.0s` |
| `2026-10-25 06:30:18` | `37.5%` | `0.0%` | 48 | 43 | `+0.0s` |
| `2026-10-25 06:15:45` | `41.51%` | `0.0%` | 53 | 45 | `+0.0s` |
| `2026-10-25 06:00:56` | `36.84%` | `0.0%` | 57 | 51 | `+0.0s` |
| `2026-10-25 05:30:19` | `24.62%` | `0.0%` | 65 | 58 | `+0.0s` |
| `2026-10-25 05:00:18` | `22.97%` | `0.0%` | 74 | 66 | `+0.0s` |
| `2026-10-25 04:33:51` | `17.05%` | `0.0%` | 88 | 71 | `+0.0s` |
| `2026-10-25 03:30:18` | `26.42%` | `0.0%` | 106 | 76 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T07:00:19.664000+00:00`.*
