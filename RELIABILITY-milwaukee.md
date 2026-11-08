# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.255000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.08%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `26` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `35` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 23.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route CN1** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 30** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 54** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `37808097` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 6244 is missing from active GPS transponder fleet |
| `37808473` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 5814 is broadcasting off-schedule with no vehicle covering 37808473 |
| `37809989` | Route BLU | `N/A` | `SCHEDULED` | Assigned vehicle 5716 is broadcasting off-schedule with no vehicle covering 37809989 |
| `37809750` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 1000 is broadcasting off-schedule with no vehicle covering 37809750 |
| `37810342` | Route 30 | `N/A` | `SCHEDULED` | Assigned vehicle 5701 is broadcasting off-schedule with no vehicle covering 37810342 |
| `37809732` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 6021 is broadcasting off-schedule with no vehicle covering 37809732 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `23.08%` | `0.0%` | 26 | 35 | `+0.0s` |
| `2026-11-08 06:00:18` | `8.22%` | `0.0%` | 73 | 71 | `+0.0s` |
| `2026-11-08 05:00:18` | `9.57%` | `0.0%` | 94 | 91 | `+0.0s` |
| `2026-11-08 04:00:19` | `9.0%` | `0.0%` | 100 | 96 | `+0.0s` |
| `2026-11-08 03:30:18` | `8.33%` | `0.0%` | 108 | 99 | `+0.0s` |
| `2026-11-08 03:00:18` | `12.07%` | `0.0%` | 116 | 108 | `+0.0s` |
| `2026-11-08 01:00:18` | `12.69%` | `0.0%` | 134 | 125 | `+0.0s` |
| `2026-11-08 00:30:18` | `8.57%` | `0.0%` | 140 | 131 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.255000+00:00`.*
