# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T13:46:35.858121+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.57%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1430` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `630` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `237` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 237 | 16.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 33 | 2.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route Boat-F7** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 442** | 36 | 2 | 33 | **`91.67%`** | `0.0%` | `+0.0s` |
| **Route 220** | 59 | 4 | 53 | **`89.83%`** | `0.0%` | `+0.0s` |
| **Route 93** | 58 | 3 | 51 | **`87.93%`** | `0.0%` | `+0.0s` |
| **Route 441** | 23 | 2 | 19 | **`82.61%`** | `0.0%` | `+0.0s` |
| **Route 120** | 28 | 3 | 22 | **`78.57%`** | `0.0%` | `+0.0s` |
| **Route 222** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 713** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route CR-Fairmount** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 712** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `78259528` | Route 93 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516522` | Route 442 | `21:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516574` | Route 442 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516527` | Route 441 | `15:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516699` | Route 441 | `17:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `FBWMLConstruction-860181-1625` | Route CR-Fairmount | `09:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516571` | Route 442 | `22:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853998` | Route 240 | `10:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78477261` | Route 87 | `10:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516678` | Route 442 | `24:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853922` | Route 238 | `10:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 13:46:35` | `16.57%` | `0.0%` | 1430 | 630 | `+0.0s` |
| `2026-10-06 06:42:11` | `99.21%` | `0.0%` | 633 | 7 | `+0.0s` |
| `2026-10-06 00:28:46` | `36.12%` | `0.0%` | 1304 | 459 | `+0.0s` |
| `2026-10-05 18:39:11` | `19.98%` | `0.0%` | 1712 | 749 | `+0.0s` |
| `2026-10-05 18:02:18` | `25.7%` | `0.0%` | 1607 | 667 | `+0.0s` |
| `2026-10-05 17:57:48` | `26.29%` | `0.0%` | 1575 | 657 | `+0.0s` |
| `2026-10-05 17:20:38` | `29.48%` | `0.0%` | 1452 | 603 | `+0.0s` |
| `2026-10-05 16:34:16` | `27.93%` | `0.0%` | 1364 | 572 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T13:46:35.858121+00:00`.*
