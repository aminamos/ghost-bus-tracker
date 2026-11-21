# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.742000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`83.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`33.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `326` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `273` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-112.3s` (`-1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-93.0s` (`-1.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 273 | 83.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 64 | 2 | 62 | **`96.88%`** | `100.0%` | `+1.6 min` |
| **Route 5** | 58 | 2 | 56 | **`96.55%`** | `0.0%` | `-343.0s` |
| **Route 1** | 73 | 4 | 68 | **`93.15%`** | `0.0%` | `-93.0s` |
| **Route 31** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+1.6 min (+99.0s)` | `+1.6 min (+99s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30798197` | Route 17 | `21:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798203` | Route 17 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798198` | Route 17 | `20:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798200` | Route 17 | `18:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798205` | Route 17 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798204` | Route 17 | `16:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798229` | Route 17 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798231` | Route 17 | `14:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798225` | Route 17 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798213` | Route 17 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798208` | Route 17 | `12:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798210` | Route 17 | `11:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798237` | Route 17 | `19:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798233` | Route 17 | `18:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798230` | Route 17 | `17:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `83.74%` | `33.33%` | 326 | 52 | `-112.3s` |
| `2026-11-21 06:30:33` | `77.53%` | `42.86%` | 356 | 80 | `-103.3s` |
| `2026-11-21 06:00:18` | `75.68%` | `28.57%` | 370 | 89 | `-138.6s` |
| `2026-11-21 05:30:18` | `8.18%` | `44.44%` | 110 | 99 | `-53.4s` |
| `2026-11-21 05:00:20` | `9.77%` | `54.55%` | 133 | 117 | `-72.5s` |
| `2026-11-21 04:30:18` | `12.5%` | `25.0%` | 144 | 125 | `-162.8s` |
| `2026-11-21 04:00:18` | `13.5%` | `58.33%` | 163 | 137 | `-117.5s` |
| `2026-11-21 03:30:18` | `15.64%` | `50.0%` | 179 | 148 | `-19.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.742000+00:00`.*
