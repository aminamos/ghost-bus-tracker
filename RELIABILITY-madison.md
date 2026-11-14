# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (City of Madison)** in **Madison, WI** (Madison Metropolitan Area, Wisconsin).
> **Transit System:** Metro Transit | **Location:** Madison, WI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:19.465000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `263` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `3` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `257` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 257 | 97.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route A** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route B** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route G** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 81** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 80** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `3629070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3818070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4869070` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2911070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2229070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3721070` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `384070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4663070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351070` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `733070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `601070` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4227070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `5278070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `573070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3045070` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `97.72%` | `0.0%` | 263 | 3 | `+0.0s` |
| `2026-11-14 06:30:22` | `45.45%` | `0.0%` | 11 | 15 | `+0.0s` |
| `2026-11-14 06:00:21` | `29.63%` | `0.0%` | 27 | 28 | `+0.0s` |
| `2026-11-14 05:30:18` | `22.92%` | `0.0%` | 48 | 37 | `+0.0s` |
| `2026-11-14 05:00:28` | `37.68%` | `0.0%` | 69 | 39 | `+0.0s` |
| `2026-11-14 04:30:18` | `51.72%` | `0.0%` | 87 | 40 | `+0.0s` |
| `2026-11-14 04:00:22` | `53.0%` | `0.0%` | 100 | 41 | `+0.0s` |
| `2026-11-14 03:30:21` | `54.08%` | `0.0%` | 98 | 42 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.465000+00:00`.*
