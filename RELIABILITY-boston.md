# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:17.751000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `599` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `42` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `572` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 572 | 95.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 15 | 2.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 109** | 82 | 0 | 82 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 220** | 74 | 0 | 74 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 59 | 0 | 59 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 47** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 94** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 95** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `78851624` | Route 220 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068323` | Route 110 | `17:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78481406` | Route 64 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068574` | Route 96 | `14:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068023` | Route 109 | `14:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78067386` | Route 94 | `12:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068270` | Route 110 | `06:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068080` | Route 109 | `19:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068188` | Route 109 | `10:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78067951` | Route 106 | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068556` | Route 96 | `10:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068045` | Route 109 | `14:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78481378` | Route 64 | `21:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78068224` | Route 110 | `13:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78481377` | Route 64 | `06:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:17` | `95.49%` | `0.0%` | 599 | 42 | `+0.0s` |
| `2026-11-01 06:30:17` | `96.97%` | `0.0%` | 594 | 42 | `+0.0s` |
| `2026-11-01 06:00:18` | `91.73%` | `0.0%` | 617 | 83 | `+0.0s` |
| `2026-11-01 05:30:18` | `75.3%` | `0.0%` | 575 | 138 | `+0.0s` |
| `2026-11-01 05:00:18` | `55.59%` | `0.0%` | 752 | 243 | `+0.0s` |
| `2026-11-01 04:30:18` | `44.1%` | `0.0%` | 923 | 282 | `+0.0s` |
| `2026-11-01 04:00:17` | `39.13%` | `0.0%` | 1012 | 296 | `+0.0s` |
| `2026-11-01 03:30:17` | `25.12%` | `0.0%` | 860 | 307 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:17.751000+00:00`.*
