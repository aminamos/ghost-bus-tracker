# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T07:00:21.047000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`70.69%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `505` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `562` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `357` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 357 | 70.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 26 | 5.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route K** | 53 | 0 | 53 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 45 | 0 | 45 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 26 | 0 | 26 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 99** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 47 | 2 | 44 | **`93.62%`** | `0.0%` | `+0.0s` |
| **Route 57** | 61 | 2 | 57 | **`93.44%`** | `0.0%` | `+0.0s` |
| **Route 4** | 50 | 1 | 45 | **`90.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |

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
| `869034` | Route 14 | `03:08:00` | `SCHEDULED` | Assigned vehicle block_1052_schedBasedVehicle is missing from active GPS transponder fleet |
| `939162` | Route 113 | `03:10:00` | `SCHEDULED` | Assigned vehicle block_4502_schedBasedVehicle is missing from active GPS transponder fleet |
| `938218` | Route 108 | `03:15:00` | `SCHEDULED` | Assigned vehicle block_4356_schedBasedVehicle is missing from active GPS transponder fleet |
| `959057` | Route 23 | `03:20:00` | `SCHEDULED` | Assigned vehicle block_3151_schedBasedVehicle is missing from active GPS transponder fleet |
| `877142` | Route 37 | `03:21:00` | `SCHEDULED` | Assigned vehicle block_7352_schedBasedVehicle is missing from active GPS transponder fleet |
| `871408` | Route 20 | `03:29:00` | `SCHEDULED` | Assigned vehicle block_1451_schedBasedVehicle is missing from active GPS transponder fleet |
| `938165` | Route 108 | `03:35:00` | `SCHEDULED` | Assigned vehicle block_4357_schedBasedVehicle is missing from active GPS transponder fleet |
| `883889` | Route 51 | `03:51:00` | `SCHEDULED` | Assigned vehicle block_3381_schedBasedVehicle is missing from active GPS transponder fleet |
| `995231` | Route 57 | `03:53:00` | `SCHEDULED` | Assigned vehicle block_7452_schedBasedVehicle is missing from active GPS transponder fleet |
| `869104` | Route 14 | `03:55:00` | `SCHEDULED` | Assigned vehicle block_1052_schedBasedVehicle is missing from active GPS transponder fleet |
| `995229` | Route 57 | `03:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `871462` | Route 20 | `04:05:00` | `SCHEDULED` | Assigned vehicle block_1451_schedBasedVehicle is missing from active GPS transponder fleet |
| `958941` | Route 23 | `04:10:00` | `SCHEDULED` | Assigned vehicle block_3151_schedBasedVehicle is missing from active GPS transponder fleet |
| `994120` | Route 57 | `04:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895891` | Route K | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 07:00:21` | `70.69%` | `0.0%` | 505 | 562 | `+0.0s` |
| `2026-10-24 06:30:18` | `68.88%` | `0.0%` | 527 | 598 | `+0.0s` |
| `2026-10-24 06:00:19` | `63.49%` | `0.0%` | 556 | 637 | `+0.0s` |
| `2026-10-24 05:30:18` | `59.57%` | `0.0%` | 601 | 670 | `+0.0s` |
| `2026-10-24 05:00:19` | `57.59%` | `0.0%` | 672 | 692 | `+0.0s` |
| `2026-10-24 04:30:18` | `53.38%` | `0.0%` | 725 | 692 | `+0.0s` |
| `2026-10-24 04:00:19` | `54.08%` | `0.0%` | 723 | 710 | `+0.0s` |
| `2026-10-24 03:30:19` | `47.34%` | `0.0%` | 771 | 737 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T07:00:21.047000+00:00`.*
