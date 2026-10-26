# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Transit Authority of River City** in **Louisville, KY** (Louisville Metropolitan Area, Kentucky).
> **Transit System:** TARC | **Location:** Louisville, KY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:22.196000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `44` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 44 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 6 | 0 | 6 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 81** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `t166-b3E9-sl10-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1AC-b3EA-sl10-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B0-b3F7-sl10-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B1-bBB9-sl10-vC` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B3-bBBA-sl10-vC` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B5-b1389-sl10-vC` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B5-b1F41-sl10-vC` | Route 8 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B5-b3F8-sl10-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B9-b2711-sl10-vC` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1BD-b138A-sl10-vC` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1C5-b3F9-sl10-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1C6-b4E21-sl10-vC` | Route 20 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1CA-b3EC-sl10-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1F4-b2712-sl10-vC` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1F4-bBBB-sl10-vC` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:22` | `100.0%` | `0.0%` | 44 | 0 | `+0.0s` |
| `2026-10-26 06:30:40` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-26 05:30:25` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-26 05:00:26` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-26 04:30:39` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-26 04:00:20` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-26 03:30:38` | `0.0%` | `0.0%` | 0 | 1 | `+0.0s` |
| `2026-10-26 01:00:28` | `5.88%` | `85.11%` | 51 | 31 | `+93.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:22.196000+00:00`.*
