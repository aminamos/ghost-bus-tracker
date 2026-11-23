# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:18.429000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.98%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.25%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `527` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `157` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `490` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-4840.6s` (`-80.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+76.5s` (`+1.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 9 | 1.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.4% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 490 | 93.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15** | 131 | 2 | 131 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 149 | 2 | 145 | **`97.32%`** | `0.0%` | `+8.8 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+25.3 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | `+44.7 min (+2684.0s)` | `+44.7 min (+2684s)` | 1 | `0.0%` |
| **Route 10** | `+25.3 min (+1518.3s)` | `+43.0 min (+2581s)` | 2 | `0.0%` |
| **Route 14** | `+8.8 min (+525.0s)` | `+8.8 min (+525s)` | 2 | `0.0%` |
| **Route 41** | `+3.1 min (+184.0s)` | `+6.4 min (+385s)` | 2 | `50.0%` |
| **Route 22** | `+2.2 min (+134.0s)` | `+2.2 min (+134s)` | 2 | `100.0%` |
| **Route 26** | `+1.9 min (+111.0s)` | `+1.9 min (+111s)` | 2 | `100.0%` |
| **Route 1** | `+1.4 min (+83.0s)` | `+1.4 min (+83s)` | 1 | `100.0%` |
| **Route 19** | `+1.2 min (+70.0s)` | `+1.2 min (+70s)` | 2 | `100.0%` |
| **Route 48** | `+1.0 min (+58.0s)` | `+1.0 min (+58s)` | 2 | `100.0%` |
| **Route 51** | `+0.2 min (+13.0s)` | `+0.2 min (+13s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | ~71.0m | ~71.0m | **`+0.0 min`** | `74.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19237366` | Route 15 | `06:45:00` | `SCHEDULED` | Assigned vehicle 4123 is broadcasting off-schedule with no vehicle covering 19237366 |
| `19237370` | Route 15 | `07:45:00` | `SCHEDULED` | Assigned vehicle 4195 is broadcasting off-schedule with no vehicle covering 19237370 |
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
| `2026-11-23 07:00:18` | `92.98%` | `56.25%` | 527 | 157 | `-4840.6s` |
| `2026-11-23 06:30:18` | `91.09%` | `80.0%` | 539 | 150 | `+163.3s` |
| `2026-11-23 06:00:20` | `88.06%` | `80.0%` | 561 | 162 | `+182.4s` |
| `2026-11-23 05:30:18` | `84.67%` | `76.36%` | 587 | 176 | `+199.3s` |
| `2026-11-23 05:00:19` | `5.51%` | `82.46%` | 127 | 195 | `+2264.2s` |
| `2026-11-23 04:30:19` | `9.21%` | `72.22%` | 152 | 201 | `+305.1s` |
| `2026-11-23 04:00:19` | `8.29%` | `79.41%` | 181 | 217 | `+217.9s` |
| `2026-11-23 03:30:18` | `11.92%` | `79.49%` | 193 | 191 | `+194.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:18.429000+00:00`.*
