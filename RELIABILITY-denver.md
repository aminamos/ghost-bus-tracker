# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-27T05:00:23.322000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`35.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `251` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `255` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `89` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 89 | 35.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 130** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 133** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route DASH** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route JUMP** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route BOND** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route SKIP** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 8 | 3 | 5 | **`62.5%`** | `0.0%` | `+0.0s` |
| **Route 15L** | 6 | 3 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `116031371` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031452` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031710` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031718` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032091` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034450` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034525` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034965` | Route 104L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035271` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035286` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116036286` | Route 113B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116036303` | Route 113G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037328` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037378` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037982` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 05:00:23` | `35.46%` | `0.0%` | 251 | 255 | `+0.0s` |
| `2026-10-27 04:30:20` | `36.36%` | `0.0%` | 275 | 269 | `+0.0s` |
| `2026-10-27 03:30:24` | `36.17%` | `0.0%` | 329 | 319 | `+0.0s` |
| `2026-10-27 02:30:21` | `37.08%` | `0.0%` | 383 | 318 | `+0.0s` |
| `2026-10-27 01:30:23` | `35.43%` | `0.0%` | 460 | 395 | `+0.0s` |
| `2026-10-27 00:30:56` | `33.89%` | `0.0%` | 602 | 506 | `+0.0s` |
| `2026-10-26 23:00:23` | `36.94%` | `0.0%` | 804 | 593 | `+0.0s` |
| `2026-10-26 22:30:28` | `36.43%` | `0.0%` | 807 | 600 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T05:00:23.322000+00:00`.*
