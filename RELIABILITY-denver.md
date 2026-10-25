# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T06:15:49.254000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `139` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `171` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `35` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 35 | 25.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15L** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route BOLT** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 4 | 4 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 40** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 0** | 5 | 5 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 38** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 5 | 4 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 153** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `116031154` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031235` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034705` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035007` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116036587` | Route 113G | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037791` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039474` | Route 153 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039717` | Route 15L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039757` | Route 15L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039781` | Route 15L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040153` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040244` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040780` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116041642` | Route 21 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116044103` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:49` | `25.18%` | `0.0%` | 139 | 171 | `+0.0s` |
| `2026-10-25 06:00:59` | `30.19%` | `0.0%` | 159 | 182 | `+0.0s` |
| `2026-10-25 05:30:23` | `36.62%` | `0.0%` | 213 | 204 | `+0.0s` |
| `2026-10-25 04:33:58` | `35.77%` | `0.0%` | 274 | 243 | `+0.0s` |
| `2026-10-25 03:30:21` | `37.79%` | `0.0%` | 307 | 267 | `+0.0s` |
| `2026-10-25 03:00:23` | `37.88%` | `0.0%` | 330 | 278 | `+0.0s` |
| `2026-10-25 02:30:21` | `35.48%` | `0.0%` | 341 | 298 | `+0.0s` |
| `2026-10-25 01:30:21` | `34.78%` | `0.0%` | 391 | 376 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:49.254000+00:00`.*
