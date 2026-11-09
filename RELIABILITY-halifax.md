# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.456000+00:00` | **Source:** live GTFS-RT feed

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
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4649333` | Route 1 | `08:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659738` | Route 82 | `15:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649319` | Route 1 | `05:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659747` | Route 82 | `21:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649388` | Route 1 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649376` | Route 1 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649365` | Route 1 | `13:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649355` | Route 1 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649343` | Route 1 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661734` | Route 9B | `21:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661730` | Route 9B | `19:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650053` | Route 10C | `18:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650046` | Route 10C | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650066` | Route 10C | `24:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4654648` | Route 433 | `17:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `100.0%` | `0.0%` | 510 | 0 | `+0.0s` |
| `2026-11-09 06:30:21` | `100.0%` | `0.0%` | 510 | 0 | `+0.0s` |
| `2026-11-09 06:00:18` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-11-09 05:30:18` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-11-09 05:00:18` | `25.0%` | `66.67%` | 4 | 4 | `-74.3s` |
| `2026-11-09 04:30:19` | `0.0%` | `83.33%` | 18 | 18 | `+428.1s` |
| `2026-11-09 04:00:21` | `0.0%` | `77.78%` | 47 | 35 | `+176.0s` |
| `2026-11-09 03:30:18` | `6.67%` | `81.16%` | 75 | 43 | `+165.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.456000+00:00`.*
