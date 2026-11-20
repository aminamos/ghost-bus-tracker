# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T06:30:25.648000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.93%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`53.57%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2282` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `247` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2212` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+3.9s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-36.0s` (`-0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2212 | 96.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 145 | 0 | 145 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 311** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 670** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 3** | `+3.5 min (+208.0s)` | `+14.9 min (+895s)` | 3 | `0.0%` |
| **Route 485** | `+0.9 min (+54.3s)` | `+1.8 min (+105s)` | 3 | `100.0%` |
| **Route 7** | `+0.1 min (+6.5s)` | `+0.8 min (+49s)` | 2 | `100.0%` |
| **Route 10** | `+0.1 min (+6.0s)` | `+0.1 min (+6s)` | 2 | `100.0%` |
| **Route 483** | `+0.1 min (+5.6s)` | `+6.5 min (+393s)` | 3 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 801** | ~10.0m | ~10.0m | **`+0.0 min`** | `69.8 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `88.4 / 100` |
| **Route 800** | ~10.0m | ~10.0m | **`+0.0 min`** | `86.8 / 100` |
| **Route 3** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.5 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `98.3 / 100` |

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
| `3014944_0948` | Route 10 | `04:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1882` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21980` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 06:30:25` | `96.93%` | `53.57%` | 2282 | 247 | `+3.9s` |
| `2026-11-20 06:00:23` | `95.28%` | `62.5%` | 2246 | 261 | `+19.7s` |
| `2026-11-20 05:30:22` | `93.15%` | `58.44%` | 2262 | 278 | `-30.2s` |
| `2026-11-20 05:00:23` | `89.97%` | `54.39%` | 2294 | 284 | `+100.8s` |
| `2026-11-20 04:30:19` | `86.73%` | `53.95%` | 2329 | 290 | `+86.7s` |
| `2026-11-20 04:00:19` | `84.06%` | `55.38%` | 2365 | 298 | `+109.1s` |
| `2026-11-20 03:30:21` | `80.75%` | `61.26%` | 2410 | 296 | `+64.6s` |
| `2026-11-20 03:00:22` | `78.93%` | `58.4%` | 2435 | 304 | `+83.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:25.648000+00:00`.*
