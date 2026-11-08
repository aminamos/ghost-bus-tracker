# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:17.829000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`53.31%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `302` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `4` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `161` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 161 | 53.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 133 | 44.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2997** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3019** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3017** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `481893` | Route 3003 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481895` | Route 3003 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481891` | Route 3003 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481889` | Route 3003 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481906` | Route 3003 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481908` | Route 3003 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481890` | Route 3003 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481892` | Route 3003 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481894` | Route 3003 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481896` | Route 3003 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481898` | Route 3003 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481900` | Route 3003 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481902` | Route 3003 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481904` | Route 3003 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479058` | Route 2992 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:17` | `53.31%` | `0.0%` | 302 | 4 | `+0.0s` |
| `2026-11-08 06:30:19` | `53.49%` | `0.0%` | 301 | 2 | `+0.0s` |
| `2026-11-08 06:00:18` | `53.31%` | `0.0%` | 302 | 2 | `+0.0s` |
| `2026-11-08 05:30:19` | `47.93%` | `0.0%` | 338 | 30 | `+0.0s` |
| `2026-11-08 05:00:18` | `13.04%` | `0.0%` | 69 | 32 | `+0.0s` |
| `2026-11-08 04:30:21` | `20.24%` | `0.0%` | 84 | 32 | `+0.0s` |
| `2026-11-08 04:00:18` | `26.32%` | `0.0%` | 95 | 32 | `+0.0s` |
| `2026-11-08 03:30:18` | `32.35%` | `0.0%` | 102 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.829000+00:00`.*
