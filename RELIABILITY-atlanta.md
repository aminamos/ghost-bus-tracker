# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T17:20:40.666177+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `349` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `176` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `33` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 33 | 9.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 54 | 15.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route A** | 5 | 4 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route 71** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 182** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 89** | 9 | 6 | 3 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 55** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 80** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 187** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 81** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 127** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 20** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `11783667` | Route 117 | `13:41:00` | `SCHEDULED` | Assigned vehicle 2327 is broadcasting off-schedule with no vehicle covering 11783667 |
| `11710350` | Route 55 | `13:30:00` | `SCHEDULED` | Assigned vehicle 2342 is broadcasting off-schedule with no vehicle covering 11710350 |
| `11697197` | Route 5 | `13:30:00` | `SCHEDULED` | Assigned vehicle 2350 is broadcasting off-schedule with no vehicle covering 11697197 |
| `11699380` | Route 12 | `13:15:00` | `SCHEDULED` | Assigned vehicle 2373 is broadcasting off-schedule with no vehicle covering 11699380 |
| `11722542` | Route 96 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3512 is broadcasting off-schedule with no vehicle covering 11722542 |
| `11720697` | Route 89 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3545 is broadcasting off-schedule with no vehicle covering 11720697 |
| `11735297` | Route 187 | `13:27:00` | `SCHEDULED` | Assigned vehicle 3552 is broadcasting off-schedule with no vehicle covering 11735297 |
| `11733615` | Route 180 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3574 is broadcasting off-schedule with no vehicle covering 11733615 |
| `11720776` | Route 89 | `13:37:00` | `SCHEDULED` | Assigned vehicle 3575 is broadcasting off-schedule with no vehicle covering 11720776 |
| `11720716` | Route 89 | `13:32:00` | `SCHEDULED` | Assigned vehicle 3577 is broadcasting off-schedule with no vehicle covering 11720716 |
| `11716370` | Route 81 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3588 is broadcasting off-schedule with no vehicle covering 11716370 |
| `11721767` | Route 95 | `13:25:00` | `SCHEDULED` | Assigned vehicle 3621 is broadcasting off-schedule with no vehicle covering 11721767 |
| `11722996` | Route 104 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3662 is broadcasting off-schedule with no vehicle covering 11722996 |
| `11719372` | Route 87 | `13:40:00` | `SCHEDULED` | Assigned vehicle 3682 is broadcasting off-schedule with no vehicle covering 11719372 |
| `11729892` | Route 127 | `13:30:00` | `SCHEDULED` | Assigned vehicle 3720 is broadcasting off-schedule with no vehicle covering 11729892 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:20:40.666177+00:00`.*
