# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-24T07:00:18.071000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.92%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `65` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `53` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 16.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 17 | 9 | 8 | **`47.06%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 2 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 13 | 13 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41604 is broadcasting off-schedule with no vehicle covering 79020 |
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41504 is broadcasting off-schedule with no vehicle covering 3912020 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41507 is broadcasting off-schedule with no vehicle covering 3010020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9728 is broadcasting off-schedule with no vehicle covering 2295020 |
| `LLR_2026-11-23_20261007_Link_RailMilling2NGS_Weekday_2LINE_4031` | Route 2LINE | `07:31:30` | `DUPLICATED` | Assigned vehicle 437.482478 is broadcasting off-schedule with no vehicle covering LLR_2026-11-23_20261007_Link_RailMilling2NGS_Weekday_2LINE_4031 |
| `LLR_2026-11-23_20261007_Link_RailMilling2NGS_Weekday_2LINE_3103` | Route 2LINE | `18:50:30` | `DUPLICATED` | Assigned vehicle 476.173728 is broadcasting off-schedule with no vehicle covering LLR_2026-11-23_20261007_Link_RailMilling2NGS_Weekday_2LINE_3103 |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 61402 is broadcasting off-schedule with no vehicle covering 3660020 |
| `881957561` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298755 is missing from active GPS transponder fleet |
| `350247561` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8298728 is missing from active GPS transponder fleet |
| `560092511` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298728 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298729 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:18` | `16.92%` | `0.0%` | 65 | 53 | `+0.0s` |
| `2026-11-24 05:30:17` | `21.05%` | `0.0%` | 95 | 71 | `+0.0s` |
| `2026-11-24 05:00:18` | `23.66%` | `0.0%` | 93 | 76 | `+0.0s` |
| `2026-11-24 04:30:17` | `21.9%` | `0.0%` | 105 | 87 | `+0.0s` |
| `2026-11-24 04:00:18` | `17.86%` | `0.0%` | 112 | 91 | `+0.0s` |
| `2026-11-24 03:30:19` | `17.89%` | `0.0%` | 123 | 101 | `+0.0s` |
| `2026-11-24 03:00:18` | `22.14%` | `0.0%` | 140 | 109 | `+0.0s` |
| `2026-11-24 02:30:18` | `23.72%` | `0.0%` | 156 | 120 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:18.071000+00:00`.*
