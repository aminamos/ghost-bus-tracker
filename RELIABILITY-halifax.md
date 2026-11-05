# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:18.211000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `424` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `424` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 424 | 100.0% |
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
| **Route 24** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 182** | 13 | 0 | 13 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4649326` | Route 1 | `07:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649335` | Route 1 | `08:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649344` | Route 1 | `10:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661714` | Route 9B | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649353` | Route 1 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649363` | Route 1 | `13:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649373` | Route 1 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649384` | Route 1 | `17:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4654646` | Route 433 | `06:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653763` | Route 320 | `06:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653790` | Route 320 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653767` | Route 320 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653794` | Route 320 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653769` | Route 320 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653796` | Route 320 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:18` | `100.0%` | `0.0%` | 424 | 0 | `+0.0s` |
| `2026-11-05 06:30:18` | `100.0%` | `0.0%` | 424 | 0 | `+0.0s` |
| `2026-11-05 06:00:18` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-05 05:30:19` | `14.29%` | `80.0%` | 7 | 5 | `+1115.4s` |
| `2026-11-05 05:00:18` | `10.34%` | `73.91%` | 29 | 24 | `+1.6s` |
| `2026-11-05 04:30:18` | `9.38%` | `79.63%` | 64 | 46 | `+18.1s` |
| `2026-11-05 04:00:20` | `8.82%` | `83.53%` | 102 | 59 | `+20.9s` |
| `2026-11-05 03:30:19` | `11.85%` | `86.96%` | 135 | 69 | `+15.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.211000+00:00`.*
