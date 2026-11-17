# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:22.123000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `510` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `510` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 510 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4653790` | Route 320 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653767` | Route 320 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653794` | Route 320 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653763` | Route 320 | `06:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658289` | Route 72 | `10:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656196` | Route 56 | `07:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650505` | Route 182 | `06:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653798` | Route 320 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650035` | Route 10C | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661511` | Route 9A | `14:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653771` | Route 320 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661500` | Route 9A | `11:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4654971` | Route 5 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659518` | Route 8 | `09:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661530` | Route 9A | `21:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:22` | `100.0%` | `0.0%` | 510 | 0 | `+0.0s` |
| `2026-11-17 06:30:19` | `100.0%` | `0.0%` | 510 | 0 | `+0.0s` |
| `2026-11-17 06:00:21` | `0.0%` | `100.0%` | 1 | 1 | `+59.0s` |
| `2026-11-17 05:30:20` | `20.0%` | `75.0%` | 5 | 7 | `+21.8s` |
| `2026-11-17 05:00:18` | `13.51%` | `74.07%` | 37 | 25 | `-34.4s` |
| `2026-11-17 04:30:19` | `16.67%` | `69.64%` | 72 | 44 | `+50.8s` |
| `2026-11-17 04:00:18` | `14.17%` | `75.51%` | 120 | 60 | `-14.4s` |
| `2026-11-17 03:30:22` | `20.13%` | `83.33%` | 154 | 69 | `+27.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:22.123000+00:00`.*
