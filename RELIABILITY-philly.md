# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:17.961000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1819` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `701` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1634` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1634 | 89.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 16 | 0.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 166 | 0 | 166 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 97 | 0 | 97 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 47 | 0 | 47 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 44 | 0 | 44 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 73** | 28 | 0 | 28 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `883456` | Route 5 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `964684` | Route 52 | `01:55:00` | `SCHEDULED` | Assigned vehicle 3677 is missing from active GPS transponder fleet |
| `966794` | Route 63 | `02:32:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `993918` | Route 57 | `02:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976472` | Route 79 | `02:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996606` | Route 47 | `02:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976475` | Route 79 | `03:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `966892` | Route 63 | `03:18:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `993919` | Route 57 | `03:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996607` | Route 47 | `03:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `993920` | Route 57 | `03:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996608` | Route 47 | `03:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976473` | Route 79 | `03:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976476` | Route 79 | `04:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:17` | `89.83%` | `0.0%` | 1819 | 701 | `+0.0s` |
| `2026-11-23 06:30:17` | `88.72%` | `0.0%` | 1853 | 701 | `+0.0s` |
| `2026-11-23 06:00:18` | `88.04%` | `0.0%` | 1906 | 679 | `+0.0s` |
| `2026-11-23 05:30:17` | `86.75%` | `0.0%` | 1940 | 670 | `+0.0s` |
| `2026-11-23 05:00:18` | `85.54%` | `0.0%` | 1957 | 628 | `+0.0s` |
| `2026-11-23 04:30:18` | `83.62%` | `0.0%` | 1960 | 593 | `+0.0s` |
| `2026-11-23 04:00:18` | `81.44%` | `0.0%` | 1993 | 623 | `+0.0s` |
| `2026-11-23 03:30:17` | `80.82%` | `0.0%` | 2002 | 646 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:17.961000+00:00`.*
