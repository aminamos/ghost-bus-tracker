# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-30T07:00:22.968000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`67.82%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `432` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `293` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 293 | 67.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 138 | 31.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 127 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `478885` | Route 2992 | `13:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478887` | Route 2992 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478873` | Route 2992 | `09:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478875` | Route 2992 | `10:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478896` | Route 2992 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478898` | Route 2992 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478890` | Route 2992 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478892` | Route 2992 | `15:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478866` | Route 2992 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478869` | Route 2992 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481746` | Route 3003 | `14:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478877` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478879` | Route 2992 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478894` | Route 2992 | `16:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481729` | Route 3003 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 07:00:22` | `67.82%` | `0.0%` | 432 | 1 | `+0.0s` |
| `2026-10-30 06:30:21` | `66.59%` | `0.0%` | 440 | 4 | `+0.0s` |
| `2026-10-30 06:00:22` | `65.99%` | `0.0%` | 444 | 4 | `+0.0s` |
| `2026-10-30 05:30:22` | `65.55%` | `0.0%` | 447 | 4 | `+0.0s` |
| `2026-10-30 05:00:19` | `65.55%` | `0.0%` | 447 | 2 | `+0.0s` |
| `2026-10-30 04:30:18` | `60.21%` | `0.0%` | 485 | 29 | `+0.0s` |
| `2026-10-30 04:00:19` | `15.07%` | `0.0%` | 73 | 30 | `+0.0s` |
| `2026-10-30 03:30:18` | `23.33%` | `0.0%` | 90 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:22.968000+00:00`.*
