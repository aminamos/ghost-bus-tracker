# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Durham Region Transit** in **Durham, ON** (Regional Municipality of Durham, Ontario).
> **Transit System:** DRT | **Location:** Durham, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:19.091000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `14` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `14` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 14 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route N1** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route N2** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `390__291001_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 6125 is missing from active GPS transponder fleet |
| `394__491004_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 8610 is missing from active GPS transponder fleet |
| `565__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8601 is missing from active GPS transponder fleet |
| `381__491002_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 6149 is missing from active GPS transponder fleet |
| `395__291002_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 8523 is missing from active GPS transponder fleet |
| `408__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8601 is missing from active GPS transponder fleet |
| `387__491005_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 6139 is missing from active GPS transponder fleet |
| `377__491005_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 6139 is missing from active GPS transponder fleet |
| `378__291002_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 8523 is missing from active GPS transponder fleet |
| `380__491002_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 6149 is missing from active GPS transponder fleet |
| `564__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `406__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `402__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8601 is missing from active GPS transponder fleet |
| `393__491004_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 8610 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:19` | `100.0%` | `0.0%` | 14 | 0 | `+0.0s` |
| `2026-10-29 06:30:23` | `28.57%` | `0.0%` | 14 | 8 | `+0.0s` |
| `2026-10-29 06:00:23` | `0.0%` | `0.0%` | 16 | 8 | `+0.0s` |
| `2026-10-29 05:30:18` | `46.67%` | `0.0%` | 15 | 9 | `+0.0s` |
| `2026-10-29 05:00:20` | `13.64%` | `0.0%` | 22 | 16 | `+0.0s` |
| `2026-10-29 04:30:20` | `12.82%` | `0.0%` | 39 | 31 | `+0.0s` |
| `2026-10-29 04:00:20` | `13.21%` | `0.0%` | 53 | 36 | `+0.0s` |
| `2026-10-29 03:30:18` | `3.9%` | `0.0%` | 77 | 43 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:19.091000+00:00`.*
