# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T17:21:54.119970+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`29.37%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1532` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `618` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `450` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 450 | 29.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 6 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 121** | 10 | 0 | 10 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 93** | 70 | 2 | 67 | **`95.71%`** | `0.0%` | `+0.0s` |
| **Route 220** | 75 | 3 | 70 | **`93.33%`** | `0.0%` | `+0.0s` |
| **Route 742** | 115 | 3 | 103 | **`89.57%`** | `0.0%` | `+0.0s` |
| **Route 120** | 38 | 4 | 32 | **`84.21%`** | `0.0%` | `+0.0s` |
| **Route 442** | 23 | 3 | 19 | **`82.61%`** | `0.0%` | `+0.0s` |
| **Route 441** | 17 | 2 | 14 | **`82.35%`** | `0.0%` | `+0.0s` |
| **Route 132** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 88** | 6 | 3 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 68** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `78259528` | Route 93 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259557` | Route 93 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590835` | Route 742 | `07:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516522` | Route 442 | `21:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590900` | Route 742 | `24:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516574` | Route 442 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590700` | Route 742 | `07:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78942124_1` | Route 39 | `14:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78265973` | Route 93 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590710` | Route 742 | `09:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590754` | Route 742 | `06:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78267308` | Route 96 | `13:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590809` | Route 742 | `18:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 17:21:54` | `29.37%` | `0.0%` | 1532 | 618 | `+0.0s` |
| `2026-10-06 17:21:03` | `29.79%` | `0.0%` | 1534 | 611 | `+0.0s` |
| `2026-10-06 13:46:35` | `16.57%` | `0.0%` | 1430 | 630 | `+0.0s` |
| `2026-10-06 06:42:11` | `99.21%` | `0.0%` | 633 | 7 | `+0.0s` |
| `2026-10-06 00:28:46` | `36.12%` | `0.0%` | 1304 | 459 | `+0.0s` |
| `2026-10-05 18:39:11` | `19.98%` | `0.0%` | 1712 | 749 | `+0.0s` |
| `2026-10-05 18:02:18` | `25.7%` | `0.0%` | 1607 | 667 | `+0.0s` |
| `2026-10-05 17:57:48` | `26.29%` | `0.0%` | 1575 | 657 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T17:21:54.119970+00:00`.*
