# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:18.748000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`30.53%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `131` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `229` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `40` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 40 | 30.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 30** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 133** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 16** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 31** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 40** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 43** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 0B** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `116031243` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031337` | Route 0 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116031639` | Route 0B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116035105` | Route 105 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037262` | Route 12 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037868` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116037870` | Route 121 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116038366` | Route 133 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116038406` | Route 133 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039050` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039088` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039146` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039865` | Route 15L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040312` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116040341` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:18` | `30.53%` | `0.0%` | 131 | 229 | `+0.0s` |
| `2026-11-23 06:30:18` | `30.22%` | `0.0%` | 182 | 206 | `+0.0s` |
| `2026-11-23 06:00:22` | `37.04%` | `0.0%` | 216 | 217 | `+0.0s` |
| `2026-11-23 05:30:18` | `37.12%` | `0.0%` | 229 | 225 | `+0.0s` |
| `2026-11-23 05:00:22` | `36.51%` | `0.0%` | 241 | 240 | `+0.0s` |
| `2026-11-23 04:30:22` | `36.94%` | `0.0%` | 268 | 251 | `+0.0s` |
| `2026-11-23 04:00:20` | `36.07%` | `0.0%` | 280 | 260 | `+0.0s` |
| `2026-11-23 03:30:18` | `36.12%` | `0.0%` | 299 | 266 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:18.748000+00:00`.*
