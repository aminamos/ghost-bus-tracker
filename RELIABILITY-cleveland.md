# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:19.625000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`88.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `338` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `161` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `298` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+174.6s` (`+2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+101.5s` (`+1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 13 | 3.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 1.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 298 | 88.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 90** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 35 | 0 | 35 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 78 | 1 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 14** | 93 | 2 | 89 | **`95.7%`** | `66.67%` | `+2.6 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 48** | 4 | 2 | 0 | **`0.0%`** | `33.33%` | `+5.6 min` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+5.6 min (+338.7s)` | `+9.1 min (+548s)` | 2 | `33.33%` |
| **Route 22** | `+4.7 min (+279.0s)` | `+4.7 min (+279s)` | 2 | `100.0%` |
| **Route 41** | `+3.5 min (+213.0s)` | `+5.2 min (+314s)` | 4 | `33.33%` |
| **Route 14** | `+2.6 min (+159.0s)` | `+6.3 min (+379s)` | 2 | `66.67%` |
| **Route 3** | `+2.6 min (+155.0s)` | `+2.6 min (+155s)` | 1 | `100.0%` |
| **Route 6** | `+2.1 min (+126.0s)` | `+4.2 min (+255s)` | 3 | `100.0%` |
| **Route 1** | `+1.8 min (+105.0s)` | `+1.8 min (+105s)` | 1 | `100.0%` |
| **Route 19** | `+1.2 min (+73.0s)` | `+1.2 min (+73s)` | 2 | `100.0%` |
| **Route 28** | `+1.1 min (+69.0s)` | `+1.1 min (+69s)` | 1 | `100.0%` |
| **Route 10** | `+1.1 min (+63.0s)` | `+1.1 min (+63s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 48** | ~60.0m | ~60.0m | **`+0.0 min`** | `96.2 / 100` |
| **Route 14** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235442` | Route 8 | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235445` | Route 8 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235446` | Route 8 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235449` | Route 8 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235450` | Route 8 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235453` | Route 8 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235454` | Route 8 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235457` | Route 8 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235458` | Route 8 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235461` | Route 8 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235462` | Route 8 | `16:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235465` | Route 8 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235466` | Route 8 | `18:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:19` | `88.17%` | `72.22%` | 338 | 161 | `+174.6s` |
| `2026-11-28 06:30:17` | `85.67%` | `86.21%` | 349 | 155 | `+151.7s` |
| `2026-11-28 05:30:19` | `76.07%` | `80.7%` | 397 | 177 | `+122.0s` |
| `2026-11-28 05:00:19` | `6.06%` | `83.64%` | 132 | 199 | `+138.3s` |
| `2026-11-28 04:30:18` | `6.13%` | `88.31%` | 163 | 203 | `+141.1s` |
| `2026-11-28 04:00:19` | `9.38%` | `77.38%` | 192 | 217 | `+177.0s` |
| `2026-11-28 03:30:19` | `10.65%` | `80.21%` | 216 | 199 | `+176.6s` |
| `2026-11-28 03:00:20` | `12.65%` | `74.47%` | 245 | 205 | `+297.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:19.625000+00:00`.*
