# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:18.829000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`70.16%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `124` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `29` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `87` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 87 | 70.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 18 | 14.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 64** | 82 | 0 | 82 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 16** | 7 | 0 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 216** | 6 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 4 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78182336` | Route 57 | `25:40:00` | `SCHEDULED` | Assigned vehicle y1799 is missing from active GPS transponder fleet |
| `78476627` | Route 64 | `16:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476666` | Route 64 | `08:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476652` | Route 64 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476616` | Route 64 | `15:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476653` | Route 64 | `13:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476673` | Route 64 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476684` | Route 64 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476631` | Route 64 | `11:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78476618` | Route 64 | `14:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:18` | `70.16%` | `0.0%` | 124 | 29 | `+0.0s` |
| `2026-11-17 06:30:18` | `44.5%` | `0.0%` | 191 | 92 | `+0.0s` |
| `2026-11-17 06:00:18` | `25.07%` | `0.0%` | 339 | 196 | `+0.0s` |
| `2026-11-17 05:30:18` | `14.08%` | `0.0%` | 561 | 274 | `+0.0s` |
| `2026-11-17 05:00:17` | `10.93%` | `0.0%` | 732 | 301 | `+0.0s` |
| `2026-11-17 04:30:18` | `10.18%` | `0.0%` | 786 | 322 | `+0.0s` |
| `2026-11-17 04:00:18` | `10.54%` | `0.0%` | 816 | 341 | `+0.0s` |
| `2026-11-17 03:30:20` | `14.17%` | `0.0%` | 840 | 381 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:18.829000+00:00`.*
