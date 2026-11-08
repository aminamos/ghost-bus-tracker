# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:17.754000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `64` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 18.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 18 | 10 | 8 | **`44.44%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 2 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 14 | 14 | 2 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_2LINE_4020` | Route 2LINE | `06:39:30` | `DUPLICATED` | Assigned vehicle 55.187115 is broadcasting off-schedule with no vehicle covering LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_2LINE_4020 |
| `2018070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41501 is broadcasting off-schedule with no vehicle covering 2018070 |
| `923070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41503 is broadcasting off-schedule with no vehicle covering 923070 |
| `4694070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9721 is broadcasting off-schedule with no vehicle covering 4694070 |
| `2456070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9722 is broadcasting off-schedule with no vehicle covering 2456070 |
| `LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_2LINE_3009` | Route 2LINE | `05:25:30` | `DUPLICATED` | Assigned vehicle 56.456779 is broadcasting off-schedule with no vehicle covering LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_2LINE_3009 |
| `LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_100479_2061` | Route 100479 | `13:44:30` | `DUPLICATED` | Assigned vehicle 49.227763 is broadcasting off-schedule with no vehicle covering LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_100479_2061 |
| `17066043__H:171:5:Saturday:3:26SEP:57012:6` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:171:5:Saturday:3:26SEP:57012:6 is missing from active GPS transponder fleet |
| `704070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9126 is broadcasting off-schedule with no vehicle covering 704070 |
| `LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_100479_2061` | Route 100479 | `13:44:30` | `DUPLICATED` | Assigned vehicle 53.974277 is broadcasting off-schedule with no vehicle covering LLR_2026-11-07_20261007_Link_RailMilling2NGS_Saturday_100479_2061 |
| `851768131` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273688 is missing from active GPS transponder fleet |
| `851768101` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273682 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:17` | `18.75%` | `0.0%` | 64 | 54 | `+0.0s` |
| `2026-11-08 06:00:17` | `16.25%` | `0.0%` | 80 | 64 | `+0.0s` |
| `2026-11-08 05:00:18` | `12.37%` | `0.0%` | 97 | 71 | `+0.0s` |
| `2026-11-08 04:30:19` | `14.29%` | `0.0%` | 105 | 77 | `+0.0s` |
| `2026-11-08 04:00:18` | `17.48%` | `0.0%` | 103 | 80 | `+0.0s` |
| `2026-11-08 03:30:18` | `17.43%` | `0.0%` | 109 | 83 | `+0.0s` |
| `2026-11-08 03:00:17` | `24.35%` | `0.0%` | 115 | 82 | `+0.0s` |
| `2026-11-08 02:30:17` | `22.22%` | `0.0%` | 126 | 88 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.754000+00:00`.*
