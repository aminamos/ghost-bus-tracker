# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-17T07:00:19.084000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.07%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `58` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+26.4s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+15.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 62.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 17 | 29.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 6.9% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-13.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-252.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.4 min` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+1.7 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-39.4s` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-327.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-12.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+21.7 min (+1301.0s)` | `+21.7 min (+1301s)` | 1 | `0.0%` |
| **Route 923** | `+5.1 min (+306.0s)` | `+12.0 min (+718s)` | 2 | `66.67%` |
| **Route 18** | `+3.4 min (+206.3s)` | `+7.0 min (+417s)` | 3 | `66.67%` |
| **Route 921** | `+2.1 min (+128.5s)` | `+3.9 min (+233s)` | 2 | `100.0%` |
| **Route 922** | `+1.8 min (+105.5s)` | `+3.3 min (+197s)` | 4 | `100.0%` |
| **Route 2** | `+1.7 min (+102.7s)` | `+7.1 min (+426s)` | 3 | `33.33%` |
| **Route 17** | `+1.1 min (+69.0s)` | `+3.0 min (+180s)` | 3 | `100.0%` |
| **Route 62** | `+1.1 min (+68.0s)` | `+2.7 min (+161s)` | 1 | `100.0%` |
| **Route 11** | `+0.9 min (+55.0s)` | `+0.9 min (+55s)` | 2 | `100.0%` |
| **Route 22** | `+0.7 min (+41.5s)` | `+0.9 min (+56s)` | 2 | `100.0%` |

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
| `2026-11-17 07:00:19` | `0.0%` | `62.07%` | 58 | 58 | `+26.4s` |
| `2026-11-17 06:30:18` | `0.0%` | `58.56%` | 115 | 111 | `+17.6s` |
| `2026-11-17 06:00:19` | `3.43%` | `56.97%` | 175 | 165 | `-30.6s` |
| `2026-11-17 05:30:18` | `4.76%` | `57.41%` | 231 | 216 | `-1.2s` |
| `2026-11-17 05:00:18` | `5.63%` | `63.02%` | 302 | 265 | `-5.9s` |
| `2026-11-17 04:30:18` | `6.07%` | `58.82%` | 379 | 323 | `+7.0s` |
| `2026-11-17 04:00:18` | `8.0%` | `59.5%` | 425 | 358 | `+15.1s` |
| `2026-11-17 03:30:19` | `8.84%` | `59.29%` | 475 | 393 | `+7.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:19.084000+00:00`.*
