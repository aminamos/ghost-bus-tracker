# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-07T07:00:18.936000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.09%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `33` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `41` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 9.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 3.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 66** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 30** | 7 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37803457` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 5514 is broadcasting off-schedule with no vehicle covering 37803457 |
| `37804690` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 6528 is broadcasting off-schedule with no vehicle covering 37804690 |
| `37843613` | Route 21 | `N/A` | `SCHEDULED` | Assigned vehicle 6214 is broadcasting off-schedule with no vehicle covering 37843613 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:18` | `9.09%` | `0.0%` | 33 | 41 | `+0.0s` |
| `2026-11-07 05:30:19` | `10.64%` | `0.0%` | 94 | 98 | `+0.0s` |
| `2026-11-07 05:00:19` | `10.0%` | `0.0%` | 100 | 99 | `+0.0s` |
| `2026-11-07 04:30:19` | `12.87%` | `0.0%` | 101 | 104 | `+0.0s` |
| `2026-11-07 00:30:18` | `10.33%` | `0.0%` | 184 | 170 | `+0.0s` |
| `2026-11-07 00:00:19` | `9.6%` | `0.0%` | 198 | 195 | `+0.0s` |
| `2026-11-06 22:00:19` | `6.72%` | `0.0%` | 238 | 221 | `+0.0s` |
| `2026-11-06 21:30:18` | `9.54%` | `0.0%` | 241 | 210 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.936000+00:00`.*
