# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Durham Region Transit** in **Durham, ON** (Regional Municipality of Durham, Ontario).
> **Transit System:** DRT | **Location:** Durham, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.439000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`43.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `16` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `9` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 43.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route N2** | 7 | 2 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route N1** | 9 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `400__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6147 is broadcasting off-schedule with no vehicle covering 400__491003_Timetable_-_2026-10 |
| `406__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8602 is broadcasting off-schedule with no vehicle covering 406__491001_Timetable_-_2026-10 |
| `402__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6147 is broadcasting off-schedule with no vehicle covering 402__491003_Timetable_-_2026-10 |
| `417__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8602 is broadcasting off-schedule with no vehicle covering 417__491001_Timetable_-_2026-10 |
| `420__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6147 is broadcasting off-schedule with no vehicle covering 420__491003_Timetable_-_2026-10 |
| `5159__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8602 is broadcasting off-schedule with no vehicle covering 5159__491001_Timetable_-_2026-10 |
| `5160__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6147 is broadcasting off-schedule with no vehicle covering 5160__491003_Timetable_-_2026-10 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `43.75%` | `0.0%` | 16 | 9 | `+0.0s` |
| `2026-11-09 06:30:21` | `20.0%` | `0.0%` | 15 | 9 | `+0.0s` |
| `2026-11-09 06:00:18` | `14.29%` | `0.0%` | 21 | 16 | `+0.0s` |
| `2026-11-09 05:30:18` | `10.53%` | `100.0%` | 38 | 28 | `+18.0s` |
| `2026-11-09 05:00:18` | `11.54%` | `83.33%` | 52 | 35 | `+157.4s` |
| `2026-11-09 04:30:19` | `8.33%` | `80.65%` | 72 | 37 | `+106.5s` |
| `2026-11-09 04:00:19` | `8.43%` | `84.91%` | 83 | 41 | `+121.3s` |
| `2026-11-09 03:30:18` | `8.6%` | `89.41%` | 93 | 47 | `+71.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.439000+00:00`.*
