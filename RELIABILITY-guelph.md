# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:20.880000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`73.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `518` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `6` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `380` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 380 | 73.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 131 | 25.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3001** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2998** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `481834` | Route 3003 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481832` | Route 3003 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480537` | Route 2998 | `13:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481347` | Route 3001 | `14:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481814` | Route 3003 | `23:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481816` | Route 3003 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481818` | Route 3003 | `21:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481820` | Route 3003 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481822` | Route 3003 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481583` | Route 3002 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480322` | Route 2997 | `17:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480337` | Route 2997 | `24:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481813` | Route 3003 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481815` | Route 3003 | `23:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481817` | Route 3003 | `22:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:20` | `73.36%` | `0.0%` | 518 | 6 | `+0.0s` |
| `2026-10-24 05:30:19` | `72.94%` | `0.0%` | 521 | 3 | `+0.0s` |
| `2026-10-24 05:00:22` | `72.8%` | `0.0%` | 522 | 2 | `+0.0s` |
| `2026-10-24 04:30:20` | `67.91%` | `0.0%` | 561 | 31 | `+0.0s` |
| `2026-10-24 04:00:20` | `16.22%` | `0.0%` | 74 | 32 | `+0.0s` |
| `2026-10-24 03:30:28` | `25.0%` | `0.0%` | 92 | 32 | `+0.0s` |
| `2026-10-24 03:00:19` | `32.08%` | `0.0%` | 106 | 32 | `+0.0s` |
| `2026-10-24 02:30:21` | `37.5%` | `0.0%` | 120 | 33 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:20.880000+00:00`.*
