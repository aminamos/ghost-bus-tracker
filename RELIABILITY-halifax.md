# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.590000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `187` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `187` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 187 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `4655277` | Route 51A | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659707` | Route 82 | `15:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659709` | Route 82 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659706` | Route 82 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659708` | Route 82 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659710` | Route 82 | `18:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659711` | Route 82 | `19:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659712` | Route 82 | `20:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659713` | Route 82 | `21:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659462` | Route 8 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659468` | Route 8 | `21:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655274` | Route 51A | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659471` | Route 8 | `24:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655278` | Route 51A | `20:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655276` | Route 51A | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `100.0%` | `0.0%` | 187 | 0 | `+0.0s` |
| `2026-11-01 06:30:18` | `100.0%` | `0.0%` | 187 | 0 | `+0.0s` |
| `2026-11-01 06:00:19` | `0.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-01 05:30:19` | `0.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-01 05:00:20` | `0.0%` | `0.0%` | 2 | 0 | `+0.0s` |
| `2026-11-01 04:30:19` | `25.0%` | `0.0%` | 4 | 4 | `+0.0s` |
| `2026-11-01 04:00:18` | `11.76%` | `53.85%` | 17 | 16 | `+284.5s` |
| `2026-11-01 03:30:18` | `2.13%` | `59.52%` | 47 | 37 | `+351.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.590000+00:00`.*
