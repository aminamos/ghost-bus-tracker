# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:17.743000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `345` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `33` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `322` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 322 | 93.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 455** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 436** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 435** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 121** | 10 | 0 | 10 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 124 | 2 | 122 | **`98.39%`** | `0.0%` | `+0.0s` |
| **Route 28** | 6 | 3 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78516989` | Route 455 | `17:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516856` | Route 455 | `06:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516829` | Route 455 | `12:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517176` | Route 116 | `13:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517378` | Route 435 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516460` | Route 116 | `21:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517106` | Route 455 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517232` | Route 116 | `13:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517207` | Route 116 | `15:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517324` | Route 435 | `11:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:17` | `93.33%` | `0.0%` | 345 | 33 | `+0.0s` |
| `2026-11-05 06:30:17` | `75.47%` | `0.0%` | 424 | 105 | `+0.0s` |
| `2026-11-05 06:00:17` | `54.5%` | `0.0%` | 567 | 203 | `+0.0s` |
| `2026-11-05 05:30:18` | `38.61%` | `0.0%` | 790 | 279 | `+0.0s` |
| `2026-11-05 05:00:17` | `32.31%` | `0.0%` | 944 | 304 | `+0.0s` |
| `2026-11-05 04:30:18` | `29.46%` | `0.0%` | 1008 | 333 | `+0.0s` |
| `2026-11-05 04:00:18` | `30.01%` | `0.0%` | 1033 | 345 | `+0.0s` |
| `2026-11-05 03:30:18` | `31.27%` | `0.0%` | 1068 | 381 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.743000+00:00`.*
