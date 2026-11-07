# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:18.936000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `388` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `388` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 388 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 25 | 0 | 25 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4660488` | Route 87 | `13:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649034` | Route 1 | `12:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649027` | Route 1 | `10:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649048` | Route 1 | `16:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649041` | Route 1 | `14:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649062` | Route 1 | `19:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649055` | Route 1 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649081` | Route 1 | `24:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649021` | Route 1 | `09:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649015` | Route 1 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649069` | Route 1 | `21:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649018` | Route 1 | `08:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649012` | Route 1 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649009` | Route 1 | `06:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649044` | Route 1 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:18` | `100.0%` | `0.0%` | 388 | 0 | `+0.0s` |
| `2026-11-07 06:30:19` | `100.0%` | `0.0%` | 388 | 0 | `+0.0s` |
| `2026-11-07 06:00:20` | `0.0%` | `0.0%` | 3 | 2 | `+815.7s` |
| `2026-11-07 05:30:18` | `16.67%` | `100.0%` | 6 | 5 | `+122.8s` |
| `2026-11-07 05:00:18` | `10.0%` | `58.33%` | 30 | 22 | `-52.2s` |
| `2026-11-07 04:30:18` | `7.94%` | `83.93%` | 63 | 42 | `+17.1s` |
| `2026-11-07 04:00:22` | `11.32%` | `79.35%` | 106 | 58 | `+54.4s` |
| `2026-11-07 03:30:20` | `12.14%` | `78.69%` | 140 | 71 | `+448.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.936000+00:00`.*
