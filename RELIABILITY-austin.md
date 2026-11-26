# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:26.580000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1440` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `223` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1389` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-43.8s` (`-0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-31.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 9 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1389 | 96.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 96 | 0 | 96 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | `+0.1 min (+5.0s)` | `+1.3 min (+79s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `97.7 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |

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
| `2999806_4107` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011617_24256` | Route 801 | `05:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998013_0076` | Route 1 | `05:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998364_1430` | Route 10 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001460_7465` | Route 300 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000943_5911` | Route 3 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001143_6393` | Route 30 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999807_4115` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010555_22453` | Route 7 | `05:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:26` | `96.46%` | `60.0%` | 1440 | 223 | `-43.8s` |
| `2026-11-26 06:30:23` | `95.15%` | `52.0%` | 1465 | 245 | `-75.2s` |
| `2026-11-26 06:00:21` | `93.07%` | `59.09%` | 1500 | 257 | `-30.7s` |
| `2026-11-26 05:30:26` | `90.25%` | `58.33%` | 1548 | 270 | `-24.5s` |
| `2026-11-26 05:00:19` | `87.38%` | `61.22%` | 1600 | 274 | `-42.6s` |
| `2026-11-26 04:30:24` | `84.07%` | `65.44%` | 1657 | 283 | `-30.6s` |
| `2026-11-26 04:00:25` | `80.83%` | `65.88%` | 1701 | 295 | `-39.6s` |
| `2026-11-26 03:30:21` | `78.01%` | `65.48%` | 1742 | 291 | `-39.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:26.580000+00:00`.*
