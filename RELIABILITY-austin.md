# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-18T06:30:23.837000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.77%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2164` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `242` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2094` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+244.1s` (`+4.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-19.0s` (`-0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 21 | 1.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2094 | 96.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 145 | 0 | 145 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 311** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 670** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 663** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 2** | `+47.8 min (+2866.0s)` | `+58.3 min (+3499s)` | 2 | `0.0%` |
| **Route 800** | `+10.4 min (+621.2s)` | `+44.5 min (+2669s)` | 4 | `50.0%` |
| **Route 3** | `+6.5 min (+387.0s)` | `+22.7 min (+1364s)` | 3 | `33.33%` |
| **Route 30** | `+1.3 min (+79.0s)` | `+1.3 min (+79s)` | 1 | `100.0%` |
| **Route 485** | `+0.9 min (+52.3s)` | `+1.7 min (+104s)` | 3 | `100.0%` |
| **Route 837** | `+0.5 min (+29.3s)` | `+3.1 min (+184s)` | 2 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 800** | ~10.0m | ~10.0m | **`+0.4 min`** | `0.0 / 100` |
| **Route 2** | ~16.0m | ~16.0m | **`+0.1 min`** | `34.1 / 100` |
| **Route 800** | ~10.0m | ~10.0m | **`+0.0 min`** | `83.3 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 3** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.9 / 100` |
| **Route 837** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.9 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `98.3 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3014942_21697` | Route 7 | `23:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011744_25242` | Route 803 | `23:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014750_15365` | Route 4 | `24:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005855_15981` | Route 483 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005910_16126` | Route 485 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005861_15931` | Route 483 | `26:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005856_15994` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005911_16142` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005862_15932` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005909_16127` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999483_3675` | Route 20 | `03:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014878_21711` | Route 7 | `04:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1882` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21980` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999482_3676` | Route 20 | `04:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 06:30:23` | `96.77%` | `60.0%` | 2164 | 242 | `+244.1s` |
| `2026-11-18 05:30:30` | `93.31%` | `55.56%` | 2196 | 269 | `+46.7s` |
| `2026-11-18 05:00:23` | `89.87%` | `60.58%` | 2230 | 276 | `+21.0s` |
| `2026-11-18 04:30:22` | `86.46%` | `61.8%` | 2274 | 284 | `+23.1s` |
| `2026-11-18 04:00:21` | `83.34%` | `61.21%` | 2317 | 290 | `+6.7s` |
| `2026-11-18 03:30:19` | `80.79%` | `63.27%` | 2353 | 297 | `+6.6s` |
| `2026-11-18 03:00:26` | `78.76%` | `62.6%` | 2387 | 308 | `+28.1s` |
| `2026-11-18 02:00:28` | `75.63%` | `54.55%` | 2413 | 330 | `+208.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:23.837000+00:00`.*
