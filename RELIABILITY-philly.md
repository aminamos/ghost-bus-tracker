# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.213000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`83.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1191` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `586` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `992` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 992 | 83.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 32 | 2.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 103 | 0 | 103 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 92** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 79** | 140 | 2 | 138 | **`98.57%`** | `0.0%` | `+0.0s` |
| **Route 4** | 52 | 1 | 51 | **`98.08%`** | `0.0%` | `+0.0s` |
| **Route 16** | 46 | 1 | 45 | **`97.83%`** | `0.0%` | `+0.0s` |
| **Route 43** | 37 | 1 | 36 | **`97.3%`** | `0.0%` | `+0.0s` |
| **Route 26** | 34 | 1 | 33 | **`97.06%`** | `0.0%` | `+0.0s` |

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
| `963581` | Route 21 | `25:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `891317` | Route 68 | `26:10:00` | `SCHEDULED` | Assigned vehicle 3569 is missing from active GPS transponder fleet |
| `885571` | Route 55 | `27:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `995087` | Route 57 | `01:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869033` | Route 14 | `02:08:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `995091` | Route 57 | `02:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `889096` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886050` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891392` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `938143` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `879497` | Route 42 | `02:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869095` | Route 14 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `982829` | Route 79 | `02:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `977151` | Route 47 | `02:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `83.29%` | `0.0%` | 1191 | 586 | `+0.0s` |
| `2026-11-21 06:30:27` | `81.06%` | `0.0%` | 1230 | 623 | `+0.0s` |
| `2026-11-21 06:00:18` | `79.44%` | `0.0%` | 1284 | 636 | `+0.0s` |
| `2026-11-21 05:30:17` | `77.8%` | `0.0%` | 1329 | 651 | `+0.0s` |
| `2026-11-21 05:00:19` | `74.58%` | `0.0%` | 1314 | 670 | `+0.0s` |
| `2026-11-21 04:30:18` | `71.25%` | `0.0%` | 1353 | 700 | `+0.0s` |
| `2026-11-21 04:00:17` | `67.65%` | `0.0%` | 1419 | 746 | `+0.0s` |
| `2026-11-21 03:30:17` | `65.79%` | `0.0%` | 1479 | 788 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.213000+00:00`.*
