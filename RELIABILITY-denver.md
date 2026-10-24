# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:22.712000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`29.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `121` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `164` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `36` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 36 | 29.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 76** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route BOLT** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route AB1** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 103W** | 6 | 3 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 104L** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 83L** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 101T** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |

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
| `116031372` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034327` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034397` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034398` | Route 103W | `N/A` | `SCHEDULED` | Assigned vehicle 72 is missing from active GPS transponder fleet |
| `116034970` | Route 104L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035266` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035331` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037327` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037403` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039283` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039363` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039691` | Route 153 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040689` | Route 169 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040858` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040942` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `29.75%` | `0.0%` | 121 | 164 | `+0.0s` |
| `2026-10-24 05:30:21` | `34.13%` | `0.0%` | 208 | 225 | `+0.0s` |
| `2026-10-24 05:00:24` | `36.47%` | `0.0%` | 255 | 244 | `+0.0s` |
| `2026-10-24 04:30:22` | `36.43%` | `0.0%` | 291 | 262 | `+0.0s` |
| `2026-10-24 04:00:23` | `37.34%` | `0.0%` | 308 | 274 | `+0.0s` |
| `2026-10-24 03:00:21` | `38.32%` | `0.0%` | 368 | 307 | `+0.0s` |
| `2026-10-24 02:00:23` | `35.76%` | `0.0%` | 425 | 352 | `+0.0s` |
| `2026-10-24 01:30:23` | `35.31%` | `0.0%` | 473 | 386 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.712000+00:00`.*
