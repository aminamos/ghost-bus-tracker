# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-21T22:30:36.714000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`36.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `817` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `616` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `300` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 300 | 36.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 120** | 4 | 1 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 208** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 32** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 120L** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route FMR** | 9 | 4 | 7 | **`77.78%`** | `0.0%` | `+0.0s` |
| **Route FF2** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 34 | 11 | 23 | **`67.65%`** | `0.0%` | `+0.0s` |
| **Route 139** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 402L** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 520** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |

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
| `116031396` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031397` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031469` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031680` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031728` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031756` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031757` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031843` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031844` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031845` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032104` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032105` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032161` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032162` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032250` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 22:30:36` | `36.72%` | `0.0%` | 817 | 616 | `+0.0s` |
| `2026-10-21 22:00:36` | `38.4%` | `0.0%` | 815 | 612 | `+0.0s` |
| `2026-10-21 21:30:36` | `37.83%` | `0.0%` | 785 | 596 | `+0.0s` |
| `2026-10-21 21:00:37` | `39.89%` | `0.0%` | 752 | 568 | `+0.0s` |
| `2026-10-21 20:30:37` | `40.48%` | `0.0%` | 709 | 538 | `+0.0s` |
| `2026-10-21 20:00:36` | `40.09%` | `0.0%` | 691 | 525 | `+0.0s` |
| `2026-10-21 19:30:40` | `37.54%` | `0.0%` | 666 | 541 | `+0.0s` |
| `2026-10-21 19:00:53` | `37.73%` | `0.0%` | 660 | 537 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T22:30:36.714000+00:00`.*
