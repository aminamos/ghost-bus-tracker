# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:18.623000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`80.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1059` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `751` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `855` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 855 | 80.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 39 | 3.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 71** | 100 | 0 | 100 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 77 | 0 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 22 | 0 | 22 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 73** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 83 | 1 | 82 | **`98.8%`** | `0.0%` | `+0.0s` |
| **Route 16** | 53 | 1 | 52 | **`98.11%`** | `0.0%` | `+0.0s` |
| **Route K** | 103 | 1 | 101 | **`98.06%`** | `0.0%` | `+0.0s` |
| **Route 41** | 39 | 1 | 38 | **`97.44%`** | `0.0%` | `+0.0s` |

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
| `957309` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `966892` | Route 63 | `03:18:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `907805` | Route K | `04:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `882380` | Route 48 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907804` | Route K | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `874435` | Route 29 | `04:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998660` | Route 4 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870890` | Route 2 | `04:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `882381` | Route 48 | `04:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `878857` | Route 41 | `05:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `907802` | Route K | `05:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `982737` | Route 45 | `05:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870891` | Route 2 | `05:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `982739` | Route 45 | `05:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:18` | `80.74%` | `0.0%` | 1059 | 751 | `+0.0s` |
| `2026-11-09 06:30:18` | `78.42%` | `0.0%` | 1103 | 761 | `+0.0s` |
| `2026-11-09 06:00:18` | `77.56%` | `0.0%` | 1154 | 751 | `+0.0s` |
| `2026-11-09 05:30:18` | `77.01%` | `0.0%` | 1170 | 722 | `+0.0s` |
| `2026-11-09 05:00:17` | `75.27%` | `0.0%` | 1189 | 748 | `+0.0s` |
| `2026-11-09 04:30:18` | `72.32%` | `0.0%` | 1196 | 690 | `+0.0s` |
| `2026-11-09 04:00:18` | `69.51%` | `0.0%` | 1230 | 659 | `+0.0s` |
| `2026-11-09 03:30:17` | `68.82%` | `0.0%` | 1241 | 666 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:18.623000+00:00`.*
