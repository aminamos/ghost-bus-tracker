# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-24T07:00:18.977000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`79.14%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `695` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `550` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 550 | 79.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 144 | 20.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 98 | 0 | 98 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3001** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2994** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `478866` | Route 2992 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478869` | Route 2992 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478898` | Route 2992 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479415` | Route 2994 | `13:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479432` | Route 2994 | `19:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479405` | Route 2994 | `10:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479407` | Route 2994 | `10:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479409` | Route 2994 | `11:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479411` | Route 2994 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479413` | Route 2994 | `12:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479431` | Route 2994 | `18:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478885` | Route 2992 | `13:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478883` | Route 2992 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478676` | Route 2991 | `23:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479397` | Route 2994 | `07:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:18` | `79.14%` | `0.0%` | 695 | 1 | `+0.0s` |
| `2026-11-24 06:30:19` | `78.8%` | `0.0%` | 698 | 1 | `+0.0s` |
| `2026-11-24 05:00:18` | `18.67%` | `0.0%` | 75 | 33 | `+0.0s` |
| `2026-11-24 04:30:18` | `28.42%` | `0.0%` | 95 | 33 | `+0.0s` |
| `2026-11-24 04:00:18` | `36.36%` | `0.0%` | 110 | 32 | `+0.0s` |
| `2026-11-24 03:30:21` | `42.4%` | `0.0%` | 125 | 32 | `+0.0s` |
| `2026-11-24 03:00:18` | `47.14%` | `0.0%` | 140 | 33 | `+0.0s` |
| `2026-11-24 02:30:18` | `49.69%` | `0.0%` | 159 | 35 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:18.977000+00:00`.*
