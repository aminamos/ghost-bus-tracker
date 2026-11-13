# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:19.562000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`83.02%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1237` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `638` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1027` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1027 | 83.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 27 | 2.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 45** | 82 | 0 | 82 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 77 | 0 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 38** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 22 | 0 | 22 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 107** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 73** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `869357` | Route 16 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993619` | Route 4 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `966794` | Route 63 | `02:32:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891352` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `958676` | Route 68 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `966892` | Route 63 | `03:18:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891354` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `958677` | Route 68 | `03:45:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `907805` | Route K | `04:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `882380` | Route 48 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907804` | Route K | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998660` | Route 4 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870890` | Route 2 | `04:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `882381` | Route 48 | `04:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:19` | `83.02%` | `0.0%` | 1237 | 638 | `+0.0s` |
| `2026-11-13 06:30:18` | `81.02%` | `0.0%` | 1275 | 644 | `+0.0s` |
| `2026-11-13 06:00:19` | `79.19%` | `0.0%` | 1331 | 670 | `+0.0s` |
| `2026-11-13 05:30:18` | `78.67%` | `0.0%` | 1355 | 695 | `+0.0s` |
| `2026-11-13 05:00:18` | `75.02%` | `0.0%` | 1389 | 691 | `+0.0s` |
| `2026-11-13 04:30:18` | `71.78%` | `0.0%` | 1407 | 732 | `+0.0s` |
| `2026-11-13 04:00:19` | `68.38%` | `0.0%` | 1458 | 776 | `+0.0s` |
| `2026-11-13 03:30:18` | `67.05%` | `0.0%` | 1481 | 804 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:19.562000+00:00`.*
