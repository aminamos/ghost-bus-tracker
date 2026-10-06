# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T17:21:06.136405+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.79%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `387` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `179` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `34` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 34 | 8.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 94 | 24.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 88** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 95** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 39** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 71** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 104** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 187** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 80** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 85** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 17** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `11726861` | Route 118 | `13:30:00` | `SCHEDULED` | Assigned vehicle 2309 is broadcasting off-schedule with no vehicle covering 11726861 |
| `11714097` | Route 75 | `13:30:00` | `SCHEDULED` | Assigned vehicle 2310 is broadcasting off-schedule with no vehicle covering 11714097 |
| `11721696` | Route 95 | `13:20:00` | `SCHEDULED` | Assigned vehicle 2325 is broadcasting off-schedule with no vehicle covering 11721696 |
| `11710377` | Route 55 | `13:24:00` | `SCHEDULED` | Assigned vehicle 2329 is broadcasting off-schedule with no vehicle covering 11710377 |
| `11697197` | Route 5 | `13:30:00` | `SCHEDULED` | Assigned vehicle 2381 is broadcasting off-schedule with no vehicle covering 11697197 |
| `11706662` | Route 39 | `13:46:00` | `SCHEDULED` | Assigned vehicle 2416 is broadcasting off-schedule with no vehicle covering 11706662 |
| `11720716` | Route 89 | `13:32:00` | `SCHEDULED` | Assigned vehicle 3552 is broadcasting off-schedule with no vehicle covering 11720716 |
| `11718374` | Route 84 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3554 is broadcasting off-schedule with no vehicle covering 11718374 |
| `11721767` | Route 95 | `13:25:00` | `SCHEDULED` | Assigned vehicle 3556 is broadcasting off-schedule with no vehicle covering 11721767 |
| `11735297` | Route 187 | `13:27:00` | `SCHEDULED` | Assigned vehicle 3562 is broadcasting off-schedule with no vehicle covering 11735297 |
| `11707310` | Route 42 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3593 is broadcasting off-schedule with no vehicle covering 11707310 |
| `11718841` | Route 85 | `13:13:00` | `SCHEDULED` | Assigned vehicle 3607 is broadcasting off-schedule with no vehicle covering 11718841 |
| `11736593` | Route 193 | `13:25:00` | `SCHEDULED` | Assigned vehicle 3621 is broadcasting off-schedule with no vehicle covering 11736593 |
| `11722996` | Route 104 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3656 is broadcasting off-schedule with no vehicle covering 11722996 |
| `11700935` | Route 15 | `13:32:00` | `SCHEDULED` | Assigned vehicle 3657 is broadcasting off-schedule with no vehicle covering 11700935 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 17:21:06` | `8.79%` | `0.0%` | 387 | 179 | `+0.0s` |
| `2026-10-06 13:46:38` | `8.35%` | `0.0%` | 443 | 174 | `+0.0s` |
| `2026-10-06 06:42:12` | `0.0%` | `0.0%` | 6 | 5 | `+0.0s` |
| `2026-10-06 00:28:48` | `12.35%` | `0.0%` | 332 | 165 | `+0.0s` |
| `2026-10-05 18:39:13` | `6.9%` | `0.0%` | 290 | 170 | `+0.0s` |
| `2026-10-05 18:02:21` | `9.06%` | `0.0%` | 320 | 180 | `+0.0s` |
| `2026-10-05 17:57:50` | `9.26%` | `0.0%` | 324 | 177 | `+0.0s` |
| `2026-10-05 17:20:40` | `9.46%` | `0.0%` | 349 | 176 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T17:21:06.136405+00:00`.*
