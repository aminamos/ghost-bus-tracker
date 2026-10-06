# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T17:21:55.963813+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`38.05%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `636` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `575` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `242` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 242 | 38.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 1.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 208** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 402L** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 32** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 120L** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 29 | 11 | 20 | **`68.97%`** | `0.0%` | `+0.0s` |
| **Route 0L** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route BOND** | 6 | 3 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 323** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 326** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |

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
| `116031416` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031417` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031460` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031690` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031738` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031777` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031778` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031816` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031817` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031925` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031941` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032120` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032176` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032178` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 17:21:55` | `38.05%` | `0.0%` | 636 | 575 | `+0.0s` |
| `2026-10-06 17:21:04` | `38.06%` | `0.0%` | 628 | 574 | `+0.0s` |
| `2026-10-06 13:46:37` | `38.89%` | `0.0%` | 720 | 619 | `+0.0s` |
| `2026-10-06 06:42:12` | `22.06%` | `0.0%` | 68 | 164 | `+0.0s` |
| `2026-10-06 00:28:48` | `32.14%` | `0.0%` | 585 | 552 | `+0.0s` |
| `2026-10-05 18:39:13` | `37.95%` | `0.0%` | 664 | 576 | `+0.0s` |
| `2026-10-05 18:02:21` | `37.97%` | `0.0%` | 669 | 568 | `+0.0s` |
| `2026-10-05 17:57:49` | `37.92%` | `0.0%` | 654 | 573 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T17:21:55.963813+00:00`.*
