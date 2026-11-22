# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-22T06:00:17.602000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.86%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `74` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `59` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 14.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 100236** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 19 | 11 | 7 | **`36.84%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 14 | 14 | 1 | **`7.14%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 17 | 17 | 1 | **`5.88%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 577** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 7 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route TLINE** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2104070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41506 is broadcasting off-schedule with no vehicle covering 2104070 |
| `3424070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9715 is broadcasting off-schedule with no vehicle covering 3424070 |
| `1002070` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9721 is broadcasting off-schedule with no vehicle covering 1002070 |
| `569521031` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298378 is missing from active GPS transponder fleet |
| `547581961` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8298441 is missing from active GPS transponder fleet |
| `353313921` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298441 is missing from active GPS transponder fleet |
| `851767961` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298437 is missing from active GPS transponder fleet |
| `851767931` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298435 is missing from active GPS transponder fleet |
| `851768121` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298435 is missing from active GPS transponder fleet |
| `LLR_2026-11-21_20261007_Link_RailMilling2NGS_Saturday_2LINE_3076` | Route 2LINE | `16:35:30` | `DUPLICATED` | Assigned vehicle 303.122632 is broadcasting off-schedule with no vehicle covering LLR_2026-11-21_20261007_Link_RailMilling2NGS_Saturday_2LINE_3076 |
| `LLR_2026-11-21_20261007_Link_RailMilling2NGS_Saturday_100479_2055` | Route 100479 | `12:44:30` | `DUPLICATED` | Assigned vehicle 258.835977 is broadcasting off-schedule with no vehicle covering LLR_2026-11-21_20261007_Link_RailMilling2NGS_Saturday_100479_2055 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 06:00:17` | `14.86%` | `0.0%` | 74 | 59 | `+0.0s` |
| `2026-11-22 05:30:19` | `10.13%` | `0.0%` | 79 | 62 | `+0.0s` |
| `2026-11-22 05:00:18` | `17.5%` | `0.0%` | 80 | 63 | `+0.0s` |
| `2026-11-22 04:30:17` | `10.71%` | `0.0%` | 84 | 67 | `+0.0s` |
| `2026-11-22 04:00:17` | `15.66%` | `0.0%` | 83 | 69 | `+0.0s` |
| `2026-11-22 03:00:17` | `23.66%` | `0.0%` | 93 | 75 | `+0.0s` |
| `2026-11-22 02:00:18` | `20.19%` | `0.0%` | 104 | 80 | `+0.0s` |
| `2026-11-22 01:30:17` | `16.83%` | `0.0%` | 101 | 79 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T06:00:17.602000+00:00`.*
