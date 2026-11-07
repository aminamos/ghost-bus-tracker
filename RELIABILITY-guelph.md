# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:18.848000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`68.08%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `448` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `5` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `305` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 305 | 68.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 137 | 30.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3023** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3019** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `478980` | Route 2992 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478979` | Route 2992 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478978` | Route 2992 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478977` | Route 2992 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478976` | Route 2992 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478975` | Route 2992 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478974` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478973` | Route 2992 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478972` | Route 2992 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478971` | Route 2992 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478970` | Route 2992 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478969` | Route 2992 | `08:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478968` | Route 2992 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478967` | Route 2992 | `07:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478966` | Route 2992 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:18` | `68.08%` | `0.0%` | 448 | 5 | `+0.0s` |
| `2026-11-07 06:30:18` | `67.93%` | `0.0%` | 449 | 3 | `+0.0s` |
| `2026-11-07 06:00:19` | `67.63%` | `0.0%` | 451 | 2 | `+0.0s` |
| `2026-11-07 05:30:18` | `63.22%` | `0.0%` | 484 | 30 | `+0.0s` |
| `2026-11-07 05:00:18` | `11.76%` | `0.0%` | 68 | 31 | `+0.0s` |
| `2026-11-07 04:30:18` | `18.29%` | `0.0%` | 82 | 31 | `+0.0s` |
| `2026-11-07 04:00:20` | `23.4%` | `0.0%` | 94 | 33 | `+0.0s` |
| `2026-11-07 03:30:19` | `28.43%` | `0.0%` | 102 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.848000+00:00`.*
