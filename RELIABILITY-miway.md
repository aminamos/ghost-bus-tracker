# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.959000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`83.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `335` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `280` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-45.0s` (`-0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-43.0s` (`-0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 280 | 83.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 88 | 3 | 84 | **`95.45%`** | `50.0%` | `-47.0s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `50.0%` | `-43.0s` |
| **Route 9** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `94.8 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30801042` | Route 103 | `20:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801058` | Route 103 | `25:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801055` | Route 103 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801041` | Route 103 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801059` | Route 103 | `21:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801056` | Route 103 | `19:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801057` | Route 103 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801054` | Route 103 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801053` | Route 103 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801075` | Route 103 | `06:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801043` | Route 103 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801074` | Route 103 | `08:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801084` | Route 103 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801112` | Route 103 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801052` | Route 103 | `11:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `83.58%` | `50.0%` | 335 | 52 | `-45.0s` |
| `2026-11-25 06:30:19` | `77.41%` | `62.5%` | 363 | 78 | `-80.1s` |
| `2026-11-25 06:00:19` | `74.6%` | `75.0%` | 378 | 89 | `-54.0s` |
| `2026-11-25 05:30:18` | `7.34%` | `40.0%` | 109 | 101 | `-93.2s` |
| `2026-11-25 05:00:18` | `7.81%` | `55.56%` | 128 | 116 | `+8.4s` |
| `2026-11-25 04:30:18` | `10.0%` | `71.43%` | 140 | 126 | `+4.3s` |
| `2026-11-25 04:00:19` | `11.32%` | `55.56%` | 159 | 140 | `-24.3s` |
| `2026-11-25 03:30:26` | `13.37%` | `30.0%` | 172 | 150 | `+181.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.959000+00:00`.*
