# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:18.761000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`88.39%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`40.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `267` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `30` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `236` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-90.0s` (`-1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-109.0s` (`-1.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 1.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 236 | 88.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 45 | 0 | 45 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 57 | 1 | 56 | **`98.25%`** | `100.0%` | `+2.5 min` |
| **Route 1** | 61 | 5 | 55 | **`90.16%`** | `25.0%` | `-150.5s` |
| **Route 48** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+2.5 min (+152.0s)` | `+2.5 min (+152s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | ~20.0m | ~20.0m | **`+0.0 min`** | `88.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30734883` | Route 1 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737297` | Route 1 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737301` | Route 1 | `07:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737306` | Route 1 | `09:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737312` | Route 1 | `11:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737320` | Route 1 | `14:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737328` | Route 1 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737336` | Route 1 | `19:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737343` | Route 1 | `22:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737349` | Route 1 | `24:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737299` | Route 1 | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737303` | Route 1 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737308` | Route 1 | `10:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737316` | Route 1 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30737324` | Route 1 | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `88.39%` | `40.0%` | 267 | 30 | `-90.0s` |
| `2026-11-22 06:30:18` | `83.28%` | `33.33%` | 287 | 48 | `-37.0s` |
| `2026-11-22 06:00:17` | `79.8%` | `33.33%` | 302 | 61 | `-77.8s` |
| `2026-11-22 05:30:33` | `11.54%` | `42.86%` | 78 | 68 | `-69.3s` |
| `2026-11-22 05:00:18` | `11.76%` | `75.0%` | 102 | 88 | `-28.5s` |
| `2026-11-22 04:30:18` | `13.91%` | `62.5%` | 115 | 98 | `-2.2s` |
| `2026-11-22 04:00:18` | `13.97%` | `40.0%` | 136 | 116 | `+40.0s` |
| `2026-11-22 03:30:20` | `13.73%` | `58.33%` | 153 | 129 | `-30.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.761000+00:00`.*
