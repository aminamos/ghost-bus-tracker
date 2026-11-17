# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:22.615000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`86.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `405` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `349` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-67.7s` (`-1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-29.5s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 4 | 1.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 349 | 86.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `50.0%` | `-135.0s` |
| **Route 1** | 88 | 3 | 84 | **`95.45%`** | `100.0%` | `-29.5s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-38.5s` |
| **Route 23** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `85.0 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.8 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `96.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30726898` | Route 1 | `04:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726651` | Route 1 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726660` | Route 1 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726670` | Route 1 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726680` | Route 1 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726691` | Route 1 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726702` | Route 1 | `18:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726711` | Route 1 | `21:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726718` | Route 1 | `23:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726724` | Route 1 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726668` | Route 1 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726678` | Route 1 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726689` | Route 1 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726659` | Route 1 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726669` | Route 1 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:22` | `86.17%` | `66.67%` | 405 | 52 | `-67.7s` |
| `2026-11-17 06:30:19` | `79.95%` | `64.29%` | 434 | 79 | `-50.5s` |
| `2026-11-17 06:00:22` | `77.61%` | `72.22%` | 451 | 91 | `-53.4s` |
| `2026-11-17 05:30:20` | `9.17%` | `28.57%` | 109 | 99 | `-113.9s` |
| `2026-11-17 05:00:18` | `9.7%` | `50.0%` | 134 | 119 | `-76.6s` |
| `2026-11-17 04:30:20` | `12.41%` | `37.5%` | 145 | 127 | `-65.5s` |
| `2026-11-17 04:00:19` | `14.29%` | `33.33%` | 161 | 137 | `-89.2s` |
| `2026-11-17 03:30:23` | `15.25%` | `25.0%` | 177 | 150 | `-70.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:22.615000+00:00`.*
