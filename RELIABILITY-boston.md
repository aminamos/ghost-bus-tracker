# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:18.237000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`41.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `56` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `31` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `23` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 23 | 41.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 14.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 112** | 22 | 0 | 22 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 6 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78156462` | Route 112 | `09:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156477` | Route 112 | `18:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156472` | Route 112 | `15:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156470` | Route 112 | `13:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156473` | Route 112 | `16:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78155477` | Route 112 | `08:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156469` | Route 112 | `14:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156465` | Route 112 | `11:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156471` | Route 112 | `15:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156468` | Route 112 | `12:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516520` | Route 116 | `25:28:00` | `SCHEDULED` | Assigned vehicle y3105 is missing from active GPS transponder fleet |
| `78156461` | Route 112 | `09:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156474` | Route 112 | `16:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156476` | Route 112 | `17:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78156475` | Route 112 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:18` | `41.07%` | `0.0%` | 56 | 31 | `+0.0s` |
| `2026-11-26 06:30:17` | `16.78%` | `0.0%` | 149 | 103 | `+0.0s` |
| `2026-11-26 06:00:17` | `9.76%` | `0.0%` | 297 | 196 | `+0.0s` |
| `2026-11-26 05:30:18` | `4.35%` | `0.0%` | 529 | 277 | `+0.0s` |
| `2026-11-26 05:00:17` | `3.26%` | `0.0%` | 675 | 304 | `+0.0s` |
| `2026-11-26 04:30:18` | `4.04%` | `0.0%` | 743 | 318 | `+0.0s` |
| `2026-11-26 04:00:17` | `4.19%` | `0.0%` | 788 | 343 | `+0.0s` |
| `2026-11-26 03:30:18` | `9.4%` | `0.0%` | 819 | 367 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:18.237000+00:00`.*
