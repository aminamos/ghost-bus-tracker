# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:20.972000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`84.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `519` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `190` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `485` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+125.7s` (`+2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+106.0s` (`+1.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 2.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 485 | 93.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+2.8 min` |
| **Route 14** | 149 | 2 | 143 | **`95.97%`** | `100.0%` | `+1.7 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 10** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `-93.0s` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+6.2 min` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+6.2 min (+371.0s)` | `+6.2 min (+371s)` | 2 | `0.0%` |
| **Route 19** | `+4.1 min (+248.0s)` | `+4.1 min (+248s)` | 1 | `100.0%` |
| **Route 51** | `+3.2 min (+194.0s)` | `+5.0 min (+299s)` | 1 | `100.0%` |
| **Route 15** | `+2.8 min (+168.0s)` | `+2.8 min (+168s)` | 1 | `100.0%` |
| **Route 26** | `+2.1 min (+126.0s)` | `+2.1 min (+126s)` | 2 | `100.0%` |
| **Route 14** | `+1.7 min (+103.0s)` | `+1.7 min (+103s)` | 2 | `100.0%` |
| **Route 6** | `+1.6 min (+96.5s)` | `+2.0 min (+123s)` | 3 | `100.0%` |
| **Route 41** | `+1.0 min (+60.0s)` | `+1.8 min (+106s)` | 2 | `100.0%` |
| **Route 28** | `+0.2 min (+10.0s)` | `+0.2 min (+10s)` | 1 | `100.0%` |

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
| `2026-11-13 07:00:20` | `93.45%` | `84.62%` | 519 | 190 | `+125.7s` |
| `2026-11-13 06:30:18` | `90.69%` | `84.62%` | 537 | 195 | `+121.4s` |
| `2026-11-13 06:00:22` | `87.84%` | `84.0%` | 559 | 195 | `+215.6s` |
| `2026-11-13 05:30:18` | `82.23%` | `79.03%` | 591 | 214 | `+215.0s` |
| `2026-11-13 05:00:19` | `7.14%` | `74.07%` | 126 | 235 | `+161.9s` |
| `2026-11-13 04:30:18` | `7.88%` | `82.67%` | 165 | 232 | `+145.5s` |
| `2026-11-13 04:00:20` | `11.22%` | `78.05%` | 196 | 229 | `+191.0s` |
| `2026-11-13 03:30:18` | `12.33%` | `77.78%` | 219 | 210 | `+188.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:20.972000+00:00`.*
