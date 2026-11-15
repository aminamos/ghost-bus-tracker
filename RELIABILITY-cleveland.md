# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:18.882000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.24%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `355` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `149` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `317` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+99.1s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+27.0s` (`+0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 4.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 317 | 89.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 77 | 1 | 76 | **`98.7%`** | `100.0%` | `+0.1 min` |
| **Route 14** | 92 | 2 | 88 | **`95.65%`** | `0.0%` | `+5.7 min` |
| **Route 22** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.0 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 14** | `+5.7 min (+344.0s)` | `+5.7 min (+344s)` | 2 | `0.0%` |
| **Route 10** | `+4.3 min (+259.0s)` | `+8.2 min (+491s)` | 2 | `50.0%` |
| **Route 22** | `+4.0 min (+237.0s)` | `+4.0 min (+237s)` | 2 | `100.0%` |
| **Route 51** | `+2.2 min (+131.0s)` | `+2.2 min (+131s)` | 1 | `100.0%` |
| **Route 1** | `+2.1 min (+126.0s)` | `+4.1 min (+246s)` | 1 | `100.0%` |
| **Route 25** | `+2.1 min (+125.0s)` | `+2.1 min (+125s)` | 2 | `100.0%` |
| **Route 26** | `+1.5 min (+89.0s)` | `+1.5 min (+89s)` | 2 | `100.0%` |
| **Route 41** | `+0.6 min (+33.5s)` | `+1.0 min (+58s)` | 2 | `100.0%` |
| **Route 6** | `+0.2 min (+10.5s)` | `+0.2 min (+12s)` | 3 | `100.0%` |
| **Route 15** | `+0.1 min (+4.0s)` | `+0.1 min (+4s)` | 1 | `100.0%` |

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
| `19235745` | Route 14 | `26:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
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
| `19237130` | Route 8 | `14:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237134` | Route 8 | `16:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237138` | Route 8 | `18:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `89.3%` | `88.24%` | 355 | 149 | `+99.1s` |
| `2026-11-15 06:30:18` | `87.36%` | `88.46%` | 364 | 143 | `+121.2s` |
| `2026-11-15 06:00:22` | `82.1%` | `69.7%` | 391 | 147 | `+13461.4s` |
| `2026-11-15 05:30:19` | `78.1%` | `78.85%` | 411 | 150 | `+3048.8s` |
| `2026-11-15 05:00:19` | `0.0%` | `0.0%` | 0 | 171 | `+0.0s` |
| `2026-11-15 04:30:18` | `0.0%` | `0.0%` | 0 | 175 | `+0.0s` |
| `2026-11-15 04:00:18` | `0.0%` | `0.0%` | 0 | 183 | `+0.0s` |
| `2026-11-15 03:30:18` | `0.0%` | `0.0%` | 0 | 183 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.882000+00:00`.*
