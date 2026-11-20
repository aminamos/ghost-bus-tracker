# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:22.611000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.43%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `524` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `218` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `486` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+100.2s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+77.5s` (`+1.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 1.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 486 | 92.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15** | 129 | 0 | 129 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 149 | 2 | 143 | **`95.97%`** | `100.0%` | `+1.9 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-5.0s` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `-55.0s` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `-57.0s` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | `+10.3 min (+617.0s)` | `+10.3 min (+617s)` | 1 | `0.0%` |
| **Route 48** | `+6.3 min (+376.0s)` | `+6.3 min (+376s)` | 2 | `0.0%` |
| **Route 6** | `+3.3 min (+196.0s)` | `+4.3 min (+257s)` | 3 | `100.0%` |
| **Route 14** | `+1.9 min (+117.0s)` | `+1.9 min (+117s)` | 2 | `100.0%` |
| **Route 41** | `+1.0 min (+59.7s)` | `+1.5 min (+89s)` | 3 | `100.0%` |
| **Route 28** | `+0.4 min (+22.0s)` | `+0.4 min (+22s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `73.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
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
| `2026-11-20 07:00:22` | `92.75%` | `71.43%` | 524 | 218 | `+100.2s` |
| `2026-11-20 06:30:18` | `90.35%` | `82.76%` | 539 | 206 | `+171.6s` |
| `2026-11-20 06:00:20` | `87.54%` | `80.0%` | 562 | 197 | `+166.0s` |
| `2026-11-20 05:30:18` | `81.76%` | `88.52%` | 592 | 215 | `+179.8s` |
| `2026-11-20 05:00:19` | `7.91%` | `87.93%` | 139 | 239 | `+170.7s` |
| `2026-11-20 04:30:18` | `8.54%` | `81.58%` | 164 | 232 | `+159.2s` |
| `2026-11-20 04:00:18` | `9.9%` | `71.59%` | 202 | 237 | `+223.1s` |
| `2026-11-20 03:30:19` | `12.16%` | `73.47%` | 222 | 218 | `+188.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:22.611000+00:00`.*
