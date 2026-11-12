# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-12T07:00:20.363000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`85.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `407` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `348` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-67.8s` (`-1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-36.5s` (`-0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 0.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 348 | 85.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `50.0%` | `-104.5s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-36.5s` |
| **Route 1** | 90 | 5 | 83 | **`92.22%`** | `50.0%` | `-62.5s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `88.4 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `93.1 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30729949` | Route 101 | `16:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729939` | Route 101 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729929` | Route 101 | `11:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729919` | Route 101 | `09:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729931` | Route 101 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729944` | Route 101 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729934` | Route 101 | `12:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729946` | Route 101 | `15:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729950` | Route 101 | `16:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729924` | Route 101 | `10:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729914` | Route 101 | `07:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729904` | Route 101 | `05:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729936` | Route 101 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729909` | Route 101 | `06:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30729906` | Route 101 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:20` | `85.5%` | `50.0%` | 407 | 54 | `-67.8s` |
| `2026-11-12 06:30:19` | `79.95%` | `78.57%` | 434 | 79 | `-23.8s` |
| `2026-11-12 06:00:19` | `77.95%` | `77.78%` | 449 | 89 | `-21.2s` |
| `2026-11-12 05:30:19` | `8.11%` | `55.56%` | 111 | 101 | `-53.3s` |
| `2026-11-12 05:00:18` | `9.7%` | `50.0%` | 134 | 119 | `+36.7s` |
| `2026-11-12 04:30:19` | `12.16%` | `37.5%` | 148 | 130 | `-100.5s` |
| `2026-11-12 04:00:19` | `14.02%` | `55.56%` | 164 | 140 | `-66.6s` |
| `2026-11-12 03:30:19` | `15.47%` | `20.0%` | 181 | 154 | `-71.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:20.363000+00:00`.*
