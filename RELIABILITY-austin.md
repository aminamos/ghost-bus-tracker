# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:21.232000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.77%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`27.27%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1515` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `177` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1466` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+467.0s` (`+7.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+515.0s` (`+8.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 0.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 0.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1466 | 96.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 311** | 94 | 0 | 94 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | `+14.6 min (+876.0s)` | `+18.1 min (+1086s)` | 3 | `0.0%` |
| **Route 486** | `+8.6 min (+513.6s)` | `+12.4 min (+746s)` | 2 | `20.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `86.4 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `88.1 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.8 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2999804_4043` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998359_1384` | Route 10 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001446_7406` | Route 300 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000943_5911` | Route 3 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002053_8461` | Route 311 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004461_13449` | Route 339 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999805_4044` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010537_22394` | Route 7 | `05:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010595_21859` | Route 7 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003816_11452` | Route 333 | `05:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012046_25571` | Route 803 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013675_2935` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013708_2534` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999660_3455` | Route 20 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000755_5098` | Route 271 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:21` | `96.77%` | `27.27%` | 1515 | 177 | `+467.0s` |
| `2026-11-15 06:30:19` | `95.82%` | `42.86%` | 1530 | 188 | `+283.2s` |
| `2026-11-15 05:30:20` | `91.67%` | `40.0%` | 1597 | 214 | `+362.3s` |
| `2026-11-15 05:00:22` | `88.92%` | `41.18%` | 1642 | 220 | `+335.3s` |
| `2026-11-15 04:30:21` | `85.91%` | `61.11%` | 1689 | 219 | `+178.8s` |
| `2026-11-15 04:00:20` | `82.25%` | `54.55%` | 1741 | 224 | `+202.5s` |
| `2026-11-15 03:30:19` | `79.55%` | `65.0%` | 1770 | 222 | `+157.2s` |
| `2026-11-15 03:00:22` | `77.7%` | `57.14%` | 1771 | 230 | `+310.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:21.232000+00:00`.*
