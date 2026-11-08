# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:17.736000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`76.32%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `266` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `97` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `203` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 203 | 76.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 5 | 1.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16** | 128 | 0 | 128 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 220** | 74 | 0 | 74 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 5 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 741** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Red** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 110** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Orange** | 7 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78898065` | Route 16 | `14:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78898054` | Route 16 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78897829` | Route 16 | `23:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851525` | Route 220 | `23:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78898145` | Route 16 | `25:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78898022` | Route 16 | `08:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851505` | Route 220 | `13:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78897222` | Route 16 | `10:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78897821` | Route 16 | `18:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78897668` | Route 16 | `19:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78898127` | Route 16 | `13:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851510` | Route 220 | `16:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78897218` | Route 16 | `07:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78898052` | Route 16 | `05:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:17` | `76.32%` | `0.0%` | 266 | 97 | `+0.0s` |
| `2026-11-08 06:30:18` | `60.29%` | `0.0%` | 345 | 143 | `+0.0s` |
| `2026-11-08 06:00:17` | `40.71%` | `0.0%` | 506 | 242 | `+0.0s` |
| `2026-11-08 05:30:18` | `29.55%` | `0.0%` | 670 | 294 | `+0.0s` |
| `2026-11-08 05:00:18` | `24.75%` | `0.0%` | 796 | 308 | `+0.0s` |
| `2026-11-08 04:30:19` | `24.15%` | `0.0%` | 828 | 313 | `+0.0s` |
| `2026-11-08 04:00:18` | `24.7%` | `0.0%` | 834 | 322 | `+0.0s` |
| `2026-11-08 03:30:17` | `24.74%` | `0.0%` | 873 | 348 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.736000+00:00`.*
