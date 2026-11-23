# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southwest Ohio Regional Transit Authority** in **Cincinnati, OH** (Cincinnati Metropolitan Area, Ohio).
> **Transit System:** Metro | **Location:** Cincinnati, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:18.570000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`24.14%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `29` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `18` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 24.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 33** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 19** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 78** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 43** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `2041711` | Route 33 | `N/A` | `SCHEDULED` | Assigned vehicle 2327 is broadcasting off-schedule with no vehicle covering 2041711 |
| `2042592` | Route 17 | `N/A` | `SCHEDULED` | Assigned vehicle 2444 is broadcasting off-schedule with no vehicle covering 2042592 |
| `2025131` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 2472 is broadcasting off-schedule with no vehicle covering 2025131 |
| `2024937` | Route 78 | `N/A` | `SCHEDULED` | Assigned vehicle 2483 is broadcasting off-schedule with no vehicle covering 2024937 |
| `2025311` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 2490 is broadcasting off-schedule with no vehicle covering 2025311 |
| `2025263` | Route 4 | `N/A` | `SCHEDULED` | Assigned vehicle 2491 is broadcasting off-schedule with no vehicle covering 2025263 |
| `2041822` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 2494 is broadcasting off-schedule with no vehicle covering 2041822 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:18` | `24.14%` | `0.0%` | 29 | 18 | `+0.0s` |
| `2026-11-23 06:30:18` | `8.57%` | `0.0%` | 35 | 20 | `+0.0s` |
| `2026-11-23 06:00:20` | `9.52%` | `0.0%` | 42 | 27 | `+0.0s` |
| `2026-11-23 05:30:18` | `3.45%` | `0.0%` | 58 | 38 | `+0.0s` |
| `2026-11-23 05:00:21` | `14.08%` | `0.0%` | 71 | 46 | `+0.0s` |
| `2026-11-23 04:30:21` | `8.6%` | `0.0%` | 93 | 57 | `+0.0s` |
| `2026-11-23 04:00:19` | `12.0%` | `0.0%` | 100 | 61 | `+0.0s` |
| `2026-11-23 03:30:18` | `9.48%` | `0.0%` | 116 | 66 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:18.570000+00:00`.*
