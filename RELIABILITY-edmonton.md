# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:23.316000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.11%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.42%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `76` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `37` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+217.2s` (`+3.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+21.0s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 41 | 53.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 5.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 2.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 17.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 002** | 14 | 7 | 4 | **`28.57%`** | `87.5%` | `+2.0 min` |
| **Route 009** | 11 | 4 | 3 | **`27.27%`** | `100.0%` | `+0.3 min` |
| **Route 004** | 15 | 8 | 3 | **`20.0%`** | `100.0%` | `+1.3 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-19.5s` |
| **Route 005** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `-51.2s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-86.0s` |
| **Route 722** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+74.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 722** | `+74.3 min (+4457.5s)` | `+74.5 min (+4473s)` | 1 | `0.0%` |
| **Route 002** | `+2.0 min (+120.0s)` | `+6.6 min (+397s)` | 7 | `87.5%` |
| **Route 918A** | `+1.3 min (+76.0s)` | `+1.3 min (+76s)` | 1 | `100.0%` |
| **Route 004** | `+1.3 min (+75.8s)` | `+4.4 min (+266s)` | 8 | `100.0%` |
| **Route 008** | `+0.4 min (+24.9s)` | `+4.7 min (+284s)` | 6 | `100.0%` |
| **Route 903** | `+0.4 min (+24.5s)` | `+0.4 min (+25s)` | 2 | `100.0%` |
| **Route 009** | `+0.3 min (+18.5s)` | `+1.4 min (+84s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.2 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33207115` | Route 002 | `24:23:00` | `SCHEDULED` | Assigned vehicle 2540 is missing from active GPS transponder fleet |
| `33206628` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33206630` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33207119` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33201544` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33201546` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33201545` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33207118` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33207120` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33206629` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33211317` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33211318` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33211316` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:23` | `17.11%` | `85.42%` | 76 | 37 | `+217.2s` |
| `2026-11-17 06:30:20` | `15.45%` | `75.29%` | 123 | 72 | `+71.8s` |
| `2026-11-17 06:00:24` | `11.73%` | `88.54%` | 196 | 112 | `+54.7s` |
| `2026-11-17 05:30:22` | `13.77%` | `82.67%` | 247 | 121 | `+53.6s` |
| `2026-11-17 05:00:18` | `14.73%` | `88.84%` | 292 | 134 | `+64.8s` |
| `2026-11-17 04:30:20` | `16.51%` | `83.21%` | 327 | 153 | `+73.1s` |
| `2026-11-17 04:00:19` | `15.99%` | `83.05%` | 444 | 233 | `+16.7s` |
| `2026-11-17 03:30:26` | `16.21%` | `81.53%` | 549 | 266 | `+15.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:23.316000+00:00`.*
