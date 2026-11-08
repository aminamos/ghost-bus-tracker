# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.255000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`88.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `268` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `31` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `237` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-68.8s` (`-1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-39.5s` (`-0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 237 | 88.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 56 | 0 | 56 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 45 | 0 | 45 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 41 | 0 | 41 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 61 | 5 | 55 | **`90.16%`** | `50.0%` | `-68.8s` |
| **Route 3** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 1** | ~20.0m | ~20.0m | **`+0.0 min`** | `93.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30734736` | Route 3 | `26:10:00` | `SCHEDULED` | Assigned vehicle 4312 is broadcasting off-schedule with no vehicle covering 30734736 |
| `30734883` | Route 1 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798419` | Route 17 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798398` | Route 17 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798425` | Route 17 | `19:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798424` | Route 17 | `16:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798415` | Route 17 | `14:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798410` | Route 17 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798418` | Route 17 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798413` | Route 17 | `13:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798397` | Route 17 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798422` | Route 17 | `18:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798420` | Route 17 | `12:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798412` | Route 17 | `11:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30798417` | Route 17 | `09:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `88.43%` | `50.0%` | 268 | 31 | `-68.8s` |
| `2026-11-08 06:30:20` | `82.99%` | `33.33%` | 288 | 49 | `-47.0s` |
| `2026-11-08 06:00:18` | `80.07%` | `33.33%` | 301 | 60 | `-7.2s` |
| `2026-11-08 05:30:20` | `11.11%` | `71.43%` | 81 | 71 | `-7.9s` |
| `2026-11-08 05:00:18` | `12.0%` | `75.0%` | 100 | 86 | `+65.9s` |
| `2026-11-08 04:30:26` | `13.91%` | `57.14%` | 115 | 98 | `-44.6s` |
| `2026-11-08 04:00:19` | `13.87%` | `47.37%` | 137 | 116 | `+46.4s` |
| `2026-11-08 03:30:18` | `14.94%` | `53.85%` | 154 | 128 | `-27.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.255000+00:00`.*
