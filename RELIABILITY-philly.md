# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.581000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`91.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2276` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `643` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2081` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2081 | 91.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 16 | 0.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 166 | 0 | 166 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 97 | 0 | 97 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 47 | 0 | 47 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 44 | 0 | 44 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 38** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `964100` | Route 40 | `25:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `885574` | Route 55 | `25:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `885571` | Route 55 | `27:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895145` | Route B1_OWL | `00:42:00` | `SCHEDULED` | Assigned vehicle 7302 is missing from active GPS transponder fleet |
| `966794` | Route 63 | `02:32:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891352` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `958676` | Route 68 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `996723` | Route 47 | `02:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996606` | Route 47 | `02:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `966892` | Route 63 | `03:18:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891354` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `996724` | Route 47 | `03:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996607` | Route 47 | `03:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `958677` | Route 68 | `03:45:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `91.43%` | `0.0%` | 2276 | 643 | `+0.0s` |
| `2026-11-25 06:30:18` | `90.1%` | `0.0%` | 2312 | 688 | `+0.0s` |
| `2026-11-25 06:00:18` | `89.09%` | `0.0%` | 2355 | 700 | `+0.0s` |
| `2026-11-25 05:30:18` | `88.41%` | `0.0%` | 2382 | 702 | `+0.0s` |
| `2026-11-25 05:00:17` | `85.18%` | `0.0%` | 2146 | 718 | `+0.0s` |
| `2026-11-25 04:30:17` | `82.51%` | `0.0%` | 2179 | 730 | `+0.0s` |
| `2026-11-25 04:00:18` | `80.34%` | `0.0%` | 2218 | 753 | `+0.0s` |
| `2026-11-25 03:30:19` | `78.81%` | `0.0%` | 2261 | 787 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.581000+00:00`.*
