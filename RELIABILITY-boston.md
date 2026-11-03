# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-03T07:00:18.413000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`91.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `315` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `29` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `288` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 288 | 91.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 99** | 43 | 0 | 43 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 95** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 85** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 112** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78174197` | Route 85 | `15:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266279` | Route 106 | `13:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78174241` | Route 85 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266272` | Route 106 | `11:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78174184` | Route 85 | `09:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259890` | Route 95 | `06:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78258772` | Route 99 | `05:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266293` | Route 106 | `18:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181983` | Route 18 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78266387` | Route 95 | `24:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `91.43%` | `0.0%` | 315 | 29 | `+0.0s` |
| `2026-11-03 06:30:18` | `72.8%` | `0.0%` | 386 | 95 | `+0.0s` |
| `2026-11-03 06:00:18` | `51.57%` | `0.0%` | 541 | 199 | `+0.0s` |
| `2026-11-03 05:30:18` | `35.84%` | `0.0%` | 759 | 268 | `+0.0s` |
| `2026-11-03 05:00:19` | `29.37%` | `0.0%` | 916 | 306 | `+0.0s` |
| `2026-11-03 04:30:18` | `28.01%` | `0.0%` | 964 | 325 | `+0.0s` |
| `2026-11-03 04:00:17` | `27.36%` | `0.0%` | 994 | 343 | `+0.0s` |
| `2026-11-03 03:30:18` | `30.45%` | `0.0%` | 1028 | 359 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.413000+00:00`.*
