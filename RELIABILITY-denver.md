# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-06T13:46:37.895977+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`38.89%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `720` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `619` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `280` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 280 | 38.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 1.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 326** | 3 | 2 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 228F** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 323** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 327** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 93L** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 0L** | 5 | 1 | 4 | **`80.0%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 29 | 10 | 20 | **`68.97%`** | `0.0%` | `+0.0s` |
| **Route FMR** | 9 | 5 | 6 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route BOND** | 6 | 3 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 117N** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |

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
| `116031430` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031431` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031471` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031506` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031698` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031745` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031796` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031797` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031830` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031831` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032131` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032142` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032259` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034484` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034539` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 13:46:37` | `38.89%` | `0.0%` | 720 | 619 | `+0.0s` |
| `2026-10-06 06:42:12` | `22.06%` | `0.0%` | 68 | 164 | `+0.0s` |
| `2026-10-06 00:28:48` | `32.14%` | `0.0%` | 585 | 552 | `+0.0s` |
| `2026-10-05 18:39:13` | `37.95%` | `0.0%` | 664 | 576 | `+0.0s` |
| `2026-10-05 18:02:21` | `37.97%` | `0.0%` | 669 | 568 | `+0.0s` |
| `2026-10-05 17:57:49` | `37.92%` | `0.0%` | 654 | 573 | `+0.0s` |
| `2026-10-05 17:20:39` | `37.83%` | `0.0%` | 637 | 588 | `+0.0s` |
| `2026-10-05 16:34:18` | `37.44%` | `0.0%` | 641 | 579 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T13:46:37.895977+00:00`.*
