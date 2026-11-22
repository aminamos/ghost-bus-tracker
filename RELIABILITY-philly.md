# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:18.082000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`78.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `924` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `547` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `723` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 723 | 78.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 43 | 4.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 103 | 0 | 103 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 35 | 0 | 35 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 79** | 129 | 2 | 127 | **`98.45%`** | `0.0%` | `+0.0s` |
| **Route 31** | 47 | 1 | 46 | **`97.87%`** | `0.0%` | `+0.0s` |
| **Route 7** | 27 | 1 | 26 | **`96.3%`** | `0.0%` | `+0.0s` |
| **Route 16** | 40 | 1 | 38 | **`95.0%`** | `0.0%` | `+0.0s` |
| **Route 55** | 37 | 2 | 35 | **`94.59%`** | `0.0%` | `+0.0s` |

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
| `869213` | Route 14 | `02:08:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `877215` | Route 37 | `02:21:00` | `SCHEDULED` | Assigned vehicle block_7351_schedBasedVehicle is missing from active GPS transponder fleet |
| `889230` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886150` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `938237` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `869270` | Route 14 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `893361` | Route 79 | `02:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `977294` | Route 47 | `02:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `893416` | Route 79 | `03:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `889236` | Route 63 | `03:06:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886140` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `995384` | Route 57 | `03:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `893362` | Route 79 | `03:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `977342` | Route 47 | `03:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `78.25%` | `0.0%` | 924 | 547 | `+0.0s` |
| `2026-11-22 06:30:17` | `75.31%` | `0.0%` | 968 | 581 | `+0.0s` |
| `2026-11-22 06:00:17` | `73.97%` | `0.0%` | 1022 | 586 | `+0.0s` |
| `2026-11-22 05:30:20` | `72.82%` | `0.0%` | 1056 | 601 | `+0.0s` |
| `2026-11-22 05:00:18` | `71.06%` | `0.0%` | 1085 | 602 | `+0.0s` |
| `2026-11-22 04:30:17` | `69.05%` | `0.0%` | 1079 | 625 | `+0.0s` |
| `2026-11-22 04:00:17` | `64.2%` | `0.0%` | 1148 | 640 | `+0.0s` |
| `2026-11-22 03:30:18` | `63.41%` | `0.0%` | 1167 | 682 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.082000+00:00`.*
