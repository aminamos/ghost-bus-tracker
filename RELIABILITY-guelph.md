# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:22.482000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`73.71%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `582` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `5` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `429` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 429 | 73.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 145 | 24.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 98 | 0 | 98 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `478910` | Route 2992 | `23:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478678` | Route 2991 | `24:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478644` | Route 2991 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478643` | Route 2991 | `06:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478906` | Route 2992 | `21:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478905` | Route 2992 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478904` | Route 2992 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478903` | Route 2992 | `20:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478909` | Route 2992 | `23:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478908` | Route 2992 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478907` | Route 2992 | `22:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483787` | Route 3013 | `10:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483789` | Route 3013 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483785` | Route 3013 | `11:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483795` | Route 3013 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:22` | `73.71%` | `0.0%` | 582 | 5 | `+0.0s` |
| `2026-11-20 06:30:18` | `73.58%` | `0.0%` | 583 | 4 | `+0.0s` |
| `2026-11-20 06:00:20` | `73.71%` | `0.0%` | 582 | 2 | `+0.0s` |
| `2026-11-20 05:30:18` | `68.88%` | `0.0%` | 617 | 30 | `+0.0s` |
| `2026-11-20 05:00:19` | `15.71%` | `0.0%` | 70 | 32 | `+0.0s` |
| `2026-11-20 04:30:18` | `24.14%` | `0.0%` | 87 | 32 | `+0.0s` |
| `2026-11-20 04:00:18` | `31.0%` | `0.0%` | 100 | 32 | `+0.0s` |
| `2026-11-20 03:30:19` | `36.28%` | `0.0%` | 113 | 33 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:22.482000+00:00`.*
