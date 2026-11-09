# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Knoxville Area Transit** in **Knoxville, TN** (Knoxville Metropolitan Area, Tennessee).
> **Transit System:** KAT | **Location:** Knoxville, TN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.930000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `39` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `5` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `39` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 39 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `17052` | Route UNKNOWN | `08:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `17053` | Route UNKNOWN | `09:15:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `17056` | Route UNKNOWN | `10:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `17057` | Route UNKNOWN | `11:15:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `17060` | Route UNKNOWN | `12:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `17061` | Route UNKNOWN | `13:15:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23027` | Route UNKNOWN | `07:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23028` | Route UNKNOWN | `08:25:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23031` | Route UNKNOWN | `09:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23032` | Route UNKNOWN | `10:25:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23035` | Route UNKNOWN | `11:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23036` | Route UNKNOWN | `12:25:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `23039` | Route UNKNOWN | `13:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `31001` | Route UNKNOWN | `06:12:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |
| `31015` | Route UNKNOWN | `07:45:00` | `SCHEDULED` | Assigned vehicle 7536 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `100.0%` | `0.0%` | 39 | 5 | `+0.0s` |
| `2026-11-09 06:30:22` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |
| `2026-11-09 06:00:19` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |
| `2026-11-09 05:30:18` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |
| `2026-11-09 05:00:18` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |
| `2026-11-09 04:30:19` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |
| `2026-11-09 04:00:19` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |
| `2026-11-09 03:30:22` | `0.0%` | `0.0%` | 0 | 5 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.930000+00:00`.*
