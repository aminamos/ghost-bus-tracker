# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T07:00:20.161000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`70.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `560` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `536` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `393` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 393 | 70.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 69 | 12.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 12** | 44 | 0 | 44 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 42 | 0 | 42 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route K** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 38 | 0 | 38 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 26 | 0 | 26 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 99** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `939259` | Route 113 | `03:10:00` | `SCHEDULED` | Assigned vehicle block_4502_schedBasedVehicle is missing from active GPS transponder fleet |
| `870709` | Route 18 | `03:10:00` | `SCHEDULED` | Assigned vehicle block_3001_schedBasedVehicle is missing from active GPS transponder fleet |
| `877216` | Route 37 | `03:21:00` | `SCHEDULED` | Assigned vehicle block_7352_schedBasedVehicle is missing from active GPS transponder fleet |
| `871508` | Route 20 | `03:29:00` | `SCHEDULED` | Assigned vehicle block_1451_schedBasedVehicle is missing from active GPS transponder fleet |
| `938238` | Route 108 | `03:35:00` | `SCHEDULED` | Assigned vehicle block_4356_schedBasedVehicle is missing from active GPS transponder fleet |
| `870648` | Route 18 | `03:50:00` | `SCHEDULED` | Assigned vehicle block_3001_schedBasedVehicle is missing from active GPS transponder fleet |
| `883980` | Route 51 | `03:51:00` | `SCHEDULED` | Assigned vehicle block_3381_schedBasedVehicle is missing from active GPS transponder fleet |
| `871564` | Route 20 | `04:05:00` | `SCHEDULED` | Assigned vehicle block_1451_schedBasedVehicle is missing from active GPS transponder fleet |
| `995314` | Route 57 | `04:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `884036` | Route 51 | `04:37:00` | `SCHEDULED` | Assigned vehicle block_3381_schedBasedVehicle is missing from active GPS transponder fleet |
| `878970` | Route 41 | `05:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998889` | Route 4 | `05:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895986` | Route K | `05:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `878971` | Route 41 | `05:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895985` | Route K | `05:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 07:00:20` | `70.18%` | `0.0%` | 560 | 536 | `+0.0s` |
| `2026-10-25 06:30:19` | `68.99%` | `0.0%` | 574 | 570 | `+0.0s` |
| `2026-10-25 06:15:45` | `67.41%` | `0.0%` | 586 | 583 | `+0.0s` |
| `2026-10-25 06:00:56` | `62.96%` | `0.0%` | 621 | 586 | `+0.0s` |
| `2026-10-25 05:30:19` | `60.45%` | `0.0%` | 660 | 614 | `+0.0s` |
| `2026-10-25 05:00:18` | `56.25%` | `0.0%` | 736 | 631 | `+0.0s` |
| `2026-10-25 04:33:51` | `57.68%` | `0.0%` | 742 | 653 | `+0.0s` |
| `2026-10-25 04:00:20` | `55.99%` | `0.0%` | 759 | 640 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T07:00:20.161000+00:00`.*
