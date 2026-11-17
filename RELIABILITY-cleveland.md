# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:21.070000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `524` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `214` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `486` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+2780.0s` (`+46.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+155.0s` (`+2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 12 | 2.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 0.6% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 486 | 92.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+0.3 min` |
| **Route 14** | 149 | 2 | 144 | **`96.64%`** | `100.0%` | `+3.3 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `33.33%` | `+40.6 min` |
| **Route 48** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+262.5 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.6 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+262.5 min (+15752.7s)` | `+768.3 min (+46096s)` | 2 | `0.0%` |
| **Route 10** | `+40.6 min (+2435.0s)` | `+63.1 min (+3788s)` | 2 | `33.33%` |
| **Route 26** | `+5.6 min (+335.0s)` | `+8.1 min (+485s)` | 2 | `50.0%` |
| **Route 14** | `+3.3 min (+196.0s)` | `+3.5 min (+213s)` | 2 | `100.0%` |
| **Route 41** | `+1.4 min (+83.0s)` | `+1.6 min (+96s)` | 3 | `100.0%` |
| **Route 6** | `+1.2 min (+73.5s)` | `+2.2 min (+131s)` | 3 | `100.0%` |
| **Route 15** | `+0.3 min (+20.0s)` | `+0.3 min (+20s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | ~64.0m | ~64.0m | **`+0.1 min`** | `54.2 / 100` |
| **Route 48** | ~783.0m | ~783.0m | **`+0.0 min`** | `99.9 / 100` |
| **Route 14** | ~19.0m | ~19.0m | **`+0.0 min`** | `98.5 / 100` |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `97.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
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

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:21` | `92.75%` | `60.0%` | 524 | 214 | `+2780.0s` |
| `2026-11-17 06:30:18` | `90.35%` | `70.97%` | 539 | 227 | `+1674.6s` |
| `2026-11-17 06:00:20` | `87.01%` | `89.66%` | 562 | 204 | `+1607.9s` |
| `2026-11-17 05:30:19` | `82.31%` | `83.33%` | 588 | 216 | `+846.7s` |
| `2026-11-17 05:00:18` | `9.85%` | `75.93%` | 132 | 243 | `+964.9s` |
| `2026-11-17 04:30:19` | `7.93%` | `73.97%` | 164 | 238 | `+655.6s` |
| `2026-11-17 04:00:18` | `9.64%` | `71.79%` | 197 | 236 | `+621.1s` |
| `2026-11-17 03:30:20` | `11.9%` | `82.22%` | 210 | 219 | `+502.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:21.070000+00:00`.*
