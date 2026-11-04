# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:20.970000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `429` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `429` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 429 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 24** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4659742` | Route 82 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661512` | Route 9A | `15:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649485` | Route 10A | `15:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649481` | Route 10A | `14:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655383` | Route 51B | `17:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659545` | Route 8 | `18:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4654647` | Route 433 | `16:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661514` | Route 9A | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659535` | Route 8 | `15:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661523` | Route 9A | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659509` | Route 8 | `05:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659741` | Route 82 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651887` | Route 24 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650044` | Route 10C | `15:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659546` | Route 8 | `19:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:20` | `100.0%` | `0.0%` | 429 | 0 | `+0.0s` |
| `2026-11-04 06:30:32` | `100.0%` | `0.0%` | 429 | 0 | `+0.0s` |
| `2026-11-04 06:00:18` | `0.0%` | `100.0%` | 1 | 1 | `+140.0s` |
| `2026-11-04 05:30:18` | `16.67%` | `80.0%` | 6 | 5 | `+108.6s` |
| `2026-11-04 05:00:17` | `3.45%` | `70.83%` | 29 | 23 | `-34.7s` |
| `2026-11-04 04:30:17` | `7.81%` | `80.7%` | 64 | 43 | `-8.3s` |
| `2026-11-04 04:00:23` | `9.62%` | `85.06%` | 104 | 57 | `+15.7s` |
| `2026-11-04 03:30:21` | `12.59%` | `85.47%` | 135 | 67 | `+22.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:20.970000+00:00`.*
