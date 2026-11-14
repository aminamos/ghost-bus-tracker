# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:18.311000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`72.85%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `792` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `610` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `577` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 577 | 72.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 45 | 5.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 48** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 38** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 46 | 1 | 45 | **`97.83%`** | `0.0%` | `+0.0s` |
| **Route 71** | 85 | 2 | 83 | **`97.65%`** | `0.0%` | `+0.0s` |
| **Route 9** | 37 | 0 | 36 | **`97.3%`** | `0.0%` | `+0.0s` |
| **Route 43** | 35 | 1 | 34 | **`97.14%`** | `0.0%` | `+0.0s` |
| **Route 4** | 35 | 1 | 34 | **`97.14%`** | `0.0%` | `+0.0s` |
| **Route K** | 55 | 1 | 53 | **`96.36%`** | `0.0%` | `+0.0s` |
| **Route 41** | 22 | 1 | 21 | **`95.45%`** | `0.0%` | `+0.0s` |

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
| `889096` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886050` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891392` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `938143` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `889113` | Route 63 | `03:09:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `885994` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891390` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `995089` | Route 57 | `03:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `995229` | Route 57 | `03:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `994120` | Route 57 | `04:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895891` | Route K | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870983` | Route 2 | `04:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `995230` | Route 57 | `04:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `878934` | Route 41 | `05:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895880` | Route K | `05:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:18` | `72.85%` | `0.0%` | 792 | 610 | `+0.0s` |
| `2026-11-14 06:30:18` | `71.52%` | `0.0%` | 825 | 630 | `+0.0s` |
| `2026-11-14 06:00:18` | `70.3%` | `0.0%` | 872 | 662 | `+0.0s` |
| `2026-11-14 05:30:18` | `67.51%` | `0.0%` | 908 | 688 | `+0.0s` |
| `2026-11-14 05:00:19` | `63.8%` | `0.0%` | 953 | 702 | `+0.0s` |
| `2026-11-14 04:30:18` | `58.87%` | `0.0%` | 987 | 721 | `+0.0s` |
| `2026-11-14 04:00:19` | `56.75%` | `0.0%` | 1008 | 741 | `+0.0s` |
| `2026-11-14 03:30:18` | `54.09%` | `0.0%` | 1063 | 769 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:18.311000+00:00`.*
