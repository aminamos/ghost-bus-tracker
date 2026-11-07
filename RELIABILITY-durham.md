# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Durham Region Transit** in **Durham, ON** (Regional Municipality of Durham, Ontario).
> **Transit System:** DRT | **Location:** Durham, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:19.014000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`53.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `15` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `7` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `8` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 8 | 53.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route N2** | 7 | 2 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route N1** | 8 | 5 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |

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
| `400__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6137 is broadcasting off-schedule with no vehicle covering 400__491003_Timetable_-_2026-10 |
| `406__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8580 is broadcasting off-schedule with no vehicle covering 406__491001_Timetable_-_2026-10 |
| `384__491004_Timetable_-_2026-10` | Route N1 | `N/A` | `SCHEDULED` | Assigned vehicle 8623 is broadcasting off-schedule with no vehicle covering 384__491004_Timetable_-_2026-10 |
| `420__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6137 is broadcasting off-schedule with no vehicle covering 420__491003_Timetable_-_2026-10 |
| `417__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8580 is broadcasting off-schedule with no vehicle covering 417__491001_Timetable_-_2026-10 |
| `402__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6137 is broadcasting off-schedule with no vehicle covering 402__491003_Timetable_-_2026-10 |
| `5159__491001_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 8580 is broadcasting off-schedule with no vehicle covering 5159__491001_Timetable_-_2026-10 |
| `5160__491003_Timetable_-_2026-10` | Route N2 | `N/A` | `SCHEDULED` | Assigned vehicle 6137 is broadcasting off-schedule with no vehicle covering 5160__491003_Timetable_-_2026-10 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:19` | `53.33%` | `0.0%` | 15 | 7 | `+0.0s` |
| `2026-11-07 06:30:19` | `50.0%` | `0.0%` | 14 | 7 | `+0.0s` |
| `2026-11-07 06:00:20` | `13.04%` | `0.0%` | 23 | 16 | `+0.0s` |
| `2026-11-07 05:30:18` | `12.5%` | `0.0%` | 40 | 31 | `+0.0s` |
| `2026-11-07 05:00:18` | `7.27%` | `0.0%` | 55 | 38 | `+0.0s` |
| `2026-11-07 04:30:18` | `7.59%` | `0.0%` | 79 | 43 | `-97.0s` |
| `2026-11-07 04:00:22` | `8.25%` | `68.42%` | 97 | 48 | `+65.6s` |
| `2026-11-07 03:30:20` | `13.89%` | `81.25%` | 108 | 56 | `+132.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:19.014000+00:00`.*
