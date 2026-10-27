# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-27T05:00:22.890000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.06%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `85` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `86` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 7.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 60** | 2 | 5 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 6 | 5 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 54** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 63** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 92** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37806414` | Route 11 | `N/A` | `SCHEDULED` | Assigned vehicle 6303 is broadcasting off-schedule with no vehicle covering 37806414 |
| `37803543` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 5708 is broadcasting off-schedule with no vehicle covering 37803543 |
| `37802447` | Route 60 | `N/A` | `SCHEDULED` | Assigned vehicle 6404 is broadcasting off-schedule with no vehicle covering 37802447 |
| `37806705` | Route BLU | `N/A` | `SCHEDULED` | Assigned vehicle 5700 is broadcasting off-schedule with no vehicle covering 37806705 |
| `37804688` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 6249 is broadcasting off-schedule with no vehicle covering 37804688 |
| `37844029` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 6304 is broadcasting off-schedule with no vehicle covering 37844029 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 05:00:22` | `7.06%` | `0.0%` | 85 | 86 | `+0.0s` |
| `2026-10-27 04:30:20` | `7.14%` | `0.0%` | 98 | 98 | `+0.0s` |
| `2026-10-27 04:00:57` | `11.0%` | `0.0%` | 100 | 101 | `+0.0s` |
| `2026-10-27 03:30:23` | `14.42%` | `0.0%` | 104 | 105 | `+0.0s` |
| `2026-10-27 02:30:20` | `7.56%` | `0.0%` | 119 | 118 | `+0.0s` |
| `2026-10-27 01:30:24` | `9.49%` | `69.23%` | 137 | 134 | `+187.2s` |
| `2026-10-27 00:30:59` | `11.33%` | `80.45%` | 150 | 147 | `+96.2s` |
| `2026-10-26 23:00:23` | `12.23%` | `0.0%` | 188 | 190 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T05:00:22.890000+00:00`.*
