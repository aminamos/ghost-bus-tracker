# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-26T06:30:18.193000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.66%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `100` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `99` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+26.1s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-10.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 65 | 65.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 28 | 28.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 6.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+1.6 min` |
| **Route 11** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+3.4 min` |
| **Route 14** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-11.0s` |
| **Route 17** | 5 | 4 | 0 | **`0.0%`** | `60.0%` | `+0.5 min` |
| **Route 18** | 5 | 4 | 0 | **`0.0%`** | `50.0%` | `-49.0s` |
| **Route 2** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 22** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-34.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `-69.4s` |
| **Route 323** | 3 | 2 | 0 | **`0.0%`** | `33.33%` | `-92.7s` |
| **Route 36** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+5.3 min (+320.0s)` | `+10.3 min (+618s)` | 2 | `50.0%` |
| **Route 925** | `+4.8 min (+285.5s)` | `+8.5 min (+509s)` | 1 | `50.0%` |
| **Route 9** | `+4.4 min (+261.5s)` | `+4.6 min (+278s)` | 2 | `100.0%` |
| **Route 11** | `+3.4 min (+205.2s)` | `+7.7 min (+460s)` | 4 | `75.0%` |
| **Route 924** | `+3.0 min (+183.0s)` | `+11.7 min (+699s)` | 6 | `83.33%` |
| **Route 923** | `+2.0 min (+120.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 2** | `+1.8 min (+105.2s)` | `+4.2 min (+249s)` | 4 | `100.0%` |
| **Route 10** | `+1.6 min (+96.8s)` | `+8.3 min (+500s)` | 4 | `50.0%` |
| **Route 921** | `+0.8 min (+48.8s)` | `+3.5 min (+207s)` | 3 | `75.0%` |
| **Route 36** | `+0.8 min (+46.3s)` | `+2.3 min (+140s)` | 2 | `100.0%` |

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
| `2026-11-26 06:30:18` | `0.0%` | `65.66%` | 100 | 99 | `+26.1s` |
| `2026-11-26 06:00:17` | `3.29%` | `56.46%` | 152 | 147 | `+10.5s` |
| `2026-11-26 05:00:17` | `5.41%` | `58.37%` | 259 | 245 | `+0.7s` |
| `2026-11-26 04:30:18` | `6.85%` | `59.2%` | 321 | 299 | `+14.8s` |
| `2026-11-26 03:30:18` | `8.58%` | `60.71%` | 431 | 392 | `+11.4s` |
| `2026-11-26 03:00:17` | `9.44%` | `63.72%` | 466 | 420 | `+14.4s` |
| `2026-11-26 02:30:18` | `9.43%` | `64.18%` | 509 | 455 | `+18.8s` |
| `2026-11-26 02:00:18` | `9.17%` | `65.0%` | 556 | 500 | `+15.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T06:30:18.193000+00:00`.*
