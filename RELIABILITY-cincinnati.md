# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southwest Ohio Regional Transit Authority** in **Cincinnati, OH** (Cincinnati Metropolitan Area, Ohio).
> **Transit System:** Metro | **Location:** Cincinnati, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-24T06:30:22.141000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.34%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `29` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `18` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 10.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 33** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 43** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 78** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2038700` | Route 33 | `N/A` | `SCHEDULED` | Assigned vehicle 2331 is broadcasting off-schedule with no vehicle covering 2038700 |
| `2030228` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 2358 is broadcasting off-schedule with no vehicle covering 2030228 |
| `2029458` | Route 78 | `N/A` | `SCHEDULED` | Assigned vehicle 2429 is broadcasting off-schedule with no vehicle covering 2029458 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `10.34%` | `0.0%` | 29 | 18 | `+0.0s` |
| `2026-10-24 05:30:20` | `4.65%` | `0.0%` | 43 | 26 | `+0.0s` |
| `2026-10-24 05:00:23` | `11.11%` | `0.0%` | 54 | 36 | `+0.0s` |
| `2026-10-24 04:30:21` | `9.33%` | `0.0%` | 75 | 49 | `+0.0s` |
| `2026-10-24 04:00:22` | `9.78%` | `0.0%` | 92 | 59 | `+0.0s` |
| `2026-10-24 03:30:34` | `8.18%` | `0.0%` | 110 | 66 | `+0.0s` |
| `2026-10-24 03:00:20` | `6.77%` | `0.0%` | 133 | 79 | `+0.0s` |
| `2026-10-24 02:30:32` | `12.41%` | `0.0%` | 145 | 92 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.141000+00:00`.*
