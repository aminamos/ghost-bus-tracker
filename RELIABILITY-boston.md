# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-10T07:00:17.871000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`82.97%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `182` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `151` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 151 | 83.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 3.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 93** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 92** | 23 | 0 | 23 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 8 | 0 | 8 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 121** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 39** | 7 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259020` | Route 92 | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78265958` | Route 93 | `12:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259533` | Route 93 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854550` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78265499` | Route 92 | `06:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78265462` | Route 92 | `12:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854570` | Route 220 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854590` | Route 220 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78515465` | Route 121 | `08:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854464` | Route 220 | `15:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:17` | `82.97%` | `0.0%` | 182 | 58 | `+0.0s` |
| `2026-11-10 06:30:17` | `59.68%` | `0.0%` | 253 | 124 | `+0.0s` |
| `2026-11-10 06:00:17` | `38.1%` | `0.0%` | 399 | 211 | `+0.0s` |
| `2026-11-10 05:30:18` | `23.2%` | `0.0%` | 612 | 289 | `+0.0s` |
| `2026-11-10 05:00:17` | `19.12%` | `0.0%` | 753 | 300 | `+0.0s` |
| `2026-11-10 04:30:18` | `17.73%` | `0.0%` | 812 | 319 | `+0.0s` |
| `2026-11-10 04:00:18` | `17.3%` | `0.0%` | 844 | 342 | `+0.0s` |
| `2026-11-10 03:30:18` | `20.9%` | `0.0%` | 866 | 369 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:17.871000+00:00`.*
