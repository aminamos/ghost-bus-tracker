# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-16T07:00:18.675000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`78.85%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `104` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `50` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `82` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 82 | 78.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 39** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78854560` | Route 220 | `13:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:18` | `78.85%` | `0.0%` | 104 | 50 | `+0.0s` |
| `2026-11-16 06:30:20` | `53.16%` | `0.0%` | 158 | 86 | `+0.0s` |
| `2026-11-16 06:00:18` | `28.72%` | `0.0%` | 289 | 178 | `+0.0s` |
| `2026-11-16 05:30:18` | `16.63%` | `0.0%` | 475 | 253 | `+0.0s` |
| `2026-11-16 05:00:18` | `12.23%` | `0.0%` | 613 | 279 | `+0.0s` |
| `2026-11-16 04:30:18` | `11.95%` | `0.0%` | 661 | 282 | `+0.0s` |
| `2026-11-16 04:00:18` | `12.84%` | `0.0%` | 670 | 286 | `+0.0s` |
| `2026-11-16 03:30:17` | `14.39%` | `0.0%` | 709 | 300 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:18.675000+00:00`.*
