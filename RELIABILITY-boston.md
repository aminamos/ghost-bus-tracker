# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T07:00:21.156000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.26%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `95` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `81` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 81 | 85.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 80 | 0 | 80 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `78850707` | Route 220 | `11:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850805` | Route 220 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850819` | Route 220 | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850843` | Route 220 | `21:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850811` | Route 220 | `13:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850829` | Route 220 | `18:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850839` | Route 220 | `20:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850711` | Route 220 | `13:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850732` | Route 220 | `23:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850718` | Route 220 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850783` | Route 220 | `06:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850701` | Route 220 | `08:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850729` | Route 220 | `22:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850696` | Route 220 | `05:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78850823` | Route 220 | `16:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 07:00:21` | `85.26%` | `0.0%` | 95 | 15 | `+0.0s` |
| `2026-10-24 06:30:18` | `90.85%` | `0.0%` | 317 | 32 | `+0.0s` |
| `2026-10-24 06:00:18` | `82.42%` | `0.0%` | 347 | 60 | `+0.0s` |
| `2026-10-24 05:30:17` | `62.91%` | `0.0%` | 453 | 135 | `+0.0s` |
| `2026-10-24 05:00:19` | `46.27%` | `0.0%` | 603 | 214 | `+0.0s` |
| `2026-10-24 04:30:18` | `33.75%` | `0.0%` | 806 | 281 | `+0.0s` |
| `2026-10-24 04:00:18` | `28.69%` | `0.0%` | 941 | 301 | `+0.0s` |
| `2026-10-24 03:30:19` | `27.37%` | `0.0%` | 972 | 316 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T07:00:21.156000+00:00`.*
