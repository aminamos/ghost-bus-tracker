# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:20.384000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`78.72%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `79` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `17` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+23.1s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+25.0s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 46.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 11.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 17 | 21.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.2 min` |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route 004** | 19 | 8 | 7 | **`36.84%`** | `90.91%` | `+2.0 min` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `71.43%` | `+0.3 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+1.6 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `77.78%` | `-59.1s` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-56.4s` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-117.5s` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 523** | `+3.1 min (+187.0s)` | `+3.1 min (+187s)` | 1 | `100.0%` |
| **Route 004** | `+2.0 min (+121.8s)` | `+6.5 min (+387s)` | 8 | `90.91%` |
| **Route 002** | `+1.6 min (+97.6s)` | `+4.2 min (+251s)` | 8 | `100.0%` |
| **Route 056** | `+0.8 min (+47.0s)` | `+1.5 min (+90s)` | 2 | `100.0%` |
| **Route 903** | `+0.4 min (+26.5s)` | `+1.4 min (+81s)` | 2 | `100.0%` |
| **Route 009** | `+0.3 min (+20.4s)` | `+3.8 min (+226s)` | 4 | `71.43%` |
| **Route 721** | `+0.2 min (+10.0s)` | `+0.2 min (+10s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `83.8 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.8 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `90.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.6 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `94.6 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.1 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32763447` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 3376 is missing from active GPS transponder fleet |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904552` | Route 004 | `26:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904550` | Route 004 | `25:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33106705` | Route 004 | `26:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:20` | `21.52%` | `78.72%` | 79 | 38 | `+23.1s` |
| `2026-11-27 06:30:22` | `17.83%` | `80.68%` | 129 | 74 | `+43.5s` |
| `2026-11-27 06:00:18` | `15.2%` | `92.81%` | 204 | 113 | `+60.7s` |
| `2026-11-27 05:30:20` | `16.14%` | `86.14%` | 254 | 119 | `+73.2s` |
| `2026-11-27 05:00:17` | `18.21%` | `87.45%` | 302 | 133 | `+80.4s` |
| `2026-11-27 04:30:20` | `19.29%` | `84.67%` | 337 | 146 | `+115.4s` |
| `2026-11-27 04:00:18` | `19.78%` | `83.9%` | 460 | 230 | `+96.5s` |
| `2026-11-27 03:30:24` | `18.25%` | `84.47%` | 559 | 263 | `+73.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:20.384000+00:00`.*
