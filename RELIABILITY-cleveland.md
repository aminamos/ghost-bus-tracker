# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.724000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.82%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `522` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `177` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `488` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+106.3s` (`+1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+88.0s` (`+1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 9 | 1.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 488 | 93.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 129 | **`99.23%`** | `100.0%` | `+2.6 min` |
| **Route 14** | 147 | 1 | 145 | **`98.64%`** | `0.0%` | `+0.0s` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+6.4 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.2 min` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | `+6.4 min (+385.0s)` | `+6.4 min (+385s)` | 2 | `0.0%` |
| **Route 19** | `+4.2 min (+250.0s)` | `+4.2 min (+250s)` | 2 | `100.0%` |
| **Route 22** | `+4.0 min (+243.0s)` | `+4.0 min (+243s)` | 1 | `100.0%` |
| **Route 15** | `+2.6 min (+159.0s)` | `+2.6 min (+159s)` | 1 | `100.0%` |
| **Route 1** | `+1.5 min (+88.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |
| **Route 6** | `+1.4 min (+81.0s)` | `+2.2 min (+130s)` | 3 | `100.0%` |
| **Route 28** | `+0.1 min (+7.0s)` | `+0.1 min (+7s)` | 1 | `100.0%` |
| **Route 41** | `+0.1 min (+6.5s)` | `+0.2 min (+12s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19237357` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233420` | Route 8 | `06:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233424` | Route 8 | `08:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233428` | Route 8 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233432` | Route 8 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233436` | Route 8 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233440` | Route 8 | `16:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233444` | Route 8 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233448` | Route 8 | `20:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233418` | Route 8 | `05:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233422` | Route 8 | `07:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233426` | Route 8 | `09:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233430` | Route 8 | `11:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233434` | Route 8 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233438` | Route 8 | `15:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `93.49%` | `81.82%` | 522 | 177 | `+106.3s` |
| `2026-11-09 06:30:20` | `91.4%` | `78.26%` | 535 | 186 | `+111.3s` |
| `2026-11-09 06:00:18` | `89.66%` | `73.91%` | 551 | 197 | `+210.1s` |
| `2026-11-09 05:30:18` | `85.86%` | `81.48%` | 580 | 205 | `+152.1s` |
| `2026-11-09 05:00:18` | `9.23%` | `80.0%` | 130 | 209 | `+157.4s` |
| `2026-11-09 04:30:19` | `9.87%` | `80.95%` | 152 | 190 | `+168.2s` |
| `2026-11-09 04:00:18` | `9.94%` | `71.88%` | 171 | 194 | `+262.1s` |
| `2026-11-09 03:30:18` | `11.79%` | `77.11%` | 195 | 214 | `+203.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.724000+00:00`.*
