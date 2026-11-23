# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:17.971000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `51` | Total runs operating in current transit schedule window |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 25.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 13 | 4 | 9 | **`69.23%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 11 | 11 | 2 | **`18.18%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 12 | 12 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 4 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `849295741` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298561 is missing from active GPS transponder fleet |
| `851804231` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298558 is missing from active GPS transponder fleet |
| `867187601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298557 is missing from active GPS transponder fleet |
| `851804811` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298549 is missing from active GPS transponder fleet |
| `851804801` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298549 is missing from active GPS transponder fleet |
| `3875010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41515 is broadcasting off-schedule with no vehicle covering 3875010 |
| `3275010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41503 is broadcasting off-schedule with no vehicle covering 3275010 |
| `3936010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9737 is broadcasting off-schedule with no vehicle covering 3936010 |
| `1065010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9733 is broadcasting off-schedule with no vehicle covering 1065010 |
| `LLR_2026-11-22_20261007_Link_RailMilling2NGS_Sunday_2LINE_3081` | Route 2LINE | `18:25:30` | `DUPLICATED` | Assigned vehicle 345.273653 is broadcasting off-schedule with no vehicle covering LLR_2026-11-22_20261007_Link_RailMilling2NGS_Sunday_2LINE_3081 |
| `LLR_2026-11-22_20261007_Link_RailMilling2NGS_Sunday_2LINE_4095` | Route 2LINE | `19:29:30` | `DUPLICATED` | Assigned vehicle 358.817612 is broadcasting off-schedule with no vehicle covering LLR_2026-11-22_20261007_Link_RailMilling2NGS_Sunday_2LINE_4095 |
| `3292010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9123 is broadcasting off-schedule with no vehicle covering 3292010 |
| `1274010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51402 is broadcasting off-schedule with no vehicle covering 1274010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:17` | `25.49%` | `0.0%` | 51 | 46 | `+0.0s` |
| `2026-11-23 06:30:17` | `16.95%` | `0.0%` | 59 | 51 | `+0.0s` |
| `2026-11-23 06:00:18` | `17.65%` | `0.0%` | 68 | 53 | `+0.0s` |
| `2026-11-23 05:30:17` | `12.0%` | `0.0%` | 75 | 57 | `+0.0s` |
| `2026-11-23 04:30:18` | `12.5%` | `0.0%` | 80 | 63 | `+0.0s` |
| `2026-11-23 04:00:18` | `15.38%` | `0.0%` | 78 | 63 | `+0.0s` |
| `2026-11-23 03:30:17` | `12.64%` | `0.0%` | 87 | 70 | `+0.0s` |
| `2026-11-23 03:00:18` | `20.93%` | `0.0%` | 86 | 71 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:17.971000+00:00`.*
