# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:22.765000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `551` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `551` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 551 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4653806` | Route 320 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649333` | Route 1 | `08:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653775` | Route 320 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653802` | Route 320 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659738` | Route 82 | `15:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659747` | Route 82 | `21:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649343` | Route 1 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649355` | Route 1 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649365` | Route 1 | `13:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649376` | Route 1 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649388` | Route 1 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650060` | Route 10C | `21:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661734` | Route 9B | `21:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650046` | Route 10C | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650066` | Route 10C | `24:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:22` | `100.0%` | `0.0%` | 551 | 0 | `+0.0s` |
| `2026-11-13 06:30:18` | `100.0%` | `0.0%` | 551 | 0 | `+0.0s` |
| `2026-11-13 06:00:30` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-13 05:30:18` | `40.0%` | `100.0%` | 5 | 5 | `+26.0s` |
| `2026-11-13 05:00:21` | `7.14%` | `68.18%` | 28 | 22 | `-45.0s` |
| `2026-11-13 04:30:18` | `7.94%` | `77.36%` | 63 | 43 | `-25.7s` |
| `2026-11-13 04:00:20` | `9.62%` | `78.16%` | 104 | 57 | `-14.3s` |
| `2026-11-13 03:30:19` | `13.77%` | `82.61%` | 138 | 70 | `+26.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:22.765000+00:00`.*
