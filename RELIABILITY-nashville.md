# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **WeGo Public Transit** in **Nashville, TN** (Nashville Metropolitan Area, Tennessee).
> **Transit System:** WeGo | **Location:** Nashville, TN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-11T07:00:18.934000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`76.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `29` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `44` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+28.2s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 19 | 65.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 17.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 3.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 52** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `75.0%` | `-25.8s` |
| **Route 50** | 4 | 3 | 0 | **`0.0%`** | `50.0%` | `+2.7 min` |
| **Route 7** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `-86.0s` |
| **Route 55** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 3** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `-106.5s` |
| **Route 4** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 22** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `-393.0s` |
| **Route 56** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 50** | `+2.7 min (+160.2s)` | `+17.3 min (+1036s)` | 3 | `50.0%` |
| **Route 4** | `+1.9 min (+115.0s)` | `+1.9 min (+115s)` | 1 | `100.0%` |
| **Route 56** | `+1.6 min (+93.0s)` | `+3.3 min (+200s)` | 2 | `100.0%` |
| **Route 55** | `+1.5 min (+92.3s)` | `+1.8 min (+109s)` | 2 | `100.0%` |
| **Route 52** | `+1.1 min (+68.8s)` | `+4.2 min (+253s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 50** | ~30.0m | ~30.0m | **`+0.0 min`** | `71.8 / 100` |
| **Route 52** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.0 / 100` |
| **Route 23** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 56** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 55** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-11 07:00:18` | `0.0%` | `76.0%` | 29 | 44 | `+28.2s` |
| `2026-11-11 06:30:18` | `2.44%` | `72.5%` | 41 | 55 | `+22.6s` |
| `2026-11-11 06:00:25` | `0.0%` | `84.38%` | 54 | 71 | `+24.9s` |
| `2026-11-11 05:30:20` | `0.0%` | `94.12%` | 69 | 79 | `+60.3s` |
| `2026-11-11 05:00:19` | `0.0%` | `80.0%` | 85 | 85 | `+337.4s` |
| `2026-11-11 04:30:18` | `0.95%` | `50.0%` | 105 | 95 | `+411.0s` |
| `2026-11-11 04:00:19` | `0.83%` | `100.0%` | 120 | 96 | `+39.0s` |
| `2026-11-11 03:00:19` | `0.0%` | `0.0%` | 144 | 119 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:18.934000+00:00`.*
