# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T17:57:50.571984+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.26%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `324` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `177` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `30` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 30 | 9.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 37 | 11.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 7** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 120** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 125** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 55** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 187** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 182** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `11729549` | Route 125 | `13:55:00` | `SCHEDULED` | Assigned vehicle 2310 is broadcasting off-schedule with no vehicle covering 11729549 |
| `11710351` | Route 55 | `14:00:00` | `SCHEDULED` | Assigned vehicle 2325 is broadcasting off-schedule with no vehicle covering 11710351 |
| `11697199` | Route 5 | `14:10:00` | `SCHEDULED` | Assigned vehicle 2356 is broadcasting off-schedule with no vehicle covering 11697199 |
| `11704873` | Route 26 | `14:14:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering 11704873 |
| `11697139` | Route 5 | `14:00:00` | `SCHEDULED` | Assigned vehicle 2371 is broadcasting off-schedule with no vehicle covering 11697139 |
| `11713122` | Route 73 | `14:06:00` | `SCHEDULED` | Assigned vehicle 2381 is broadcasting off-schedule with no vehicle covering 11713122 |
| `11706663` | Route 39 | `14:01:00` | `SCHEDULED` | Assigned vehicle 2405 is broadcasting off-schedule with no vehicle covering 11706663 |
| `11735299` | Route 187 | `14:07:00` | `SCHEDULED` | Assigned vehicle 3552 is broadcasting off-schedule with no vehicle covering 11735299 |
| `11784656` | Route 83 | `14:00:00` | `SCHEDULED` | Assigned vehicle 3555 is broadcasting off-schedule with no vehicle covering 11784656 |
| `11708735` | Route 49 | `14:06:00` | `SCHEDULED` | Assigned vehicle 3562 is broadcasting off-schedule with no vehicle covering 11708735 |
| `11720795` | Route 89 | `13:59:00` | `SCHEDULED` | Assigned vehicle 3572 is broadcasting off-schedule with no vehicle covering 11720795 |
| `11719413` | Route 87 | `13:55:00` | `SCHEDULED` | Assigned vehicle 3616 is broadcasting off-schedule with no vehicle covering 11719413 |
| `11754749` | Route 182 | `14:00:00` | `SCHEDULED` | Assigned vehicle 3628 is broadcasting off-schedule with no vehicle covering 11754749 |
| `11726862` | Route 118 | `14:00:00` | `SCHEDULED` | Assigned vehicle 3649 is broadcasting off-schedule with no vehicle covering 11726862 |
| `11729893` | Route 127 | `14:10:00` | `SCHEDULED` | Assigned vehicle 3650 is broadcasting off-schedule with no vehicle covering 11729893 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:57:50.571984+00:00`.*
