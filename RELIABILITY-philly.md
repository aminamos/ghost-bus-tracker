# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:18.158000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.05%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2091` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `702` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1862` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1862 | 89.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 70 | 3.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 166 | 0 | 166 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 98 | 0 | 98 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 44 | 0 | 44 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
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
| `878827` | Route 40 | `25:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3039` | Route 79 | `01:56:00` | `SCHEDULED` | Assigned vehicle block_7602_schedBasedVehicle is missing from active GPS transponder fleet |
| `2661` | Route 63 | `02:32:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `3029` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `5425` | Route 42 | `02:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1504` | Route 57 | `02:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3033` | Route 68 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `541` | Route 47 | `02:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2753` | Route 63 | `03:18:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `1505` | Route 57 | `03:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3031` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `660` | Route 47 | `03:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `542` | Route 47 | `03:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3034` | Route 68 | `03:45:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:18` | `89.05%` | `0.0%` | 2091 | 702 | `+0.0s` |
| `2026-11-27 06:30:18` | `87.56%` | `0.0%` | 2122 | 718 | `+0.0s` |
| `2026-11-27 06:00:17` | `86.8%` | `0.0%` | 2175 | 715 | `+0.0s` |
| `2026-11-27 05:30:18` | `87.52%` | `0.0%` | 2172 | 681 | `+0.0s` |
| `2026-11-27 05:00:17` | `87.43%` | `0.0%` | 2172 | 607 | `+0.0s` |
| `2026-11-27 04:30:18` | `86.06%` | `0.0%` | 2173 | 599 | `+0.0s` |
| `2026-11-27 04:00:17` | `84.06%` | `0.0%` | 2208 | 599 | `+0.0s` |
| `2026-11-27 03:30:18` | `84.44%` | `0.0%` | 2198 | 611 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:18.158000+00:00`.*
