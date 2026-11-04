# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-04T06:00:18.626000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `84` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `85` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 8.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 60** | 2 | 5 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 54** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 63** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 92** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37803591` | Route 35 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `37803606` | Route 35 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `37803418` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 6201 is broadcasting off-schedule with no vehicle covering 37803418 |
| `37802447` | Route 60 | `N/A` | `SCHEDULED` | Assigned vehicle 6404 is broadcasting off-schedule with no vehicle covering 37802447 |
| `37806705` | Route BLU | `N/A` | `SCHEDULED` | Assigned vehicle 5902 is broadcasting off-schedule with no vehicle covering 37806705 |
| `37804688` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 6251 is broadcasting off-schedule with no vehicle covering 37804688 |
| `37844029` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 6104 is broadcasting off-schedule with no vehicle covering 37844029 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 06:00:18` | `8.33%` | `0.0%` | 84 | 85 | `+0.0s` |
| `2026-11-04 05:30:18` | `8.25%` | `0.0%` | 97 | 98 | `+0.0s` |
| `2026-11-04 05:00:17` | `6.48%` | `0.0%` | 108 | 102 | `+0.0s` |
| `2026-11-04 04:30:18` | `9.91%` | `0.0%` | 111 | 104 | `+0.0s` |
| `2026-11-04 02:30:19` | `6.08%` | `0.0%` | 148 | 135 | `+0.0s` |
| `2026-11-04 01:30:18` | `10.39%` | `0.0%` | 154 | 151 | `+0.0s` |
| `2026-11-04 01:00:18` | `9.88%` | `0.0%` | 162 | 156 | `+0.0s` |
| `2026-11-04 00:30:19` | `9.89%` | `0.0%` | 182 | 172 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T06:00:18.626000+00:00`.*
