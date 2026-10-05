# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T16:34:19.261202+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `372` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `172` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `25` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 25 | 6.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 75 | 20.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route A** | 4 | 4 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 187** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 20** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 162** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 22** | 5 | 5 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 125** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 184** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 83** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 180** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `11729587` | Route 125 | `12:40:00` | `SCHEDULED` | Assigned vehicle 2310 is broadcasting off-schedule with no vehicle covering 11729587 |
| `11704891` | Route 26 | `12:45:00` | `SCHEDULED` | Assigned vehicle 2387 is broadcasting off-schedule with no vehicle covering 11704891 |
| `11736618` | Route 193 | `12:37:00` | `SCHEDULED` | Assigned vehicle 3507 is broadcasting off-schedule with no vehicle covering 11736618 |
| `11734487` | Route 184 | `12:49:00` | `SCHEDULED` | Assigned vehicle 3528 is broadcasting off-schedule with no vehicle covering 11734487 |
| `11735295` | Route 187 | `12:47:00` | `SCHEDULED` | Assigned vehicle 3552 is broadcasting off-schedule with no vehicle covering 11735295 |
| `11732594` | Route 165 | `12:11:00` | `SCHEDULED` | Assigned vehicle 3554 is broadcasting off-schedule with no vehicle covering 11732594 |
| `11784568` | Route 83 | `12:30:00` | `SCHEDULED` | Assigned vehicle 3556 is broadcasting off-schedule with no vehicle covering 11784568 |
| `11733654` | Route 180 | `12:45:00` | `SCHEDULED` | Assigned vehicle 3574 is broadcasting off-schedule with no vehicle covering 11733654 |
| `11719370` | Route 87 | `12:40:00` | `SCHEDULED` | Assigned vehicle 3616 is broadcasting off-schedule with no vehicle covering 11719370 |
| `11703516` | Route 22 | `12:47:00` | `SCHEDULED` | Assigned vehicle 3643 is broadcasting off-schedule with no vehicle covering 11703516 |
| `11706658` | Route 39 | `12:46:00` | `SCHEDULED` | Assigned vehicle 3663 is broadcasting off-schedule with no vehicle covering 11706658 |
| `11695291` | Route 2 | `12:30:00` | `SCHEDULED` | Assigned vehicle 3664 is broadcasting off-schedule with no vehicle covering 11695291 |
| `11732020` | Route 162 | `12:37:00` | `SCHEDULED` | Assigned vehicle 3722 is broadcasting off-schedule with no vehicle covering 11732020 |
| `11697763` | Route 7 | `12:45:00` | `SCHEDULED` | Assigned vehicle 3741 is broadcasting off-schedule with no vehicle covering 11697763 |
| `11733133` | Route 178 | `12:46:00` | `SCHEDULED` | Assigned vehicle 3753 is broadcasting off-schedule with no vehicle covering 11733133 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T16:34:19.261202+00:00`.*
