# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-18T06:30:19.172000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `61` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `71` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `4` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 4 | 6.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 5 | 5 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 63** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37803061` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 5619 is broadcasting off-schedule with no vehicle covering 37803061 |
| `37803219` | Route RED | `N/A` | `SCHEDULED` | Assigned vehicle 5701 is broadcasting off-schedule with no vehicle covering 37803219 |
| `37804689` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 1008 is broadcasting off-schedule with no vehicle covering 37804689 |
| `37844311` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 5806 is broadcasting off-schedule with no vehicle covering 37844311 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 06:30:19` | `6.56%` | `0.0%` | 61 | 71 | `+0.0s` |
| `2026-11-18 05:00:20` | `7.62%` | `82.98%` | 105 | 103 | `+103.3s` |
| `2026-11-18 04:00:18` | `14.04%` | `77.89%` | 114 | 110 | `+126.1s` |
| `2026-11-18 03:30:18` | `7.87%` | `85.48%` | 127 | 121 | `+99.1s` |
| `2026-11-18 02:00:19` | `16.22%` | `0.0%` | 148 | 144 | `+0.0s` |
| `2026-11-18 00:30:18` | `11.86%` | `0.0%` | 177 | 171 | `+0.0s` |
| `2026-11-18 00:00:19` | `8.67%` | `0.0%` | 196 | 196 | `+0.0s` |
| `2026-11-17 23:30:19` | `10.09%` | `0.0%` | 218 | 211 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:19.172000+00:00`.*
