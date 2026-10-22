# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T18:30:36.491000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`39.51%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2144` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1178` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `847` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 847 | 39.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 131 | 6.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 475** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 478** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 492** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 206** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 477** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 447** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 49 | 2 | 45 | **`91.84%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 3 | 29 | **`87.88%`** | `0.0%` | `+0.0s` |
| **Route 41** | 40 | 5 | 34 | **`85.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 93 | 10 | 79 | **`84.95%`** | `0.0%` | `+0.0s` |

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
| `907782` | Route K | `13:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998386` | Route 51 | `13:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907826` | Route K | `14:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `964842` | Route 65 | `14:22:00` | `SCHEDULED` | Assigned vehicle block_9618_schedBasedVehicle is missing from active GPS transponder fleet |
| `974632` | Route 53 | `14:23:00` | `SCHEDULED` | Assigned vehicle 3819 is missing from active GPS transponder fleet |
| `935347` | Route 84 | `14:23:00` | `SCHEDULED` | Assigned vehicle block_1521_schedBasedVehicle is missing from active GPS transponder fleet |
| `870863` | Route 2 | `14:25:00` | `SCHEDULED` | Assigned vehicle block_3484_schedBasedVehicle is missing from active GPS transponder fleet |
| `935278` | Route 14 | `14:26:00` | `SCHEDULED` | Assigned vehicle block_1073_schedBasedVehicle is missing from active GPS transponder fleet |
| `957237` | Route 107 | `14:30:00` | `SCHEDULED` | Assigned vehicle block_4345_schedBasedVehicle is missing from active GPS transponder fleet |
| `941464` | Route M1 | `14:30:00` | `SCHEDULED` | Assigned vehicle block_4020_schedBasedVehicle is missing from active GPS transponder fleet |
| `957238` | Route 107 | `14:31:00` | `SCHEDULED` | Assigned vehicle block_4346_schedBasedVehicle is missing from active GPS transponder fleet |
| `870901` | Route 2 | `14:31:00` | `SCHEDULED` | Assigned vehicle block_7108_schedBasedVehicle is missing from active GPS transponder fleet |
| `963338` | Route 42 | `14:31:00` | `SCHEDULED` | Assigned vehicle block_9145_schedBasedVehicle is missing from active GPS transponder fleet |
| `956994` | Route 104 | `14:35:00` | `SCHEDULED` | Assigned vehicle block_4228_schedBasedVehicle is missing from active GPS transponder fleet |
| `963792` | Route 31 | `14:35:00` | `SCHEDULED` | Assigned vehicle block_9213_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:30:36` | `39.51%` | `0.0%` | 2144 | 1178 | `+0.0s` |
| `2026-10-22 18:00:38` | `44.63%` | `0.0%` | 2057 | 1140 | `+0.0s` |
| `2026-10-22 17:30:38` | `43.27%` | `0.0%` | 1902 | 1140 | `+0.0s` |
| `2026-10-22 17:00:37` | `42.36%` | `0.0%` | 1825 | 1097 | `+0.0s` |
| `2026-10-22 16:31:16` | `41.86%` | `0.0%` | 1751 | 1067 | `+0.0s` |
| `2026-10-22 16:01:16` | `40.93%` | `0.0%` | 1698 | 1072 | `+0.0s` |
| `2026-10-22 15:30:39` | `29.69%` | `0.0%` | 1401 | 1067 | `+0.0s` |
| `2026-10-22 15:01:08` | `29.94%` | `0.0%` | 1426 | 1075 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:30:36.491000+00:00`.*
