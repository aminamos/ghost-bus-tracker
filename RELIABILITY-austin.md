# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** Austin | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:44.223000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`61.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.65%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2474` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `411` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1523` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+25.0s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-27.5s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 404 | 16.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 264 | 10.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 45 | 1.8% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1523 | 61.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 223 | 9.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 483** | 14 | 0 | 14 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 71 | 3 | 61 | **`85.92%`** | `90.0%` | `+0.1 min` |
| **Route 466** | 27 | 1 | 23 | **`85.19%`** | `100.0%` | `-22.0s` |
| **Route 322** | 60 | 2 | 51 | **`85.0%`** | `77.78%` | `+0.1 min` |
| **Route 18** | 74 | 5 | 62 | **`83.78%`** | `75.0%` | `-25.8s` |
| **Route 20** | 145 | 7 | 115 | **`79.31%`** | `71.43%` | `+4.1 min` |
| **Route 2** | 120 | 7 | 95 | **`79.17%`** | `50.0%` | `-1.3s` |
| **Route 337** | 123 | 8 | 97 | **`78.86%`** | `80.95%` | `-26.3s` |
| **Route 271** | 43 | 3 | 33 | **`76.74%`** | `60.0%` | `-19.3s` |
| **Route 335** | 43 | 3 | 33 | **`76.74%`** | `40.0%` | `-76.2s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 663** | `+23.8 min (+1427.9s)` | `+60.4 min (+3622s)` | 3 | `16.67%` |
| **Route 20** | `+4.1 min (+243.2s)` | `+13.3 min (+799s)` | 7 | `71.43%` |
| **Route 392** | `+3.3 min (+196.8s)` | `+15.7 min (+941s)` | 4 | `44.44%` |
| **Route 350** | `+1.8 min (+108.1s)` | `+13.2 min (+792s)` | 4 | `66.67%` |
| **Route 345** | `+1.3 min (+80.7s)` | `+8.3 min (+497s)` | 1 | `70.0%` |
| **Route 803** | `+1.3 min (+80.4s)` | `+23.9 min (+1437s)` | 15 | `23.53%` |
| **Route 333** | `+1.1 min (+64.9s)` | `+12.3 min (+740s)` | 11 | `81.82%` |
| **Route 228** | `+0.9 min (+57.0s)` | `+4.8 min (+289s)` | 2 | `87.5%` |
| **Route 3** | `+0.7 min (+39.7s)` | `+14.3 min (+861s)` | 8 | `35.71%` |
| **Route 339** | `+0.6 min (+34.3s)` | `+9.6 min (+576s)` | 3 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 663** | ~20.0m | ~20.0m | **`+0.2 min`** | `0.0 / 100` |
| **Route 663** | ~20.0m | ~20.0m | **`+0.2 min`** | `0.0 / 100` |
| **Route 803** | ~11.0m | ~11.0m | **`+0.1 min`** | `19.3 / 100` |
| **Route 640** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 803** | ~11.0m | ~11.0m | **`+0.0 min`** | `50.4 / 100` |
| **Route 801** | ~10.0m | ~10.0m | **`+0.0 min`** | `54.7 / 100` |
| **Route 801** | ~9.5m | ~9.5m | **`+0.0 min`** | `60.7 / 100` |
| **Route 3** | ~30.0m | ~30.0m | **`+0.0 min`** | `78.5 / 100` |
| **Route 20** | ~15.0m | ~15.0m | **`+0.0 min`** | `70.8 / 100` |
| **Route 392** | ~35.0m | ~35.0m | **`+0.0 min`** | `81.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3014842_21328` | Route 7 | `12:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010812_21951` | Route 800 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014363_8513` | Route 311 | `13:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001634_7623` | Route 310 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013914_10028` | Route 322 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014721_14879` | Route 4 | `13:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014979_1060` | Route 10 | `13:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014981_1062` | Route 10 | `14:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011328_23254` | Route 801 | `15:04:00` | `SCHEDULED` | Assigned vehicle block_801072_schedBasedVehicle is missing from active GPS transponder fleet |
| `3014730_14753` | Route 4 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003670_11391` | Route 333 | `16:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004077_12931` | Route 337 | `16:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3009090_19740` | Route 663 | `16:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010872_22646` | Route 800 | `16:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014987_1066` | Route 10 | `16:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:44.223000+00:00`.*
