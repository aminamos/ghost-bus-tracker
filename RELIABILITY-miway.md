# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:24.621000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `536` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `478` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-56.2s` (`-0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-34.5s` (`-0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 0.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 478 | 89.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 119 | 2 | 116 | **`97.48%`** | `50.0%` | `-75.0s` |
| **Route 1** | 88 | 3 | 84 | **`95.45%`** | `50.0%` | `-34.5s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-59.0s` |
| **Route 31** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 2** | ~10.0m | ~10.0m | **`+0.0 min`** | `87.5 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.1 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `96.2 / 100` |

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
| `2026-11-26 07:00:24` | `89.18%` | `50.0%` | 536 | 54 | `-56.2s` |
| `2026-11-26 06:30:20` | `85.08%` | `58.33%` | 563 | 78 | `-79.2s` |
| `2026-11-26 06:00:19` | `83.88%` | `71.43%` | 577 | 88 | `-39.6s` |
| `2026-11-26 05:30:24` | `10.81%` | `33.33%` | 111 | 99 | `-67.8s` |
| `2026-11-26 05:00:18` | `10.45%` | `76.92%` | 134 | 117 | `+74.2s` |
| `2026-11-26 04:30:21` | `14.09%` | `50.0%` | 149 | 127 | `+5.2s` |
| `2026-11-26 04:00:20` | `16.36%` | `69.23%` | 165 | 137 | `-48.8s` |
| `2026-11-26 03:30:20` | `18.58%` | `75.0%` | 183 | 148 | `-24.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:24.621000+00:00`.*
