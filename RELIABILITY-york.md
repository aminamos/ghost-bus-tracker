# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-05T07:00:18.229000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+36.8s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 23 | 92.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 8.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 2 | **`28.57%`** | `100.0%` | `+0.1 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+1.3 min (+78.0s)` | `+1.3 min (+78s)` | 1 | `100.0%` |
| **Route 77** | `+0.8 min (+47.0s)` | `+1.9 min (+116s)` | 4 | `100.0%` |
| **Route 107** | `+0.7 min (+44.2s)` | `+2.4 min (+141s)` | 2 | `100.0%` |
| **Route 9899** | `+0.6 min (+37.0s)` | `+1.9 min (+115s)` | 4 | `100.0%` |
| **Route 20** | `+0.1 min (+7.4s)` | `+1.4 min (+83s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `82.6 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `92.7 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `94.4 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `93.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024940` | Route 20 | `02:47:00` | `SCHEDULED` | Assigned vehicle C2017 is broadcasting off-schedule with no vehicle covering 2024940 |
| `2025027` | Route 20 | `02:04:00` | `SCHEDULED` | Assigned vehicle C2017 is broadcasting off-schedule with no vehicle covering 2025027 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:18` | `8.0%` | `100.0%` | 25 | 15 | `+36.8s` |
| `2026-11-05 06:30:18` | `0.0%` | `88.24%` | 34 | 19 | `+73.6s` |
| `2026-11-05 06:00:18` | `2.22%` | `88.64%` | 45 | 29 | `+118.2s` |
| `2026-11-05 05:30:20` | `8.96%` | `83.61%` | 67 | 43 | `+107.3s` |
| `2026-11-05 05:00:18` | `13.54%` | `79.52%` | 96 | 61 | `+80.5s` |
| `2026-11-05 04:30:18` | `9.52%` | `85.09%` | 126 | 76 | `+89.0s` |
| `2026-11-05 04:00:20` | `4.58%` | `87.67%` | 153 | 87 | `+52.2s` |
| `2026-11-05 03:30:19` | `8.94%` | `88.96%` | 179 | 97 | `+62.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.229000+00:00`.*
