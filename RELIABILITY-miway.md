# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:21.309000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.77%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `394` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `56` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `334` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-87.0s` (`-1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-56.5s` (`-0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 334 | 84.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 89 | 4 | 84 | **`94.38%`** | `50.0%` | `-117.5s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-56.5s` |
| **Route 5** | 58 | 3 | 54 | **`93.1%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `86.9 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30801043` | Route 103 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801071` | Route 103 | `07:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801059` | Route 103 | `21:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801044` | Route 103 | `22:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801045` | Route 103 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801042` | Route 103 | `20:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801041` | Route 103 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801069` | Route 103 | `08:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801095` | Route 103 | `11:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801054` | Route 103 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801057` | Route 103 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801056` | Route 103 | `19:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801083` | Route 103 | `12:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801084` | Route 103 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801086` | Route 103 | `16:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:21` | `84.77%` | `50.0%` | 394 | 56 | `-87.0s` |
| `2026-11-04 06:30:33` | `79.76%` | `50.0%` | 420 | 80 | `-107.3s` |
| `2026-11-04 06:00:18` | `77.42%` | `58.33%` | 434 | 89 | `-49.2s` |
| `2026-11-04 05:30:18` | `6.48%` | `28.57%` | 108 | 100 | `-96.1s` |
| `2026-11-04 05:00:17` | `7.75%` | `62.5%` | 129 | 117 | `-73.6s` |
| `2026-11-04 04:30:18` | `9.93%` | `0.0%` | 141 | 127 | `-101.4s` |
| `2026-11-04 04:00:25` | `11.46%` | `12.5%` | 157 | 138 | `-177.8s` |
| `2026-11-04 03:30:21` | `12.87%` | `11.11%` | 171 | 149 | `-554.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:21.309000+00:00`.*
