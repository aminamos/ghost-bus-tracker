# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.703000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`73.55%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `518` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `2` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `381` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 381 | 73.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 133 | 25.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2995** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3032** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `478735` | Route 2991 | `14:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478973` | Route 2992 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478974` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478975` | Route 2992 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478976` | Route 2992 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478991` | Route 2992 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478992` | Route 2992 | `20:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478718` | Route 2991 | `06:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478719` | Route 2991 | `06:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478720` | Route 2991 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478721` | Route 2991 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478722` | Route 2991 | `08:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478723` | Route 2991 | `08:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478724` | Route 2991 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `478725` | Route 2991 | `09:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `73.55%` | `0.0%` | 518 | 2 | `+0.0s` |
| `2026-11-21 06:30:23` | `73.41%` | `0.0%` | 519 | 1 | `+0.0s` |
| `2026-11-21 06:00:18` | `72.85%` | `0.0%` | 523 | 2 | `+0.0s` |
| `2026-11-21 05:30:18` | `68.52%` | `0.0%` | 559 | 30 | `+0.0s` |
| `2026-11-21 05:00:19` | `14.86%` | `0.0%` | 74 | 33 | `+0.0s` |
| `2026-11-21 04:30:18` | `23.08%` | `0.0%` | 91 | 33 | `+0.0s` |
| `2026-11-21 04:00:17` | `28.7%` | `0.0%` | 108 | 35 | `+0.0s` |
| `2026-11-21 03:30:18` | `35.65%` | `0.0%` | 115 | 33 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.703000+00:00`.*
