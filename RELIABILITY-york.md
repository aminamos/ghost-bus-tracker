# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-07T07:00:19.666000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+131.9s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 20 | 80.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 12.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 4.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 0 | **`0.0%`** | `71.43%` | `+4.7 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+2.3 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `-6.5s` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+1.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+4.7 min (+281.3s)` | `+18.7 min (+1124s)` | 4 | `71.43%` |
| **Route 77** | `+2.3 min (+139.3s)` | `+6.0 min (+359s)` | 4 | `83.33%` |
| **Route 1** | `+1.8 min (+108.0s)` | `+1.8 min (+108s)` | 1 | `100.0%` |
| **Route 9899** | `+1.4 min (+84.8s)` | `+5.4 min (+324s)` | 4 | `80.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `31.3 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `77.3 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `87.7 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `83.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:19` | `0.0%` | `80.0%` | 25 | 15 | `+131.9s` |
| `2026-11-07 06:30:20` | `0.0%` | `73.53%` | 34 | 19 | `+188.1s` |
| `2026-11-07 06:00:21` | `4.44%` | `86.05%` | 45 | 27 | `+74.9s` |
| `2026-11-07 05:30:19` | `5.88%` | `81.25%` | 68 | 46 | `+127.7s` |
| `2026-11-07 05:00:19` | `10.42%` | `83.72%` | 96 | 62 | `+104.7s` |
| `2026-11-07 04:30:19` | `9.52%` | `86.84%` | 126 | 75 | `+99.7s` |
| `2026-11-07 04:00:24` | `5.84%` | `90.34%` | 154 | 86 | `+60.2s` |
| `2026-11-07 03:30:21` | `8.29%` | `84.94%` | 181 | 100 | `+65.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:19.666000+00:00`.*
