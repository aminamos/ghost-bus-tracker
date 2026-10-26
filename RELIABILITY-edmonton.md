# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-26T07:00:22.446000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.27%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `45` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `24` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+2.1s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-12.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 26 | 57.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 22.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 11 | 6 | 1 | **`9.09%`** | `90.0%` | `+0.8 min` |
| **Route 008** | 8 | 4 | 0 | **`0.0%`** | `37.5%` | `-72.4s` |
| **Route 051** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.7 min` |
| **Route 002** | 10 | 5 | 0 | **`0.0%`** | `87.5%` | `+0.3 min` |
| **Route 009** | 8 | 4 | 0 | **`0.0%`** | `71.43%` | `-76.1s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 511** | `+4.7 min (+281.0s)` | `+5.4 min (+326s)` | 2 | `50.0%` |
| **Route 056** | `+1.7 min (+101.0s)` | `+1.7 min (+101s)` | 1 | `100.0%` |
| **Route 004** | `+0.8 min (+48.7s)` | `+3.1 min (+185s)` | 6 | `90.0%` |
| **Route 002** | `+0.3 min (+16.2s)` | `+1.4 min (+84s)` | 5 | `87.5%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.0 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.4 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.9 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32754185` | Route 004 | `23:57:00` | `SCHEDULED` | Assigned vehicle 3054 is broadcasting off-schedule with no vehicle covering 32754185 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:22` | `2.22%` | `70.27%` | 45 | 24 | `+2.1s` |
| `2026-10-26 06:30:42` | `0.0%` | `71.43%` | 68 | 47 | `+30.2s` |
| `2026-10-26 05:00:27` | `1.61%` | `82.68%` | 186 | 106 | `+13.4s` |
| `2026-10-26 04:00:20` | `2.17%` | `81.65%` | 230 | 123 | `+86.4s` |
| `2026-10-26 03:30:39` | `3.24%` | `80.87%` | 247 | 129 | `+42.3s` |
| `2026-10-26 01:00:29` | `5.45%` | `82.48%` | 404 | 232 | `+115.9s` |
| `2026-10-26 00:30:45` | `5.81%` | `82.5%` | 482 | 253 | `+113.9s` |
| `2026-10-25 23:30:22` | `7.31%` | `83.62%` | 520 | 257 | `+86.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:22.446000+00:00`.*
