# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-03T07:00:19.436000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.51%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`90.7%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `74` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+27.3s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+15.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 52.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 5.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 13.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.0 min` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `100.0%` | `+0.1 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+0.9 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.2 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `87.5%` | `+0.2 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-14.5s` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 901** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `-95.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 523** | `+2.6 min (+156.0s)` | `+2.6 min (+156s)` | 1 | `100.0%` |
| **Route 004** | `+1.2 min (+71.9s)` | `+2.8 min (+167s)` | 7 | `100.0%` |
| **Route 918A** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 002** | `+0.9 min (+52.2s)` | `+3.2 min (+194s)` | 8 | `100.0%` |
| **Route 903** | `+0.8 min (+49.0s)` | `+1.5 min (+90s)` | 2 | `100.0%` |
| **Route 005** | `+0.6 min (+36.8s)` | `+1.7 min (+104s)` | 4 | `100.0%` |
| **Route 008** | `+0.2 min (+14.9s)` | `+3.3 min (+200s)` | 6 | `87.5%` |
| **Route 009** | `+0.1 min (+7.3s)` | `+1.7 min (+100s)` | 4 | `100.0%` |
| **Route 721** | `+0.0 min (+2.0s)` | `+0.0 min (+2s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.9 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.1 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `99.1 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.2 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32763447` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 2257 is missing from active GPS transponder fleet |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:19` | `13.51%` | `90.7%` | 74 | 38 | `+27.3s` |
| `2026-11-03 06:30:27` | `11.67%` | `82.76%` | 120 | 74 | `-4.7s` |
| `2026-11-03 06:00:20` | `10.71%` | `89.94%` | 196 | 113 | `+53.0s` |
| `2026-11-03 05:30:21` | `10.84%` | `82.44%` | 249 | 122 | `+192.1s` |
| `2026-11-03 05:00:29` | `13.4%` | `86.07%` | 291 | 133 | `+161.3s` |
| `2026-11-03 03:00:18` | `18.08%` | `83.73%` | 625 | 265 | `+77.4s` |
| `2026-11-03 02:30:25` | `20.68%` | `80.54%` | 672 | 273 | `+104.2s` |
| `2026-11-03 02:00:21` | `22.91%` | `82.15%` | 707 | 280 | `+106.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:19.436000+00:00`.*
