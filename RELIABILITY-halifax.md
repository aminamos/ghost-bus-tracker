# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:18.253000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `396` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `396` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 396 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 182** | 13 | 0 | 13 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51B** | 13 | 0 | 13 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4659545` | Route 8 | `18:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4654647` | Route 433 | `16:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661514` | Route 9A | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661523` | Route 9A | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659509` | Route 8 | `05:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659741` | Route 82 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659535` | Route 8 | `15:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653774` | Route 320 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661516` | Route 9A | `16:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650500` | Route 182 | `05:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653801` | Route 320 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653778` | Route 320 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653805` | Route 320 | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661537` | Route 9A | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659546` | Route 8 | `19:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `100.0%` | `0.0%` | 396 | 0 | `+0.0s` |
| `2026-11-06 06:30:19` | `100.0%` | `0.0%` | 396 | 0 | `+0.0s` |
| `2026-11-06 06:00:18` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-06 05:30:20` | `20.0%` | `100.0%` | 5 | 4 | `+37.5s` |
| `2026-11-06 05:00:19` | `6.67%` | `80.95%` | 30 | 23 | `+27.6s` |
| `2026-11-06 04:30:19` | `6.15%` | `78.33%` | 65 | 44 | `-11.2s` |
| `2026-11-06 04:00:23` | `9.71%` | `79.55%` | 103 | 57 | `+8.8s` |
| `2026-11-06 03:30:21` | `10.87%` | `84.3%` | 138 | 68 | `+28.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.253000+00:00`.*
