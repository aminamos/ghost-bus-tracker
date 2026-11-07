# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:18.268000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`55.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `144` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `78` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `80` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 80 | 55.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 80 | 0 | 80 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 110** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 741** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 39** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 5 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2026-11-07 07:00:18` | `55.56%` | `0.0%` | 144 | 78 | `+0.0s` |
| `2026-11-07 06:30:18` | `32.67%` | `0.0%` | 251 | 157 | `+0.0s` |
| `2026-11-07 06:00:18` | `19.32%` | `0.0%` | 414 | 233 | `+0.0s` |
| `2026-11-07 05:30:18` | `13.55%` | `0.0%` | 598 | 286 | `+0.0s` |
| `2026-11-07 05:00:17` | `10.93%` | `0.0%` | 732 | 306 | `+0.0s` |
| `2026-11-07 04:30:18` | `10.31%` | `0.0%` | 795 | 324 | `+0.0s` |
| `2026-11-07 04:00:18` | `10.69%` | `0.0%` | 814 | 340 | `+0.0s` |
| `2026-11-07 03:30:18` | `15.22%` | `0.0%` | 828 | 356 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.268000+00:00`.*
