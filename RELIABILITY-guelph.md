# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:18.361000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`56.39%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `321` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `4` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `181` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 181 | 56.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 134 | 41.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3017** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `479050` | Route 2992 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479056` | Route 2992 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479057` | Route 2992 | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479834` | Route 2995 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479814` | Route 2995 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479833` | Route 2995 | `11:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479815` | Route 2995 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478775` | Route 2991 | `09:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478776` | Route 2991 | `09:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478777` | Route 2991 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478778` | Route 2991 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478779` | Route 2991 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479058` | Route 2992 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479813` | Route 2995 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479055` | Route 2992 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `56.39%` | `0.0%` | 321 | 4 | `+0.0s` |
| `2026-11-22 06:30:18` | `55.86%` | `0.0%` | 324 | 4 | `+0.0s` |
| `2026-11-22 06:00:17` | `56.39%` | `0.0%` | 321 | 1 | `+0.0s` |
| `2026-11-22 05:30:22` | `50.56%` | `0.0%` | 360 | 31 | `+0.0s` |
| `2026-11-22 05:00:18` | `15.28%` | `0.0%` | 72 | 33 | `+0.0s` |
| `2026-11-22 04:30:17` | `23.6%` | `0.0%` | 89 | 33 | `+0.0s` |
| `2026-11-22 04:00:17` | `30.39%` | `0.0%` | 102 | 33 | `+0.0s` |
| `2026-11-22 03:30:19` | `36.94%` | `0.0%` | 111 | 31 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.361000+00:00`.*
