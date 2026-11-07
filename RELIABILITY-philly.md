# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:18.463000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`68.62%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `631` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `596` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `433` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 433 | 68.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 22 | 3.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 48** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 46 | 0 | 45 | **`97.83%`** | `0.0%` | `+0.0s` |
| **Route 71** | 85 | 2 | 83 | **`97.65%`** | `0.0%` | `+0.0s` |
| **Route 41** | 22 | 1 | 21 | **`95.45%`** | `0.0%` | `+0.0s` |
| **Route K** | 56 | 2 | 53 | **`94.64%`** | `0.0%` | `+0.0s` |
| **Route 31** | 23 | 0 | 21 | **`91.3%`** | `0.0%` | `+0.0s` |
| **Route 4** | 36 | 1 | 32 | **`88.89%`** | `0.0%` | `+0.0s` |
| **Route 2** | 43 | 2 | 38 | **`88.37%`** | `0.0%` | `+0.0s` |
| **Route 68** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `877143` | Route 37 | `02:21:00` | `SCHEDULED` | Assigned vehicle block_7351_schedBasedVehicle is missing from active GPS transponder fleet |
| `889096` | Route 63 | `02:30:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `886050` | Route 56 | `02:33:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891392` | Route 68 | `02:35:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `40927` | Route 108 | `02:40:00` | `SCHEDULED` | Assigned vehicle block_4355_schedBasedVehicle is missing from active GPS transponder fleet |
| `889113` | Route 63 | `03:09:00` | `SCHEDULED` | Assigned vehicle block_7651_schedBasedVehicle is missing from active GPS transponder fleet |
| `885994` | Route 56 | `03:17:00` | `SCHEDULED` | Assigned vehicle block_3602_schedBasedVehicle is missing from active GPS transponder fleet |
| `891390` | Route 68 | `03:25:00` | `SCHEDULED` | Assigned vehicle block_7851_schedBasedVehicle is missing from active GPS transponder fleet |
| `895891` | Route K | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870983` | Route 2 | `04:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `878934` | Route 41 | `05:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895880` | Route K | `05:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `870982` | Route 2 | `05:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `895892` | Route K | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `880695` | Route 45 | `05:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:18` | `68.62%` | `0.0%` | 631 | 596 | `+0.0s` |
| `2026-11-07 06:30:18` | `65.92%` | `0.0%` | 669 | 621 | `+0.0s` |
| `2026-11-07 06:00:18` | `64.19%` | `0.0%` | 726 | 649 | `+0.0s` |
| `2026-11-07 05:30:18` | `61.07%` | `0.0%` | 763 | 670 | `+0.0s` |
| `2026-11-07 05:00:18` | `57.88%` | `0.0%` | 800 | 698 | `+0.0s` |
| `2026-11-07 04:30:18` | `52.43%` | `0.0%` | 803 | 717 | `+0.0s` |
| `2026-11-07 04:00:19` | `49.82%` | `0.0%` | 849 | 759 | `+0.0s` |
| `2026-11-07 03:30:18` | `47.06%` | `0.0%` | 901 | 795 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.463000+00:00`.*
