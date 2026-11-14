# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-14T05:30:18.915000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `97` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `102` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 9 | 9.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 21** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 53** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 6 | 5 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 80** | 6 | 5 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 35** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 92** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 6 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37803541` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 6110 is broadcasting off-schedule with no vehicle covering 37803541 |
| `37803829` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 5610 is broadcasting off-schedule with no vehicle covering 37803829 |
| `37806330` | Route 80 | `N/A` | `SCHEDULED` | Assigned vehicle 6010 is broadcasting off-schedule with no vehicle covering 37806330 |
| `37843598` | Route 21 | `N/A` | `SCHEDULED` | Assigned vehicle 6401 is broadcasting off-schedule with no vehicle covering 37843598 |
| `37802528` | Route 60 | `N/A` | `SCHEDULED` | Assigned vehicle 5808 is broadcasting off-schedule with no vehicle covering 37802528 |
| `37803473` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 6411 is broadcasting off-schedule with no vehicle covering 37803473 |
| `37803075` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 5627 is broadcasting off-schedule with no vehicle covering 37803075 |
| `37804691` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 6254 is broadcasting off-schedule with no vehicle covering 37804691 |
| `37843610` | Route 21 | `N/A` | `SCHEDULED` | Assigned vehicle 6108 is broadcasting off-schedule with no vehicle covering 37843610 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 05:30:18` | `9.28%` | `0.0%` | 97 | 102 | `+0.0s` |
| `2026-11-14 04:30:18` | `12.15%` | `0.0%` | 107 | 108 | `+0.0s` |
| `2026-11-14 03:30:18` | `8.87%` | `0.0%` | 124 | 120 | `+0.0s` |
| `2026-11-14 01:00:18` | `9.58%` | `60.61%` | 167 | 159 | `+211.1s` |
| `2026-11-14 00:30:21` | `11.86%` | `70.78%` | 177 | 172 | `+139.1s` |
| `2026-11-14 00:00:18` | `8.67%` | `0.0%` | 196 | 195 | `+0.0s` |
| `2026-11-13 23:30:18` | `6.51%` | `0.0%` | 215 | 212 | `+0.0s` |
| `2026-11-13 23:00:19` | `9.48%` | `0.0%` | 232 | 214 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T05:30:18.915000+00:00`.*
