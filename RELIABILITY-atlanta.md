# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T18:30:37.860000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.08%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `421` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `176` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 34 | 8.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 168 | 39.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 180** | 5 | 4 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 189** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 6 | 6 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 119** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 125** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 118** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 39** | 8 | 6 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `11730156` | Route 128 | `14:30:00` | `SCHEDULED` | Assigned vehicle 2317 is broadcasting off-schedule with no vehicle covering 11730156 |
| `11783706` | Route 117 | `14:30:00` | `SCHEDULED` | Assigned vehicle 2327 is broadcasting off-schedule with no vehicle covering 11783706 |
| `11732560` | Route 165 | `14:30:00` | `SCHEDULED` | Assigned vehicle 2328 is broadcasting off-schedule with no vehicle covering 11732560 |
| `11699345` | Route 12 | `14:35:00` | `SCHEDULED` | Assigned vehicle 2361 is broadcasting off-schedule with no vehicle covering 11699345 |
| `11715142` | Route 78 | `14:40:00` | `SCHEDULED` | Assigned vehicle 3533 is broadcasting off-schedule with no vehicle covering 11715142 |
| `11722545` | Route 96 | `14:30:00` | `SCHEDULED` | Assigned vehicle 3572 is broadcasting off-schedule with no vehicle covering 11722545 |
| `11719374` | Route 87 | `14:40:00` | `SCHEDULED` | Assigned vehicle 3612 is broadcasting off-schedule with no vehicle covering 11719374 |
| `11706665` | Route 39 | `14:31:00` | `SCHEDULED` | Assigned vehicle 3645 is broadcasting off-schedule with no vehicle covering 11706665 |
| `11700937` | Route 15 | `14:02:00` | `SCHEDULED` | Assigned vehicle 3647 is broadcasting off-schedule with no vehicle covering 11700937 |
| `11714094` | Route 75 | `12:00:00` | `SCHEDULED` | Assigned vehicle 3659 is broadcasting off-schedule with no vehicle covering 11714094 |
| `11695250` | Route 2 | `14:00:00` | `SCHEDULED` | Assigned vehicle 3660 is broadcasting off-schedule with no vehicle covering 11695250 |
| `11727395` | Route 119 | `14:30:00` | `SCHEDULED` | Assigned vehicle 3669 is broadcasting off-schedule with no vehicle covering 11727395 |
| `11706666` | Route 39 | `14:46:00` | `SCHEDULED` | Assigned vehicle 3676 is broadcasting off-schedule with no vehicle covering 11706666 |
| `11697201` | Route 5 | `14:50:00` | `SCHEDULED` | Assigned vehicle 3685 is broadcasting off-schedule with no vehicle covering 11697201 |
| `11697767` | Route 7 | `14:45:00` | `SCHEDULED` | Assigned vehicle 3702 is broadcasting off-schedule with no vehicle covering 11697767 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:30:37` | `8.08%` | `0.0%` | 421 | 176 | `+0.0s` |
| `2026-10-22 15:01:10` | `8.5%` | `0.0%` | 412 | 178 | `+0.0s` |
| `2026-10-22 12:30:38` | `6.65%` | `0.0%` | 481 | 185 | `+0.0s` |
| `2026-10-22 12:00:43` | `7.73%` | `0.0%` | 440 | 180 | `+0.0s` |
| `2026-10-22 11:30:36` | `9.66%` | `0.0%` | 435 | 181 | `+0.0s` |
| `2026-10-22 11:00:36` | `9.29%` | `0.0%` | 452 | 187 | `+0.0s` |
| `2026-10-22 10:30:35` | `9.81%` | `0.0%` | 418 | 180 | `+0.0s` |
| `2026-10-22 10:00:34` | `11.08%` | `0.0%` | 388 | 179 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:30:37.860000+00:00`.*
