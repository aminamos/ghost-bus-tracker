# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:19.944000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `357` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `357` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 357 | 100.0% |
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
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `4658286` | Route 72 | `08:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661717` | Route 9B | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649736` | Route 10B | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649731` | Route 10B | `13:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649424` | Route 1 | `24:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649418` | Route 1 | `23:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649411` | Route 1 | `21:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649402` | Route 1 | `20:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649393` | Route 1 | `18:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649382` | Route 1 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649371` | Route 1 | `14:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649361` | Route 1 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649351` | Route 1 | `11:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649342` | Route 1 | `10:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649332` | Route 1 | `08:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:19` | `100.0%` | `0.0%` | 357 | 0 | `+0.0s` |
| `2026-11-27 06:00:18` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-27 05:30:19` | `20.0%` | `75.0%` | 5 | 4 | `-54.5s` |
| `2026-11-27 05:00:17` | `6.9%` | `65.0%` | 29 | 23 | `+18.8s` |
| `2026-11-27 04:30:20` | `7.81%` | `76.36%` | 64 | 44 | `-6.5s` |
| `2026-11-27 04:00:17` | `5.88%` | `82.56%` | 102 | 57 | `+74.2s` |
| `2026-11-27 03:30:19` | `8.96%` | `81.51%` | 134 | 68 | `+31.0s` |
| `2026-11-27 03:00:18` | `10.18%` | `79.58%` | 167 | 81 | `+38.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:19.944000+00:00`.*
