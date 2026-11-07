# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:18.744000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `354` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `173` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `318` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+132.9s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+130.0s` (`+2.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 3.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 0.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 318 | 89.8% |
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
| **Route 14** | 91 | 2 | 88 | **`96.7%`** | `100.0%` | `+3.2 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.4 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-27.7s` |
| **Route 10** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+4.1 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+6.2 min (+370.0s)` | `+6.2 min (+370s)` | 2 | `0.0%` |
| **Route 10** | `+4.1 min (+247.0s)` | `+4.1 min (+247s)` | 3 | `100.0%` |
| **Route 51** | `+3.9 min (+235.0s)` | `+5.7 min (+340s)` | 1 | `50.0%` |
| **Route 6** | `+3.7 min (+224.0s)` | `+5.9 min (+356s)` | 3 | `50.0%` |
| **Route 26** | `+3.3 min (+197.0s)` | `+3.3 min (+197s)` | 2 | `100.0%` |
| **Route 14** | `+3.2 min (+191.0s)` | `+3.2 min (+191s)` | 2 | `100.0%` |
| **Route 1** | `+2.4 min (+144.0s)` | `+2.4 min (+144s)` | 1 | `100.0%` |
| **Route 3** | `+1.0 min (+61.0s)` | `+1.0 min (+61s)` | 1 | `100.0%` |
| **Route 28** | `+0.0 min (+2.0s)` | `+0.0 min (+2s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `63.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19233600` | Route 15 | `07:45:00` | `SCHEDULED` | Assigned vehicle 4036 is broadcasting off-schedule with no vehicle covering 19233600 |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235445` | Route 8 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235449` | Route 8 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235453` | Route 8 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235457` | Route 8 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235461` | Route 8 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235465` | Route 8 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235469` | Route 8 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235443` | Route 8 | `06:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235447` | Route 8 | `08:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235451` | Route 8 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235455` | Route 8 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235459` | Route 8 | `14:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235463` | Route 8 | `16:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:18` | `89.83%` | `73.33%` | 354 | 173 | `+132.9s` |
| `2026-11-07 06:30:19` | `86.89%` | `68.97%` | 366 | 181 | `+194.3s` |
| `2026-11-07 06:00:20` | `82.52%` | `67.74%` | 389 | 187 | `+361.5s` |
| `2026-11-07 05:30:18` | `78.66%` | `80.77%` | 417 | 201 | `+138.8s` |
| `2026-11-07 05:00:18` | `8.27%` | `65.0%` | 133 | 217 | `+279.4s` |
| `2026-11-07 04:30:18` | `6.17%` | `72.37%` | 162 | 224 | `+282.4s` |
| `2026-11-07 04:00:20` | `7.89%` | `58.62%` | 190 | 226 | `+308.7s` |
| `2026-11-07 03:30:19` | `8.72%` | `70.48%` | 218 | 211 | `+933.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.744000+00:00`.*
