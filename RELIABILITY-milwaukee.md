# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-27T06:00:18.137000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.73%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `51` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 13.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GRE** | 4 | 4 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 19** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 30** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37800221` | Route GRE | `N/A` | `SCHEDULED` | Assigned vehicle 6011 is broadcasting off-schedule with no vehicle covering 37800221 |
| `37799502` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 5725 is broadcasting off-schedule with no vehicle covering 37799502 |
| `37800535` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 1000 is broadcasting off-schedule with no vehicle covering 37800535 |
| `37842620` | Route 76 | `N/A` | `SCHEDULED` | Assigned vehicle 6307 is broadcasting off-schedule with no vehicle covering 37842620 |
| `37801409` | Route 30 | `N/A` | `SCHEDULED` | Assigned vehicle 5526 is broadcasting off-schedule with no vehicle covering 37801409 |
| `37799098` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 6240 is broadcasting off-schedule with no vehicle covering 37799098 |
| `37800296` | Route GRE | `N/A` | `SCHEDULED` | Assigned vehicle 5610 is broadcasting off-schedule with no vehicle covering 37800296 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 06:00:18` | `13.73%` | `0.0%` | 51 | 58 | `+0.0s` |
| `2026-11-27 05:00:17` | `7.14%` | `0.0%` | 98 | 84 | `+0.0s` |
| `2026-11-27 04:00:17` | `7.92%` | `0.0%` | 101 | 88 | `+0.0s` |
| `2026-11-27 03:00:18` | `11.4%` | `0.0%` | 114 | 99 | `+0.0s` |
| `2026-11-27 02:30:18` | `9.82%` | `0.0%` | 112 | 99 | `+0.0s` |
| `2026-11-27 01:00:17` | `11.54%` | `0.0%` | 130 | 110 | `+0.0s` |
| `2026-11-27 00:30:17` | `14.96%` | `0.0%` | 127 | 117 | `+0.0s` |
| `2026-11-26 23:00:17` | `9.62%` | `0.0%` | 156 | 132 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T06:00:18.137000+00:00`.*
