# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:19.005000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `285` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `25` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `263` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 263 | 92.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 34E** | 80 | 0 | 80 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 215** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 121** | 10 | 0 | 10 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `78853687` | Route 215 | `07:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181983` | Route 18 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853871` | Route 215 | `13:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853813` | Route 215 | `22:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853764` | Route 215 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78942192` | Route 34E | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78941742` | Route 34E | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78942177` | Route 34E | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853913` | Route 215 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854550` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:19` | `92.28%` | `0.0%` | 285 | 25 | `+0.0s` |
| `2026-11-04 06:30:19` | `70.03%` | `0.0%` | 367 | 97 | `+0.0s` |
| `2026-11-04 06:00:18` | `48.94%` | `0.0%` | 519 | 197 | `+0.0s` |
| `2026-11-04 05:30:17` | `33.24%` | `0.0%` | 746 | 278 | `+0.0s` |
| `2026-11-04 05:00:17` | `27.42%` | `0.0%` | 897 | 302 | `+0.0s` |
| `2026-11-04 04:30:17` | `19.52%` | `0.0%` | 876 | 327 | `+0.0s` |
| `2026-11-04 04:00:20` | `19.66%` | `0.0%` | 895 | 336 | `+0.0s` |
| `2026-11-04 03:30:19` | `24.04%` | `0.0%` | 936 | 372 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:19.005000+00:00`.*
