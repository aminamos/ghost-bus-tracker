# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-18T07:00:22.608000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.73%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `523` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `189` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `485` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+140.4s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+102.0s` (`+1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 1.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 0.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 485 | 92.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `0.0%` | `+7.3 min` |
| **Route 14** | 149 | 2 | 143 | **`95.97%`** | `100.0%` | `+0.5 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 48** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+7.6 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+7.6 min (+458.5s)` | `+9.0 min (+542s)` | 2 | `0.0%` |
| **Route 15** | `+7.3 min (+441.0s)` | `+7.3 min (+441s)` | 1 | `0.0%` |
| **Route 6** | `+3.9 min (+236.0s)` | `+4.3 min (+256s)` | 3 | `100.0%` |
| **Route 1** | `+1.7 min (+102.0s)` | `+1.7 min (+102s)` | 1 | `100.0%` |
| **Route 41** | `+1.4 min (+85.7s)` | `+2.5 min (+150s)` | 3 | `100.0%` |
| **Route 14** | `+0.5 min (+28.0s)` | `+0.5 min (+28s)` | 2 | `100.0%` |
| **Route 28** | `+0.2 min (+15.0s)` | `+0.2 min (+15s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `61.3 / 100` |

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
| `2026-11-18 07:00:22` | `92.73%` | `66.67%` | 523 | 189 | `+140.4s` |
| `2026-11-18 06:30:19` | `90.52%` | `78.57%` | 538 | 216 | `+145.8s` |
| `2026-11-18 06:00:21` | `86.99%` | `79.17%` | 561 | 216 | `+181.8s` |
| `2026-11-18 05:00:18` | `8.82%` | `86.54%` | 136 | 251 | `+109.7s` |
| `2026-11-18 04:30:19` | `8.02%` | `76.71%` | 162 | 249 | `+176.6s` |
| `2026-11-18 04:00:17` | `11.5%` | `74.03%` | 200 | 240 | `+208.5s` |
| `2026-11-18 03:30:18` | `11.93%` | `82.56%` | 218 | 220 | `+838.5s` |
| `2026-11-18 03:00:19` | `13.77%` | `86.96%` | 247 | 232 | `+119.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T07:00:22.608000+00:00`.*
