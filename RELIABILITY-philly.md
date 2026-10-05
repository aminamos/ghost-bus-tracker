# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-05T18:39:12.121959+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `898` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `613` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `14` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 14 | 1.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 271 | 30.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 71** | 8 | 6 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 79** | 6 | 5 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 16** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 81** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 9** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 4** | 8 | 4 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 88** | 9 | 4 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route K** | 9 | 8 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route 51** | 10 | 9 | 1 | **`10.0%`** | `0.0%` | `+0.0s` |
| **Route 40** | 12 | 11 | 1 | **`8.33%`** | `0.0%` | `+0.0s` |

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
| `869341` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993612` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `964091` | Route 40 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998282` | Route 51 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993735` | Route 57 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `975938` | Route 64 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `964846` | Route 65 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996978` | Route 71 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `997049` | Route 71 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976529` | Route 79 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `997161` | Route 81 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `894552` | Route 88 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `894957` | Route 9 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907782` | Route K | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 18:39:12` | `1.56%` | `0.0%` | 898 | 613 | `+0.0s` |
| `2026-10-05 18:02:19` | `1.33%` | `0.0%` | 830 | 549 | `+0.0s` |
| `2026-10-05 17:57:48` | `1.21%` | `0.0%` | 829 | 523 | `+0.0s` |
| `2026-10-05 17:20:38` | `0.81%` | `0.0%` | 743 | 499 | `+0.0s` |
| `2026-10-05 16:34:17` | `0.81%` | `0.0%` | 739 | 490 | `+0.0s` |
| `2026-10-05 12:15:25` | `0.41%` | `0.0%` | 974 | 667 | `+0.0s` |
| `2026-10-05 12:14:21` | `0.31%` | `0.0%` | 973 | 667 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:39:12.121959+00:00`.*
