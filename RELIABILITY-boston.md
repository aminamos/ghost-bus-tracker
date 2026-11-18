# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-18T07:00:20.264000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`75.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `112` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `31` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `84` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 84 | 75.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 64** | 82 | 0 | 82 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Red** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `78476642` | Route 64 | `23:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476622` | Route 64 | `13:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476641` | Route 64 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476674` | Route 64 | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476678` | Route 64 | `06:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476627` | Route 64 | `16:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476666` | Route 64 | `08:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476652` | Route 64 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476616` | Route 64 | `15:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476653` | Route 64 | `13:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476673` | Route 64 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476684` | Route 64 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476631` | Route 64 | `11:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476618` | Route 64 | `14:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476683` | Route 64 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 07:00:20` | `75.0%` | `0.0%` | 112 | 31 | `+0.0s` |
| `2026-11-18 06:30:18` | `43.52%` | `0.0%` | 193 | 97 | `+0.0s` |
| `2026-11-18 06:00:19` | `23.56%` | `0.0%` | 348 | 200 | `+0.0s` |
| `2026-11-18 05:30:19` | `14.24%` | `0.0%` | 569 | 272 | `+0.0s` |
| `2026-11-18 05:00:18` | `11.37%` | `0.0%` | 721 | 301 | `+0.0s` |
| `2026-11-18 04:30:18` | `10.61%` | `0.0%` | 782 | 322 | `+0.0s` |
| `2026-11-18 04:00:17` | `11.44%` | `0.0%` | 804 | 349 | `+0.0s` |
| `2026-11-18 03:30:18` | `15.87%` | `0.0%` | 838 | 366 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T07:00:20.264000+00:00`.*
