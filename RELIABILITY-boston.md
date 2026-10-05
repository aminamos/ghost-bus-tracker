# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-05T18:02:18.834514+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1607` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `667` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `413` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 413 | 25.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 5 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 424** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 746** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 220** | 75 | 5 | 69 | **`92.0%`** | `0.0%` | `+0.0s` |
| **Route 455** | 45 | 6 | 38 | **`84.44%`** | `0.0%` | `+0.0s` |
| **Route 714** | 6 | 1 | 5 | **`83.33%`** | `0.0%` | `+0.0s` |
| **Route 116** | 125 | 13 | 104 | **`83.2%`** | `0.0%` | `+0.0s` |
| **Route 93** | 40 | 3 | 33 | **`82.5%`** | `0.0%` | `+0.0s` |
| **Route 80** | 28 | 2 | 23 | **`82.14%`** | `0.0%` | `+0.0s` |
| **Route 436** | 16 | 3 | 13 | **`81.25%`** | `0.0%` | `+0.0s` |
| **Route 211** | 6 | 1 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |

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
| `78516856` | Route 455 | `06:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854268` | Route 211 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516829` | Route 455 | `12:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260879` | Route 96 | `14:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78475863` | Route 80 | `09:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78942251` | Route 32 | `14:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78985471` | Route 712 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259704` | Route 137 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259563` | Route 101 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516460` | Route 116 | `21:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590843` | Route 746 | `14:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 18:02:18` | `25.7%` | `0.0%` | 1607 | 667 | `+0.0s` |
| `2026-10-05 17:57:48` | `26.29%` | `0.0%` | 1575 | 657 | `+0.0s` |
| `2026-10-05 17:20:38` | `29.48%` | `0.0%` | 1452 | 603 | `+0.0s` |
| `2026-10-05 16:34:16` | `27.93%` | `0.0%` | 1364 | 572 | `+0.0s` |
| `2026-10-05 12:15:24` | `10.28%` | `0.0%` | 1731 | 808 | `+0.0s` |
| `2026-10-05 12:14:27` | `10.27%` | `0.0%` | 1724 | 808 | `+0.0s` |
| `2026-10-05 12:05:46` | `9.89%` | `0.0%` | 1779 | 815 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:02:18.834514+00:00`.*
