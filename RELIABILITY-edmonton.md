# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:19.432000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.38%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `73` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `36` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+46.0s` (`+0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+13.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 46.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 17.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 6.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 16.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+6.4 min` |
| **Route 004** | 14 | 6 | 4 | **`28.57%`** | `90.0%` | `+0.2 min` |
| **Route 002** | 15 | 7 | 3 | **`20.0%`** | `90.0%` | `+2.3 min` |
| **Route 009** | 13 | 6 | 2 | **`15.38%`** | `100.0%` | `+0.6 min` |
| **Route 005** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+2.0 min` |
| **Route 008** | 10 | 7 | 0 | **`0.0%`** | `11.11%` | `-69.9s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-124.5s` |
| **Route 006** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 511** | `+6.4 min (+382.0s)` | `+7.1 min (+427s)` | 2 | `0.0%` |
| **Route A16** | `+6.2 min (+372.0s)` | `+6.2 min (+372s)` | 1 | `0.0%` |
| **Route 722** | `+2.9 min (+176.0s)` | `+2.9 min (+176s)` | 1 | `100.0%` |
| **Route 002** | `+2.3 min (+135.2s)` | `+14.1 min (+843s)` | 7 | `90.0%` |
| **Route 005** | `+2.0 min (+121.7s)` | `+8.9 min (+534s)` | 3 | `33.33%` |
| **Route 103** | `+1.0 min (+62.0s)` | `+1.0 min (+62s)` | 1 | `100.0%` |
| **Route 009** | `+0.6 min (+35.9s)` | `+1.8 min (+109s)` | 6 | `100.0%` |
| **Route 006** | `+0.3 min (+18.5s)` | `+0.7 min (+42s)` | 2 | `100.0%` |
| **Route 004** | `+0.2 min (+12.1s)` | `+0.9 min (+56s)` | 6 | `90.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `75.5 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `83.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32766775` | Route 002 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765273` | Route 004 | `25:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765278` | Route 004 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765274` | Route 004 | `26:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32765275` | Route 004 | `26:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766771` | Route 002 | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770894` | Route 511 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770893` | Route 511 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770895` | Route 511 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770117` | Route 009 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32770118` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32766776` | Route 002 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:19` | `16.44%` | `65.38%` | 73 | 36 | `+46.0s` |
| `2026-11-22 06:30:20` | `13.71%` | `76.09%` | 124 | 76 | `+11.7s` |
| `2026-11-22 06:00:18` | `13.37%` | `75.17%` | 187 | 106 | `+83.3s` |
| `2026-11-22 05:00:18` | `15.19%` | `83.41%` | 270 | 122 | `+39.7s` |
| `2026-11-22 04:30:18` | `15.89%` | `83.47%` | 302 | 134 | `+27.4s` |
| `2026-11-22 04:00:20` | `17.51%` | `81.52%` | 354 | 161 | `+52.0s` |
| `2026-11-22 03:30:21` | `18.73%` | `80.13%` | 395 | 174 | `+72.8s` |
| `2026-11-22 03:00:19` | `20.23%` | `83.73%` | 435 | 180 | `+71.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:19.432000+00:00`.*
