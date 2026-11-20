# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T06:30:18.941000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `58` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `69` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `9` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 9 | 15.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 66** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 5 | 5 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 30** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 63** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37806715` | Route BLU | `N/A` | `SCHEDULED` | Assigned vehicle 6216 is broadcasting off-schedule with no vehicle covering 37806715 |
| `37841969` | Route 15 | `N/A` | `SCHEDULED` | Assigned vehicle 6326 is broadcasting off-schedule with no vehicle covering 37841969 |
| `37805045` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 5627 is broadcasting off-schedule with no vehicle covering 37805045 |
| `37803061` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 6257 is broadcasting off-schedule with no vehicle covering 37803061 |
| `37803219` | Route RED | `N/A` | `SCHEDULED` | Assigned vehicle 6312 is broadcasting off-schedule with no vehicle covering 37803219 |
| `37804689` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 1008 is broadcasting off-schedule with no vehicle covering 37804689 |
| `37803475` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 6228 is broadcasting off-schedule with no vehicle covering 37803475 |
| `37805292` | Route 30 | `N/A` | `SCHEDULED` | Assigned vehicle 5900 is broadcasting off-schedule with no vehicle covering 37805292 |
| `37844311` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 5532 is broadcasting off-schedule with no vehicle covering 37844311 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 06:30:18` | `15.52%` | `0.0%` | 58 | 69 | `+0.0s` |
| `2026-11-20 05:30:18` | `9.57%` | `0.0%` | 94 | 98 | `+0.0s` |
| `2026-11-20 04:30:18` | `11.93%` | `0.0%` | 109 | 108 | `+0.0s` |
| `2026-11-20 04:00:18` | `9.65%` | `0.0%` | 114 | 111 | `+0.0s` |
| `2026-11-20 03:00:19` | `13.85%` | `0.0%` | 130 | 128 | `+0.0s` |
| `2026-11-20 02:30:18` | `8.45%` | `0.0%` | 142 | 135 | `+0.0s` |
| `2026-11-20 01:30:18` | `8.97%` | `0.0%` | 156 | 151 | `+0.0s` |
| `2026-11-20 01:00:18` | `11.38%` | `0.0%` | 167 | 156 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:18.941000+00:00`.*
