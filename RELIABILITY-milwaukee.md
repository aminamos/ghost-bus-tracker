# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-16T06:00:19.681000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `5` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 5 | 11.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 30** | 3 | 4 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 19** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route RED** | 6 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 80** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `37799502` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 5808 is broadcasting off-schedule with no vehicle covering 37799502 |
| `37800535` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 6258 is broadcasting off-schedule with no vehicle covering 37800535 |
| `37801409` | Route 30 | `N/A` | `SCHEDULED` | Assigned vehicle 5805 is broadcasting off-schedule with no vehicle covering 37801409 |
| `37799098` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 6529 is broadcasting off-schedule with no vehicle covering 37799098 |
| `37800714` | Route 63 | `N/A` | `SCHEDULED` | Assigned vehicle 6408 is broadcasting off-schedule with no vehicle covering 37800714 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 06:00:19` | `11.36%` | `0.0%` | 44 | 57 | `+0.0s` |
| `2026-11-16 03:30:20` | `17.17%` | `80.25%` | 99 | 98 | `+105.2s` |
| `2026-11-16 02:30:18` | `7.41%` | `0.0%` | 108 | 99 | `+0.0s` |
| `2026-11-16 01:00:18` | `7.87%` | `0.0%` | 127 | 113 | `+0.0s` |
| `2026-11-15 23:30:19` | `8.78%` | `0.0%` | 148 | 129 | `+0.0s` |
| `2026-11-15 23:00:19` | `11.76%` | `0.0%` | 153 | 128 | `+0.0s` |
| `2026-11-15 22:30:19` | `7.64%` | `0.0%` | 157 | 127 | `+0.0s` |
| `2026-11-15 22:00:19` | `5.42%` | `0.0%` | 166 | 131 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T06:00:19.681000+00:00`.*
