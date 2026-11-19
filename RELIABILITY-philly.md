# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-19T07:00:18.736000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.65%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2653` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `663` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2458` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2458 | 92.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 16 | 0.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 166 | 0 | 166 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 109 | 0 | 109 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 98 | 0 | 98 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 97 | 0 | 97 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 47 | 0 | 47 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 44 | 0 | 44 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `885574` | Route 55 | `25:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `885571` | Route 55 | `27:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993915` | Route 57 | `01:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `868944` | Route 14 | `02:08:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `966794` | Route 63 | `02:32:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891352` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `963348` | Route 42 | `02:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993918` | Route 57 | `02:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `868952` | Route 14 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `958676` | Route 68 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `976472` | Route 79 | `02:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996723` | Route 47 | `02:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996606` | Route 47 | `02:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976475` | Route 79 | `03:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 07:00:18` | `92.65%` | `0.0%` | 2653 | 663 | `+0.0s` |
| `2026-11-19 06:30:18` | `91.52%` | `0.0%` | 2688 | 684 | `+0.0s` |
| `2026-11-19 06:00:18` | `90.78%` | `0.0%` | 2733 | 677 | `+0.0s` |
| `2026-11-19 05:30:20` | `89.98%` | `0.0%` | 2765 | 704 | `+0.0s` |
| `2026-11-19 05:00:18` | `88.3%` | `0.0%` | 2760 | 730 | `+0.0s` |
| `2026-11-19 04:30:17` | `85.96%` | `0.0%` | 2793 | 753 | `+0.0s` |
| `2026-11-19 04:00:18` | `83.82%` | `0.0%` | 2837 | 794 | `+0.0s` |
| `2026-11-19 03:30:18` | `83.05%` | `0.0%` | 2867 | 838 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:18.736000+00:00`.*
