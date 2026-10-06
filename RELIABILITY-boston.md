# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T06:42:11.165102+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`99.21%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `633` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `7` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `628` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 628 | 99.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 77** | 187 | 0 | 187 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 741** | 127 | 0 | 127 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 743** | 110 | 0 | 110 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 435** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 34 | 0 | 34 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 80** | 27 | 0 | 27 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 99** | 22 | 0 | 22 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78477846` | Route 77 | `06:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591960` | Route 741 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591955` | Route 741 | `16:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78475863` | Route 80 | `09:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591573` | Route 743 | `17:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266279` | Route 106 | `13:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78477678` | Route 77 | `20:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591880` | Route 741 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78477673` | Route 77 | `20:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266272` | Route 106 | `11:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78477836` | Route 77 | `05:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78477854` | Route 77 | `04:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591571` | Route 743 | `20:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 06:42:11` | `99.21%` | `0.0%` | 633 | 7 | `+0.0s` |
| `2026-10-06 00:28:46` | `36.12%` | `0.0%` | 1304 | 459 | `+0.0s` |
| `2026-10-05 18:39:11` | `19.98%` | `0.0%` | 1712 | 749 | `+0.0s` |
| `2026-10-05 18:02:18` | `25.7%` | `0.0%` | 1607 | 667 | `+0.0s` |
| `2026-10-05 17:57:48` | `26.29%` | `0.0%` | 1575 | 657 | `+0.0s` |
| `2026-10-05 17:20:38` | `29.48%` | `0.0%` | 1452 | 603 | `+0.0s` |
| `2026-10-05 16:34:16` | `27.93%` | `0.0%` | 1364 | 572 | `+0.0s` |
| `2026-10-05 12:15:24` | `10.28%` | `0.0%` | 1731 | 808 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T06:42:11.165102+00:00`.*
