# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-16T07:00:20.362000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.8%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`77.78%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `528` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `193` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `490` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+197.2s` (`+3.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+132.5s` (`+2.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 14 | 2.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 490 | 92.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 131 | 2 | 130 | **`99.24%`** | `100.0%` | `+2.7 min` |
| **Route 14** | 150 | 2 | 146 | **`97.33%`** | `100.0%` | `+3.8 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 22** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.6 min` |
| **Route 19** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+11.6 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19** | `+11.6 min (+695.5s)` | `+24.2 min (+1453s)` | 3 | `0.0%` |
| **Route 48** | `+6.2 min (+370.0s)` | `+6.2 min (+370s)` | 2 | `0.0%` |
| **Route 22** | `+4.6 min (+276.0s)` | `+4.6 min (+276s)` | 2 | `100.0%` |
| **Route 14** | `+3.8 min (+226.5s)` | `+4.2 min (+253s)` | 2 | `100.0%` |
| **Route 3** | `+3.2 min (+192.0s)` | `+3.2 min (+192s)` | 1 | `100.0%` |
| **Route 15** | `+2.7 min (+164.0s)` | `+2.7 min (+164s)` | 2 | `100.0%` |
| **Route 28** | `+2.2 min (+132.0s)` | `+2.2 min (+132s)` | 1 | `100.0%` |
| **Route 51** | `+2.1 min (+124.0s)` | `+3.8 min (+229s)` | 1 | `100.0%` |
| **Route 26** | `+1.6 min (+98.0s)` | `+1.6 min (+98s)` | 2 | `100.0%` |
| **Route 6** | `+1.6 min (+96.7s)` | `+2.2 min (+133s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19237366` | Route 15 | `06:45:00` | `SCHEDULED` | Assigned vehicle 4125 is broadcasting off-schedule with no vehicle covering 19237366 |
| `19237358` | Route 14 | `26:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
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

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:20` | `92.8%` | `77.78%` | 528 | 193 | `+197.2s` |
| `2026-11-16 06:30:23` | `91.79%` | `85.19%` | 536 | 168 | `+98.3s` |
| `2026-11-16 06:00:19` | `89.49%` | `69.23%` | 552 | 188 | `+199.2s` |
| `2026-11-16 05:30:19` | `86.76%` | `80.0%` | 574 | 193 | `+206.3s` |
| `2026-11-16 05:00:19` | `9.6%` | `71.93%` | 125 | 202 | `+347.3s` |
| `2026-11-16 04:30:19` | `9.15%` | `68.12%` | 142 | 199 | `+221.1s` |
| `2026-11-16 04:00:19` | `10.12%` | `75.81%` | 168 | 205 | `+155.8s` |
| `2026-11-16 03:30:18` | `11.58%` | `82.5%` | 190 | 198 | `+157.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:20.362000+00:00`.*
