# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Durham Region Transit** in **Durham, ON** (Regional Municipality of Durham, Ontario).
> **Transit System:** DRT | **Location:** Durham, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:22.306000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`42.86%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `14` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `7` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 42.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route N2** | 6 | 2 | 6 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route N1** | 8 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `406__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6103 is broadcasting off-schedule with no vehicle covering 406__491001_Timetable_-_2026-10 |
| `5160__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8624 is broadcasting off-schedule with no vehicle covering 5160__491003_Timetable_-_2026-10 |
| `420__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8624 is broadcasting off-schedule with no vehicle covering 420__491003_Timetable_-_2026-10 |
| `402__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8624 is broadcasting off-schedule with no vehicle covering 402__491003_Timetable_-_2026-10 |
| `411__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6103 is broadcasting off-schedule with no vehicle covering 411__491001_Timetable_-_2026-10 |
| `564__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6103 is broadcasting off-schedule with no vehicle covering 564__491001_Timetable_-_2026-10 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `42.86%` | `0.0%` | 14 | 7 | `+0.0s` |
| `2026-10-24 05:30:20` | `46.67%` | `0.0%` | 15 | 9 | `+0.0s` |
| `2026-10-24 05:00:24` | `13.04%` | `0.0%` | 23 | 15 | `+0.0s` |
| `2026-10-24 04:30:21` | `10.0%` | `0.0%` | 40 | 31 | `+0.0s` |
| `2026-10-24 04:00:22` | `12.73%` | `0.0%` | 55 | 37 | `+0.0s` |
| `2026-10-24 03:30:34` | `7.69%` | `0.0%` | 78 | 42 | `+0.0s` |
| `2026-10-24 03:00:20` | `2.33%` | `0.0%` | 86 | 48 | `+0.0s` |
| `2026-10-24 02:30:33` | `10.48%` | `0.0%` | 105 | 58 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.306000+00:00`.*
