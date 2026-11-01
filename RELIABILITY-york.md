# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.779000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`38.89%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `18` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `6` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-1964.3s` (`-32.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-1679.0s` (`-28.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 61.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 38.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 107** | 4 | 1 | 2 | **`50.0%`** | `0.0%` | `-1966.5s` |
| **Route 77** | 6 | 2 | 2 | **`33.33%`** | `0.0%` | `-2035.2s` |
| **Route 20** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `-2444.0s` |
| **Route 9899** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `-1548.3s` |

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
| **Route 107** | ~11.0m | ~11.0m | **`+0.5 min`** | `0.0 / 100` |
| **Route 77** | ~12.0m | ~12.0m | **`+0.3 min`** | `0.0 / 100` |
| **Route 9899** | ~26.0m | ~26.0m | **`+0.1 min`** | `21.6 / 100` |
| **Route 20** | ~20.5m | ~20.5m | **`+0.1 min`** | `37.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2012860` | Route 107 | `01:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2012511` | Route 77 | `02:05:00` | `SCHEDULED` | Assigned vehicle C1901 is missing from active GPS transponder fleet |
| `2012393` | Route 20 | `02:10:00` | `SCHEDULED` | Assigned vehicle C2250 is missing from active GPS transponder fleet |
| `2012883` | Route 107 | `02:25:00` | `SCHEDULED` | Assigned vehicle C2632 is missing from active GPS transponder fleet |
| `2012552` | Route 77 | `01:53:00` | `SCHEDULED` | Assigned vehicle C1821 is missing from active GPS transponder fleet |
| `2007708` | Route 9899 | `01:36:00` | `SCHEDULED` | Assigned vehicle M1406 is missing from active GPS transponder fleet |
| `2007181` | Route 1 | `01:57:00` | `SCHEDULED` | Assigned vehicle M1117 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `38.89%` | `0.0%` | 18 | 6 | `-1964.3s` |
| `2026-11-01 06:30:19` | `19.23%` | `33.33%` | 26 | 12 | `-848.0s` |
| `2026-11-01 06:00:21` | `36.96%` | `68.97%` | 46 | 14 | `+111.3s` |
| `2026-11-01 05:30:19` | `0.0%` | `78.57%` | 14 | 18 | `+118.6s` |
| `2026-11-01 05:00:21` | `8.0%` | `78.26%` | 25 | 26 | `+356.3s` |
| `2026-11-01 04:30:19` | `7.55%` | `79.59%` | 53 | 43 | `+134.0s` |
| `2026-11-01 04:00:18` | `11.9%` | `86.49%` | 84 | 58 | `+117.1s` |
| `2026-11-01 03:30:18` | `8.87%` | `87.61%` | 124 | 73 | `+100.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.779000+00:00`.*
