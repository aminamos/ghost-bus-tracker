# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:23.310000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`77.55%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `79` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `40` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+6.6s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+14.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 38 | 48.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 11.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 16.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.7 min` |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 009** | 12 | 5 | 3 | **`25.0%`** | `57.14%` | `+1.2 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+1.6 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `90.0%` | `+0.1 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `75.0%` | `-134.6s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-22.0s` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-165.5s` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `-42.2s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 715** | `+7.0 min (+423.0s)` | `+7.0 min (+423s)` | 1 | `0.0%` |
| **Route 052** | `+4.3 min (+256.0s)` | `+4.3 min (+256s)` | 1 | `100.0%` |
| **Route 523** | `+2.8 min (+170.0s)` | `+2.8 min (+170s)` | 1 | `100.0%` |
| **Route 002** | `+1.6 min (+97.0s)` | `+4.3 min (+261s)` | 8 | `100.0%` |
| **Route 009** | `+1.2 min (+74.7s)` | `+6.4 min (+382s)` | 5 | `57.14%` |
| **Route 903** | `+0.7 min (+40.5s)` | `+1.1 min (+66s)` | 2 | `100.0%` |
| **Route 721** | `+0.7 min (+40.0s)` | `+0.7 min (+40s)` | 1 | `100.0%` |
| **Route 004** | `+0.1 min (+7.8s)` | `+1.3 min (+79s)` | 7 | `90.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `73.3 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `89.4 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `89.5 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.9 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.9 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33299504` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 3065 is missing from active GPS transponder fleet |
| `33291425` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33291427` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33291426` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33296068` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33296066` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33295735` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33295734` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33301548` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33301550` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33301549` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33295736` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33296067` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:23` | `16.46%` | `77.55%` | 79 | 40 | `+6.6s` |
| `2026-11-13 06:30:18` | `16.8%` | `77.91%` | 125 | 73 | `+9.4s` |
| `2026-11-13 06:00:32` | `12.5%` | `88.82%` | 200 | 112 | `+56.9s` |
| `2026-11-13 05:30:20` | `14.73%` | `79.62%` | 258 | 123 | `+56.2s` |
| `2026-11-13 05:00:25` | `17.43%` | `88.8%` | 304 | 135 | `+64.7s` |
| `2026-11-13 04:30:18` | `21.28%` | `84.62%` | 343 | 149 | `+75.0s` |
| `2026-11-13 04:00:25` | `18.97%` | `81.34%` | 464 | 234 | `+58.7s` |
| `2026-11-13 03:30:19` | `18.78%` | `83.56%` | 575 | 267 | `+47.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:23.310000+00:00`.*
