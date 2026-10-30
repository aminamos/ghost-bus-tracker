# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-30T07:00:27.264000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.4%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `68` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `35` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+25.4s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+48.0s` (`+0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 35 | 51.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 10.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 16.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `71.43%` | `+0.3 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+1.4 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.6 min` |
| **Route 008** | 10 | 5 | 2 | **`20.0%`** | `71.43%` | `-49.7s` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-5.0s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-78.5s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-52.5s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 052** | `+4.8 min (+290.0s)` | `+4.8 min (+290s)` | 1 | `100.0%` |
| **Route 004** | `+1.6 min (+98.3s)` | `+2.9 min (+174s)` | 7 | `100.0%` |
| **Route 002** | `+1.4 min (+82.0s)` | `+3.0 min (+177s)` | 8 | `100.0%` |
| **Route 918A** | `+0.9 min (+54.0s)` | `+0.9 min (+54s)` | 1 | `100.0%` |
| **Route 903** | `+0.9 min (+52.0s)` | `+1.9 min (+115s)` | 2 | `100.0%` |
| **Route 009** | `+0.3 min (+15.1s)` | `+1.5 min (+92s)` | 4 | `71.43%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `78.8 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.7 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.8 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.6 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32755348` | Route 008 | `26:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32755349` | Route 008 | `26:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 07:00:27` | `16.18%` | `81.4%` | 68 | 35 | `+25.4s` |
| `2026-10-30 06:30:29` | `16.0%` | `83.52%` | 125 | 74 | `+24.1s` |
| `2026-10-30 06:00:28` | `13.47%` | `84.77%` | 193 | 110 | `+66.6s` |
| `2026-10-30 05:30:28` | `15.26%` | `86.46%` | 249 | 118 | `+73.7s` |
| `2026-10-30 05:00:20` | `18.0%` | `90.3%` | 300 | 133 | `+65.6s` |
| `2026-10-30 04:30:18` | `20.63%` | `89.06%` | 349 | 151 | `+92.1s` |
| `2026-10-30 04:00:25` | `18.86%` | `84.99%` | 472 | 233 | `+63.7s` |
| `2026-10-30 03:30:18` | `20.96%` | `87.76%` | 582 | 263 | `+121.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:27.264000+00:00`.*
