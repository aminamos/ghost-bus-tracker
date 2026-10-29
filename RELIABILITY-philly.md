# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:18.540000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.61%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `968` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `604` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `819` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 819 | 84.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 20 | 2.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 65** | 77 | 0 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route K** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 63 | 1 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 40** | 61 | 0 | 61 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `891285` | Route 68 | `03:13:00` | `SCHEDULED` | Assigned vehicle block_7854_schedBasedVehicle is missing from active GPS transponder fleet |
| `958826` | Route 23 | `03:20:00` | `SCHEDULED` | Assigned vehicle block_3151_schedBasedVehicle is missing from active GPS transponder fleet |
| `877050` | Route 37 | `03:21:00` | `SCHEDULED` | Assigned vehicle block_7352_schedBasedVehicle is missing from active GPS transponder fleet |
| `993912` | Route 57 | `03:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993196` | Route 17 | `03:29:00` | `SCHEDULED` | Assigned vehicle block_7302_schedBasedVehicle is missing from active GPS transponder fleet |
| `871260` | Route 20 | `03:29:00` | `SCHEDULED` | Assigned vehicle block_1451_schedBasedVehicle is missing from active GPS transponder fleet |
| `957315` | Route 108 | `03:35:00` | `SCHEDULED` | Assigned vehicle block_4357_schedBasedVehicle is missing from active GPS transponder fleet |
| `957781` | Route 113 | `03:40:00` | `SCHEDULED` | Assigned vehicle block_4503_schedBasedVehicle is missing from active GPS transponder fleet |
| `966796` | Route 63 | `03:41:00` | `SCHEDULED` | Assigned vehicle block_7653_schedBasedVehicle is missing from active GPS transponder fleet |
| `940328` | Route D1 | `03:41:00` | `SCHEDULED` | Assigned vehicle block_4101_schedBasedVehicle is missing from active GPS transponder fleet |
| `957970` | Route 115 | `03:43:00` | `SCHEDULED` | Assigned vehicle block_4565_schedBasedVehicle is missing from active GPS transponder fleet |
| `891288` | Route 68 | `03:43:00` | `SCHEDULED` | Assigned vehicle block_7854_schedBasedVehicle is missing from active GPS transponder fleet |
| `998309` | Route 51 | `03:49:00` | `SCHEDULED` | Assigned vehicle block_3381_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `84.61%` | `0.0%` | 968 | 604 | `+0.0s` |
| `2026-10-29 06:00:19` | `80.26%` | `0.0%` | 998 | 675 | `+0.0s` |
| `2026-10-29 05:30:18` | `78.56%` | `0.0%` | 1031 | 701 | `+0.0s` |
| `2026-10-29 05:00:18` | `76.33%` | `0.0%` | 1090 | 704 | `+0.0s` |
| `2026-10-29 04:30:18` | `74.96%` | `0.0%` | 1118 | 729 | `+0.0s` |
| `2026-10-29 04:00:18` | `72.21%` | `0.0%` | 1155 | 745 | `+0.0s` |
| `2026-10-29 03:30:18` | `67.45%` | `0.0%` | 1186 | 779 | `+0.0s` |
| `2026-10-29 03:00:18` | `63.81%` | `0.0%` | 1227 | 784 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.540000+00:00`.*
