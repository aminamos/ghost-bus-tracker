# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-21T22:30:36.612000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.39%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `482` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `178` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `26` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 26 | 5.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 169 | 35.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 74** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 83** | 7 | 5 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route A** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 184** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 55** | 8 | 5 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 185** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 95** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 75** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `11700943` | Route 15 | `15:24:00` | `SCHEDULED` | Assigned vehicle 2303 is broadcasting off-schedule with no vehicle covering 11700943 |
| `11723973` | Route 111 | `18:19:00` | `SCHEDULED` | Assigned vehicle 2308 is broadcasting off-schedule with no vehicle covering 11723973 |
| `11721716` | Route 95 | `18:20:00` | `SCHEDULED` | Assigned vehicle 2328 is broadcasting off-schedule with no vehicle covering 11721716 |
| `11704897` | Route 26 | `18:43:00` | `SCHEDULED` | Assigned vehicle 2359 is broadcasting off-schedule with no vehicle covering 11704897 |
| `11734499` | Route 184 | `18:49:00` | `SCHEDULED` | Assigned vehicle 3513 is broadcasting off-schedule with no vehicle covering 11734499 |
| `11784701` | Route 83 | `18:36:00` | `SCHEDULED` | Assigned vehicle 3520 is broadcasting off-schedule with no vehicle covering 11784701 |
| `11710390` | Route 55 | `18:31:00` | `SCHEDULED` | Assigned vehicle 3580 is broadcasting off-schedule with no vehicle covering 11710390 |
| `11707320` | Route 42 | `18:30:00` | `SCHEDULED` | Assigned vehicle 3593 is broadcasting off-schedule with no vehicle covering 11707320 |
| `11706681` | Route 39 | `18:31:00` | `SCHEDULED` | Assigned vehicle 3640 is broadcasting off-schedule with no vehicle covering 11706681 |
| `11714067` | Route 75 | `17:40:00` | `SCHEDULED` | Assigned vehicle 3649 is broadcasting off-schedule with no vehicle covering 11714067 |
| `11784700` | Route 83 | `18:24:00` | `SCHEDULED` | Assigned vehicle 3695 is broadcasting off-schedule with no vehicle covering 11784700 |
| `11784617` | Route 83 | `18:23:00` | `SCHEDULED` | Assigned vehicle 4628 is broadcasting off-schedule with no vehicle covering 11784617 |
| `11709507` | Route 51 | `18:30:00` | `SCHEDULED` | Assigned vehicle 4640 is broadcasting off-schedule with no vehicle covering 11709507 |
| `11782195` | Route 20 | `18:30:00` | `SCHEDULED` | Assigned vehicle 4675 is broadcasting off-schedule with no vehicle covering 11782195 |
| `11726871` | Route 118 | `18:30:00` | `SCHEDULED` | Assigned vehicle 4676 is broadcasting off-schedule with no vehicle covering 11726871 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 22:30:36` | `5.39%` | `0.0%` | 482 | 178 | `+0.0s` |
| `2026-10-21 22:00:36` | `5.58%` | `0.0%` | 484 | 178 | `+0.0s` |
| `2026-10-21 21:30:36` | `5.04%` | `0.0%` | 496 | 183 | `+0.0s` |
| `2026-10-21 21:00:37` | `3.48%` | `0.0%` | 517 | 184 | `+0.0s` |
| `2026-10-21 20:30:37` | `5.26%` | `0.0%` | 513 | 186 | `+0.0s` |
| `2026-10-21 20:00:36` | `5.97%` | `0.0%` | 519 | 185 | `+0.0s` |
| `2026-10-21 18:30:40` | `6.07%` | `0.0%` | 428 | 173 | `+0.0s` |
| `2026-10-21 16:01:17` | `10.2%` | `0.0%` | 392 | 177 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T22:30:36.612000+00:00`.*
