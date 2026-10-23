# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:21.834000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`82.37%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `851` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `645` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `701` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 701 | 82.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 21 | 2.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 65** | 77 | 0 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route K** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 22 | 0 | 22 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 99** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `868908` | Route 14 | `03:08:00` | `SCHEDULED` | Assigned vehicle block_1052_schedBasedVehicle is missing from active GPS transponder fleet |
| `957712` | Route 113 | `03:10:00` | `SCHEDULED` | Assigned vehicle block_4502_schedBasedVehicle is missing from active GPS transponder fleet |
| `998213` | Route 18 | `03:10:00` | `SCHEDULED` | Assigned vehicle block_3001_schedBasedVehicle is missing from active GPS transponder fleet |
| `891285` | Route 68 | `03:13:00` | `SCHEDULED` | Assigned vehicle block_7854_schedBasedVehicle is missing from active GPS transponder fleet |
| `958826` | Route 23 | `03:20:00` | `SCHEDULED` | Assigned vehicle block_3151_schedBasedVehicle is missing from active GPS transponder fleet |
| `877050` | Route 37 | `03:21:00` | `SCHEDULED` | Assigned vehicle block_7352_schedBasedVehicle is missing from active GPS transponder fleet |
| `993196` | Route 17 | `03:29:00` | `SCHEDULED` | Assigned vehicle block_7302_schedBasedVehicle is missing from active GPS transponder fleet |
| `871260` | Route 20 | `03:29:00` | `SCHEDULED` | Assigned vehicle block_1451_schedBasedVehicle is missing from active GPS transponder fleet |
| `957315` | Route 108 | `03:35:00` | `SCHEDULED` | Assigned vehicle block_4357_schedBasedVehicle is missing from active GPS transponder fleet |
| `957781` | Route 113 | `03:40:00` | `SCHEDULED` | Assigned vehicle block_4503_schedBasedVehicle is missing from active GPS transponder fleet |
| `966796` | Route 63 | `03:41:00` | `SCHEDULED` | Assigned vehicle block_7653_schedBasedVehicle is missing from active GPS transponder fleet |
| `957970` | Route 115 | `03:43:00` | `SCHEDULED` | Assigned vehicle block_4565_schedBasedVehicle is missing from active GPS transponder fleet |
| `891288` | Route 68 | `03:43:00` | `SCHEDULED` | Assigned vehicle block_7854_schedBasedVehicle is missing from active GPS transponder fleet |
| `998309` | Route 51 | `03:49:00` | `SCHEDULED` | Assigned vehicle block_3381_schedBasedVehicle is missing from active GPS transponder fleet |
| `998087` | Route 18 | `03:50:00` | `SCHEDULED` | Assigned vehicle block_3001_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:21` | `82.37%` | `0.0%` | 851 | 645 | `+0.0s` |
| `2026-10-23 06:30:20` | `80.16%` | `0.0%` | 877 | 678 | `+0.0s` |
| `2026-10-23 06:00:19` | `76.08%` | `0.0%` | 899 | 678 | `+0.0s` |
| `2026-10-23 05:30:19` | `74.36%` | `0.0%` | 932 | 692 | `+0.0s` |
| `2026-10-23 05:15:26` | `71.3%` | `0.0%` | 979 | 712 | `+0.0s` |
| `2026-10-23 05:00:36` | `71.29%` | `0.0%` | 996 | 711 | `+0.0s` |
| `2026-10-23 04:30:33` | `69.31%` | `0.0%` | 1036 | 713 | `+0.0s` |
| `2026-10-23 04:00:37` | `68.61%` | `0.0%` | 1048 | 719 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:21.834000+00:00`.*
