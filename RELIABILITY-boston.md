# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:18.813000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.05%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `228` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `21` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `219` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 219 | 96.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 80 | 0 | 80 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 95** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 94** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 112** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `78850707` | Route 220 | `11:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78064718` | Route 96 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850805` | Route 220 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78064708` | Route 96 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850819` | Route 220 | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78064725` | Route 96 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850843` | Route 220 | `21:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78064714` | Route 96 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850811` | Route 220 | `13:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78064743` | Route 96 | `21:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850829` | Route 220 | `18:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850839` | Route 220 | `20:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850711` | Route 220 | `13:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78064818` | Route 101 | `18:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78063344` | Route 94 | `16:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:18` | `96.05%` | `0.0%` | 228 | 21 | `+0.0s` |
| `2026-10-31 06:30:18` | `92.38%` | `0.0%` | 328 | 39 | `+0.0s` |
| `2026-10-31 06:00:19` | `82.87%` | `0.0%` | 362 | 70 | `+0.0s` |
| `2026-10-31 05:30:18` | `64.27%` | `0.0%` | 473 | 141 | `+0.0s` |
| `2026-10-31 05:00:19` | `46.56%` | `0.0%` | 640 | 230 | `+0.0s` |
| `2026-10-31 04:30:19` | `35.27%` | `0.0%` | 825 | 284 | `+0.0s` |
| `2026-10-31 04:00:17` | `29.9%` | `0.0%` | 970 | 309 | `+0.0s` |
| `2026-10-31 03:30:17` | `28.09%` | `0.0%` | 1004 | 326 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:18.813000+00:00`.*
