# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-12T07:00:18.437000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`51.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `213` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `111` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `110` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 110 | 51.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 25 | 0 | 25 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route Red** | 25 | 16 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Orange** | 24 | 13 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Blue** | 9 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 12 | 10 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 104** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78941099` | Route 51 | `08:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854550` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854570` | Route 220 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854590` | Route 220 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854464` | Route 220 | `15:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854576` | Route 220 | `17:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854596` | Route 220 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854542` | Route 220 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854530` | Route 220 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854450` | Route 220 | `08:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:18` | `51.64%` | `0.0%` | 213 | 111 | `+0.0s` |
| `2026-11-12 06:30:18` | `38.79%` | `0.0%` | 281 | 164 | `+0.0s` |
| `2026-11-12 06:00:17` | `24.88%` | `0.0%` | 426 | 255 | `+0.0s` |
| `2026-11-12 05:30:17` | `17.14%` | `0.0%` | 595 | 300 | `+0.0s` |
| `2026-11-12 05:00:18` | `14.6%` | `0.0%` | 719 | 314 | `+0.0s` |
| `2026-11-12 04:30:18` | `13.83%` | `0.0%` | 759 | 329 | `+0.0s` |
| `2026-11-12 04:00:18` | `14.43%` | `0.0%` | 776 | 340 | `+0.0s` |
| `2026-11-12 03:30:18` | `19.34%` | `0.0%` | 817 | 362 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:18.437000+00:00`.*
