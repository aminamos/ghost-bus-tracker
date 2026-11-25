# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.824000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`75.41%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `614` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `4` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `463` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 463 | 75.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 144 | 23.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3001** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2994** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2999** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `478645` | Route 2991 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478652` | Route 2991 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478653` | Route 2991 | `11:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478654` | Route 2991 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478882` | Route 2992 | `12:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478884` | Route 2992 | `13:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478886` | Route 2992 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478888` | Route 2992 | `14:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478875` | Route 2992 | `10:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478877` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478879` | Route 2992 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478901` | Route 2992 | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478902` | Route 2992 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478903` | Route 2992 | `20:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478904` | Route 2992 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `75.41%` | `0.0%` | 614 | 4 | `+0.0s` |
| `2026-11-25 06:30:19` | `75.28%` | `0.0%` | 615 | 3 | `+0.0s` |
| `2026-11-25 06:00:19` | `74.88%` | `0.0%` | 617 | 3 | `+0.0s` |
| `2026-11-25 05:30:18` | `69.92%` | `0.0%` | 655 | 32 | `+0.0s` |
| `2026-11-25 05:00:17` | `16.67%` | `0.0%` | 72 | 33 | `+0.0s` |
| `2026-11-25 04:30:17` | `25.56%` | `0.0%` | 90 | 33 | `+0.0s` |
| `2026-11-25 04:00:18` | `33.01%` | `0.0%` | 103 | 32 | `+0.0s` |
| `2026-11-25 03:30:20` | `39.82%` | `0.0%` | 113 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.824000+00:00`.*
