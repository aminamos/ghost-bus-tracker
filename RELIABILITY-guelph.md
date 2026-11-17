# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:20.932000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`74.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `574` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 429 | 74.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 144 | 25.1% |

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
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 133 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `478644` | Route 2991 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478645` | Route 2991 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478646` | Route 2991 | `08:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478647` | Route 2991 | `08:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478881` | Route 2992 | `12:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478883` | Route 2992 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478885` | Route 2992 | `13:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478908` | Route 2992 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478909` | Route 2992 | `23:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478910` | Route 2992 | `23:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478911` | Route 2992 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478893` | Route 2992 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478895` | Route 2992 | `16:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478897` | Route 2992 | `17:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478655` | Route 2991 | `12:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:20` | `74.74%` | `0.0%` | 574 | 1 | `+0.0s` |
| `2026-11-17 06:30:18` | `74.35%` | `0.0%` | 577 | 1 | `+0.0s` |
| `2026-11-17 06:00:20` | `73.84%` | `0.0%` | 581 | 1 | `+0.0s` |
| `2026-11-17 05:30:19` | `69.21%` | `0.0%` | 617 | 29 | `+0.0s` |
| `2026-11-17 05:00:18` | `15.94%` | `0.0%` | 69 | 30 | `+0.0s` |
| `2026-11-17 04:30:19` | `24.42%` | `0.0%` | 86 | 30 | `+0.0s` |
| `2026-11-17 04:00:18` | `31.31%` | `0.0%` | 99 | 30 | `+0.0s` |
| `2026-11-17 03:30:20` | `36.94%` | `0.0%` | 111 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:20.932000+00:00`.*
