# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southwest Ohio Regional Transit Authority** in **Cincinnati, OH** (Cincinnati Metropolitan Area, Ohio).
> **Transit System:** Metro | **Location:** Cincinnati, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.374000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`20.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `30` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `18` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 20.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 33** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 19** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 17** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 78** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 43** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2041822` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 2371 is broadcasting off-schedule with no vehicle covering 2041822 |
| `2041711` | Route 33 | `N/A` | `SCHEDULED` | Assigned vehicle 2372 is broadcasting off-schedule with no vehicle covering 2041711 |
| `2025311` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 2397 is broadcasting off-schedule with no vehicle covering 2025311 |
| `2042592` | Route 17 | `N/A` | `SCHEDULED` | Assigned vehicle 2478 is broadcasting off-schedule with no vehicle covering 2042592 |
| `2024937` | Route 78 | `N/A` | `SCHEDULED` | Assigned vehicle 2511 is broadcasting off-schedule with no vehicle covering 2024937 |
| `2025131` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 2515 is broadcasting off-schedule with no vehicle covering 2025131 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `20.0%` | `0.0%` | 30 | 18 | `+0.0s` |
| `2026-11-09 06:30:21` | `8.57%` | `0.0%` | 35 | 20 | `+0.0s` |
| `2026-11-09 06:00:18` | `9.76%` | `0.0%` | 41 | 26 | `+0.0s` |
| `2026-11-09 05:30:18` | `1.67%` | `0.0%` | 60 | 39 | `+0.0s` |
| `2026-11-09 05:00:18` | `9.46%` | `100.0%` | 74 | 46 | `+180.0s` |
| `2026-11-09 04:30:19` | `8.51%` | `90.0%` | 94 | 58 | `+115.6s` |
| `2026-11-09 04:00:19` | `13.13%` | `92.11%` | 99 | 61 | `+83.7s` |
| `2026-11-09 03:30:18` | `9.48%` | `88.0%` | 116 | 66 | `+122.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.374000+00:00`.*
