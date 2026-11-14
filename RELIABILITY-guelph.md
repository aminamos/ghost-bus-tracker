# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:18.821000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`70.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `541` | Total runs operating in current transit schedule window |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 381 | 70.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 154 | 28.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `478747` | Route 2991 | `20:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478746` | Route 2991 | `20:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478749` | Route 2991 | `21:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478748` | Route 2991 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478751` | Route 2991 | `22:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478750` | Route 2991 | `22:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478724` | Route 2991 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478723` | Route 2991 | `08:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478729` | Route 2991 | `11:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478973` | Route 2992 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478728` | Route 2991 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478727` | Route 2991 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478726` | Route 2991 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478725` | Route 2991 | `09:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478732` | Route 2991 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:18` | `70.43%` | `0.0%` | 541 | 3 | `+0.0s` |
| `2026-11-14 06:30:19` | `70.3%` | `0.0%` | 542 | 2 | `+0.0s` |
| `2026-11-14 06:00:19` | `69.91%` | `0.0%` | 545 | 3 | `+0.0s` |
| `2026-11-14 05:30:18` | `65.69%` | `0.0%` | 583 | 31 | `+0.0s` |
| `2026-11-14 05:00:20` | `14.86%` | `0.0%` | 74 | 32 | `+0.0s` |
| `2026-11-14 04:30:18` | `23.08%` | `0.0%` | 91 | 32 | `+0.0s` |
| `2026-11-14 04:00:20` | `29.81%` | `0.0%` | 104 | 32 | `+0.0s` |
| `2026-11-14 03:30:18` | `35.04%` | `0.0%` | 117 | 33 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:18.821000+00:00`.*
