# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:18.252000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `408` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `55` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `348` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+132.1s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 4 | 1.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 0.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 348 | 85.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `50.0%` | `-140.5s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-39.5s` |
| **Route 1** | 90 | 5 | 83 | **`92.22%`** | `50.0%` | `+5.9 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+5.9 min (+354.2s)` | `+25.7 min (+1544s)` | 5 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | ~15.0m | ~15.0m | **`+0.1 min`** | `23.5 / 100` |
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `84.4 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30799990` | Route 5 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799992` | Route 5 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800001` | Route 5 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800005` | Route 5 | `09:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799963` | Route 5 | `08:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799991` | Route 5 | `03:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800008` | Route 5 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799970` | Route 5 | `05:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799994` | Route 5 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799995` | Route 5 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800007` | Route 5 | `14:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30800006` | Route 5 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799964` | Route 5 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799969` | Route 5 | `04:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799993` | Route 5 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `85.29%` | `50.0%` | 408 | 55 | `+132.1s` |
| `2026-11-06 06:30:19` | `80.18%` | `71.43%` | 434 | 79 | `-41.7s` |
| `2026-11-06 06:00:18` | `78.17%` | `68.75%` | 449 | 89 | `-29.8s` |
| `2026-11-06 05:30:20` | `9.26%` | `42.86%` | 108 | 98 | `-84.9s` |
| `2026-11-06 05:00:19` | `10.0%` | `66.67%` | 130 | 115 | `-15.6s` |
| `2026-11-06 04:30:20` | `12.41%` | `60.0%` | 145 | 127 | `+89.7s` |
| `2026-11-06 04:00:24` | `13.75%` | `60.0%` | 160 | 137 | `-77.8s` |
| `2026-11-06 03:30:21` | `14.84%` | `42.86%` | 182 | 154 | `+29.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.252000+00:00`.*
