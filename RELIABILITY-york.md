# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-19T07:00:20.365000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+77.1s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 88.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 8.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 20** | 7 | 4 | 0 | **`0.0%`** | `71.43%` | `+3.0 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+3.0 min (+178.6s)` | `+11.7 min (+699s)` | 4 | `71.43%` |
| **Route 77** | `+1.1 min (+69.0s)` | `+2.2 min (+132s)` | 4 | `100.0%` |
| **Route 9899** | `+0.9 min (+55.2s)` | `+3.1 min (+186s)` | 4 | `100.0%` |
| **Route 107** | `+0.1 min (+8.0s)` | `+0.7 min (+39s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `62.2 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `91.7 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `91.1 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `96.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 07:00:20` | `0.0%` | `88.0%` | 25 | 15 | `+77.1s` |
| `2026-11-19 06:30:20` | `2.94%` | `81.82%` | 34 | 18 | `+119.5s` |
| `2026-11-19 06:00:21` | `11.36%` | `87.18%` | 44 | 27 | `+57.5s` |
| `2026-11-19 05:30:26` | `8.96%` | `83.61%` | 67 | 45 | `+63.3s` |
| `2026-11-19 05:00:19` | `9.38%` | `85.06%` | 96 | 62 | `+133.6s` |
| `2026-11-19 04:30:19` | `6.35%` | `88.98%` | 126 | 75 | `+62.2s` |
| `2026-11-19 04:00:21` | `5.84%` | `87.59%` | 154 | 87 | `+67.8s` |
| `2026-11-19 03:30:18` | `6.08%` | `90.0%` | 181 | 97 | `+63.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:20.365000+00:00`.*
