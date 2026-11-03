# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-03T07:00:18.998000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+29.5s` (`+0.5 min`) | Average delay across all active tracked runs |
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
| **Route 20** | 7 | 4 | 1 | **`14.29%`** | `100.0%` | `+0.3 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+1.2 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `-18.2s` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | `+1.2 min (+74.0s)` | `+5.1 min (+304s)` | 4 | `83.33%` |
| **Route 1** | `+1.0 min (+59.0s)` | `+1.0 min (+59s)` | 1 | `100.0%` |
| **Route 9899** | `+0.7 min (+42.4s)` | `+1.5 min (+88s)` | 4 | `100.0%` |
| **Route 20** | `+0.3 min (+17.2s)` | `+2.0 min (+120s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `82.2 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `87.8 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `93.0 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `97.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2006 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `4.0%` | `91.67%` | 25 | 15 | `+29.5s` |
| `2026-11-03 06:30:26` | `0.0%` | `94.12%` | 34 | 19 | `+50.4s` |
| `2026-11-03 06:00:19` | `4.44%` | `88.37%` | 45 | 27 | `+27.6s` |
| `2026-11-03 05:30:19` | `5.88%` | `89.06%` | 68 | 45 | `+52.3s` |
| `2026-11-03 05:00:27` | `3.12%` | `92.47%` | 96 | 61 | `+37.1s` |
| `2026-11-03 04:30:22` | `5.56%` | `93.28%` | 126 | 75 | `+26.1s` |
| `2026-11-03 04:00:20` | `7.14%` | `87.41%` | 154 | 86 | `+39.9s` |
| `2026-11-03 03:30:21` | `2.81%` | `87.86%` | 178 | 97 | `+35.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.998000+00:00`.*
