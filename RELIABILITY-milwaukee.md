# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-15T07:00:19.247000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `32` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `36` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 6.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 15** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 30** | 7 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 54** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 80** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37808097` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 6320 is missing from active GPS transponder fleet |
| `37808311` | Route RED | `N/A` | `SCHEDULED` | Assigned vehicle 6309 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:19` | `6.25%` | `0.0%` | 32 | 36 | `+0.0s` |
| `2026-11-15 06:30:18` | `5.88%` | `0.0%` | 51 | 55 | `+0.0s` |
| `2026-11-15 03:30:19` | `10.43%` | `0.0%` | 115 | 102 | `+0.0s` |
| `2026-11-15 02:00:18` | `12.0%` | `0.0%` | 125 | 113 | `+0.0s` |
| `2026-11-15 01:30:19` | `9.16%` | `0.0%` | 131 | 116 | `+0.0s` |
| `2026-11-15 00:00:18` | `7.43%` | `0.0%` | 148 | 136 | `+0.0s` |
| `2026-11-14 23:30:19` | `10.53%` | `0.0%` | 152 | 137 | `+0.0s` |
| `2026-11-14 23:00:18` | `7.32%` | `0.0%` | 164 | 144 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.247000+00:00`.*
