# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (City of Madison)** in **Madison, WI** (Madison Metropolitan Area, Wisconsin).
> **Transit System:** Metro Transit | **Location:** Madison, WI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T06:15:48.269000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`75.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `24` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `3` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `18` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 75.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route G** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 80** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 81** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `1055010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4465010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `5264010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2495010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1753010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `364010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4344010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `327010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1086010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `5139010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4675010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3275010` | Route G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `5120070` | Route 80 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3704070` | Route 81 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `190070` | Route 82 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:48` | `75.0%` | `0.0%` | 24 | 3 | `+0.0s` |
| `2026-10-25 06:01:04` | `73.91%` | `0.0%` | 23 | 3 | `+0.0s` |
| `2026-10-25 05:30:23` | `73.91%` | `0.0%` | 23 | 4 | `+0.0s` |
| `2026-10-25 05:00:33` | `75.0%` | `0.0%` | 24 | 11 | `+0.0s` |
| `2026-10-25 04:33:58` | `26.32%` | `0.0%` | 19 | 23 | `+0.0s` |
| `2026-10-25 03:30:21` | `43.06%` | `0.0%` | 72 | 36 | `+0.0s` |
| `2026-10-25 03:00:22` | `41.98%` | `0.0%` | 81 | 37 | `+0.0s` |
| `2026-10-25 02:30:20` | `52.83%` | `0.0%` | 106 | 38 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:48.269000+00:00`.*
