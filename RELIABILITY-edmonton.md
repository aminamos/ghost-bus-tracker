# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** Edmonton | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:41.005000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`51.4%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.15%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1541` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `399` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `792` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+92.2s` (`+1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+34.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 562 | 36.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 80 | 5.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 52 | 3.4% |
| 🔴 **Severe Delay** | Over 15m late | 16 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 792 | 51.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 150X** | 9 | 0 | 9 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 671** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 917** | 51 | 3 | 47 | **`92.16%`** | `100.0%` | `-17.8s` |
| **Route 713** | 23 | 1 | 21 | **`91.3%`** | `100.0%` | `+2.0 min` |
| **Route 112** | 41 | 2 | 37 | **`90.24%`** | `66.67%` | `+3.4 min` |
| **Route 106** | 71 | 5 | 64 | **`90.14%`** | `71.43%` | `-27.3s` |
| **Route 924** | 9 | 1 | 8 | **`88.89%`** | `0.0%` | `+7.0 min` |
| **Route 124** | 52 | 4 | 46 | **`88.46%`** | `66.67%` | `+0.9 min` |
| **Route 560** | 17 | 2 | 15 | **`88.24%`** | `50.0%` | `+3.9 min` |
| **Route 916** | 57 | 4 | 50 | **`87.72%`** | `50.0%` | `+2.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 712** | `+30.8 min (+1846.7s)` | `+49.9 min (+2996s)` | 2 | `33.33%` |
| **Route A7** | `+18.9 min (+1134.5s)` | `+33.1 min (+1986s)` | 2 | `50.0%` |
| **Route 721** | `+18.3 min (+1095.8s)` | `+24.4 min (+1463s)` | 3 | `0.0%` |
| **Route 613** | `+17.9 min (+1073.0s)` | `+28.6 min (+1718s)` | 2 | `0.0%` |
| **Route 684** | `+17.3 min (+1037.5s)` | `+29.5 min (+1770s)` | 2 | `0.0%` |
| **Route 618** | `+14.5 min (+869.0s)` | `+14.5 min (+869s)` | 1 | `0.0%` |
| **Route 722** | `+13.2 min (+791.0s)` | `+23.4 min (+1407s)` | 4 | `16.67%` |
| **Route 616** | `+10.8 min (+647.0s)` | `+10.8 min (+647s)` | 1 | `0.0%` |
| **Route 109** | `+7.8 min (+469.2s)` | `+16.7 min (+1001s)` | 4 | `37.5%` |
| **Route 440** | `+7.4 min (+442.0s)` | `+7.4 min (+442s)` | 1 | `0.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 683** | ~3.0m | ~3.0m | **`+1.7 min`** | `0.0 / 100` |
| **Route 684** | ~5.0m | ~5.0m | **`+0.2 min`** | `0.0 / 100` |
| **Route 712** | ~30.0m | ~30.0m | **`+0.1 min`** | `29.1 / 100` |
| **Route 705** | ~30.0m | ~30.0m | **`+0.1 min`** | `46.9 / 100` |
| **Route 110X** | ~15.0m | ~15.0m | **`+0.0 min`** | `41.4 / 100` |
| **Route A7** | ~60.0m | ~60.0m | **`+0.0 min`** | `76.3 / 100` |
| **Route 722** | ~20.0m | ~20.0m | **`+0.0 min`** | `62.1 / 100` |
| **Route 114** | ~15.0m | ~15.0m | **`+0.0 min`** | `58.0 / 100` |
| **Route 004** | ~12.0m | ~12.0m | **`+0.0 min`** | `53.8 / 100` |
| **Route 722** | ~20.0m | ~20.0m | **`+0.0 min`** | `64.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33126141` | Route 613 | `14:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762974` | Route 709 | `22:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762966` | Route 709 | `22:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762967` | Route 709 | `23:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762968` | Route 709 | `23:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762972` | Route 709 | `24:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32759143` | Route 705 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32759144` | Route 705 | `17:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32758697` | Route 112 | `18:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32758710` | Route 112 | `15:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32755699` | Route 701 | `13:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33997397` | Route 729 | `18:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33997350` | Route 729 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33997402` | Route 729 | `20:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33997355` | Route 729 | `21:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:41.005000+00:00`.*
