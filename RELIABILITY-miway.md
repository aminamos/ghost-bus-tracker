# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-10T07:00:21.802000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.1%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `407` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `348` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-22.0s` (`-0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 9.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 19 | 4.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 348 | 85.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `66.67%` | `-28.0s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `80.0%` | `+0.1 min` |
| **Route 1** | 89 | 4 | 83 | **`93.26%`** | `66.67%` | `-33.2s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-28.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |
| **Route 23** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-1.0s` |
| **Route 31** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-178.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 61** | `+1.4 min (+85.0s)` | `+4.2 min (+250s)` | 4 | `100.0%` |
| **Route 48** | `+1.3 min (+76.0s)` | `+1.3 min (+76s)` | 1 | `100.0%` |
| **Route 9** | `+1.0 min (+57.5s)` | `+3.6 min (+214s)` | 2 | `50.0%` |
| **Route 46** | `+0.9 min (+55.0s)` | `+0.9 min (+55s)` | 1 | `100.0%` |
| **Route 42** | `+0.8 min (+45.0s)` | `+3.3 min (+197s)` | 3 | `66.67%` |
| **Route 3** | `+0.6 min (+35.0s)` | `+1.0 min (+59s)` | 3 | `100.0%` |
| **Route 36** | `+0.4 min (+23.0s)` | `+1.1 min (+69s)` | 2 | `100.0%` |
| **Route 23** | `+0.3 min (+20.0s)` | `+0.8 min (+48s)` | 2 | `100.0%` |
| **Route 11** | `+0.2 min (+13.0s)` | `+1.5 min (+89s)` | 2 | `50.0%` |
| **Route 17** | `+0.1 min (+5.4s)` | `+1.5 min (+89s)` | 3 | `80.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 42** | ~15.0m | ~15.0m | **`+0.0 min`** | `86.9 / 100` |
| **Route 51** | ~35.0m | ~35.0m | **`+0.0 min`** | `93.8 / 100` |
| **Route 61** | ~18.0m | ~18.0m | **`+0.0 min`** | `91.0 / 100` |
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `92.2 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 7** | ~1400.0m | ~1400.0m | **`+0.0 min`** | `99.7 / 100` |
| **Route 35** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.1 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `96.3 / 100` |
| **Route 61** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.5 / 100` |
| **Route 7** | ~35.0m | ~35.0m | **`+0.0 min`** | `99.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30729909` | Route 101 | `06:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729919` | Route 101 | `09:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729929` | Route 101 | `11:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729941` | Route 101 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729924` | Route 101 | `10:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729934` | Route 101 | `12:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729936` | Route 101 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729930` | Route 101 | `11:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729944` | Route 101 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729955` | Route 101 | `18:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729963` | Route 101 | `20:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729939` | Route 101 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729949` | Route 101 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729965` | Route 101 | `21:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729916` | Route 101 | `08:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:21` | `85.5%` | `66.1%` | 407 | 54 | `-22.0s` |
| `2026-11-10 06:30:19` | `79.72%` | `71.43%` | 434 | 79 | `-2.7s` |
| `2026-11-10 06:00:18` | `77.78%` | `84.62%` | 450 | 90 | `-18.1s` |
| `2026-11-10 05:30:21` | `5.71%` | `60.0%` | 105 | 99 | `-33.6s` |
| `2026-11-10 05:00:19` | `6.4%` | `80.0%` | 125 | 115 | `+3.2s` |
| `2026-11-10 04:30:20` | `7.91%` | `35.29%` | 139 | 127 | `+118.7s` |
| `2026-11-10 04:00:19` | `10.39%` | `48.44%` | 154 | 137 | `-16.9s` |
| `2026-11-10 03:30:25` | `11.56%` | `45.75%` | 173 | 153 | `-46.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:21.802000+00:00`.*
