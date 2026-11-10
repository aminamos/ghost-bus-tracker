# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-10T07:00:18.738000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+46.5s` (`+0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+4.5s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 88.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 4.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 1 | **`14.29%`** | `83.33%` | `+1.5 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `-4.7s` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+1.5 min (+88.3s)` | `+6.7 min (+403s)` | 4 | `83.33%` |
| **Route 1** | `+1.2 min (+72.0s)` | `+1.2 min (+72s)` | 1 | `100.0%` |
| **Route 77** | `+0.8 min (+51.0s)` | `+2.0 min (+121s)` | 4 | `100.0%` |
| **Route 9899** | `+0.8 min (+47.2s)` | `+1.9 min (+115s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `77.4 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `87.4 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `93.0 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `95.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2020 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:18` | `4.0%` | `91.67%` | 25 | 15 | `+46.5s` |
| `2026-11-10 06:30:19` | `2.94%` | `78.79%` | 34 | 19 | `+103.1s` |
| `2026-11-10 06:00:18` | `4.44%` | `83.72%` | 45 | 28 | `+40.7s` |
| `2026-11-10 05:30:21` | `5.88%` | `87.5%` | 68 | 45 | `+65.7s` |
| `2026-11-10 05:00:19` | `9.38%` | `90.8%` | 96 | 63 | `+58.3s` |
| `2026-11-10 04:30:20` | `7.14%` | `85.47%` | 126 | 74 | `+38.9s` |
| `2026-11-10 04:00:20` | `5.84%` | `87.59%` | 154 | 86 | `+46.7s` |
| `2026-11-10 03:30:18` | `1.1%` | `89.39%` | 181 | 99 | `+55.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:18.738000+00:00`.*
