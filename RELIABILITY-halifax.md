# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.233000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `291` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `291` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 291 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `4661413` | Route 9A | `13:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659442` | Route 8 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659438` | Route 8 | `06:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649972` | Route 10C | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656157` | Route 56 | `22:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659713` | Route 82 | `21:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659708` | Route 82 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659709` | Route 82 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659706` | Route 82 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659441` | Route 8 | `08:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659460` | Route 8 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659466` | Route 8 | `20:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656156` | Route 56 | `21:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655280` | Route 51A | `22:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659470` | Route 8 | `23:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `100.0%` | `0.0%` | 291 | 0 | `+0.0s` |
| `2026-11-08 06:30:20` | `100.0%` | `0.0%` | 291 | 0 | `+0.0s` |
| `2026-11-08 06:00:18` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-11-08 05:30:19` | `0.0%` | `100.0%` | 2 | 4 | `-60.0s` |
| `2026-11-08 05:00:18` | `7.69%` | `44.44%` | 13 | 11 | `-56.2s` |
| `2026-11-08 04:30:24` | `0.0%` | `75.0%` | 42 | 35 | `+36.7s` |
| `2026-11-08 04:00:19` | `8.75%` | `84.29%` | 80 | 50 | `+30.2s` |
| `2026-11-08 03:30:18` | `9.85%` | `83.48%` | 132 | 67 | `+69.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.233000+00:00`.*
