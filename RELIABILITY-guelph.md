# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:19.163000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`74.41%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `594` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `4` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `442` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 442 | 74.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 144 | 24.2% |

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
| **Route 2999** | 28 | 0 | 28 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `478665` | Route 2991 | `17:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478664` | Route 2991 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478878` | Route 2992 | `11:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478876` | Route 2992 | `10:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478874` | Route 2992 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478872` | Route 2992 | `09:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478901` | Route 2992 | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478900` | Route 2992 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478672` | Route 2991 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478663` | Route 2991 | `16:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478880` | Route 2992 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478875` | Route 2992 | `10:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478873` | Route 2992 | `09:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478871` | Route 2992 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478869` | Route 2992 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:19` | `74.41%` | `0.0%` | 594 | 4 | `+0.0s` |
| `2026-11-27 06:30:19` | `74.29%` | `0.0%` | 595 | 3 | `+0.0s` |
| `2026-11-27 06:00:17` | `74.29%` | `0.0%` | 595 | 2 | `+0.0s` |
| `2026-11-27 05:30:19` | `69.84%` | `0.0%` | 630 | 30 | `+0.0s` |
| `2026-11-27 05:00:17` | `15.94%` | `0.0%` | 69 | 31 | `+0.0s` |
| `2026-11-27 04:30:18` | `24.18%` | `0.0%` | 91 | 32 | `+0.0s` |
| `2026-11-27 04:00:17` | `30.19%` | `0.0%` | 106 | 32 | `+0.0s` |
| `2026-11-27 03:30:18` | `34.43%` | `0.0%` | 122 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:19.163000+00:00`.*
