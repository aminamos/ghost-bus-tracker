# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:18.758000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`57.59%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `349` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `4` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `201` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 201 | 57.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 140 | 40.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3019** | 5 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `479848` | Route 2995 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479828` | Route 2995 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479847` | Route 2995 | `18:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479827` | Route 2995 | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479846` | Route 2995 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479826` | Route 2995 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479845` | Route 2995 | `17:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479040` | Route 2992 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479039` | Route 2992 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478780` | Route 2991 | `11:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478779` | Route 2991 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478778` | Route 2991 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478777` | Route 2991 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479825` | Route 2995 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478781` | Route 2991 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `57.59%` | `0.0%` | 349 | 4 | `+0.0s` |
| `2026-11-15 06:30:18` | `56.46%` | `0.0%` | 356 | 4 | `+0.0s` |
| `2026-11-15 06:00:22` | `56.94%` | `0.0%` | 353 | 1 | `+0.0s` |
| `2026-11-15 05:30:19` | `52.2%` | `0.0%` | 387 | 29 | `+0.0s` |
| `2026-11-15 05:00:18` | `16.18%` | `0.0%` | 68 | 30 | `+0.0s` |
| `2026-11-15 04:30:18` | `25.3%` | `0.0%` | 83 | 29 | `+0.0s` |
| `2026-11-15 04:00:18` | `32.29%` | `0.0%` | 96 | 29 | `+0.0s` |
| `2026-11-15 03:30:18` | `39.05%` | `0.0%` | 105 | 27 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.758000+00:00`.*
