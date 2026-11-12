# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-12T07:00:19.270000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`74.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `578` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `3` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 429 | 74.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 145 | 25.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 98 | 0 | 98 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `484051` | Route 3014 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484053` | Route 3014 | `23:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484052` | Route 3014 | `23:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484054` | Route 3014 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478644` | Route 2991 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478645` | Route 2991 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478641` | Route 2991 | `05:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478642` | Route 2991 | `06:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478643` | Route 2991 | `06:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478675` | Route 2991 | `22:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478878` | Route 2992 | `11:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478880` | Route 2992 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478890` | Route 2992 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478892` | Route 2992 | `15:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478894` | Route 2992 | `16:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:19` | `74.22%` | `0.0%` | 578 | 3 | `+0.0s` |
| `2026-11-12 06:30:18` | `73.97%` | `0.0%` | 580 | 3 | `+0.0s` |
| `2026-11-12 06:00:18` | `73.71%` | `0.0%` | 582 | 2 | `+0.0s` |
| `2026-11-12 05:30:18` | `69.04%` | `0.0%` | 617 | 30 | `+0.0s` |
| `2026-11-12 05:00:18` | `16.18%` | `0.0%` | 68 | 30 | `+0.0s` |
| `2026-11-12 04:30:18` | `24.14%` | `0.0%` | 87 | 31 | `+0.0s` |
| `2026-11-12 04:00:18` | `31.0%` | `0.0%` | 100 | 31 | `+0.0s` |
| `2026-11-12 03:30:18` | `36.28%` | `0.0%` | 113 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:19.270000+00:00`.*
