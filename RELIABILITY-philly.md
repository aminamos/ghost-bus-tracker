# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:18.132000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`77.08%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `925` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `611` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `713` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 713 | 77.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 40 | 4.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 103 | 0 | 103 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 120** | 14 | 0 | 14 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 73** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 31** | 61 | 1 | 60 | **`98.36%`** | `0.0%` | `+0.0s` |
| **Route 16** | 46 | 1 | 45 | **`97.83%`** | `0.0%` | `+0.0s` |
| **Route 40** | 41 | 1 | 40 | **`97.56%`** | `0.0%` | `+0.0s` |
| **Route 4** | 35 | 1 | 34 | **`97.14%`** | `0.0%` | `+0.0s` |
| **Route 43** | 23 | 1 | 22 | **`95.65%`** | `0.0%` | `+0.0s` |

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
| `5879` | Route 40 | `25:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1105` | Route 55 | `27:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869033` | Route 14 | `02:08:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `877143` | Route 37 | `02:21:00` | `SCHEDULED` | Assigned vehicle block_7351_schedBasedVehicle is missing from active GPS transponder fleet |
| `889096` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886050` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891392` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `938143` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `879577` | Route 42 | `02:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869095` | Route 14 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `977215` | Route 47 | `02:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `889113` | Route 63 | `03:09:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `885994` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891390` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `977216` | Route 47 | `03:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:18` | `77.08%` | `0.0%` | 925 | 611 | `+0.0s` |
| `2026-11-28 06:30:17` | `74.14%` | `0.0%` | 959 | 649 | `+0.0s` |
| `2026-11-28 06:00:17` | `73.87%` | `0.0%` | 999 | 672 | `+0.0s` |
| `2026-11-28 05:30:18` | `73.04%` | `0.0%` | 1020 | 687 | `+0.0s` |
| `2026-11-28 05:00:18` | `70.59%` | `0.0%` | 1037 | 687 | `+0.0s` |
| `2026-11-28 04:30:17` | `65.37%` | `0.0%` | 1080 | 717 | `+0.0s` |
| `2026-11-28 04:00:18` | `62.23%` | `0.0%` | 1120 | 745 | `+0.0s` |
| `2026-11-28 03:30:18` | `60.12%` | `0.0%` | 1166 | 777 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:18.132000+00:00`.*
