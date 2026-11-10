# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-10T07:00:18.496000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`69.68%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `475` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `331` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 331 | 69.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 144 | 30.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 133 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `478671` | Route 2991 | `20:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478670` | Route 2991 | `20:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478675` | Route 2991 | `22:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478674` | Route 2991 | `22:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478673` | Route 2991 | `21:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478672` | Route 2991 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478878` | Route 2992 | `11:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478876` | Route 2992 | `10:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478883` | Route 2992 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478881` | Route 2992 | `12:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478879` | Route 2992 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478877` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478875` | Route 2992 | `10:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478873` | Route 2992 | `09:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478871` | Route 2992 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:18` | `69.68%` | `0.0%` | 475 | 0 | `+0.0s` |
| `2026-11-10 06:30:18` | `69.25%` | `0.0%` | 478 | 0 | `+0.0s` |
| `2026-11-10 06:00:17` | `68.39%` | `0.0%` | 484 | 2 | `+0.0s` |
| `2026-11-10 05:30:19` | `63.46%` | `0.0%` | 520 | 30 | `+0.0s` |
| `2026-11-10 05:00:18` | `13.04%` | `0.0%` | 69 | 32 | `+0.0s` |
| `2026-11-10 04:30:18` | `20.24%` | `0.0%` | 84 | 32 | `+0.0s` |
| `2026-11-10 04:00:18` | `26.32%` | `0.0%` | 95 | 32 | `+0.0s` |
| `2026-11-10 03:30:18` | `31.73%` | `0.0%` | 104 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:18.496000+00:00`.*
