# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.780000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.8%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `250` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `8` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `242` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+1.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+1.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 242 | 96.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 56 | 0 | 56 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 56 | 2 | 54 | **`96.43%`** | `50.0%` | `+0.0 min` |
| **Route 26** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+0.0 min (+1.0s)` | `+1.8 min (+108s)` | 2 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | ~20.0m | ~20.0m | **`+0.0 min`** | `91.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30742016` | Route 7 | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742058` | Route 7 | `22:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742052` | Route 7 | `20:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742046` | Route 7 | `18:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742038` | Route 7 | `14:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742032` | Route 7 | `12:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742018` | Route 7 | `07:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742012` | Route 7 | `05:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742056` | Route 7 | `21:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742050` | Route 7 | `19:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742044` | Route 7 | `17:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742060` | Route 7 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742054` | Route 7 | `21:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742048` | Route 7 | `18:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30742042` | Route 7 | `16:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `96.8%` | `50.0%` | 250 | 8 | `+1.0s` |
| `2026-11-01 06:30:20` | `93.08%` | `50.0%` | 260 | 17 | `+1804.8s` |
| `2026-11-01 06:00:21` | `89.01%` | `20.0%` | 273 | 29 | `+2807.6s` |
| `2026-11-01 05:30:19` | `83.96%` | `0.0%` | 293 | 47 | `+3587.0s` |
| `2026-11-01 05:00:20` | `79.74%` | `0.0%` | 311 | 63 | `+3681.7s` |
| `2026-11-01 04:30:19` | `10.98%` | `50.0%` | 82 | 72 | `-11.2s` |
| `2026-11-01 04:00:18` | `12.12%` | `88.89%` | 99 | 85 | `+30.3s` |
| `2026-11-01 03:30:18` | `14.66%` | `75.0%` | 116 | 99 | `+116.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.780000+00:00`.*
