# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:17.823000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`74.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `495` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `495` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `370` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 370 | 74.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 110 | 22.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 45** | 61 | 0 | 61 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 55 | 0 | 55 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route K** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 26 | 0 | 26 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 41 | 1 | 39 | **`95.12%`** | `0.0%` | `+0.0s` |

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
| `993974` | Route 4 | `25:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `995325` | Route 57 | `01:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869213` | Route 14 | `02:08:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `973581` | Route 60 | `02:08:00` | `SCHEDULED` | Assigned vehicle 3411 is missing from active GPS transponder fleet |
| `877215` | Route 37 | `02:21:00` | `SCHEDULED` | Assigned vehicle block_7351_schedBasedVehicle is missing from active GPS transponder fleet |
| `995326` | Route 57 | `02:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `889230` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886150` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `938237` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `869270` | Route 14 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `889236` | Route 63 | `03:06:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886140` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `995327` | Route 57 | `03:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `995314` | Route 57 | `04:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `871060` | Route 2 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:17` | `74.75%` | `0.0%` | 495 | 495 | `+0.0s` |
| `2026-11-01 06:30:17` | `73.13%` | `0.0%` | 495 | 532 | `+0.0s` |
| `2026-11-01 06:00:18` | `64.14%` | `0.0%` | 555 | 572 | `+0.0s` |
| `2026-11-01 05:30:18` | `54.26%` | `0.0%` | 658 | 612 | `+0.0s` |
| `2026-11-01 05:00:18` | `53.76%` | `0.0%` | 718 | 628 | `+0.0s` |
| `2026-11-01 04:30:18` | `50.84%` | `0.0%` | 771 | 629 | `+0.0s` |
| `2026-11-01 04:00:17` | `49.68%` | `0.0%` | 773 | 632 | `+0.0s` |
| `2026-11-01 03:30:17` | `49.12%` | `0.0%` | 737 | 657 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:17.823000+00:00`.*
