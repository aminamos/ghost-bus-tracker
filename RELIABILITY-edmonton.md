# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-24T06:30:22.945000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.48%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.95%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `116` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `74` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+36.0s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+4.5s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 68 | 58.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 11.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 2.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 9.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 916** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-154.0s` |
| **Route 002** | 13 | 7 | 5 | **`38.46%`** | `100.0%` | `+1.3 min` |
| **Route 004** | 15 | 8 | 4 | **`26.67%`** | `100.0%` | `+0.8 min` |
| **Route 008** | 10 | 7 | 0 | **`0.0%`** | `77.78%` | `+0.7 min` |
| **Route 107** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-10.5s` |
| **Route 109** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.5 min` |
| **Route 053** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-15.5s` |
| **Route 005** | 7 | 6 | 0 | **`0.0%`** | `85.71%` | `-18.3s` |
| **Route 901** | 4 | 3 | 0 | **`0.0%`** | `25.0%` | `-74.0s` |
| **Route 052** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 709** | `+4.9 min (+292.0s)` | `+5.8 min (+346s)` | 1 | `50.0%` |
| **Route 009** | `+4.7 min (+284.0s)` | `+10.3 min (+616s)` | 5 | `50.0%` |
| **Route 119** | `+4.4 min (+264.0s)` | `+4.4 min (+264s)` | 1 | `100.0%` |
| **Route 716** | `+4.2 min (+252.0s)` | `+4.2 min (+252s)` | 1 | `100.0%` |
| **Route 007** | `+2.3 min (+139.8s)` | `+5.0 min (+300s)` | 4 | `100.0%` |
| **Route 052** | `+1.7 min (+100.0s)` | `+2.5 min (+152s)` | 2 | `100.0%` |
| **Route 519** | `+1.6 min (+93.5s)` | `+1.8 min (+108s)` | 2 | `100.0%` |
| **Route 918B** | `+1.5 min (+90.0s)` | `+1.5 min (+90s)` | 1 | `100.0%` |
| **Route 109** | `+1.5 min (+89.5s)` | `+4.1 min (+246s)` | 2 | `50.0%` |
| **Route 002** | `+1.3 min (+78.8s)` | `+3.2 min (+193s)` | 7 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `88.6 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `89.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.5 / 100` |
| **Route 903** | ~60.0m | ~60.0m | **`+0.0 min`** | `97.0 / 100` |
| **Route 008** | ~29.5m | ~29.5m | **`+0.0 min`** | `98.0 / 100` |
| **Route 901** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.9 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32762449` | Route 518 | `23:38:00` | `SCHEDULED` | Assigned vehicle 2267 is broadcasting off-schedule with no vehicle covering 32762449 |
| `32763923` | Route 916 | `23:59:00` | `SCHEDULED` | Assigned vehicle 2534 is missing from active GPS transponder fleet |
| `32904643` | Route 004 | `25:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760328` | Route 002 | `24:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760329` | Route 002 | `25:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `9.48%` | `80.95%` | 116 | 74 | `+36.0s` |
| `2026-10-24 05:30:20` | `12.3%` | `85.07%` | 244 | 122 | `+60.4s` |
| `2026-10-24 05:00:23` | `13.99%` | `88.02%` | 293 | 134 | `+80.1s` |
| `2026-10-24 04:30:21` | `16.82%` | `86.26%` | 333 | 149 | `+73.1s` |
| `2026-10-24 04:00:22` | `16.4%` | `84.31%` | 445 | 231 | `+54.4s` |
| `2026-10-24 03:00:21` | `20.53%` | `83.44%` | 643 | 268 | `+47.7s` |
| `2026-10-24 02:00:24` | `26.23%` | `81.71%` | 732 | 279 | `+72.9s` |
| `2026-10-24 01:30:24` | `29.27%` | `82.98%` | 772 | 288 | `+123.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.945000+00:00`.*
