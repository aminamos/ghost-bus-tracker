# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-30T05:00:18.905000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.76%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.88%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `170` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `167` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+14.8s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-11.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 100 | 58.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 56 | 32.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 10 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 1.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 68** | 5 | 3 | 1 | **`20.0%`** | `50.0%` | `-230.2s` |
| **Route 64** | 6 | 3 | 1 | **`16.67%`** | `80.0%` | `+0.7 min` |
| **Route 18** | 9 | 7 | 1 | **`11.11%`** | `62.5%` | `-16.9s` |
| **Route 10** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-75.3s` |
| **Route 11** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 14** | 6 | 4 | 0 | **`0.0%`** | `33.33%` | `+1.2 min` |
| **Route 17** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+0.1 min` |
| **Route 2** | 6 | 4 | 0 | **`0.0%`** | `50.0%` | `-25.2s` |
| **Route 22** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-43.4s` |
| **Route 3** | 6 | 5 | 0 | **`0.0%`** | `50.0%` | `-49.7s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 71** | `+12.0 min (+722.5s)` | `+18.8 min (+1130s)` | 1 | `0.0%` |
| **Route 94** | `+3.4 min (+202.3s)` | `+4.3 min (+260s)` | 3 | `100.0%` |
| **Route 54** | `+3.3 min (+195.8s)` | `+7.8 min (+470s)` | 4 | `80.0%` |
| **Route 923** | `+3.3 min (+195.3s)` | `+8.6 min (+518s)` | 3 | `83.33%` |
| **Route 925** | `+3.2 min (+189.8s)` | `+9.2 min (+550s)` | 4 | `83.33%` |
| **Route 924** | `+2.6 min (+153.4s)` | `+15.0 min (+898s)` | 7 | `77.78%` |
| **Route 323** | `+1.5 min (+91.0s)` | `+9.6 min (+575s)` | 2 | `60.0%` |
| **Route 921** | `+1.5 min (+91.0s)` | `+5.1 min (+307s)` | 4 | `71.43%` |
| **Route 901** | `+1.2 min (+75.0s)` | `+2.5 min (+150s)` | 2 | `100.0%` |
| **Route 14** | `+1.2 min (+72.2s)` | `+12.3 min (+737s)` | 4 | `33.33%` |

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
| `1385125` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360805` | Route 64 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367762` | Route 68 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 05:00:18` | `1.76%` | `59.88%` | 170 | 167 | `+14.8s` |
| `2026-10-30 04:30:18` | `4.44%` | `63.26%` | 225 | 215 | `+31.8s` |
| `2026-10-30 03:30:18` | `7.27%` | `59.56%` | 344 | 319 | `+41.7s` |
| `2026-10-30 03:00:18` | `8.02%` | `62.13%` | 399 | 367 | `+57.3s` |
| `2026-10-30 02:30:19` | `9.19%` | `62.47%` | 446 | 397 | `+35.9s` |
| `2026-10-30 02:00:18` | `8.69%` | `63.53%` | 495 | 436 | `+54.2s` |
| `2026-10-30 01:30:19` | `8.87%` | `65.81%` | 530 | 465 | `+57.5s` |
| `2026-10-30 01:00:18` | `9.57%` | `69.46%` | 575 | 501 | `+63.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T05:00:18.905000+00:00`.*
