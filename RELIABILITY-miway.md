# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:20.391000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.54%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `478` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `50` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `428` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+58.4s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-22.0s` (`-0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 4 | 0.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 428 | 89.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 23 | 0 | 23 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 80 | 2 | 78 | **`97.5%`** | `100.0%` | `+3.5 min` |
| **Route 17** | 64 | 2 | 62 | **`96.88%`** | `100.0%` | `-25.0s` |
| **Route 23** | 53 | 2 | 51 | **`96.23%`** | `0.0%` | `-65.0s` |
| **Route 1** | 72 | 3 | 69 | **`95.83%`** | `100.0%` | `-22.0s` |
| **Route 35** | 61 | 3 | 58 | **`95.08%`** | `100.0%` | `+3.2 min` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 2** | `+3.5 min (+213.0s)` | `+3.5 min (+213s)` | 2 | `100.0%` |
| **Route 35** | `+3.2 min (+191.0s)` | `+3.2 min (+191s)` | 3 | `100.0%` |

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
| `30800280` | Route 23 | `26:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734831` | Route 1 | `08:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734824` | Route 1 | `06:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30735104` | Route 1 | `03:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734866` | Route 1 | `20:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734880` | Route 1 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734875` | Route 1 | `23:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734869` | Route 1 | `21:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734855` | Route 1 | `16:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734847` | Route 1 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734839` | Route 1 | `11:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30735102` | Route 1 | `03:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734883` | Route 1 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734878` | Route 1 | `24:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734873` | Route 1 | `22:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:20` | `89.54%` | `80.0%` | 478 | 50 | `+58.4s` |
| `2026-11-28 06:30:17` | `84.54%` | `55.56%` | 511 | 79 | `-23.2s` |
| `2026-11-28 06:00:18` | `82.39%` | `50.0%` | 528 | 89 | `-20.1s` |
| `2026-11-28 05:30:19` | `13.68%` | `58.33%` | 117 | 99 | `+84.8s` |
| `2026-11-28 05:00:20` | `15.11%` | `80.0%` | 139 | 115 | `+76.1s` |
| `2026-11-28 04:30:17` | `18.47%` | `64.71%` | 157 | 127 | `-44.3s` |
| `2026-11-28 04:00:20` | `20.69%` | `57.89%` | 174 | 136 | `+14.4s` |
| `2026-11-28 03:30:20` | `23.12%` | `61.11%` | 199 | 150 | `+96.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:20.391000+00:00`.*
