# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-18T07:00:33.773000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `453` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `453` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 453 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 24** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4656224` | Route 56 | `21:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661519` | Route 9A | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661478` | Route 9A | `05:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661525` | Route 9A | `18:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650054` | Route 10C | `18:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661709` | Route 9B | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656226` | Route 56 | `22:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659744` | Route 82 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649723` | Route 10B | `09:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649726` | Route 10B | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650047` | Route 10C | `16:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661534` | Route 9A | `23:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661738` | Route 9B | `24:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649735` | Route 10B | `14:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649740` | Route 10B | `16:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 07:00:33` | `100.0%` | `0.0%` | 453 | 0 | `+0.0s` |
| `2026-11-18 06:30:19` | `100.0%` | `0.0%` | 453 | 0 | `+0.0s` |
| `2026-11-18 06:00:25` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-18 05:30:26` | `20.0%` | `75.0%` | 5 | 4 | `-20.8s` |
| `2026-11-18 05:00:18` | `6.9%` | `66.67%` | 29 | 22 | `-41.7s` |
| `2026-11-18 04:30:19` | `4.69%` | `69.09%` | 64 | 45 | `-8.7s` |
| `2026-11-18 04:00:18` | `7.77%` | `85.71%` | 103 | 58 | `+9.1s` |
| `2026-11-18 03:30:18` | `8.63%` | `82.4%` | 139 | 71 | `+9.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T07:00:33.773000+00:00`.*
