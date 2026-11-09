# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.223000+00:00` | **Source:** live GTFS-RT feed

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
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `478876` | Route 2992 | `10:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478878` | Route 2992 | `11:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478880` | Route 2992 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478882` | Route 2992 | `12:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481743` | Route 3003 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481741` | Route 3003 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481739` | Route 3003 | `07:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481737` | Route 3003 | `08:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481747` | Route 3003 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481749` | Route 3003 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481751` | Route 3003 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481753` | Route 3003 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481755` | Route 3003 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481757` | Route 3003 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481759` | Route 3003 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `69.68%` | `0.0%` | 475 | 0 | `+0.0s` |
| `2026-11-09 06:30:20` | `69.25%` | `0.0%` | 478 | 0 | `+0.0s` |
| `2026-11-09 06:00:18` | `68.39%` | `0.0%` | 484 | 2 | `+0.0s` |
| `2026-11-09 05:30:18` | `67.83%` | `0.0%` | 488 | 2 | `+0.0s` |
| `2026-11-09 05:00:18` | `0.0%` | `0.0%` | 5 | 2 | `+0.0s` |
| `2026-11-09 04:30:18` | `0.0%` | `0.0%` | 8 | 2 | `+0.0s` |
| `2026-11-09 04:00:18` | `0.0%` | `0.0%` | 11 | 2 | `+0.0s` |
| `2026-11-09 03:30:17` | `0.0%` | `0.0%` | 16 | 5 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.223000+00:00`.*
