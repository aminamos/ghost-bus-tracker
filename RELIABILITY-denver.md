# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.542000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.31%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `166` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `184` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `47` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 47 | 28.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 133** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route AT** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route DASH** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 40** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 43** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 0B** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `116031131` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031235` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031572` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034572` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034705` | Route 103W | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116034999` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035000` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037780` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037791` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116038293` | Route 133 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116038324` | Route 133 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039757` | Route 15L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040153` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040737` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116041930` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `28.31%` | `0.0%` | 166 | 184 | `+0.0s` |
| `2026-11-08 06:30:21` | `34.72%` | `0.0%` | 216 | 217 | `+0.0s` |
| `2026-11-08 06:00:18` | `36.07%` | `0.0%` | 244 | 234 | `+0.0s` |
| `2026-11-08 05:30:21` | `36.4%` | `0.0%` | 272 | 245 | `+0.0s` |
| `2026-11-08 05:00:18` | `37.15%` | `0.0%` | 288 | 254 | `+0.0s` |
| `2026-11-08 04:30:26` | `36.89%` | `0.0%` | 309 | 265 | `+0.0s` |
| `2026-11-08 04:00:19` | `37.35%` | `0.0%` | 332 | 281 | `+0.0s` |
| `2026-11-08 03:30:18` | `37.89%` | `0.0%` | 351 | 300 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.542000+00:00`.*
