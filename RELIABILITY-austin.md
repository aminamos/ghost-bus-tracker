# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:24.542000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.87%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `337` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `225` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `286` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-56.2s` (`-0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-58.5s` (`-1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 5 | 1.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 1.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 286 | 84.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 127 | 0 | 127 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 311** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 935** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 837** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | `+0.6 min (+36.0s)` | `+1.6 min (+98s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 484** | ~45.0m | ~45.0m | **`+0.0 min`** | `98.5 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 484** | ~45.0m | ~45.0m | **`+0.0 min`** | `97.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3014944_0990` | Route 10 | `04:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014945_0991` | Route 10 | `04:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3015008_0463` | Route 10 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014392_7873` | Route 311 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013899_9892` | Route 322 | `05:04:16` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014946_0992` | Route 10 | `05:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3015009_0464` | Route 10 | `05:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014393_7874` | Route 311 | `05:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014947_0993` | Route 10 | `05:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3015010_0465` | Route 10 | `05:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998856_1609` | Route 18 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013900_9893` | Route 322 | `05:39:16` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014394_7875` | Route 311 | `05:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014948_0994` | Route 10 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3015011_0466` | Route 10 | `05:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:24` | `84.87%` | `50.0%` | 337 | 225 | `-56.2s` |
| `2026-11-13 06:30:19` | `79.94%` | `58.33%` | 359 | 239 | `-70.5s` |
| `2026-11-13 05:30:23` | `64.0%` | `43.48%` | 425 | 277 | `-61.8s` |
| `2026-11-13 05:00:22` | `54.33%` | `58.06%` | 497 | 284 | `-50.2s` |
| `2026-11-13 04:30:21` | `39.46%` | `73.53%` | 517 | 292 | `-32.9s` |
| `2026-11-13 04:00:23` | `26.48%` | `66.67%` | 525 | 305 | `-47.2s` |
| `2026-11-13 03:30:27` | `22.57%` | `73.91%` | 607 | 302 | `-23.9s` |
| `2026-11-13 03:00:26` | `21.43%` | `73.47%` | 644 | 312 | `+2.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:24.542000+00:00`.*
