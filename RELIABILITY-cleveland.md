# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.709000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.4%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`87.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `500` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `200` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `462` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+100.6s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+115.0s` (`+1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 14 | 2.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 462 | 92.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+0.0 min` |
| **Route 14** | 149 | 2 | 143 | **`95.97%`** | `100.0%` | `+2.5 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 10** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `-47.0s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 51** | `+4.7 min (+282.0s)` | `+6.5 min (+387s)` | 1 | `50.0%` |
| **Route 22** | `+2.6 min (+155.0s)` | `+2.6 min (+155s)` | 2 | `100.0%` |
| **Route 48** | `+2.5 min (+153.0s)` | `+2.5 min (+153s)` | 2 | `100.0%` |
| **Route 14** | `+2.5 min (+150.0s)` | `+2.5 min (+150s)` | 2 | `100.0%` |
| **Route 6** | `+2.1 min (+124.0s)` | `+3.4 min (+204s)` | 3 | `100.0%` |
| **Route 28** | `+1.9 min (+117.0s)` | `+1.9 min (+117s)` | 1 | `100.0%` |
| **Route 41** | `+1.4 min (+86.0s)` | `+1.9 min (+113s)` | 3 | `100.0%` |
| **Route 15** | `+0.0 min (+2.0s)` | `+0.0 min (+2s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `84.2 / 100` |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233417` | Route 8 | `05:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233420` | Route 8 | `06:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233421` | Route 8 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233424` | Route 8 | `08:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233425` | Route 8 | `09:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233428` | Route 8 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233429` | Route 8 | `11:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233432` | Route 8 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233433` | Route 8 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233436` | Route 8 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233437` | Route 8 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233440` | Route 8 | `16:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233441` | Route 8 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233444` | Route 8 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `92.4%` | `87.5%` | 500 | 200 | `+100.6s` |
| `2026-11-25 06:30:18` | `89.92%` | `86.21%` | 516 | 218 | `+97.4s` |
| `2026-11-25 06:00:19` | `87.8%` | `84.21%` | 533 | 199 | `+57.1s` |
| `2026-11-25 05:30:18` | `82.38%` | `87.5%` | 562 | 211 | `+81.1s` |
| `2026-11-25 05:00:17` | `6.2%` | `85.45%` | 129 | 234 | `+91.9s` |
| `2026-11-25 04:30:18` | `7.14%` | `82.86%` | 154 | 242 | `+138.5s` |
| `2026-11-25 04:00:18` | `10.22%` | `87.5%` | 186 | 244 | `+128.1s` |
| `2026-11-25 03:30:21` | `11.22%` | `81.48%` | 205 | 228 | `+124.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.709000+00:00`.*
