# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-06T07:00:17.924000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.79%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.18%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `56` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `55` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+35.3s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+2.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 32 | 57.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 19 | 33.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 5.4% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 63** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-64.0s` |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-66.5s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-35.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+1.6 min` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.4 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-18.0s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-19.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+0.3 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-66.3s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 924** | `+5.1 min (+308.8s)` | `+19.6 min (+1173s)` | 4 | `50.0%` |
| **Route 923** | `+3.8 min (+228.0s)` | `+7.0 min (+417s)` | 2 | `66.67%` |
| **Route 18** | `+2.4 min (+145.7s)` | `+4.6 min (+275s)` | 3 | `100.0%` |
| **Route 922** | `+1.7 min (+103.2s)` | `+4.9 min (+296s)` | 4 | `75.0%` |
| **Route 17** | `+1.6 min (+99.0s)` | `+5.5 min (+331s)` | 3 | `66.67%` |
| **Route 64** | `+1.6 min (+94.5s)` | `+3.9 min (+236s)` | 1 | `100.0%` |
| **Route 921** | `+1.4 min (+83.0s)` | `+2.2 min (+130s)` | 2 | `100.0%` |
| **Route 11** | `+1.1 min (+68.5s)` | `+1.6 min (+96s)` | 2 | `100.0%` |
| **Route 925** | `+0.5 min (+28.0s)` | `+1.8 min (+110s)` | 2 | `100.0%` |
| **Route 3** | `+0.3 min (+20.8s)` | `+6.9 min (+416s)` | 5 | `40.0%` |

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
| `1274952` | Route 63 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:17` | `1.79%` | `58.18%` | 56 | 55 | `+35.3s` |
| `2026-11-06 06:30:18` | `1.8%` | `58.72%` | 111 | 109 | `+24.4s` |
| `2026-11-06 05:30:18` | `7.93%` | `61.24%` | 227 | 209 | `-14.8s` |
| `2026-11-06 05:00:18` | `8.93%` | `57.25%` | 280 | 255 | `+0.4s` |
| `2026-11-06 04:30:19` | `9.14%` | `59.75%` | 350 | 318 | `+13.5s` |
| `2026-11-06 04:00:20` | `11.5%` | `65.34%` | 400 | 354 | `+18.2s` |
| `2026-11-06 03:30:19` | `11.65%` | `63.34%` | 455 | 401 | `+16.9s` |
| `2026-11-06 03:00:18` | `10.84%` | `66.43%` | 489 | 429 | `+12.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:17.924000+00:00`.*
