# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-24T07:00:18.148000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`56.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `69` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `26` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `39` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 39 | 56.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 4 | 5.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 112** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 28** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 8 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 8 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78181983` | Route 18 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260507` | Route 112 | `08:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181981` | Route 18 | `11:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266964` | Route 112 | `19:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181980` | Route 18 | `12:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181977` | Route 18 | `07:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260519` | Route 112 | `13:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260536` | Route 112 | `19:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181975` | Route 18 | `08:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260518` | Route 112 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181972` | Route 18 | `19:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260532` | Route 112 | `18:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181976` | Route 18 | `06:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266940` | Route 112 | `07:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181974` | Route 18 | `08:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:18` | `56.52%` | `0.0%` | 69 | 26 | `+0.0s` |
| `2026-11-24 06:30:18` | `25.32%` | `0.0%` | 154 | 99 | `+0.0s` |
| `2026-11-24 06:00:17` | `12.82%` | `0.0%` | 312 | 201 | `+0.0s` |
| `2026-11-24 05:30:17` | `7.24%` | `0.0%` | 539 | 271 | `+0.0s` |
| `2026-11-24 05:00:18` | `5.84%` | `0.0%` | 685 | 292 | `+0.0s` |
| `2026-11-24 04:30:18` | `5.56%` | `0.0%` | 737 | 312 | `+0.0s` |
| `2026-11-24 04:00:18` | `5.5%` | `0.0%` | 764 | 333 | `+0.0s` |
| `2026-11-24 03:30:19` | `10.78%` | `0.0%` | 807 | 359 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:18.148000+00:00`.*
