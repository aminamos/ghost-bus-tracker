# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.308000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`74.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `546` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `2` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `406` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 406 | 74.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 138 | 25.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3001** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2998** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `478879` | Route 2992 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478869` | Route 2992 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478883` | Route 2992 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478881` | Route 2992 | `12:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478862` | Route 2992 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478861` | Route 2992 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478866` | Route 2992 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478864` | Route 2992 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478863` | Route 2992 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478887` | Route 2992 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478902` | Route 2992 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478905` | Route 2992 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478904` | Route 2992 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478877` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478875` | Route 2992 | `10:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `74.36%` | `0.0%` | 546 | 2 | `+0.0s` |
| `2026-10-28 06:30:19` | `73.29%` | `0.0%` | 554 | 5 | `+0.0s` |
| `2026-10-28 06:00:19` | `72.76%` | `0.0%` | 558 | 5 | `+0.0s` |
| `2026-10-28 05:30:22` | `72.63%` | `0.0%` | 559 | 4 | `+0.0s` |
| `2026-10-28 05:00:23` | `72.63%` | `0.0%` | 559 | 2 | `+0.0s` |
| `2026-10-28 04:30:22` | `68.24%` | `0.0%` | 592 | 29 | `+0.0s` |
| `2026-10-28 04:00:21` | `12.5%` | `0.0%` | 64 | 30 | `+0.0s` |
| `2026-10-28 03:30:18` | `19.23%` | `0.0%` | 78 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.308000+00:00`.*
