# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.185000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`67.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `93` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `41` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `63` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 63 | 67.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 211** | 45 | 0 | 45 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 217** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 121** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78854268` | Route 211 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853986` | Route 217 | `06:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854281` | Route 211 | `09:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78515465` | Route 121 | `08:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854269` | Route 211 | `16:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854265` | Route 211 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854290` | Route 211 | `19:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854276` | Route 211 | `06:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854274` | Route 211 | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853979` | Route 217 | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854261` | Route 211 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854297` | Route 211 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853985` | Route 217 | `17:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854253` | Route 211 | `06:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853984` | Route 217 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `67.74%` | `0.0%` | 93 | 41 | `+0.0s` |
| `2026-11-25 06:30:18` | `36.0%` | `0.0%` | 175 | 104 | `+0.0s` |
| `2026-11-25 06:00:18` | `19.15%` | `0.0%` | 329 | 203 | `+0.0s` |
| `2026-11-25 05:30:17` | `11.25%` | `0.0%` | 551 | 276 | `+0.0s` |
| `2026-11-25 05:00:17` | `8.54%` | `0.0%` | 714 | 302 | `+0.0s` |
| `2026-11-25 04:30:17` | `8.65%` | `0.0%` | 763 | 318 | `+0.0s` |
| `2026-11-25 04:00:18` | `9.77%` | `0.0%` | 798 | 338 | `+0.0s` |
| `2026-11-25 03:30:18` | `12.89%` | `0.0%` | 830 | 362 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.185000+00:00`.*
