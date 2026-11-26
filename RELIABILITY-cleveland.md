# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:21.158000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.79%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`93.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `333` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `150` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `299` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+65.9s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+65.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 14 | 4.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 299 | 89.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15** | 77 | 1 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 35 | 0 | 35 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 91 | 1 | 89 | **`97.8%`** | `100.0%` | `+1.8 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.0 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19** | `+3.0 min (+177.0s)` | `+5.2 min (+312s)` | 2 | `50.0%` |
| **Route 10** | `+2.2 min (+132.5s)` | `+3.3 min (+200s)` | 2 | `100.0%` |
| **Route 14** | `+1.8 min (+105.0s)` | `+1.8 min (+105s)` | 1 | `100.0%` |
| **Route 22** | `+1.3 min (+76.0s)` | `+1.3 min (+76s)` | 2 | `100.0%` |
| **Route 51** | `+1.2 min (+70.0s)` | `+1.2 min (+70s)` | 1 | `100.0%` |
| **Route 6** | `+1.1 min (+64.5s)` | `+2.2 min (+131s)` | 3 | `100.0%` |
| **Route 28** | `+0.6 min (+33.0s)` | `+0.6 min (+33s)` | 1 | `100.0%` |
| **Route 41** | `+0.2 min (+11.7s)` | `+1.2 min (+72s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `49.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19233600` | Route 15 | `07:45:00` | `SCHEDULED` | Assigned vehicle 4036 is broadcasting off-schedule with no vehicle covering 19233600 |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370226` | Route 8 | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370229` | Route 8 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370230` | Route 8 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370233` | Route 8 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370234` | Route 8 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370237` | Route 8 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370238` | Route 8 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370241` | Route 8 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370242` | Route 8 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370245` | Route 8 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370246` | Route 8 | `16:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19370249` | Route 8 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:21` | `89.79%` | `93.33%` | 333 | 150 | `+65.9s` |
| `2026-11-26 06:30:19` | `86.42%` | `78.57%` | 346 | 166 | `+126.0s` |
| `2026-11-26 06:00:18` | `83.98%` | `90.48%` | 362 | 178 | `+115.7s` |
| `2026-11-26 05:30:21` | `76.65%` | `80.7%` | 394 | 184 | `+97.8s` |
| `2026-11-26 05:00:18` | `8.8%` | `90.57%` | 125 | 207 | `+102.6s` |
| `2026-11-26 04:30:20` | `7.1%` | `83.33%` | 155 | 208 | `+142.6s` |
| `2026-11-26 04:00:19` | `10.7%` | `75.95%` | 187 | 217 | `+181.8s` |
| `2026-11-26 03:30:19` | `11.17%` | `76.14%` | 206 | 205 | `+137.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:21.158000+00:00`.*
