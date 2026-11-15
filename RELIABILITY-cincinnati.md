# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southwest Ohio Regional Transit Authority** in **Cincinnati, OH** (Cincinnati Metropolitan Area, Ohio).
> **Transit System:** Metro | **Location:** Cincinnati, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:18.940000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.13%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `31` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `19` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `5` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 5 | 16.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 3.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 33** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 43** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 78** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 7 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2040639` | Route 33 | `N/A` | `SCHEDULED` | Assigned vehicle 2338 is broadcasting off-schedule with no vehicle covering 2040639 |
| `2024112` | Route 4 | `N/A` | `SCHEDULED` | Assigned vehicle 2426 is broadcasting off-schedule with no vehicle covering 2024112 |
| `2024009` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 2510 is broadcasting off-schedule with no vehicle covering 2024009 |
| `2023829` | Route 78 | `N/A` | `SCHEDULED` | Assigned vehicle 2519 is broadcasting off-schedule with no vehicle covering 2023829 |
| `2024202` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 2545 is broadcasting off-schedule with no vehicle covering 2024202 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `16.13%` | `0.0%` | 31 | 19 | `+0.0s` |
| `2026-11-15 06:30:18` | `10.26%` | `0.0%` | 39 | 24 | `+0.0s` |
| `2026-11-15 06:00:32` | `15.22%` | `0.0%` | 46 | 30 | `+0.0s` |
| `2026-11-15 05:30:19` | `8.47%` | `0.0%` | 59 | 38 | `+0.0s` |
| `2026-11-15 05:00:19` | `6.25%` | `0.0%` | 80 | 49 | `+0.0s` |
| `2026-11-15 04:30:19` | `9.8%` | `0.0%` | 102 | 63 | `+0.0s` |
| `2026-11-15 04:00:19` | `9.91%` | `0.0%` | 111 | 66 | `+0.0s` |
| `2026-11-15 03:30:18` | `8.0%` | `0.0%` | 125 | 71 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.940000+00:00`.*
