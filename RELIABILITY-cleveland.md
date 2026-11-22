# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:18.362000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`90.91%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`86.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `352` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `130` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `320` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+258.3s` (`+4.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+129.0s` (`+2.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 13 | 3.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 320 | 90.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15** | 77 | 1 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 93 | 2 | 89 | **`95.7%`** | `100.0%` | `+3.7 min` |
| **Route 6** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 25** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19** | `+18.9 min (+1135.0s)` | `+21.2 min (+1270s)` | 1 | `0.0%` |
| **Route 14** | `+3.7 min (+224.0s)` | `+4.4 min (+263s)` | 2 | `100.0%` |
| **Route 10** | `+3.2 min (+194.0s)` | `+3.2 min (+194s)` | 1 | `100.0%` |
| **Route 51** | `+2.1 min (+129.0s)` | `+2.1 min (+129s)` | 1 | `100.0%` |
| **Route 1** | `+2.1 min (+124.0s)` | `+4.1 min (+244s)` | 1 | `100.0%` |
| **Route 26** | `+1.9 min (+115.0s)` | `+1.9 min (+115s)` | 2 | `100.0%` |
| **Route 41** | `+1.9 min (+111.5s)` | `+3.5 min (+211s)` | 2 | `100.0%` |
| **Route 25** | `+1.6 min (+99.0s)` | `+1.6 min (+99s)` | 2 | `100.0%` |
| **Route 48** | `+1.1 min (+64.0s)` | `+1.1 min (+64s)` | 2 | `100.0%` |
| **Route 22** | `+1.0 min (+62.0s)` | `+1.0 min (+62s)` | 2 | `100.0%` |

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
| `19235910` | Route 6 | `03:10:00` | `SCHEDULED` | Assigned vehicle 4134 is broadcasting off-schedule with no vehicle covering 19235910 |
| `19235751` | Route 15 | `06:15:00` | `SCHEDULED` | Assigned vehicle 4185 is broadcasting off-schedule with no vehicle covering 19235751 |
| `19235745` | Route 14 | `26:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235744` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237116` | Route 8 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237120` | Route 8 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237124` | Route 8 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237128` | Route 8 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237132` | Route 8 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237136` | Route 8 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237140` | Route 8 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237114` | Route 8 | `06:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237118` | Route 8 | `08:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237122` | Route 8 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237126` | Route 8 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `90.91%` | `86.67%` | 352 | 130 | `+258.3s` |
| `2026-11-22 06:30:18` | `87.6%` | `87.5%` | 363 | 136 | `+127.5s` |
| `2026-11-22 06:00:17` | `84.07%` | `87.5%` | 383 | 144 | `+316.8s` |
| `2026-11-22 05:30:22` | `78.78%` | `75.0%` | 410 | 155 | `+152.3s` |
| `2026-11-22 05:00:18` | `6.15%` | `81.48%` | 130 | 171 | `+156.5s` |
| `2026-11-22 04:30:18` | `8.78%` | `78.08%` | 148 | 178 | `+157.4s` |
| `2026-11-22 04:00:18` | `9.6%` | `72.6%` | 177 | 180 | `+176.4s` |
| `2026-11-22 03:30:20` | `11.92%` | `71.6%` | 193 | 170 | `+170.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.362000+00:00`.*
