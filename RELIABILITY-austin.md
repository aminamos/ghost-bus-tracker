# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:22.809000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`47.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2159` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `228` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2108` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-12.5s` (`-0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-19.0s` (`-0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2108 | 97.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 196 | 0 | 196 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 185 | 0 | 185 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 145 | 0 | 145 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 311** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 801** | 96 | 0 | 96 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 837** | `+8.6 min (+514.0s)` | `+8.6 min (+514s)` | 1 | `0.0%` |
| **Route 485** | `+0.8 min (+45.8s)` | `+1.6 min (+95s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `88.9 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.9 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `98.6 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3014943_21698` | Route 7 | `23:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010891_23447` | Route 800 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005856_15994` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005911_16142` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005862_15932` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005909_16127` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999483_3675` | Route 20 | `03:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014878_21711` | Route 7 | `04:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1882` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21980` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999482_3676` | Route 20 | `04:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004045_12697` | Route 337 | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997877_0014` | Route 1 | `04:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001189_6959` | Route 300 | `04:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004336_13343` | Route 339 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:22` | `97.64%` | `47.62%` | 2159 | 228 | `-12.5s` |
| `2026-11-17 06:30:19` | `96.72%` | `52.78%` | 2167 | 248 | `-12.0s` |
| `2026-11-17 06:00:24` | `95.14%` | `59.65%` | 2181 | 260 | `-2.7s` |
| `2026-11-17 05:30:21` | `93.13%` | `56.32%` | 2199 | 279 | `-37.9s` |
| `2026-11-17 05:00:20` | `89.62%` | `60.74%` | 2236 | 285 | `-23.8s` |
| `2026-11-17 04:30:24` | `86.66%` | `61.99%` | 2272 | 289 | `-33.4s` |
| `2026-11-17 04:00:22` | `83.51%` | `61.79%` | 2316 | 302 | `-34.3s` |
| `2026-11-17 03:30:25` | `80.59%` | `65.86%` | 2354 | 298 | `-16.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:22.809000+00:00`.*
