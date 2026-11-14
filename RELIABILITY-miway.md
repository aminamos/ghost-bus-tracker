# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:19.351000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`33.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `321` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `47` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `274` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-108.3s` (`-1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-158.0s` (`-2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 274 | 85.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 64 | 2 | 62 | **`96.88%`** | `100.0%` | `+2.0 min` |
| **Route 5** | 58 | 2 | 56 | **`96.55%`** | `0.0%` | `-288.0s` |
| **Route 1** | 72 | 3 | 69 | **`95.83%`** | `0.0%` | `-158.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+2.0 min (+121.0s)` | `+2.0 min (+121s)` | 2 | `100.0%` |

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
| `30797877` | Route 5 | `24:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797872` | Route 5 | `13:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797868` | Route 5 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797867` | Route 5 | `17:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797876` | Route 5 | `16:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797880` | Route 5 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797883` | Route 5 | `20:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797882` | Route 5 | `22:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797890` | Route 5 | `11:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797891` | Route 5 | `13:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797892` | Route 5 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797893` | Route 5 | `17:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797894` | Route 5 | `19:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797889` | Route 5 | `21:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30797895` | Route 5 | `23:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `85.36%` | `33.33%` | 321 | 47 | `-108.3s` |
| `2026-11-14 06:30:22` | `78.19%` | `42.86%` | 353 | 77 | `-118.1s` |
| `2026-11-14 06:00:20` | `75.0%` | `44.44%` | 372 | 91 | `-84.2s` |
| `2026-11-14 05:30:18` | `9.26%` | `57.14%` | 108 | 98 | `-18.9s` |
| `2026-11-14 05:00:27` | `9.92%` | `90.0%` | 131 | 116 | `+76.0s` |
| `2026-11-14 04:30:18` | `12.24%` | `44.44%` | 147 | 129 | `-103.8s` |
| `2026-11-14 04:00:23` | `13.77%` | `50.0%` | 167 | 143 | `-74.4s` |
| `2026-11-14 03:30:18` | `14.81%` | `44.44%` | 189 | 161 | `-75.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.351000+00:00`.*
