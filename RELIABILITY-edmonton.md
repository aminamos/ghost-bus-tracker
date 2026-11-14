# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-14T07:00:19.198000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.93%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.59%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `67` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `34` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+22.7s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+21.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 58.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 10.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 4.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 14.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 4 | **`57.14%`** | `0.0%` | `+0.0s` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `87.5%` | `+2.0 min` |
| **Route 004** | 15 | 8 | 3 | **`20.0%`** | `100.0%` | `+1.2 min` |
| **Route 008** | 9 | 5 | 0 | **`0.0%`** | `75.0%` | `-141.2s` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-50.5s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 009** | 7 | 4 | 0 | **`0.0%`** | `71.43%` | `+1.0 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.2 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-100.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 715** | `+6.8 min (+410.0s)` | `+6.8 min (+410s)` | 1 | `0.0%` |
| **Route 918A** | `+2.4 min (+142.0s)` | `+2.4 min (+142s)` | 1 | `100.0%` |
| **Route 002** | `+2.0 min (+121.8s)` | `+6.4 min (+382s)` | 8 | `87.5%` |
| **Route 004** | `+1.2 min (+73.0s)` | `+3.8 min (+230s)` | 8 | `100.0%` |
| **Route 721** | `+1.0 min (+62.0s)` | `+1.0 min (+62s)` | 1 | `100.0%` |
| **Route 009** | `+1.0 min (+57.3s)` | `+7.0 min (+419s)` | 4 | `71.43%` |
| **Route 903** | `+0.6 min (+37.0s)` | `+1.8 min (+109s)` | 2 | `100.0%` |
| **Route 901** | `+0.2 min (+10.5s)` | `+1.8 min (+106s)` | 2 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.5m | ~30.5m | **`+0.0 min`** | `73.7 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `90.8 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `91.5 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.3 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.1 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.7 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33295736` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33291427` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33291425` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33291426` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33291424` | Route 511 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33295735` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33301550` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33295734` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33301549` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33301548` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `14.93%` | `79.59%` | 67 | 34 | `+22.7s` |
| `2026-11-14 06:30:23` | `12.17%` | `80.68%` | 115 | 72 | `+38.7s` |
| `2026-11-14 06:00:22` | `10.27%` | `87.58%` | 185 | 111 | `+70.4s` |
| `2026-11-14 05:30:20` | `10.17%` | `83.74%` | 236 | 119 | `+61.0s` |
| `2026-11-14 05:00:26` | `12.5%` | `88.89%` | 280 | 133 | `+80.4s` |
| `2026-11-14 04:30:18` | `14.01%` | `85.82%` | 314 | 150 | `+73.1s` |
| `2026-11-14 04:00:24` | `13.21%` | `83.14%` | 424 | 230 | `+65.5s` |
| `2026-11-14 03:30:21` | `17.2%` | `78.38%` | 558 | 263 | `+42.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.198000+00:00`.*
