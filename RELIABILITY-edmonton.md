# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:31.705000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.63%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `75` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+502.2s` (`+8.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+36.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 53.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 8.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.7% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 16.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `71.43%` | `+0.0 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `83.33%` | `+1.9 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.1 min` |
| **Route 903** | 4 | 3 | 0 | **`0.0%`** | `75.0%` | `+96.3 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+0.7 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-88.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 903** | `+96.3 min (+5780.5s)` | `+380.5 min (+22828s)` | 3 | `75.0%` |
| **Route 002** | `+1.9 min (+112.2s)` | `+5.7 min (+344s)` | 8 | `83.33%` |
| **Route 909** | `+1.6 min (+99.0s)` | `+1.6 min (+99s)` | 1 | `100.0%` |
| **Route 004** | `+1.1 min (+65.2s)` | `+2.1 min (+126s)` | 7 | `100.0%` |
| **Route 005** | `+0.7 min (+42.0s)` | `+7.8 min (+467s)` | 5 | `40.0%` |
| **Route 918A** | `+0.4 min (+24.0s)` | `+0.4 min (+24s)` | 1 | `100.0%` |
| **Route 008** | `+0.3 min (+18.9s)` | `+0.8 min (+50s)` | 6 | `100.0%` |
| **Route 009** | `+0.0 min (+2.7s)` | `+0.9 min (+56s)` | 4 | `71.43%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 903** | ~385.0m | ~385.0m | **`+0.8 min`** | `50.5 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `73.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.1 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.8 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:31` | `16.0%` | `81.63%` | 75 | 37 | `+502.2s` |
| `2026-11-20 06:30:19` | `15.0%` | `79.52%` | 120 | 71 | `+275.3s` |
| `2026-11-20 06:00:20` | `11.73%` | `88.05%` | 196 | 114 | `+171.0s` |
| `2026-11-20 05:30:19` | `12.76%` | `88.12%` | 243 | 122 | `+128.7s` |
| `2026-11-20 05:00:20` | `14.83%` | `90.04%` | 290 | 136 | `+118.4s` |
| `2026-11-20 04:30:18` | `17.03%` | `82.69%` | 323 | 148 | `+233.7s` |
| `2026-11-20 04:00:21` | `15.32%` | `82.4%` | 444 | 238 | `+83.4s` |
| `2026-11-20 03:30:25` | `15.88%` | `82.84%` | 548 | 267 | `+60.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:31.705000+00:00`.*
