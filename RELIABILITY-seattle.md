# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T18:30:35.918000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `155` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `105` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `36` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 36 | 23.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 59 | 30 | 29 | **`49.15%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 8 | 5 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 8 | 5 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 535** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 512** | 6 | 5 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 16 | 16 | 1 | **`6.25%`** | `0.0%` | `+0.0s` |
| **Route 560** | 4 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 6 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100511** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 6 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `LLR_2026-10-22_20261007_Link_RailMilling2JPS_Weekday_2LINE_4035` | Route 2LINE | `08:03:30` | `DUPLICATED` | Assigned vehicle 666.623779 is broadcasting off-schedule with no vehicle covering LLR_2026-10-22_20261007_Link_RailMilling2JPS_Weekday_2LINE_4035 |
| `1130020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51402 is broadcasting off-schedule with no vehicle covering 1130020 |
| `3186020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9220 is broadcasting off-schedule with no vehicle covering 3186020 |
| `482020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41513 is broadcasting off-schedule with no vehicle covering 482020 |
| `17068721__H:121:0:Weekday:3:26SEP:52038:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52038:12345 is missing from active GPS transponder fleet |
| `2899020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9718 is broadcasting off-schedule with no vehicle covering 2899020 |
| `1402020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9718 is broadcasting off-schedule with no vehicle covering 1402020 |
| `4517020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9716 is broadcasting off-schedule with no vehicle covering 4517020 |
| `3821020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9717 is broadcasting off-schedule with no vehicle covering 3821020 |
| `4392020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9728 is broadcasting off-schedule with no vehicle covering 4392020 |
| `17069052__H:121:0:Weekday:3:26SEP:52035:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52035:12345 is missing from active GPS transponder fleet |
| `17069082__H:121:0:Weekday:3:26SEP:52032:12345` | Route 535 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52032:12345 is missing from active GPS transponder fleet |
| `851843321` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8273923 is missing from active GPS transponder fleet |
| `851843341` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273923 is missing from active GPS transponder fleet |
| `851839361` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273873 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:30:35` | `23.23%` | `0.0%` | 155 | 105 | `+0.0s` |
| `2026-10-22 17:30:36` | `0.0%` | `0.0%` | 19 | 111 | `+0.0s` |
| `2026-10-22 16:01:15` | `19.46%` | `0.0%` | 149 | 98 | `+0.0s` |
| `2026-10-22 15:01:08` | `21.34%` | `0.0%` | 239 | 163 | `+0.0s` |
| `2026-10-22 14:00:42` | `23.35%` | `0.0%` | 227 | 150 | `+0.0s` |
| `2026-10-22 13:31:53` | `27.19%` | `0.0%` | 217 | 138 | `+0.0s` |
| `2026-10-22 12:30:36` | `29.87%` | `0.0%` | 154 | 100 | `+0.0s` |
| `2026-10-22 12:00:39` | `30.77%` | `0.0%` | 65 | 71 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:30:35.918000+00:00`.*
