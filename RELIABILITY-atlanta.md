# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T18:39:13.807049+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.9%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `290` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `170` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 20 | 6.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 33 | 11.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 7** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 39** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 125** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 22** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 49** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `11708736` | Route 49 | `14:46:00` | `SCHEDULED` | Assigned vehicle 2329 is broadcasting off-schedule with no vehicle covering 11708736 |
| `11697141` | Route 5 | `14:40:00` | `SCHEDULED` | Assigned vehicle 2370 is broadcasting off-schedule with no vehicle covering 11697141 |
| `11722546` | Route 96 | `14:50:00` | `SCHEDULED` | Assigned vehicle 3512 is broadcasting off-schedule with no vehicle covering 11722546 |
| `11722603` | Route 96 | `14:25:00` | `SCHEDULED` | Assigned vehicle 3532 is broadcasting off-schedule with no vehicle covering 11722603 |
| `11732599` | Route 165 | `14:40:00` | `SCHEDULED` | Assigned vehicle 3554 is broadcasting off-schedule with no vehicle covering 11732599 |
| `11715138` | Route 78 | `13:40:00` | `SCHEDULED` | Assigned vehicle 3565 is broadcasting off-schedule with no vehicle covering 11715138 |
| `11721772` | Route 95 | `14:40:00` | `SCHEDULED` | Assigned vehicle 3573 is broadcasting off-schedule with no vehicle covering 11721772 |
| `11725249` | Route 115 | `14:43:00` | `SCHEDULED` | Assigned vehicle 3635 is broadcasting off-schedule with no vehicle covering 11725249 |
| `11706666` | Route 39 | `14:46:00` | `SCHEDULED` | Assigned vehicle 3663 is broadcasting off-schedule with no vehicle covering 11706666 |
| `11697727` | Route 7 | `14:45:00` | `SCHEDULED` | Assigned vehicle 3702 is broadcasting off-schedule with no vehicle covering 11697727 |
| `11695839` | Route 3 | `15:00:00` | `SCHEDULED` | Assigned vehicle 3707 is broadcasting off-schedule with no vehicle covering 11695839 |
| `11719708` | Route 88 | `14:40:00` | `SCHEDULED` | Assigned vehicle 3719 is broadcasting off-schedule with no vehicle covering 11719708 |
| `11729894` | Route 127 | `14:50:00` | `SCHEDULED` | Assigned vehicle 3720 is broadcasting off-schedule with no vehicle covering 11729894 |
| `11707274` | Route 42 | `14:45:00` | `SCHEDULED` | Assigned vehicle 3733 is broadcasting off-schedule with no vehicle covering 11707274 |
| `11733137` | Route 178 | `14:46:00` | `SCHEDULED` | Assigned vehicle 3753 is broadcasting off-schedule with no vehicle covering 11733137 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 18:39:13` | `6.9%` | `0.0%` | 290 | 170 | `+0.0s` |
| `2026-10-05 18:02:21` | `9.06%` | `0.0%` | 320 | 180 | `+0.0s` |
| `2026-10-05 17:57:50` | `9.26%` | `0.0%` | 324 | 177 | `+0.0s` |
| `2026-10-05 17:20:40` | `9.46%` | `0.0%` | 349 | 176 | `+0.0s` |
| `2026-10-05 16:34:19` | `6.72%` | `0.0%` | 372 | 172 | `+0.0s` |
| `2026-10-05 12:15:27` | `7.61%` | `0.0%` | 447 | 176 | `+0.0s` |
| `2026-10-05 12:14:31` | `7.4%` | `0.0%` | 446 | 175 | `+0.0s` |
| `2026-10-05 12:10:54` | `7.42%` | `0.0%` | 445 | 175 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:39:13.807049+00:00`.*
