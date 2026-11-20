# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:33.559000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`86.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `404` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `51` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `350` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-11.0s` (`-0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 350 | 86.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 71 | 1 | 70 | **`98.59%`** | `0.0%` | `+0.0s` |
| **Route 1** | 88 | 3 | 84 | **`95.45%`** | `50.0%` | `-51.5s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `100.0%` | `+0.5 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+0.5 min (+29.5s)` | `+1.0 min (+59s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `94.3 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30726651` | Route 1 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726898` | Route 1 | `04:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726724` | Route 1 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726718` | Route 1 | `23:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726711` | Route 1 | `21:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726702` | Route 1 | `18:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726691` | Route 1 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726680` | Route 1 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726670` | Route 1 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726660` | Route 1 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726689` | Route 1 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726678` | Route 1 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726668` | Route 1 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726710` | Route 1 | `20:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726701` | Route 1 | `18:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:33` | `86.63%` | `75.0%` | 404 | 51 | `-11.0s` |
| `2026-11-20 06:30:18` | `80.0%` | `58.33%` | 435 | 80 | `-61.1s` |
| `2026-11-20 06:00:20` | `77.61%` | `72.22%` | 451 | 91 | `-34.9s` |
| `2026-11-20 05:30:18` | `9.01%` | `62.5%` | 111 | 101 | `+173.9s` |
| `2026-11-20 05:00:20` | `9.77%` | `72.73%` | 133 | 118 | `+59.5s` |
| `2026-11-20 04:30:18` | `12.41%` | `50.0%` | 145 | 127 | `-49.4s` |
| `2026-11-20 04:00:18` | `14.11%` | `30.0%` | 163 | 139 | `-131.1s` |
| `2026-11-20 03:30:20` | `15.73%` | `75.0%` | 178 | 150 | `+124.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:33.559000+00:00`.*
