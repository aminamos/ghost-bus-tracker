# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-26T07:00:19.556000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`90.2%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1918` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `601` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1730` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1730 | 90.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 25 | 1.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route L1** | 110 | 0 | 110 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 99 | 0 | 99 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 59 | 0 | 59 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 49** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 32** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 38** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `893360` | Route 79 | `01:56:00` | `SCHEDULED` | Assigned vehicle block_7602_schedBasedVehicle is missing from active GPS transponder fleet |
| `977352` | Route 47 | `02:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `877215` | Route 37 | `02:21:00` | `SCHEDULED` | Assigned vehicle block_7351_schedBasedVehicle is missing from active GPS transponder fleet |
| `889230` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886150` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `938237` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `3650` | Route 17 | `02:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `977294` | Route 47 | `02:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `876877` | Route 33 | `03:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `977354` | Route 47 | `03:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `889236` | Route 63 | `03:06:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886140` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-26 07:00:19` | `90.2%` | `0.0%` | 1918 | 601 | `+0.0s` |
| `2026-11-26 06:30:18` | `88.91%` | `0.0%` | 1956 | 616 | `+0.0s` |
| `2026-11-26 06:00:18` | `87.09%` | `0.0%` | 2022 | 663 | `+0.0s` |
| `2026-11-26 05:30:23` | `86.43%` | `0.0%` | 2071 | 679 | `+0.0s` |
| `2026-11-26 05:00:18` | `84.4%` | `0.0%` | 2115 | 710 | `+0.0s` |
| `2026-11-26 04:30:19` | `82.3%` | `0.0%` | 2152 | 725 | `+0.0s` |
| `2026-11-26 04:00:18` | `80.12%` | `0.0%` | 2208 | 738 | `+0.0s` |
| `2026-11-26 03:30:18` | `79.05%` | `0.0%` | 2258 | 772 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T07:00:19.556000+00:00`.*
