# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.703000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `258` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `258` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 258 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4649037` | Route 1 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649044` | Route 1 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649021` | Route 1 | `09:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649597` | Route 10B | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649594` | Route 10B | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656088` | Route 56 | `19:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649901` | Route 10C | `09:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656068` | Route 56 | `09:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656093` | Route 56 | `22:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661374` | Route 9A | `10:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656092` | Route 56 | `21:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649609` | Route 10B | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661376` | Route 9A | `12:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658190` | Route 72 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661380` | Route 9A | `16:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `100.0%` | `0.0%` | 258 | 0 | `+0.0s` |
| `2026-11-21 06:30:31` | `100.0%` | `0.0%` | 258 | 0 | `+0.0s` |
| `2026-11-21 06:00:18` | `50.0%` | `0.0%` | 2 | 1 | `+0.0s` |
| `2026-11-21 05:30:18` | `20.0%` | `75.0%` | 5 | 4 | `+57.5s` |
| `2026-11-21 05:00:20` | `6.9%` | `65.22%` | 29 | 22 | `-28.8s` |
| `2026-11-21 04:30:18` | `6.35%` | `78.18%` | 63 | 44 | `-5.9s` |
| `2026-11-21 04:00:18` | `7.41%` | `81.11%` | 108 | 61 | `+75.9s` |
| `2026-11-21 03:30:18` | `10.29%` | `82.05%` | 136 | 69 | `+54.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.703000+00:00`.*
