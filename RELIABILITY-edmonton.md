# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-11T07:00:19.171000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`86.54%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `68` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+109.1s` (`+1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+40.5s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 45 | 66.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 7.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 2.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 10.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.2 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+1.5 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+0.7 min` |
| **Route 511** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+40.9 min` |
| **Route 009** | 8 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-118.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `-34.8s` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `100.0%` | `-5.1s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-3.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 509A** | `+54.2 min (+3252.0s)` | `+54.2 min (+3252s)` | 1 | `0.0%` |
| **Route 511** | `+40.9 min (+2451.0s)` | `+40.9 min (+2451s)` | 2 | `0.0%` |
| **Route 523** | `+2.6 min (+156.0s)` | `+2.6 min (+156s)` | 1 | `100.0%` |
| **Route 002** | `+1.5 min (+92.2s)` | `+3.8 min (+230s)` | 8 | `100.0%` |
| **Route 004** | `+0.7 min (+43.9s)` | `+1.8 min (+108s)` | 7 | `100.0%` |
| **Route 918A** | `+0.7 min (+42.0s)` | `+0.7 min (+42s)` | 1 | `100.0%` |
| **Route 903** | `+0.7 min (+41.0s)` | `+0.7 min (+42s)` | 2 | `100.0%` |
| **Route 009** | `+0.2 min (+13.0s)` | `+0.7 min (+44s)` | 4 | `100.0%` |
| **Route 721** | `+0.2 min (+12.0s)` | `+0.2 min (+12s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.9 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.9 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.9 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `98.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33272665` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 3085 is missing from active GPS transponder fleet |
| `33276367` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33276366` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33270793` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33270791` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33270792` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33276365` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-11 07:00:19` | `10.29%` | `86.54%` | 68 | 38 | `+109.1s` |
| `2026-11-11 06:30:18` | `9.73%` | `81.11%` | 113 | 73 | `+1.7s` |
| `2026-11-11 06:00:27` | `7.1%` | `89.81%` | 183 | 113 | `+55.2s` |
| `2026-11-11 05:30:23` | `9.62%` | `87.06%` | 239 | 122 | `+58.2s` |
| `2026-11-11 05:00:19` | `10.8%` | `88.02%` | 287 | 136 | `+65.5s` |
| `2026-11-11 04:30:20` | `14.64%` | `86.97%` | 321 | 149 | `+249.5s` |
| `2026-11-11 04:00:18` | `14.83%` | `84.55%` | 445 | 235 | `+222.7s` |
| `2026-11-11 03:00:19` | `17.07%` | `81.02%` | 621 | 268 | `+121.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:19.171000+00:00`.*
