# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-03T07:00:18.764000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `359` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `359` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 359 | 100.0% |
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
| **Route 51A** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 182** | 13 | 0 | 13 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51B** | 13 | 0 | 13 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 135** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4661736` | Route 9B | `22:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659546` | Route 8 | `19:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650500` | Route 182 | `05:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661516` | Route 9A | `16:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661537` | Route 9A | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660594` | Route 87 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649413` | Route 1 | `21:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649404` | Route 1 | `20:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649395` | Route 1 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649385` | Route 1 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649374` | Route 1 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659555` | Route 8 | `23:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659740` | Route 82 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661527` | Route 9A | `19:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659527` | Route 8 | `12:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `100.0%` | `0.0%` | 359 | 0 | `+0.0s` |
| `2026-11-03 06:30:26` | `100.0%` | `0.0%` | 359 | 0 | `+0.0s` |
| `2026-11-03 06:00:19` | `0.0%` | `100.0%` | 1 | 1 | `-39.0s` |
| `2026-11-03 05:30:18` | `20.0%` | `100.0%` | 5 | 4 | `+48.8s` |
| `2026-11-03 05:00:24` | `7.14%` | `72.73%` | 28 | 21 | `-41.8s` |
| `2026-11-03 04:30:21` | `9.38%` | `69.09%` | 64 | 44 | `-15.1s` |
| `2026-11-03 04:00:19` | `8.41%` | `82.42%` | 107 | 58 | `+12.3s` |
| `2026-11-03 03:30:20` | `11.51%` | `85.71%` | 139 | 68 | `+17.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.764000+00:00`.*
