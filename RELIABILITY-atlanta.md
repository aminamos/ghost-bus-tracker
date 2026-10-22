# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T15:01:10.579000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `412` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `178` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `35` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 35 | 8.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 106 | 25.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 189** | 4 | 2 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 120** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 89** | 7 | 5 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 104** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 20** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route A** | 8 | 3 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 10 | 6 | 2 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `11696346` | Route 4 | `10:50:00` | `SCHEDULED` | Assigned vehicle 2305 is broadcasting off-schedule with no vehicle covering 11696346 |
| `11723021` | Route 104 | `10:45:00` | `SCHEDULED` | Assigned vehicle 2307 is broadcasting off-schedule with no vehicle covering 11723021 |
| `11725801` | Route 116 | `10:58:00` | `SCHEDULED` | Assigned vehicle 2310 is broadcasting off-schedule with no vehicle covering 11725801 |
| `11730180` | Route 128 | `10:59:00` | `SCHEDULED` | Assigned vehicle 2317 is broadcasting off-schedule with no vehicle covering 11730180 |
| `11728924` | Route 121 | `11:00:00` | `SCHEDULED` | Assigned vehicle 2327 is broadcasting off-schedule with no vehicle covering 11728924 |
| `11704305` | Route 23 | `11:11:00` | `SCHEDULED` | Assigned vehicle 2388 is broadcasting off-schedule with no vehicle covering 11704305 |
| `11736636` | Route 193 | `11:15:00` | `SCHEDULED` | Assigned vehicle 3522 is broadcasting off-schedule with no vehicle covering 11736636 |
| `11720792` | Route 89 | `11:07:00` | `SCHEDULED` | Assigned vehicle 3529 is broadcasting off-schedule with no vehicle covering 11720792 |
| `11720675` | Route 89 | `11:02:00` | `SCHEDULED` | Assigned vehicle 3535 is broadcasting off-schedule with no vehicle covering 11720675 |
| `11720736` | Route 89 | `11:18:00` | `SCHEDULED` | Assigned vehicle 3538 is broadcasting off-schedule with no vehicle covering 11720736 |
| `11703513` | Route 22 | `11:17:00` | `SCHEDULED` | Assigned vehicle 3649 is broadcasting off-schedule with no vehicle covering 11703513 |
| `11695286` | Route 2 | `10:50:00` | `SCHEDULED` | Assigned vehicle 3661 is broadcasting off-schedule with no vehicle covering 11695286 |
| `11729584` | Route 125 | `11:10:00` | `SCHEDULED` | Assigned vehicle 3665 is broadcasting off-schedule with no vehicle covering 11729584 |
| `11719367` | Route 87 | `11:10:00` | `SCHEDULED` | Assigned vehicle 3687 is broadcasting off-schedule with no vehicle covering 11719367 |
| `11697720` | Route 7 | `11:15:00` | `SCHEDULED` | Assigned vehicle 3705 is broadcasting off-schedule with no vehicle covering 11697720 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 15:01:10` | `8.5%` | `0.0%` | 412 | 178 | `+0.0s` |
| `2026-10-22 12:30:38` | `6.65%` | `0.0%` | 481 | 185 | `+0.0s` |
| `2026-10-22 12:00:43` | `7.73%` | `0.0%` | 440 | 180 | `+0.0s` |
| `2026-10-22 11:30:36` | `9.66%` | `0.0%` | 435 | 181 | `+0.0s` |
| `2026-10-22 11:00:36` | `9.29%` | `0.0%` | 452 | 187 | `+0.0s` |
| `2026-10-22 10:30:35` | `9.81%` | `0.0%` | 418 | 180 | `+0.0s` |
| `2026-10-22 10:00:34` | `11.08%` | `0.0%` | 388 | 179 | `+0.0s` |
| `2026-10-22 09:30:35` | `5.63%` | `0.0%` | 373 | 163 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T15:01:10.579000+00:00`.*
