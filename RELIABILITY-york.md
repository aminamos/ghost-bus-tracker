# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-13T07:00:24.344000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`92.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+53.5s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 23 | 92.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+0.4 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 20** | 7 | 4 | 0 | **`0.0%`** | `85.71%` | `+1.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | `+1.5 min (+87.3s)` | `+3.5 min (+211s)` | 4 | `100.0%` |
| **Route 20** | `+1.3 min (+80.4s)` | `+6.8 min (+410s)` | 4 | `85.71%` |
| **Route 9899** | `+0.4 min (+25.4s)` | `+2.0 min (+119s)` | 4 | `80.0%` |
| **Route 107** | `+0.3 min (+18.0s)` | `+1.8 min (+109s)` | 2 | `100.0%` |
| **Route 1** | `+0.3 min (+16.0s)` | `+0.3 min (+16s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `78.4 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `87.1 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `88.7 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `93.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:24` | `0.0%` | `92.0%` | 25 | 15 | `+53.5s` |
| `2026-11-13 06:30:19` | `0.0%` | `94.12%` | 34 | 19 | `+47.5s` |
| `2026-11-13 05:30:19` | `4.41%` | `86.15%` | 68 | 47 | `+83.4s` |
| `2026-11-13 05:00:22` | `11.46%` | `88.24%` | 96 | 61 | `+81.4s` |
| `2026-11-13 04:30:19` | `10.57%` | `87.27%` | 123 | 72 | `+78.0s` |
| `2026-11-13 04:00:21` | `7.14%` | `88.81%` | 154 | 86 | `+61.2s` |
| `2026-11-13 03:30:19` | `3.87%` | `91.95%` | 181 | 100 | `+60.7s` |
| `2026-11-13 03:00:22` | `8.21%` | `88.95%` | 207 | 112 | `+60.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:24.344000+00:00`.*
