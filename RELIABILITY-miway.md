# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:19.666000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `325` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `51` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `273` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-121.0s` (`-2.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-58.0s` (`-1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 273 | 84.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 64 | 2 | 62 | **`96.88%`** | `100.0%` | `-4.0s` |
| **Route 5** | 58 | 2 | 56 | **`96.55%`** | `0.0%` | `-301.0s` |
| **Route 1** | 73 | 4 | 68 | **`93.15%`** | `100.0%` | `-58.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |

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
| `30734855` | Route 1 | `16:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734847` | Route 1 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734839` | Route 1 | `11:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30735102` | Route 1 | `03:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734883` | Route 1 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734878` | Route 1 | `24:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734873` | Route 1 | `22:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734860` | Route 1 | `18:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734852` | Route 1 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734844` | Route 1 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734836` | Route 1 | `10:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734828` | Route 1 | `07:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734821` | Route 1 | `05:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734826` | Route 1 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30734820` | Route 1 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:19` | `84.0%` | `66.67%` | 325 | 51 | `-121.0s` |
| `2026-11-07 06:30:19` | `77.53%` | `28.57%` | 356 | 80 | `-34.9s` |
| `2026-11-07 06:00:20` | `75.0%` | `44.44%` | 372 | 91 | `-83.3s` |
| `2026-11-07 05:30:19` | `9.17%` | `66.67%` | 109 | 99 | `-24.0s` |
| `2026-11-07 05:00:19` | `9.85%` | `70.0%` | 132 | 117 | `-17.4s` |
| `2026-11-07 04:30:19` | `12.33%` | `33.33%` | 146 | 128 | `+112.7s` |
| `2026-11-07 04:00:23` | `12.96%` | `64.29%` | 162 | 138 | `-48.6s` |
| `2026-11-07 03:30:21` | `15.64%` | `52.94%` | 179 | 151 | `+2.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:19.666000+00:00`.*
