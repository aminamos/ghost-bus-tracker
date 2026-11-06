# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:18.033000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`65.4%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `448` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `6` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 293 | 65.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 145 | 32.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3019** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3017** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3032** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `481474` | Route 3002 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480224` | Route 2997 | `06:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481472` | Route 3002 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480222` | Route 2997 | `05:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481509` | Route 3002 | `24:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480242` | Route 2997 | `15:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481490` | Route 3002 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480240` | Route 2997 | `14:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481488` | Route 3002 | `14:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480238` | Route 2997 | `13:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478901` | Route 2992 | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478900` | Route 2992 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478903` | Route 2992 | `20:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478902` | Route 2992 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478905` | Route 2992 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `65.4%` | `0.0%` | 448 | 6 | `+0.0s` |
| `2026-11-06 06:30:18` | `65.26%` | `0.0%` | 449 | 5 | `+0.0s` |
| `2026-11-06 06:00:18` | `65.62%` | `0.0%` | 445 | 2 | `+0.0s` |
| `2026-11-06 05:30:21` | `60.58%` | `0.0%` | 482 | 30 | `+0.0s` |
| `2026-11-06 05:00:18` | `11.43%` | `0.0%` | 70 | 32 | `+0.0s` |
| `2026-11-06 04:30:19` | `17.86%` | `0.0%` | 84 | 32 | `+0.0s` |
| `2026-11-06 04:00:21` | `23.4%` | `0.0%` | 94 | 32 | `+0.0s` |
| `2026-11-06 03:30:19` | `27.88%` | `0.0%` | 104 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.033000+00:00`.*
