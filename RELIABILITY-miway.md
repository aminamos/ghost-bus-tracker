# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-11T07:00:19.013000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.79%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `407` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `348` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-22.1s` (`-0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-17.0s` (`-0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 9.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 20 | 4.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 348 | 85.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `66.67%` | `-70.7s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `80.0%` | `+0.0 min` |
| **Route 1** | 89 | 4 | 83 | **`93.26%`** | `83.33%` | `-36.2s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-33.5s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 61** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+0.3 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-131.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7** | `+3.4 min (+202.0s)` | `+15.4 min (+926s)` | 4 | `50.0%` |
| **Route 9** | `+2.7 min (+160.5s)` | `+4.0 min (+243s)` | 2 | `100.0%` |
| **Route 36** | `+1.8 min (+110.5s)` | `+3.5 min (+212s)` | 2 | `100.0%` |
| **Route 48** | `+1.3 min (+76.0s)` | `+1.3 min (+76s)` | 1 | `100.0%` |
| **Route 61** | `+0.3 min (+16.0s)` | `+2.6 min (+158s)` | 4 | `50.0%` |
| **Route 6** | `+0.1 min (+6.0s)` | `+0.4 min (+24s)` | 2 | `100.0%` |
| **Route 17** | `+0.0 min (+1.6s)` | `+2.7 min (+163s)` | 3 | `80.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7** | ~35.0m | ~35.0m | **`+0.0 min`** | `78.4 / 100` |
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `83.4 / 100` |
| **Route 42** | ~15.0m | ~15.0m | **`+0.0 min`** | `87.7 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.7 / 100` |
| **Route 61** | ~18.0m | ~18.0m | **`+0.0 min`** | `96.2 / 100` |
| **Route 26** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 51** | ~35.0m | ~35.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 7** | ~1400.0m | ~1400.0m | **`+0.0 min`** | `99.7 / 100` |
| **Route 35** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.5 / 100` |
| **Route 26** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30800008` | Route 5 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800007` | Route 5 | `14:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800006` | Route 5 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800004` | Route 5 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800003` | Route 5 | `04:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799992` | Route 5 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799990` | Route 5 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800005` | Route 5 | `09:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800001` | Route 5 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799991` | Route 5 | `03:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799994` | Route 5 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799995` | Route 5 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799993` | Route 5 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799987` | Route 5 | `23:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799944` | Route 5 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-11 07:00:19` | `85.5%` | `63.79%` | 407 | 54 | `-22.1s` |
| `2026-11-11 06:30:18` | `79.82%` | `54.55%` | 436 | 81 | `-45.7s` |
| `2026-11-11 06:00:26` | `77.78%` | `76.19%` | 450 | 90 | `-12.2s` |
| `2026-11-11 05:30:20` | `9.17%` | `14.29%` | 109 | 99 | `-113.0s` |
| `2026-11-11 05:00:20` | `9.85%` | `63.64%` | 132 | 117 | `+5.4s` |
| `2026-11-11 04:30:18` | `12.24%` | `22.22%` | 147 | 129 | `-54.1s` |
| `2026-11-11 04:00:18` | `14.11%` | `22.22%` | 163 | 139 | `-145.7s` |
| `2026-11-11 03:30:33` | `14.92%` | `30.77%` | 181 | 153 | `-60.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:19.013000+00:00`.*
