# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.213000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`31.37%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `102` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `88` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `32` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 32 | 31.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 2.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 43** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 110** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 741** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 6 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 7 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Red** | 6 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 39** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78980135` | Route 43 | `20:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980214` | Route 43 | `07:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980343` | Route 43 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980327` | Route 43 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980228` | Route 43 | `06:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980329` | Route 43 | `17:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980148` | Route 43 | `23:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980153` | Route 43 | `24:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78979267` | Route 66 | `25:32:00` | `SCHEDULED` | Assigned vehicle y1775 is missing from active GPS transponder fleet |
| `78980219` | Route 43 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980141` | Route 43 | `21:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980224` | Route 43 | `06:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980132` | Route 43 | `18:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980134` | Route 43 | `09:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78980221` | Route 43 | `07:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `31.37%` | `0.0%` | 102 | 88 | `+0.0s` |
| `2026-11-21 06:30:19` | `17.96%` | `0.0%` | 206 | 157 | `+0.0s` |
| `2026-11-21 06:00:18` | `8.42%` | `0.0%` | 380 | 251 | `+0.0s` |
| `2026-11-21 05:30:17` | `5.52%` | `0.0%` | 543 | 297 | `+0.0s` |
| `2026-11-21 05:00:18` | `5.1%` | `0.0%` | 686 | 323 | `+0.0s` |
| `2026-11-21 04:30:18` | `4.32%` | `0.0%` | 717 | 343 | `+0.0s` |
| `2026-11-21 04:00:17` | `2.14%` | `0.0%` | 748 | 369 | `+0.0s` |
| `2026-11-21 03:30:17` | `6.56%` | `0.0%` | 777 | 394 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.213000+00:00`.*
