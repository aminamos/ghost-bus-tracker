# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-03T07:00:18.560000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`67.05%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `437` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `293` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 293 | 67.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 144 | 33.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3031** | 11 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 133 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `480260` | Route 2997 | `24:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481508` | Route 3002 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480258` | Route 2997 | `23:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481506` | Route 3002 | `23:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480256` | Route 2997 | `22:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481504` | Route 3002 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480254` | Route 2997 | `21:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481502` | Route 3002 | `21:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480252` | Route 2997 | `20:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481500` | Route 3002 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480250` | Route 2997 | `19:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481498` | Route 3002 | `19:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480248` | Route 2997 | `18:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481496` | Route 3002 | `18:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480246` | Route 2997 | `17:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `67.05%` | `0.0%` | 437 | 0 | `+0.0s` |
| `2026-11-03 06:30:21` | `66.59%` | `0.0%` | 440 | 0 | `+0.0s` |
| `2026-11-03 06:00:18` | `65.84%` | `0.0%` | 445 | 1 | `+0.0s` |
| `2026-11-03 05:30:18` | `60.58%` | `0.0%` | 482 | 31 | `+0.0s` |
| `2026-11-03 05:00:21` | `11.59%` | `0.0%` | 69 | 32 | `+0.0s` |
| `2026-11-03 04:30:19` | `18.07%` | `0.0%` | 83 | 32 | `+0.0s` |
| `2026-11-03 04:00:18` | `23.66%` | `0.0%` | 93 | 32 | `+0.0s` |
| `2026-11-03 03:30:19` | `28.71%` | `0.0%` | 101 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.560000+00:00`.*
