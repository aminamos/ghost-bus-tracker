# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:22.442000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`83.87%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `186` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `30` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `156` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 156 | 83.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 43 | 0 | 43 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 56 | 1 | 55 | **`98.21%`** | `0.0%` | `+0.0s` |
| **Route 17** | 60 | 2 | 58 | **`96.67%`** | `0.0%` | `+0.0s` |
| **Route 42** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `30505821` | Route 7 | `24:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505815` | Route 7 | `22:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505809` | Route 7 | `20:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505803` | Route 7 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505797` | Route 7 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505791` | Route 7 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505785` | Route 7 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505779` | Route 7 | `07:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505773` | Route 7 | `05:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505818` | Route 7 | `23:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505812` | Route 7 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505806` | Route 7 | `19:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505800` | Route 7 | `16:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505794` | Route 7 | `14:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30505788` | Route 7 | `11:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `83.87%` | `0.0%` | 186 | 30 | `+0.0s` |
| `2026-10-24 05:30:21` | `66.24%` | `60.0%` | 237 | 80 | `+295.2s` |
| `2026-10-24 05:00:24` | `63.75%` | `50.0%` | 251 | 91 | `+76.8s` |
| `2026-10-24 04:30:21` | `5.61%` | `80.0%` | 107 | 100 | `-28.6s` |
| `2026-10-24 04:00:22` | `6.4%` | `50.0%` | 125 | 115 | `-43.3s` |
| `2026-10-24 03:30:34` | `8.51%` | `25.0%` | 141 | 129 | `+121.8s` |
| `2026-10-24 03:00:20` | `9.09%` | `25.0%` | 154 | 140 | `+29.0s` |
| `2026-10-24 02:30:33` | `10.18%` | `25.0%` | 167 | 150 | `-3.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.442000+00:00`.*
