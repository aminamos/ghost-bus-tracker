# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T07:00:19.151000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.9%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `58` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+24.8s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-7.5s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 56.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 22 | 37.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.4% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-32.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-16.5s` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-68.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+0.5 min` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.7 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-75.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-8.2s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-158.3s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+17.8 min (+1068.0s)` | `+17.8 min (+1068s)` | 1 | `0.0%` |
| **Route 18** | `+4.7 min (+283.3s)` | `+8.8 min (+527s)` | 3 | `66.67%` |
| **Route 921** | `+3.2 min (+191.5s)` | `+4.4 min (+265s)` | 2 | `100.0%` |
| **Route 924** | `+2.4 min (+144.5s)` | `+5.2 min (+312s)` | 4 | `75.0%` |
| **Route 64** | `+1.9 min (+113.0s)` | `+4.0 min (+238s)` | 1 | `100.0%` |
| **Route 36** | `+1.7 min (+103.0s)` | `+3.5 min (+209s)` | 2 | `100.0%` |
| **Route 2** | `+0.8 min (+46.0s)` | `+0.9 min (+52s)` | 2 | `100.0%` |
| **Route 925** | `+0.5 min (+30.5s)` | `+3.5 min (+213s)` | 2 | `50.0%` |
| **Route 17** | `+0.5 min (+29.7s)` | `+3.8 min (+228s)` | 3 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:19` | `0.0%` | `56.9%` | 58 | 58 | `+24.8s` |
| `2026-11-04 05:30:17` | `2.72%` | `62.79%` | 257 | 215 | `+18.9s` |
| `2026-11-04 05:00:17` | `3.61%` | `62.16%` | 305 | 259 | `+3.5s` |
| `2026-11-04 04:30:17` | `4.01%` | `65.93%` | 374 | 317 | `+17.1s` |
| `2026-11-04 04:00:20` | `5.83%` | `66.57%` | 429 | 362 | `+23.3s` |
| `2026-11-04 03:30:19` | `7.01%` | `63.66%` | 471 | 388 | `+15.6s` |
| `2026-11-04 02:30:18` | `6.12%` | `66.23%` | 539 | 456 | `+44.6s` |
| `2026-11-04 02:00:18` | `6.67%` | `70.12%` | 585 | 492 | `+51.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:19.151000+00:00`.*
