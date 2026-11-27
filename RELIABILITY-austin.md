# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:23.559000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1407` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `155` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1407` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1407 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 800** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2999804_4043` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998359_1384` | Route 10 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001446_7406` | Route 300 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000943_5911` | Route 3 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999805_4044` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010537_22394` | Route 7 | `05:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010595_21859` | Route 7 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003816_11452` | Route 333 | `05:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012046_25571` | Route 803 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998451_0854` | Route 10 | `05:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013675_2935` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013708_2534` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999660_3455` | Route 20 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000755_5098` | Route 271 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000968_5620` | Route 3 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:23` | `100.0%` | `0.0%` | 1407 | 155 | `+0.0s` |
| `2026-11-27 06:30:20` | `99.65%` | `0.0%` | 1410 | 163 | `+431.5s` |
| `2026-11-27 06:00:27` | `99.15%` | `25.0%` | 1416 | 175 | `-107.8s` |
| `2026-11-27 05:30:21` | `97.76%` | `46.15%` | 1430 | 180 | `+99.9s` |
| `2026-11-27 05:00:19` | `95.4%` | `56.67%` | 1457 | 187 | `+13.3s` |
| `2026-11-27 04:30:31` | `91.9%` | `59.26%` | 1494 | 192 | `-7.0s` |
| `2026-11-27 04:00:21` | `88.22%` | `66.27%` | 1528 | 196 | `-11.7s` |
| `2026-11-27 03:30:24` | `84.39%` | `71.05%` | 1563 | 197 | `+6.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:23.559000+00:00`.*
