# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-21T16:31:23.401000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`42.78%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1697` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1077` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `726` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 726 | 42.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 43 | 2.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 8** | 48 | 2 | 44 | **`91.67%`** | `0.0%` | `+0.0s` |
| **Route K** | 81 | 6 | 73 | **`90.12%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 3 | 29 | **`87.88%`** | `0.0%` | `+0.0s` |
| **Route 51** | 94 | 9 | 82 | **`87.23%`** | `0.0%` | `+0.0s` |
| **Route 65** | 77 | 7 | 67 | **`87.01%`** | `0.0%` | `+0.0s` |
| **Route 16** | 56 | 6 | 48 | **`85.71%`** | `0.0%` | `+0.0s` |
| **Route 41** | 42 | 4 | 36 | **`85.71%`** | `0.0%` | `+0.0s` |
| **Route 64** | 77 | 10 | 65 | **`84.42%`** | `0.0%` | `+0.0s` |
| **Route 57** | 88 | 11 | 71 | **`80.68%`** | `0.0%` | `+0.0s` |
| **Route 4** | 43 | 8 | 34 | **`79.07%`** | `0.0%` | `+0.0s` |

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
| `993596` | Route 4 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `975930` | Route 64 | `11:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `964961` | Route 65 | `11:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998376` | Route 51 | `11:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `963956` | Route 40 | `12:27:00` | `SCHEDULED` | Assigned vehicle block_9318_schedBasedVehicle is missing from active GPS transponder fleet |
| `963789` | Route 31 | `12:28:00` | `SCHEDULED` | Assigned vehicle block_9210_schedBasedVehicle is missing from active GPS transponder fleet |
| `842963` | Route LUCYGR | `12:30:00` | `SCHEDULED` | Assigned vehicle 4606 is missing from active GPS transponder fleet |
| `934933` | Route 70 | `12:34:00` | `SCHEDULED` | Assigned vehicle block_1215_schedBasedVehicle is missing from active GPS transponder fleet |
| `957038` | Route 104 | `12:35:00` | `SCHEDULED` | Assigned vehicle block_4225_schedBasedVehicle is missing from active GPS transponder fleet |
| `942963` | Route 82 | `12:35:00` | `SCHEDULED` | Assigned vehicle block_2715_schedBasedVehicle is missing from active GPS transponder fleet |
| `954393` | Route 25 | `12:38:00` | `SCHEDULED` | Assigned vehicle block_2186_schedBasedVehicle is missing from active GPS transponder fleet |
| `957458` | Route 109 | `12:40:00` | `SCHEDULED` | Assigned vehicle block_4410_schedBasedVehicle is missing from active GPS transponder fleet |
| `934999` | Route 67 | `12:41:00` | `SCHEDULED` | Assigned vehicle block_1429_schedBasedVehicle is missing from active GPS transponder fleet |
| `907822` | Route K | `12:41:00` | `SCHEDULED` | Assigned vehicle block_2617_schedBasedVehicle is missing from active GPS transponder fleet |
| `971933` | Route T5 | `12:41:00` | `SCHEDULED` | Assigned vehicle block_8270_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 16:31:23` | `42.78%` | `0.0%` | 1697 | 1077 | `+0.0s` |
| `2026-10-21 16:01:19` | `42.09%` | `0.0%` | 1668 | 1078 | `+0.0s` |
| `2026-10-21 15:30:36` | `30.3%` | `0.0%` | 1373 | 1090 | `+0.0s` |
| `2026-10-21 15:00:38` | `30.74%` | `0.0%` | 1415 | 1100 | `+0.0s` |
| `2026-10-21 14:31:05` | `30.65%` | `0.0%` | 1439 | 1118 | `+0.0s` |
| `2026-10-21 14:00:38` | `28.35%` | `0.0%` | 1545 | 1123 | `+0.0s` |
| `2026-10-21 13:30:45` | `28.96%` | `0.0%` | 1630 | 1134 | `+0.0s` |
| `2026-10-21 13:00:41` | `28.63%` | `0.0%` | 1743 | 1145 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T16:31:23.401000+00:00`.*
