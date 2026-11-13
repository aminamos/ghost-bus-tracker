# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-13T06:30:17.920000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `83` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 13.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 28 | 16 | 11 | **`39.29%`** | `0.0%` | `+0.0s` |
| **Route 560** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100511** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 15 | 15 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 6 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 11 | 11 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `2226020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9735 is broadcasting off-schedule with no vehicle covering 2226020 |
| `851839341` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298628 is missing from active GPS transponder fleet |
| `1799020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9217 is broadcasting off-schedule with no vehicle covering 1799020 |
| `567020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9217 is broadcasting off-schedule with no vehicle covering 567020 |
| `1095020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9306 is broadcasting off-schedule with no vehicle covering 1095020 |
| `17068830__H:121:0:Weekday:3:26SEP:52062:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52062:12345 is missing from active GPS transponder fleet |
| `17068762__H:121:0:Weekday:3:26SEP:52062:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52062:12345 is missing from active GPS transponder fleet |
| `350247351` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298727 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298729 is missing from active GPS transponder fleet |
| `851857151` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298706 is missing from active GPS transponder fleet |
| `559501081` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298707 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 06:30:17` | `13.25%` | `0.0%` | 83 | 58 | `+0.0s` |
| `2026-11-13 06:00:19` | `19.59%` | `0.0%` | 97 | 66 | `+0.0s` |
| `2026-11-13 05:30:18` | `25.96%` | `0.0%` | 104 | 76 | `+0.0s` |
| `2026-11-13 05:00:18` | `21.19%` | `0.0%` | 118 | 84 | `+0.0s` |
| `2026-11-13 04:30:18` | `20.0%` | `0.0%` | 125 | 89 | `+0.0s` |
| `2026-11-13 04:00:18` | `20.9%` | `0.0%` | 134 | 94 | `+0.0s` |
| `2026-11-13 03:00:18` | `19.51%` | `0.0%` | 164 | 118 | `+0.0s` |
| `2026-11-13 02:30:18` | `24.19%` | `0.0%` | 186 | 139 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T06:30:17.920000+00:00`.*
