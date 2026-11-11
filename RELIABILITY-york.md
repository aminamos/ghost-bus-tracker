# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-11T07:00:19.013000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+43.0s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

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
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `-11.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+1.5 min (+90.7s)` | `+5.4 min (+325s)` | 4 | `83.33%` |
| **Route 9899** | `+1.1 min (+66.2s)` | `+4.6 min (+274s)` | 4 | `100.0%` |
| **Route 77** | `+0.8 min (+49.8s)` | `+2.0 min (+122s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `81.8 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `89.2 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `92.2 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `95.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2242 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-11 07:00:19` | `4.0%` | `91.67%` | 25 | 15 | `+43.0s` |
| `2026-11-11 06:30:18` | `0.0%` | `85.29%` | 34 | 19 | `+57.7s` |
| `2026-11-11 06:00:26` | `4.44%` | `88.37%` | 45 | 27 | `+61.4s` |
| `2026-11-11 05:30:21` | `7.35%` | `88.89%` | 68 | 46 | `+55.6s` |
| `2026-11-11 05:00:20` | `10.42%` | `88.37%` | 96 | 61 | `+61.7s` |
| `2026-11-11 04:30:18` | `7.94%` | `85.34%` | 126 | 76 | `+56.5s` |
| `2026-11-11 04:00:19` | `7.79%` | `90.14%` | 154 | 87 | `+51.4s` |
| `2026-11-11 03:00:19` | `10.24%` | `89.67%` | 205 | 112 | `+77.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:19.013000+00:00`.*
