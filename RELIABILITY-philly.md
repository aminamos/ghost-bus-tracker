# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:17.717000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`80.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1130` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `666` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `906` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 906 | 80.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 36 | 3.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 45** | 82 | 0 | 82 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 77 | 0 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 22 | 0 | 22 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 32** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 58 | 1 | 57 | **`98.28%`** | `0.0%` | `+0.0s` |
| **Route 4** | 53 | 1 | 52 | **`98.11%`** | `0.0%` | `+0.0s` |
| **Route 16** | 52 | 1 | 51 | **`98.08%`** | `0.0%` | `+0.0s` |
| **Route K** | 102 | 1 | 100 | **`98.04%`** | `0.0%` | `+0.0s` |

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
| `966794` | Route 63 | `02:32:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891352` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `958676` | Route 68 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `966892` | Route 63 | `03:18:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `891354` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `958677` | Route 68 | `03:45:00` | `SCHEDULED` | Assigned vehicle block_7852_schedBasedVehicle is missing from active GPS transponder fleet |
| `907805` | Route K | `04:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `882380` | Route 48 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `958074` | Route 119 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907804` | Route K | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `995909` | Route 53 | `04:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `892818` | Route 75 | `04:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998660` | Route 4 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870890` | Route 2 | `04:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:17` | `80.18%` | `0.0%` | 1130 | 666 | `+0.0s` |
| `2026-11-05 06:30:17` | `78.53%` | `0.0%` | 1160 | 684 | `+0.0s` |
| `2026-11-05 06:00:17` | `76.23%` | `0.0%` | 1220 | 696 | `+0.0s` |
| `2026-11-05 05:30:18` | `76.45%` | `0.0%` | 1240 | 718 | `+0.0s` |
| `2026-11-05 05:00:17` | `74.11%` | `0.0%` | 1271 | 744 | `+0.0s` |
| `2026-11-05 04:30:18` | `69.47%` | `0.0%` | 1310 | 762 | `+0.0s` |
| `2026-11-05 04:00:18` | `66.64%` | `0.0%` | 1343 | 778 | `+0.0s` |
| `2026-11-05 03:30:18` | `64.93%` | `0.0%` | 1380 | 817 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.717000+00:00`.*
