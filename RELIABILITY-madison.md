# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (City of Madison)** in **Madison, WI** (Madison Metropolitan Area, Wisconsin).
> **Transit System:** Metro Transit | **Location:** Madison, WI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.763000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`98.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `171` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `3` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `169` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 169 | 98.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route A** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route B** | 61 | 0 | 61 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route F** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route E** | 14 | 0 | 14 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 75** | 6 | 0 | 6 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `5051020` | Route F | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1306020` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4992020` | Route E | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `271020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1524020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2414020` | Route F | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `5097020` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `29020` | Route F | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1679020` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1198020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4550020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1238020` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3631020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2392020` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `305020` | Route 75 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `98.83%` | `0.0%` | 171 | 3 | `+0.0s` |
| `2026-10-28 06:30:21` | `97.13%` | `0.0%` | 174 | 3 | `+0.0s` |
| `2026-10-28 06:00:21` | `96.61%` | `0.0%` | 177 | 4 | `+0.0s` |
| `2026-10-28 05:30:26` | `96.15%` | `0.0%` | 182 | 15 | `+0.0s` |
| `2026-10-28 05:00:25` | `89.8%` | `0.0%` | 196 | 29 | `+0.0s` |
| `2026-10-28 04:30:32` | `83.33%` | `0.0%` | 210 | 38 | `+0.0s` |
| `2026-10-28 04:00:33` | `38.24%` | `0.0%` | 68 | 39 | `+0.0s` |
| `2026-10-28 03:30:18` | `50.57%` | `0.0%` | 87 | 39 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.763000+00:00`.*
