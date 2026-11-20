# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T06:30:18.965000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`35.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `207` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `253` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `74` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 74 | 35.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 88** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route SKIP** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 7 | 2 | 5 | **`71.43%`** | `0.0%` | `+0.0s` |
| **Route 65** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 76** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 42** | 5 | 3 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `116031374` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031468` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031713` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032090` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034451` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034527` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034946` | Route 104L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035209` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035314` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116036008` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116036410` | Route 113G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037327` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037406` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037970` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116038069` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 06:30:18` | `35.75%` | `0.0%` | 207 | 253 | `+0.0s` |
| `2026-11-20 06:00:21` | `37.5%` | `0.0%` | 248 | 269 | `+0.0s` |
| `2026-11-20 05:30:18` | `35.13%` | `0.0%` | 279 | 304 | `+0.0s` |
| `2026-11-20 05:00:20` | `38.64%` | `0.0%` | 308 | 319 | `+0.0s` |
| `2026-11-20 04:30:18` | `35.45%` | `0.0%` | 330 | 331 | `+0.0s` |
| `2026-11-20 04:00:19` | `38.02%` | `0.0%` | 363 | 329 | `+0.0s` |
| `2026-11-20 03:30:21` | `36.41%` | `0.0%` | 390 | 345 | `+0.0s` |
| `2026-11-20 03:00:19` | `36.52%` | `0.0%` | 408 | 358 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:18.965000+00:00`.*
