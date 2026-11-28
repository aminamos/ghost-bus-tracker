# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:19.827000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`81.69%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `295` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `241` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 241 | 81.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 54 | 18.3% |

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
| **Route 58** | 17 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 17 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 67** | 10 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `4656093` | Route 56 | `22:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649623` | Route 10B | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649624` | Route 10B | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649925` | Route 10C | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649068` | Route 1 | `21:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649074` | Route 1 | `22:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649080` | Route 1 | `24:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649033` | Route 1 | `12:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649040` | Route 1 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649047` | Route 1 | `15:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649054` | Route 1 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649061` | Route 1 | `19:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656086` | Route 56 | `18:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649913` | Route 10C | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649917` | Route 10C | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:19` | `81.69%` | `0.0%` | 295 | 0 | `+0.0s` |
| `2026-11-28 06:30:17` | `81.69%` | `0.0%` | 295 | 0 | `+0.0s` |
| `2026-11-28 06:00:18` | `50.0%` | `0.0%` | 2 | 1 | `+0.0s` |
| `2026-11-28 05:30:19` | `12.5%` | `100.0%` | 8 | 7 | `+37.2s` |
| `2026-11-28 05:00:19` | `5.88%` | `50.0%` | 34 | 27 | `+183.6s` |
| `2026-11-28 04:30:17` | `5.88%` | `64.41%` | 68 | 48 | `+177.1s` |
| `2026-11-28 04:00:19` | `8.33%` | `66.32%` | 108 | 63 | `+155.6s` |
| `2026-11-28 03:30:19` | `11.43%` | `73.73%` | 140 | 73 | `+145.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:19.827000+00:00`.*
