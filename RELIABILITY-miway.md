# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:33.421000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.09%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `285` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `271` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 271 | 95.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 62 | 0 | 62 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 55 | 0 | 55 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 71 | 4 | 67 | **`94.37%`** | `0.0%` | `+0.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `30798204` | Route 17 | `16:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798205` | Route 17 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798200` | Route 17 | `18:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798198` | Route 17 | `20:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798197` | Route 17 | `21:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798203` | Route 17 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798224` | Route 17 | `09:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798228` | Route 17 | `11:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798236` | Route 17 | `22:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798234` | Route 17 | `23:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798235` | Route 17 | `24:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798239` | Route 17 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798256` | Route 17 | `06:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798227` | Route 17 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798226` | Route 17 | `12:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:33` | `95.09%` | `0.0%` | 285 | 14 | `+0.0s` |
| `2026-10-31 06:30:19` | `90.37%` | `0.0%` | 301 | 29 | `+0.0s` |
| `2026-10-31 06:00:20` | `83.18%` | `75.0%` | 327 | 54 | `+15.2s` |
| `2026-10-31 05:30:21` | `77.62%` | `57.14%` | 353 | 78 | `-43.9s` |
| `2026-10-31 05:00:33` | `75.07%` | `58.33%` | 369 | 89 | `-0.6s` |
| `2026-10-31 04:30:22` | `8.11%` | `12.5%` | 111 | 101 | `-124.4s` |
| `2026-10-31 04:00:18` | `9.16%` | `75.0%` | 131 | 116 | `+5.1s` |
| `2026-10-31 03:30:18` | `12.41%` | `33.33%` | 145 | 128 | `-122.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:33.421000+00:00`.*
