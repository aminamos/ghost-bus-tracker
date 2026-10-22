# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:00:21.379000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`34.1%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2211` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1191` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `754` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 754 | 34.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 164 | 7.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 475** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route B3** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 33 | 3 | 29 | **`87.88%`** | `0.0%` | `+0.0s` |
| **Route 8** | 49 | 5 | 41 | **`83.67%`** | `0.0%` | `+0.0s` |
| **Route 51** | 95 | 10 | 79 | **`83.16%`** | `0.0%` | `+0.0s` |
| **Route 41** | 41 | 5 | 34 | **`82.93%`** | `0.0%` | `+0.0s` |
| **Route K** | 83 | 11 | 68 | **`81.93%`** | `0.0%` | `+0.0s` |
| **Route 65** | 80 | 9 | 65 | **`81.25%`** | `0.0%` | `+0.0s` |
| **Route 57** | 90 | 13 | 71 | **`78.89%`** | `0.0%` | `+0.0s` |
| **Route 64** | 78 | 12 | 61 | **`78.21%`** | `0.0%` | `+0.0s` |

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
| `907780` | Route K | `13:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `869328` | Route 16 | `14:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907826` | Route K | `14:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `974632` | Route 53 | `14:23:00` | `SCHEDULED` | Assigned vehicle 3819 is missing from active GPS transponder fleet |
| `958544` | Route 57 | `14:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `963573` | Route 21 | `14:52:00` | `SCHEDULED` | Assigned vehicle block_9149_schedBasedVehicle is missing from active GPS transponder fleet |
| `975599` | Route 46 | `14:52:00` | `SCHEDULED` | Assigned vehicle block_9458_schedBasedVehicle is missing from active GPS transponder fleet |
| `968229` | Route T1 | `14:52:00` | `SCHEDULED` | Assigned vehicle block_9568_schedBasedVehicle is missing from active GPS transponder fleet |
| `954402` | Route 25 | `14:53:00` | `SCHEDULED` | Assigned vehicle block_2191_schedBasedVehicle is missing from active GPS transponder fleet |
| `869340` | Route 16 | `14:54:00` | `SCHEDULED` | Assigned vehicle block_3817_schedBasedVehicle is missing from active GPS transponder fleet |
| `933000` | Route 3 | `14:54:00` | `SCHEDULED` | Assigned vehicle block_2220_schedBasedVehicle is missing from active GPS transponder fleet |
| `942976` | Route 82 | `14:54:00` | `SCHEDULED` | Assigned vehicle block_2724_schedBasedVehicle is missing from active GPS transponder fleet |
| `841871` | Route 90 | `14:54:00` | `SCHEDULED` | Assigned vehicle block_6709_schedBasedVehicle is missing from active GPS transponder fleet |
| `957637` | Route 111 | `14:56:00` | `SCHEDULED` | Assigned vehicle block_4459_schedBasedVehicle is missing from active GPS transponder fleet |
| `963712` | Route 30 | `14:56:00` | `SCHEDULED` | Assigned vehicle block_9179_schedBasedVehicle is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:00:21` | `34.1%` | `0.0%` | 2211 | 1191 | `+0.0s` |
| `2026-10-22 18:30:36` | `39.51%` | `0.0%` | 2144 | 1178 | `+0.0s` |
| `2026-10-22 18:00:38` | `44.63%` | `0.0%` | 2057 | 1140 | `+0.0s` |
| `2026-10-22 17:30:38` | `43.27%` | `0.0%` | 1902 | 1140 | `+0.0s` |
| `2026-10-22 17:00:37` | `42.36%` | `0.0%` | 1825 | 1097 | `+0.0s` |
| `2026-10-22 16:31:16` | `41.86%` | `0.0%` | 1751 | 1067 | `+0.0s` |
| `2026-10-22 16:01:16` | `40.93%` | `0.0%` | 1698 | 1072 | `+0.0s` |
| `2026-10-22 15:30:39` | `29.69%` | `0.0%` | 1401 | 1067 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:00:21.379000+00:00`.*
