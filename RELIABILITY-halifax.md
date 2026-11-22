# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:18.581000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `222` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `222` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 222 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4649967` | Route 10C | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649666` | Route 10B | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661407` | Route 9A | `07:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661409` | Route 9A | `09:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661411` | Route 9A | `11:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661413` | Route 9A | `13:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661415` | Route 9A | `15:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661417` | Route 9A | `17:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661419` | Route 9A | `19:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661421` | Route 9A | `21:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661423` | Route 9A | `23:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656139` | Route 56 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649662` | Route 10B | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649147` | Route 1 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649152` | Route 1 | `07:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `100.0%` | `0.0%` | 222 | 0 | `+0.0s` |
| `2026-11-22 06:30:18` | `100.0%` | `0.0%` | 222 | 0 | `+0.0s` |
| `2026-11-22 06:00:17` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-11-22 05:30:29` | `0.0%` | `0.0%` | 2 | 3 | `-181.0s` |
| `2026-11-22 05:00:18` | `0.0%` | `70.0%` | 12 | 12 | `+14.3s` |
| `2026-11-22 04:30:18` | `2.44%` | `74.29%` | 41 | 35 | `+74.1s` |
| `2026-11-22 04:00:18` | `2.63%` | `79.17%` | 76 | 51 | `+23.1s` |
| `2026-11-22 03:30:20` | `5.79%` | `75.68%` | 121 | 66 | `+87.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.581000+00:00`.*
