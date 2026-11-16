# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-16T07:00:21.948000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`20.97%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`83.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `62` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `25` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+48.9s` (`+0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+12.5s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 30 | 48.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 6.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 21.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 8 | 2 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 004** | 14 | 5 | 4 | **`28.57%`** | `88.89%` | `+0.4 min` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `100.0%` | `+0.6 min` |
| **Route 002** | 14 | 5 | 3 | **`21.43%`** | `88.89%` | `+1.7 min` |
| **Route 051** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 008** | 8 | 4 | 0 | **`0.0%`** | `75.0%` | `-49.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 103** | `+13.7 min (+824.0s)` | `+13.7 min (+824s)` | 1 | `0.0%` |
| **Route 002** | `+1.7 min (+103.7s)` | `+6.0 min (+358s)` | 5 | `88.89%` |
| **Route 009** | `+0.6 min (+38.1s)` | `+1.1 min (+66s)` | 4 | `100.0%` |
| **Route 004** | `+0.4 min (+24.3s)` | `+1.4 min (+84s)` | 5 | `88.89%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.1 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.0 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.7 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32753579` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754190` | Route 004 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752875` | Route 511 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752873` | Route 511 | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753942` | Route 009 | `26:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753941` | Route 009 | `26:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753940` | Route 009 | `25:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754188` | Route 004 | `25:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754197` | Route 004 | `26:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753578` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752874` | Route 511 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753581` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754189` | Route 004 | `25:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:21` | `20.97%` | `83.33%` | 62 | 25 | `+48.9s` |
| `2026-11-16 06:30:31` | `23.86%` | `66.67%` | 88 | 46 | `+1410.5s` |
| `2026-11-16 06:00:20` | `16.28%` | `66.32%` | 129 | 75 | `+853.5s` |
| `2026-11-16 05:30:23` | `16.85%` | `70.71%` | 178 | 86 | `+563.2s` |
| `2026-11-16 05:00:23` | `15.91%` | `76.7%` | 220 | 104 | `+448.9s` |
| `2026-11-16 04:30:19` | `18.37%` | `75.0%` | 245 | 108 | `+445.9s` |
| `2026-11-16 04:00:20` | `19.27%` | `79.72%` | 275 | 121 | `+376.0s` |
| `2026-11-16 03:30:18` | `21.93%` | `77.09%` | 301 | 128 | `+312.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:21.948000+00:00`.*
