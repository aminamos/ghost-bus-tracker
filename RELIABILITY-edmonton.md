# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-23T07:01:26.826000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.09%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.43%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `66` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `36` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+158.5s` (`+2.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+20.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 56.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 7.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 9.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 002** | 13 | 7 | 3 | **`23.08%`** | `100.0%` | `+1.2 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+0.7 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.6 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-77.0s` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `75.0%` | `-7.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 009** | 7 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-182.0s` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+40.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 509A** | `+54.9 min (+3295.0s)` | `+54.9 min (+3295s)` | 1 | `0.0%` |
| **Route 511** | `+40.9 min (+2454.0s)` | `+40.9 min (+2454s)` | 2 | `0.0%` |
| **Route 715** | `+8.3 min (+496.0s)` | `+8.3 min (+496s)` | 1 | `0.0%` |
| **Route 052** | `+4.8 min (+285.0s)` | `+4.8 min (+285s)` | 1 | `100.0%` |
| **Route 903** | `+1.3 min (+78.0s)` | `+2.2 min (+134s)` | 2 | `100.0%` |
| **Route 002** | `+1.2 min (+74.0s)` | `+1.4 min (+84s)` | 7 | `100.0%` |
| **Route 918A** | `+1.1 min (+66.0s)` | `+1.1 min (+66s)` | 1 | `100.0%` |
| **Route 004** | `+0.7 min (+42.9s)` | `+1.9 min (+114s)` | 7 | `100.0%` |
| **Route 005** | `+0.6 min (+34.8s)` | `+7.4 min (+446s)` | 5 | `60.0%` |
| **Route 009** | `+0.4 min (+24.7s)` | `+1.1 min (+65s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `81.4 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.8 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:26` | `9.09%` | `80.43%` | 66 | 36 | `+158.5s` |
| `2026-10-23 06:30:26` | `11.4%` | `80.49%` | 114 | 72 | `+46.5s` |
| `2026-10-23 06:00:21` | `7.37%` | `86.96%` | 190 | 112 | `+85.1s` |
| `2026-10-23 05:30:23` | `10.37%` | `89.32%` | 241 | 120 | `+54.6s` |
| `2026-10-23 05:15:29` | `11.94%` | `90.0%` | 268 | 127 | `+43.2s` |
| `2026-10-23 05:00:40` | `12.5%` | `86.13%` | 288 | 134 | `+82.2s` |
| `2026-10-23 04:30:38` | `16.26%` | `88.8%` | 326 | 148 | `+66.5s` |
| `2026-10-23 04:00:42` | `15.07%` | `85.11%` | 438 | 229 | `+63.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:26.826000+00:00`.*
