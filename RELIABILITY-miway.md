# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:20.393000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`90.12%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `607` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `547` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-12.3s` (`-0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 4 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 547 | 90.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 135** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 119 | 2 | 116 | **`97.48%`** | `100.0%` | `+0.5 min` |
| **Route 1** | 88 | 3 | 84 | **`95.45%`** | `50.0%` | `-34.0s` |
| **Route 35** | 66 | 3 | 62 | **`93.94%`** | `0.0%` | `+0.0s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-32.5s` |
| **Route 23** | 43 | 2 | 40 | **`93.02%`** | `0.0%` | `+0.0s` |
| **Route 42** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 2** | `+0.5 min (+29.5s)` | `+1.0 min (+59s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 2** | ~10.0m | ~10.0m | **`+0.0 min`** | `95.1 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `96.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30801167` | Route 135 | `15:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801042` | Route 103 | `20:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801072` | Route 103 | `07:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801068` | Route 103 | `09:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801045` | Route 103 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801071` | Route 103 | `07:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801052` | Route 103 | `11:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801053` | Route 103 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801054` | Route 103 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801057` | Route 103 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801056` | Route 103 | `19:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801044` | Route 103 | `22:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801081` | Route 103 | `07:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801124` | Route 103 | `21:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801059` | Route 103 | `21:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:20` | `90.12%` | `66.67%` | 607 | 54 | `-12.3s` |
| `2026-11-27 06:30:20` | `86.16%` | `75.0%` | 636 | 79 | `-43.3s` |
| `2026-11-27 06:00:18` | `84.56%` | `75.0%` | 654 | 90 | `-29.3s` |
| `2026-11-27 05:30:20` | `10.81%` | `83.33%` | 111 | 99 | `+64.5s` |
| `2026-11-27 05:00:17` | `10.53%` | `75.0%` | 133 | 116 | `+26.2s` |
| `2026-11-27 04:30:20` | `14.09%` | `63.64%` | 149 | 127 | `-8.7s` |
| `2026-11-27 04:00:17` | `16.27%` | `41.67%` | 166 | 138 | `-12.7s` |
| `2026-11-27 03:30:20` | `18.09%` | `42.86%` | 188 | 153 | `+45.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:20.393000+00:00`.*
