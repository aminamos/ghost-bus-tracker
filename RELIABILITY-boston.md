# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-11T07:00:18.244000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`91.59%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `345` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `61` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `316` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 316 | 91.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 742** | 125 | 0 | 125 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 41 | 1 | 40 | **`97.56%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `78679349` | Route 742 | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78678219` | Route 742 | `09:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78856644` | Route 220 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78930155` | Route 35 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78856586` | Route 220 | `20:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78930008` | Route 35 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78268218` | Route 10 | `23:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78678334` | Route 742 | `14:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78856676` | Route 220 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78929979` | Route 35 | `15:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78678330` | Route 742 | `08:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78268311` | Route 10 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78856670` | Route 220 | `13:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78678218` | Route 742 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78856569` | Route 220 | `11:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-11 07:00:18` | `91.59%` | `0.0%` | 345 | 61 | `+0.0s` |
| `2026-11-11 06:30:17` | `77.13%` | `0.0%` | 411 | 115 | `+0.0s` |
| `2026-11-11 06:00:19` | `55.04%` | `0.0%` | 565 | 221 | `+0.0s` |
| `2026-11-11 05:30:18` | `39.74%` | `0.0%` | 775 | 290 | `+0.0s` |
| `2026-11-11 05:00:18` | `33.37%` | `0.0%` | 914 | 314 | `+0.0s` |
| `2026-11-11 04:30:18` | `31.74%` | `0.0%` | 961 | 339 | `+0.0s` |
| `2026-11-11 04:00:18` | `31.54%` | `0.0%` | 986 | 343 | `+0.0s` |
| `2026-11-11 03:30:20` | `34.52%` | `0.0%` | 1014 | 370 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:18.244000+00:00`.*
