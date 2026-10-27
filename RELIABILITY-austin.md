# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-27T05:00:23.446000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`94.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.32%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2007` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `267` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1897` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-7.5s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-45.0s` (`-0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 26 | 1.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 20 | 1.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1897 | 94.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 9 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 337** | 123 | 0 | 123 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 663** | 106 | 0 | 106 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 71 | 0 | 71 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 670** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 318** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 324** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 201** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+2.2 min (+129.5s)` | `+2.8 min (+167s)` | 2 | `100.0%` |
| **Route 3** | `+1.7 min (+103.0s)` | `+17.0 min (+1021s)` | 5 | `40.0%` |
| **Route 837** | `+1.4 min (+85.0s)` | `+1.4 min (+85s)` | 7 | `100.0%` |
| **Route 7** | `+0.9 min (+53.5s)` | `+4.6 min (+277s)` | 4 | `100.0%` |
| **Route 486** | `+0.3 min (+17.0s)` | `+1.9 min (+117s)` | 2 | `75.0%` |
| **Route 485** | `+0.2 min (+13.0s)` | `+0.2 min (+13s)` | 2 | `100.0%` |
| **Route 800** | `+0.0 min (+2.6s)` | `+1.2 min (+72s)` | 5 | `80.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 3** | ~30.0m | ~30.0m | **`+0.0 min`** | `70.9 / 100` |
| **Route 7** | ~17.0m | ~17.0m | **`+0.0 min`** | `86.6 / 100` |
| **Route 801** | ~10.0m | ~10.0m | **`+0.0 min`** | `82.7 / 100` |
| **Route 3** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.3 / 100` |
| **Route 800** | ~10.0m | ~10.0m | **`+0.0 min`** | `89.7 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.3 / 100` |
| **Route 800** | ~10.0m | ~10.0m | **`+0.0 min`** | `95.0 / 100` |
| **Route 1** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.8 / 100` |
| **Route 7** | ~17.0m | ~17.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 2** | ~16.0m | ~16.0m | **`+0.0 min`** | `97.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3010888_22735` | Route 800 | `23:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010790_21963` | Route 800 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003869_12225` | Route 335 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005912_15519` | Route 485 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005854_15381` | Route 483 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005972_15583` | Route 486 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005860_15338` | Route 483 | `26:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005855_15382` | Route 483 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005974_15584` | Route 486 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005861_15339` | Route 483 | `26:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005856_15390` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005977_15600` | Route 486 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005911_15520` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005862_15340` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005909_15508` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 05:00:23` | `94.52%` | `55.32%` | 2007 | 267 | `-7.5s` |
| `2026-10-27 04:30:20` | `92.13%` | `56.34%` | 2033 | 276 | `+8.7s` |
| `2026-10-27 04:00:58` | `88.79%` | `58.88%` | 2069 | 281 | `+33.6s` |
| `2026-10-27 03:30:24` | `85.67%` | `58.22%` | 2107 | 286 | `+5.7s` |
| `2026-10-27 02:30:21` | `79.06%` | `58.87%` | 2197 | 285 | `+131.5s` |
| `2026-10-27 01:30:24` | `76.07%` | `58.71%` | 2236 | 325 | `+162.1s` |
| `2026-10-27 00:31:18` | `71.67%` | `61.39%` | 2291 | 354 | `+218.1s` |
| `2026-10-26 23:00:26` | `65.47%` | `39.86%` | 2404 | 368 | `+542.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T05:00:23.446000+00:00`.*
