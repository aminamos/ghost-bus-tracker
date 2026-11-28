# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:19.109000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`73.41%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `519` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `3` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `381` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 381 | 73.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 134 | 25.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3001** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2994** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3017** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `478975` | Route 2992 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478733` | Route 2991 | `13:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478969` | Route 2992 | `08:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478968` | Route 2992 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478737` | Route 2991 | `15:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478736` | Route 2991 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478965` | Route 2992 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478964` | Route 2992 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478967` | Route 2992 | `07:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478966` | Route 2992 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478963` | Route 2992 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `482440` | Route 3005 | `24:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `482436` | Route 3005 | `22:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481573` | Route 3002 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480324` | Route 2997 | `18:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:19` | `73.41%` | `0.0%` | 519 | 3 | `+0.0s` |
| `2026-11-28 06:30:17` | `73.27%` | `0.0%` | 520 | 2 | `+0.0s` |
| `2026-11-28 06:00:18` | `72.76%` | `0.0%` | 525 | 4 | `+0.0s` |
| `2026-11-28 05:30:18` | `68.27%` | `0.0%` | 561 | 32 | `+0.0s` |
| `2026-11-28 05:00:18` | `14.29%` | `0.0%` | 77 | 33 | `+0.0s` |
| `2026-11-28 04:30:17` | `23.08%` | `0.0%` | 91 | 32 | `+0.0s` |
| `2026-11-28 04:00:18` | `29.25%` | `0.0%` | 106 | 33 | `+0.0s` |
| `2026-11-28 03:30:18` | `35.04%` | `0.0%` | 117 | 33 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:19.109000+00:00`.*
