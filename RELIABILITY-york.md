# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-17T07:00:22.892000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.35%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`90.91%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `23` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+80.5s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+4.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 20 | 87.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 8.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 4.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 5 | 3 | 1 | **`20.0%`** | `100.0%` | `+0.0 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `+1.7 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.3 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+3.2 min (+194.0s)` | `+3.2 min (+194s)` | 1 | `100.0%` |
| **Route 9899** | `+2.3 min (+135.6s)` | `+7.1 min (+427s)` | 4 | `80.0%` |
| **Route 107** | `+1.7 min (+102.2s)` | `+9.0 min (+539s)` | 2 | `83.33%` |
| **Route 77** | `+0.8 min (+46.3s)` | `+1.4 min (+84s)` | 4 | `100.0%` |
| **Route 20** | `+0.0 min (+2.0s)` | `+0.1 min (+8s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `44.9 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `85.0 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `93.7 / 100` |
| **Route 20** | ~21.0m | ~21.0m | **`+0.0 min`** | `99.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2211 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:22` | `4.35%` | `90.91%` | 23 | 14 | `+80.5s` |
| `2026-11-17 06:30:19` | `0.0%` | `88.24%` | 34 | 19 | `+211.8s` |
| `2026-11-17 06:00:22` | `4.44%` | `86.05%` | 45 | 27 | `+27.3s` |
| `2026-11-17 05:30:21` | `4.41%` | `89.23%` | 68 | 46 | `+51.2s` |
| `2026-11-17 05:00:18` | `6.32%` | `93.26%` | 95 | 61 | `+45.9s` |
| `2026-11-17 04:30:20` | `8.0%` | `86.96%` | 125 | 74 | `+29.3s` |
| `2026-11-17 04:00:18` | `5.23%` | `89.66%` | 153 | 85 | `+32.5s` |
| `2026-11-17 03:30:24` | `6.15%` | `86.9%` | 179 | 99 | `+47.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:22.892000+00:00`.*
