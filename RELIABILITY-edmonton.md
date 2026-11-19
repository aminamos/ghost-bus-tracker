# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-19T07:00:19.767000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.11%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`86.36%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `76` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+34.1s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+24.5s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 38 | 50.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 6.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 17.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.1 min` |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `100.0%` | `+0.1 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.0 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+2.5 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+1.9 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `85.71%` | `+0.2 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-186.0s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-153.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 523** | `+2.7 min (+161.0s)` | `+2.7 min (+161s)` | 1 | `100.0%` |
| **Route 002** | `+2.5 min (+147.0s)` | `+5.0 min (+297s)` | 8 | `100.0%` |
| **Route 005** | `+1.9 min (+111.4s)` | `+7.0 min (+419s)` | 5 | `80.0%` |
| **Route 918A** | `+1.3 min (+78.0s)` | `+1.3 min (+78s)` | 1 | `100.0%` |
| **Route 903** | `+1.0 min (+59.5s)` | `+1.3 min (+77s)` | 2 | `100.0%` |
| **Route 004** | `+1.0 min (+58.2s)` | `+1.9 min (+113s)` | 7 | `100.0%` |
| **Route 909** | `+0.9 min (+53.0s)` | `+0.9 min (+53s)` | 1 | `100.0%` |
| **Route 008** | `+0.2 min (+9.3s)` | `+2.1 min (+124s)` | 6 | `85.71%` |
| **Route 721** | `+0.1 min (+8.0s)` | `+0.1 min (+8s)` | 1 | `100.0%` |
| **Route 009** | `+0.1 min (+7.3s)` | `+0.8 min (+49s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `88.1 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.1 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.9 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.5 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32763447` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 3085 is missing from active GPS transponder fleet |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 07:00:19` | `17.11%` | `86.36%` | 76 | 37 | `+34.1s` |
| `2026-11-19 06:30:19` | `17.07%` | `83.13%` | 123 | 70 | `+16.5s` |
| `2026-11-19 06:00:22` | `12.24%` | `90.26%` | 196 | 114 | `+45.3s` |
| `2026-11-19 05:30:28` | `12.2%` | `86.27%` | 246 | 123 | `+48.9s` |
| `2026-11-19 05:00:18` | `14.68%` | `88.19%` | 293 | 136 | `+72.1s` |
| `2026-11-19 04:30:19` | `16.61%` | `87.5%` | 319 | 146 | `+50.5s` |
| `2026-11-19 03:30:18` | `15.73%` | `85.33%` | 553 | 266 | `+25.5s` |
| `2026-11-19 03:00:18` | `17.68%` | `84.22%` | 622 | 268 | `+25.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:19.767000+00:00`.*
