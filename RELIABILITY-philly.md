# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T18:00:38.108000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`44.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2057` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1140` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `918` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 918 | 44.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 141 | 6.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route B2** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 439** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 48 | 1 | 46 | **`95.83%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 3 | 30 | **`90.91%`** | `0.0%` | `+0.0s` |
| **Route 41** | 40 | 3 | 35 | **`87.5%`** | `0.0%` | `+0.0s` |
| **Route 51** | 93 | 9 | 79 | **`84.95%`** | `0.0%` | `+0.0s` |
| **Route 65** | 77 | 9 | 65 | **`84.42%`** | `0.0%` | `+0.0s` |
| **Route K** | 82 | 9 | 69 | **`84.15%`** | `0.0%` | `+0.0s` |
| **Route 64** | 78 | 9 | 65 | **`83.33%`** | `0.0%` | `+0.0s` |
| **Route 57** | 90 | 12 | 71 | **`78.89%`** | `0.0%` | `+0.0s` |

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
| `998382` | Route 51 | `13:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998279` | Route 51 | `13:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `957010` | Route 104 | `13:55:00` | `SCHEDULED` | Assigned vehicle block_4226_schedBasedVehicle is missing from active GPS transponder fleet |
| `840867` | Route 124 | `13:55:00` | `SCHEDULED` | Assigned vehicle block_6180_schedBasedVehicle is missing from active GPS transponder fleet |
| `882402` | Route 48 | `13:55:00` | `SCHEDULED` | Assigned vehicle block_5439_schedBasedVehicle is missing from active GPS transponder fleet |
| `982780` | Route 45 | `13:56:00` | `SCHEDULED` | Assigned vehicle block_7067_schedBasedVehicle is missing from active GPS transponder fleet |
| `978650` | Route B2 | `13:56:00` | `SCHEDULED` | Assigned vehicle block_80030_schedBasedVehicle is missing from active GPS transponder fleet |
| `932966` | Route 3 | `13:58:00` | `SCHEDULED` | Assigned vehicle block_2219_schedBasedVehicle is missing from active GPS transponder fleet |
| `984053` | Route 72 | `13:58:00` | `SCHEDULED` | Assigned vehicle block_2636_schedBasedVehicle is missing from active GPS transponder fleet |
| `957997` | Route 117 | `13:59:00` | `SCHEDULED` | Assigned vehicle block_4607_schedBasedVehicle is missing from active GPS transponder fleet |
| `935345` | Route 84 | `13:59:00` | `SCHEDULED` | Assigned vehicle block_1516_schedBasedVehicle is missing from active GPS transponder fleet |
| `908220` | Route 8 | `14:00:00` | `SCHEDULED` | Assigned vehicle block_2308_schedBasedVehicle is missing from active GPS transponder fleet |
| `841861` | Route 90 | `14:00:00` | `SCHEDULED` | Assigned vehicle block_6708_schedBasedVehicle is missing from active GPS transponder fleet |
| `935178` | Route BLVDDIR | `14:00:00` | `SCHEDULED` | Assigned vehicle block_1115_schedBasedVehicle is missing from active GPS transponder fleet |
| `941405` | Route M1 | `14:00:00` | `SCHEDULED` | Assigned vehicle block_4018_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:00:38` | `44.63%` | `0.0%` | 2057 | 1140 | `+0.0s` |
| `2026-10-22 17:30:38` | `43.27%` | `0.0%` | 1902 | 1140 | `+0.0s` |
| `2026-10-22 17:00:37` | `42.36%` | `0.0%` | 1825 | 1097 | `+0.0s` |
| `2026-10-22 16:31:16` | `41.86%` | `0.0%` | 1751 | 1067 | `+0.0s` |
| `2026-10-22 16:01:16` | `40.93%` | `0.0%` | 1698 | 1072 | `+0.0s` |
| `2026-10-22 15:30:39` | `29.69%` | `0.0%` | 1401 | 1067 | `+0.0s` |
| `2026-10-22 15:01:08` | `29.94%` | `0.0%` | 1426 | 1075 | `+0.0s` |
| `2026-10-22 14:30:48` | `29.36%` | `0.0%` | 1478 | 1096 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:00:38.108000+00:00`.*
