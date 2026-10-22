# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T18:00:38.208000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.81%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1627` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `660` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `420` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 420 | 25.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 0.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 554** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 211** | 3 | 1 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 746** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route Boat-F6** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 220** | 77 | 3 | 73 | **`94.81%`** | `0.0%` | `+0.0s` |
| **Route 238** | 28 | 2 | 25 | **`89.29%`** | `0.0%` | `+0.0s` |
| **Route 455** | 38 | 6 | 32 | **`84.21%`** | `0.0%` | `+0.0s` |
| **Route 116** | 137 | 14 | 115 | **`83.94%`** | `0.0%` | `+0.0s` |
| **Route 714** | 5 | 1 | 4 | **`80.0%`** | `0.0%` | `+0.0s` |
| **Route 236** | 14 | 2 | 11 | **`78.57%`** | `0.0%` | `+0.0s` |

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
| `78852185` | Route 236 | `13:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78600893` | Route 116 | `08:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854268` | Route 211 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260879` | Route 96 | `14:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853965` | Route 238 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78942124_1` | Route 39 | `14:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78942251` | Route 32 | `14:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181416` | Route 23 | `14:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78985471` | Route 712 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259704` | Route 137 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259563` | Route 101 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78600236` | Route 116 | `04:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:00:38` | `25.81%` | `0.0%` | 1627 | 660 | `+0.0s` |
| `2026-10-22 17:30:36` | `29.85%` | `0.0%` | 1551 | 615 | `+0.0s` |
| `2026-10-22 17:00:37` | `30.41%` | `0.0%` | 1473 | 577 | `+0.0s` |
| `2026-10-22 16:31:17` | `28.18%` | `0.0%` | 1430 | 568 | `+0.0s` |
| `2026-10-22 16:01:15` | `27.03%` | `0.0%` | 1439 | 558 | `+0.0s` |
| `2026-10-22 15:30:37` | `19.11%` | `0.0%` | 1277 | 542 | `+0.0s` |
| `2026-10-22 15:01:07` | `19.44%` | `0.0%` | 1317 | 544 | `+0.0s` |
| `2026-10-22 14:30:48` | `21.32%` | `0.0%` | 1360 | 558 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:00:38.208000+00:00`.*
