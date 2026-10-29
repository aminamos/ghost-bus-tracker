# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:18.808000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`42.8%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `243` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `104` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 104 | 42.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 138 | 56.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3001** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2998** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 127 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3031** | 11 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `481290` | Route 3001 | `24:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481287` | Route 3001 | `22:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480480` | Route 2998 | `23:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481284` | Route 3001 | `21:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480477` | Route 2998 | `21:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481281` | Route 3001 | `19:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480474` | Route 2998 | `20:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481278` | Route 3001 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480471` | Route 2998 | `18:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481272` | Route 3001 | `15:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480465` | Route 2998 | `15:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481275` | Route 3001 | `16:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480468` | Route 2998 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480454` | Route 2998 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481261` | Route 3001 | `09:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `42.8%` | `0.0%` | 243 | 1 | `+0.0s` |
| `2026-10-29 06:30:21` | `41.77%` | `0.0%` | 249 | 2 | `+0.0s` |
| `2026-10-29 06:00:20` | `41.11%` | `0.0%` | 253 | 3 | `+0.0s` |
| `2026-10-29 05:30:18` | `41.27%` | `0.0%` | 252 | 1 | `+0.0s` |
| `2026-10-29 05:00:19` | `40.47%` | `0.0%` | 257 | 2 | `+0.0s` |
| `2026-10-29 04:30:19` | `35.96%` | `0.0%` | 292 | 30 | `+0.0s` |
| `2026-10-29 04:00:19` | `14.08%` | `0.0%` | 71 | 31 | `+0.0s` |
| `2026-10-29 03:30:18` | `21.84%` | `0.0%` | 87 | 31 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.808000+00:00`.*
