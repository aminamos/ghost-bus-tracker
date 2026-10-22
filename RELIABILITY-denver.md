# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:00:21.754000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`38.6%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `658` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `551` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `254` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 254 | 38.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 9** | 3 | 1 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 206** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 228A** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 88L** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route AT** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 0L** | 7 | 2 | 5 | **`71.43%`** | `0.0%` | `+0.0s` |
| **Route FREE** | 34 | 10 | 24 | **`70.59%`** | `0.0%` | `+0.0s` |
| **Route 135** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |

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
| `116031410` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031411` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031476` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031480` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031687` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031735` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031770` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031771` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031773` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031809` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031810` | Route 0L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031920` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031939` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032115` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116032268` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:00:21` | `38.6%` | `0.0%` | 658 | 551 | `+0.0s` |
| `2026-10-22 18:30:37` | `37.31%` | `0.0%` | 654 | 540 | `+0.0s` |
| `2026-10-22 18:00:41` | `39.4%` | `0.0%` | 665 | 535 | `+0.0s` |
| `2026-10-22 17:30:39` | `39.02%` | `0.0%` | 651 | 538 | `+0.0s` |
| `2026-10-22 17:00:40` | `39.72%` | `0.0%` | 642 | 529 | `+0.0s` |
| `2026-10-22 16:31:20` | `39.18%` | `0.0%` | 661 | 526 | `+0.0s` |
| `2026-10-22 15:30:47` | `39.15%` | `0.0%` | 682 | 535 | `+0.0s` |
| `2026-10-22 15:01:09` | `37.8%` | `0.0%` | 717 | 577 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:00:21.754000+00:00`.*
