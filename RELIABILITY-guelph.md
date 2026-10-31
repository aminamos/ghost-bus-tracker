# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:22.287000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`67.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `397` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `3` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `267` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 267 | 67.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 127 | 32.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 127 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `478727` | Route 2991 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478724` | Route 2991 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478726` | Route 2991 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478725` | Route 2991 | `09:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483868` | Route 3013 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483867` | Route 3013 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `483866` | Route 3013 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478747` | Route 2991 | `20:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478746` | Route 2991 | `20:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478745` | Route 2991 | `19:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478744` | Route 2991 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478748` | Route 2991 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478754` | Route 2991 | `24:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478740` | Route 2991 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478739` | Route 2991 | `16:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:22` | `67.25%` | `0.0%` | 397 | 3 | `+0.0s` |
| `2026-10-31 06:00:19` | `65.28%` | `0.0%` | 409 | 5 | `+0.0s` |
| `2026-10-31 05:30:19` | `65.12%` | `0.0%` | 410 | 4 | `+0.0s` |
| `2026-10-31 05:00:22` | `64.96%` | `0.0%` | 411 | 4 | `+0.0s` |
| `2026-10-31 04:30:20` | `60.22%` | `0.0%` | 445 | 29 | `+0.0s` |
| `2026-10-31 04:00:17` | `11.59%` | `0.0%` | 69 | 30 | `+0.0s` |
| `2026-10-31 03:30:17` | `18.52%` | `0.0%` | 81 | 30 | `+0.0s` |
| `2026-10-31 02:30:18` | `30.0%` | `0.0%` | 100 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:22.287000+00:00`.*
