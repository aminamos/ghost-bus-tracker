# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-09T07:00:19.796000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`90.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `20` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+87.4s` (`+1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+13.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 18 | 90.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 5.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 5.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 9899** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 77** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 20** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+2.8 min (+165.4s)` | `+11.0 min (+658s)` | 4 | `80.0%` |
| **Route 9899** | `+1.3 min (+78.6s)` | `+3.7 min (+220s)` | 3 | `100.0%` |
| **Route 77** | `+1.3 min (+78.6s)` | `+4.2 min (+255s)` | 3 | `100.0%` |
| **Route 107** | `+1.1 min (+63.0s)` | `+3.3 min (+200s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~23.0m | ~23.0m | **`+0.0 min`** | `81.5 / 100` |
| **Route 107** | ~10.0m | ~10.0m | **`+0.0 min`** | `86.7 / 100` |
| **Route 77** | ~20.0m | ~20.0m | **`+0.0 min`** | `91.4 / 100` |
| **Route 9899** | ~23.0m | ~23.0m | **`+0.0 min`** | `93.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `0.0%` | `90.0%` | 20 | 13 | `+87.4s` |
| `2026-11-09 06:30:22` | `12.0%` | `90.91%` | 25 | 15 | `+40.8s` |
| `2026-11-09 06:00:18` | `0.0%` | `80.0%` | 35 | 22 | `+5.5s` |
| `2026-11-09 05:30:18` | `8.16%` | `86.67%` | 49 | 34 | `+84.7s` |
| `2026-11-09 05:00:18` | `9.84%` | `90.91%` | 61 | 37 | `+51.5s` |
| `2026-11-09 04:30:19` | `10.53%` | `86.76%` | 76 | 41 | `+43.3s` |
| `2026-11-09 04:00:19` | `4.82%` | `91.14%` | 83 | 45 | `+106.3s` |
| `2026-11-09 03:30:18` | `5.56%` | `91.76%` | 90 | 50 | `+55.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.796000+00:00`.*
