# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Transit Authority of River City** in **Louisville, KY** (Louisville Metropolitan Area, Kentucky).
> **Transit System:** TARC | **Location:** Louisville, KY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.464000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `48` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `48` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 48 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 6 | 0 | 6 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 93** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 99** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `t142-b16B49-slF-vC` | Route 93 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t146-b16B49-slF-vC` | Route 93 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t166-b3E9-slF-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1A1-b16B49-slF-vC` | Route 93 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1AC-b3EA-slF-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1AD-b182B9-slF-vC` | Route 99 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B0-b3F7-slF-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B1-b182B9-slF-vC` | Route 99 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B1-bBB9-slF-vC` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B3-bBBA-slF-vC` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B5-b1389-slF-vC` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B5-b1F41-slF-vC` | Route 8 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B5-b3F8-slF-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B9-b16B49-slF-vC` | Route 93 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t1B9-b2711-slF-vC` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `100.0%` | `0.0%` | 48 | 0 | `+0.0s` |
| `2026-10-28 06:30:20` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-28 06:00:20` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-28 05:30:24` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-28 05:00:24` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-28 04:30:24` | `50.0%` | `0.0%` | 2 | 1 | `-720.0s` |
| `2026-10-28 04:00:24` | `70.0%` | `33.33%` | 10 | 3 | `-37.3s` |
| `2026-10-28 03:30:18` | `18.18%` | `83.33%` | 22 | 13 | `+0.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.464000+00:00`.*
