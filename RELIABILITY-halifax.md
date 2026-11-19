# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-19T07:00:19.763000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `469` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `469` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 469 | 100.0% |
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
| `4650505` | Route 182 | `06:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650208` | Route 135 | `06:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661500` | Route 9A | `11:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661530` | Route 9A | `21:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661725` | Route 9B | `17:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661511` | Route 9A | `14:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659736` | Route 82 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659737` | Route 82 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656201` | Route 56 | `09:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661729` | Route 9B | `19:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661505` | Route 9A | `12:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661715` | Route 9B | `09:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659735` | Route 82 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655788` | Route 54 | `14:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661484` | Route 9A | `06:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 07:00:19` | `100.0%` | `0.0%` | 469 | 0 | `+0.0s` |
| `2026-11-19 06:30:19` | `100.0%` | `0.0%` | 469 | 0 | `+0.0s` |
| `2026-11-19 06:00:20` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-19 05:30:23` | `20.0%` | `50.0%` | 5 | 3 | `-8.0s` |
| `2026-11-19 05:00:18` | `3.45%` | `68.18%` | 29 | 23 | `-7.5s` |
| `2026-11-19 04:30:19` | `7.81%` | `84.62%` | 64 | 45 | `-0.9s` |
| `2026-11-19 04:00:20` | `8.0%` | `82.76%` | 100 | 57 | `+7.2s` |
| `2026-11-19 03:30:18` | `9.77%` | `86.96%` | 133 | 67 | `+17.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:19.763000+00:00`.*
