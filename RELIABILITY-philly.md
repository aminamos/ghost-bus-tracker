# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:17.800000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`66.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `632` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `567` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `420` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 420 | 66.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 47 | 7.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 48** | 55 | 0 | 55 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 38** | 29 | 0 | 29 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 62 | 1 | 61 | **`98.39%`** | `0.0%` | `+0.0s` |
| **Route K** | 40 | 1 | 39 | **`97.5%`** | `0.0%` | `+0.0s` |
| **Route 16** | 39 | 1 | 38 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 71** | 70 | 2 | 68 | **`97.14%`** | `0.0%` | `+0.0s` |
| **Route 41** | 22 | 1 | 21 | **`95.45%`** | `0.0%` | `+0.0s` |
| **Route 43** | 33 | 2 | 31 | **`93.94%`** | `0.0%` | `+0.0s` |
| **Route 2** | 42 | 2 | 39 | **`92.86%`** | `0.0%` | `+0.0s` |
| **Route 4** | 35 | 1 | 31 | **`88.57%`** | `0.0%` | `+0.0s` |

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
| `895889` | Route K | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869213` | Route 14 | `02:08:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `877215` | Route 37 | `02:21:00` | `SCHEDULED` | Assigned vehicle block_7351_schedBasedVehicle is missing from active GPS transponder fleet |
| `889230` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886150` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `938237` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `869270` | Route 14 | `02:55:00` | `SCHEDULED` | Assigned vehicle block_1051_schedBasedVehicle is missing from active GPS transponder fleet |
| `889236` | Route 63 | `03:06:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886140` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `871060` | Route 2 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `878970` | Route 41 | `05:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `880010` | Route 43 | `05:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998889` | Route 4 | `05:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `983631` | Route 45 | `05:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `871041` | Route 2 | `05:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:17` | `66.46%` | `0.0%` | 632 | 567 | `+0.0s` |
| `2026-11-08 06:30:18` | `63.12%` | `0.0%` | 667 | 599 | `+0.0s` |
| `2026-11-08 06:00:17` | `61.5%` | `0.0%` | 722 | 612 | `+0.0s` |
| `2026-11-08 05:30:18` | `60.16%` | `0.0%` | 748 | 630 | `+0.0s` |
| `2026-11-08 05:00:18` | `57.78%` | `0.0%` | 765 | 643 | `+0.0s` |
| `2026-11-08 04:30:20` | `54.59%` | `0.0%` | 773 | 676 | `+0.0s` |
| `2026-11-08 04:00:18` | `51.51%` | `0.0%` | 796 | 703 | `+0.0s` |
| `2026-11-08 03:30:17` | `48.56%` | `0.0%` | 836 | 743 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.800000+00:00`.*
