# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-10T07:00:17.828000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`47.17%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `56` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `53` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+8.9s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-32.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 25 | 44.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 24 | 42.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 7.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 5.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.4 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-202.0s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-101.5s` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.9 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-78.0s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-95.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-41.4s` |
| **Route 38** | 3 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-148.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-67.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 924** | `+5.6 min (+338.0s)` | `+10.2 min (+609s)` | 3 | `66.67%` |
| **Route 18** | `+4.9 min (+292.3s)` | `+10.9 min (+653s)` | 3 | `66.67%` |
| **Route 923** | `+4.4 min (+265.0s)` | `+7.2 min (+432s)` | 2 | `33.33%` |
| **Route 11** | `+2.4 min (+141.5s)` | `+3.0 min (+179s)` | 2 | `100.0%` |
| **Route 64** | `+1.6 min (+93.0s)` | `+3.6 min (+218s)` | 1 | `100.0%` |
| **Route 921** | `+1.5 min (+90.5s)` | `+2.5 min (+149s)` | 2 | `100.0%` |
| **Route 925** | `+0.4 min (+21.5s)` | `+3.0 min (+183s)` | 2 | `50.0%` |
| **Route 724** | `+0.1 min (+8.5s)` | `+1.5 min (+92s)` | 1 | `50.0%` |

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
| `2026-11-10 07:00:17` | `0.0%` | `47.17%` | 56 | 53 | `+8.9s` |
| `2026-11-10 06:30:17` | `0.93%` | `53.4%` | 107 | 103 | `+45.1s` |
| `2026-11-10 05:00:18` | `3.78%` | `55.17%` | 291 | 261 | `+113.9s` |
| `2026-11-10 04:30:18` | `4.76%` | `61.27%` | 357 | 315 | `+32.9s` |
| `2026-11-10 04:00:18` | `7.3%` | `60.64%` | 397 | 344 | `-1.4s` |
| `2026-11-10 03:30:18` | `7.05%` | `62.97%` | 454 | 397 | `+26.9s` |
| `2026-11-10 03:00:18` | `7.04%` | `65.57%` | 483 | 424 | `+32.9s` |
| `2026-11-10 02:30:18` | `7.13%` | `67.18%` | 519 | 454 | `+36.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:17.828000+00:00`.*
