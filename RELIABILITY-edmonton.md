# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-02T07:00:18.454000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.49%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `57` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `24` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+15.0s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+10.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 57.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 14.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 19.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 15 | 6 | 5 | **`33.33%`** | `100.0%` | `+1.2 min` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `85.71%` | `+0.3 min` |
| **Route 002** | 14 | 5 | 3 | **`21.43%`** | `88.89%` | `-0.1s` |
| **Route 008** | 10 | 5 | 0 | **`0.0%`** | `40.0%` | `-61.9s` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 511** | `+2.2 min (+130.7s)` | `+4.0 min (+238s)` | 2 | `100.0%` |
| **Route 004** | `+1.2 min (+73.5s)` | `+3.8 min (+225s)` | 6 | `100.0%` |
| **Route 056** | `+0.6 min (+37.0s)` | `+0.6 min (+37s)` | 1 | `100.0%` |
| **Route 009** | `+0.3 min (+17.0s)` | `+1.4 min (+84s)` | 4 | `85.71%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.1 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 511** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.1 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.6 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.1 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32754185` | Route 004 | `23:57:00` | `SCHEDULED` | Assigned vehicle 2408 is broadcasting off-schedule with no vehicle covering 32754185 |
| `32754189` | Route 004 | `25:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753578` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753581` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754197` | Route 004 | `26:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754188` | Route 004 | `25:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754005` | Route 009 | `26:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754004` | Route 009 | `26:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754003` | Route 009 | `25:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754190` | Route 004 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753579` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `19.3%` | `80.49%` | 57 | 24 | `+15.0s` |
| `2026-11-02 06:30:18` | `16.67%` | `66.67%` | 84 | 47 | `+26.4s` |
| `2026-11-02 06:00:23` | `13.39%` | `77.32%` | 127 | 77 | `+18.3s` |
| `2026-11-02 05:30:24` | `15.14%` | `78.47%` | 185 | 88 | `+36.4s` |
| `2026-11-02 05:00:19` | `16.59%` | `75.56%` | 229 | 106 | `+37.7s` |
| `2026-11-02 04:30:21` | `19.85%` | `72.96%` | 262 | 114 | `+58.1s` |
| `2026-11-02 04:00:18` | `22.22%` | `79.55%` | 297 | 122 | `+60.3s` |
| `2026-11-02 03:30:29` | `25.61%` | `81.36%` | 328 | 128 | `+44.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.454000+00:00`.*
