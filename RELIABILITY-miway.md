# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** Mississauga | **Location:** Mississauga, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:57.954000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.98%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`24.06%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `368` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `346` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `22` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-176.5s` (`-2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-203.0s` (`-3.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 83 | 22.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 235 | 63.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 26 | 7.1% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 22 | 6.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 7** | 29 | 7 | 22 | **`75.86%`** | `14.29%` | `-227.1s` |
| **Route 103** | 6 | 6 | 0 | **`0.0%`** | `16.67%` | `+31.7 min` |
| **Route 1** | 11 | 11 | 0 | **`0.0%`** | `9.09%` | `-157.0s` |
| **Route 110** | 9 | 9 | 0 | **`0.0%`** | `33.33%` | `-177.9s` |
| **Route 53** | 6 | 6 | 0 | **`0.0%`** | `16.67%` | `-356.2s` |
| **Route 101** | 9 | 9 | 0 | **`0.0%`** | `0.0%` | `-414.4s` |
| **Route 8** | 7 | 7 | 0 | **`0.0%`** | `14.29%` | `-342.6s` |
| **Route 2** | 14 | 14 | 0 | **`0.0%`** | `28.57%` | `+2.8 min` |
| **Route 45** | 8 | 8 | 0 | **`0.0%`** | `0.0%` | `-419.2s` |
| **Route 109** | 11 | 11 | 0 | **`0.0%`** | `54.55%` | `-108.4s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 103** | `+31.7 min (+1903.0s)` | `+216.1 min (+12965s)` | 6 | `16.67%` |
| **Route 49** | `+10.3 min (+618.0s)` | `+10.3 min (+618s)` | 1 | `0.0%` |
| **Route 321** | `+6.5 min (+391.0s)` | `+6.5 min (+391s)` | 1 | `0.0%` |
| **Route 126** | `+4.9 min (+295.6s)` | `+12.7 min (+763s)` | 8 | `50.0%` |
| **Route 2** | `+2.8 min (+166.7s)` | `+13.4 min (+807s)` | 14 | `28.57%` |
| **Route 22** | `+2.0 min (+118.5s)` | `+4.7 min (+284s)` | 2 | `100.0%` |
| **Route 312** | `+1.1 min (+69.0s)` | `+1.1 min (+69s)` | 1 | `100.0%` |
| **Route 74** | `+0.4 min (+23.0s)` | `+0.4 min (+23s)` | 1 | `100.0%` |
| **Route 135** | `+0.0 min (+0.3s)` | `+1.1 min (+63s)` | 7 | `85.71%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 103** | ~28.0m | ~28.0m | **`+2.7 min`** | `0.0 / 100` |
| **Route 13** | ~4.5m | ~4.5m | **`+0.1 min`** | `0.0 / 100` |
| **Route 2** | ~8.5m | ~8.5m | **`+0.1 min`** | `7.1 / 100` |
| **Route 35** | ~12.0m | ~12.0m | **`+0.1 min`** | `22.9 / 100` |
| **Route 28** | ~17.5m | ~17.5m | **`+0.0 min`** | `46.7 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `51.5 / 100` |
| **Route 39** | ~20.0m | ~20.0m | **`+0.0 min`** | `60.1 / 100` |
| **Route 57** | ~12.0m | ~12.0m | **`+0.0 min`** | `49.5 / 100` |
| **Route 4** | ~39.0m | ~39.0m | **`+0.0 min`** | `72.7 / 100` |
| **Route 101** | ~15.0m | ~15.0m | **`+0.0 min`** | `56.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30497004` | Route 7 | `21:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497008` | Route 7 | `24:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497001` | Route 7 | `20:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497006` | Route 7 | `22:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497010` | Route 7 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497000` | Route 7 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497005` | Route 7 | `22:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497009` | Route 7 | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30496996` | Route 7 | `18:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497002` | Route 7 | `20:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30496993` | Route 7 | `16:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30496999` | Route 7 | `19:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30496991` | Route 7 | `15:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30496997` | Route 7 | `18:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30497003` | Route 7 | `21:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:57.954000+00:00`.*
