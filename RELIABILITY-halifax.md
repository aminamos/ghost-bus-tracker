# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:18.966000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `316` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `316` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 316 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 25 | 0 | 25 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4656131` | Route 56 | `09:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655265` | Route 51A | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659450` | Route 8 | `12:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660548` | Route 87 | `20:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659444` | Route 8 | `09:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656142` | Route 56 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655271` | Route 51A | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649667` | Route 10B | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649673` | Route 10B | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649968` | Route 10C | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649658` | Route 10B | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659445` | Route 8 | `10:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661672` | Route 9B | `20:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656153` | Route 56 | `20:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656137` | Route 56 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `100.0%` | `0.0%` | 316 | 0 | `+0.0s` |
| `2026-11-15 06:30:18` | `100.0%` | `0.0%` | 316 | 0 | `+0.0s` |
| `2026-11-15 06:00:30` | `0.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-15 05:30:19` | `0.0%` | `0.0%` | 2 | 3 | `-67.0s` |
| `2026-11-15 05:00:19` | `7.69%` | `72.73%` | 13 | 11 | `+26.7s` |
| `2026-11-15 04:30:19` | `5.0%` | `73.53%` | 40 | 31 | `+37.4s` |
| `2026-11-15 04:00:19` | `4.11%` | `85.29%` | 73 | 49 | `+0.6s` |
| `2026-11-15 03:30:18` | `7.44%` | `84.68%` | 121 | 64 | `+21.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.966000+00:00`.*
