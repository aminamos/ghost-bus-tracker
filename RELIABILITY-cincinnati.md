# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southwest Ohio Regional Transit Authority** in **Cincinnati, OH** (Cincinnati Metropolitan Area, Ohio).
> **Transit System:** Metro | **Location:** Cincinnati, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-27T07:00:34.099000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.04%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `23` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `17` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 13.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 33** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 78** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 43** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2028053` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 2438 is broadcasting off-schedule with no vehicle covering 2028053 |
| `2028052` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 2448 is broadcasting off-schedule with no vehicle covering 2028052 |
| `2030348` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 2547 is broadcasting off-schedule with no vehicle covering 2030348 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 07:00:34` | `13.04%` | `0.0%` | 23 | 17 | `+0.0s` |
| `2026-10-27 06:30:33` | `10.34%` | `0.0%` | 29 | 18 | `+0.0s` |
| `2026-10-27 05:30:34` | `4.88%` | `0.0%` | 41 | 24 | `+0.0s` |
| `2026-10-27 05:00:22` | `11.32%` | `0.0%` | 53 | 35 | `+0.0s` |
| `2026-10-27 04:30:19` | `13.04%` | `0.0%` | 69 | 46 | `+0.0s` |
| `2026-10-27 04:00:23` | `10.71%` | `0.0%` | 84 | 55 | `+0.0s` |
| `2026-10-27 03:30:23` | `12.0%` | `0.0%` | 100 | 63 | `+0.0s` |
| `2026-10-27 03:00:36` | `8.8%` | `0.0%` | 125 | 77 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T07:00:34.099000+00:00`.*
