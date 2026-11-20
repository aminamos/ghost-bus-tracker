# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:19.632000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.2%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `412` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `46` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `384` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 384 | 93.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 111** | 383 | 3 | 380 | **`99.22%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 7 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78262351` | Route 111 | `04:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262666` | Route 111 | `07:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262635` | Route 111 | `24:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262373` | Route 111 | `10:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262360` | Route 111 | `08:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262516` | Route 111 | `13:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262404` | Route 111 | `06:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262440` | Route 111 | `07:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262523` | Route 111 | `19:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262681` | Route 111 | `12:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262562` | Route 111 | `08:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262633` | Route 111 | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262417` | Route 111 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262698` | Route 111 | `21:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262490` | Route 111 | `14:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:19` | `93.2%` | `0.0%` | 412 | 46 | `+0.0s` |
| `2026-11-20 06:30:18` | `76.46%` | `0.0%` | 497 | 116 | `+0.0s` |
| `2026-11-20 06:00:18` | `58.3%` | `0.0%` | 657 | 216 | `+0.0s` |
| `2026-11-20 05:30:18` | `43.04%` | `0.0%` | 862 | 281 | `+0.0s` |
| `2026-11-20 05:00:18` | `35.94%` | `0.0%` | 1024 | 310 | `+0.0s` |
| `2026-11-20 04:30:17` | `33.83%` | `0.0%` | 1073 | 324 | `+0.0s` |
| `2026-11-20 04:00:17` | `32.73%` | `0.0%` | 1112 | 344 | `+0.0s` |
| `2026-11-20 03:30:18` | `35.9%` | `0.0%` | 1142 | 362 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:19.632000+00:00`.*
