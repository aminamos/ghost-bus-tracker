# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-28T07:00:18.006000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `56` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `56` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+126.9s` (`+2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+66.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 42 | 75.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 10.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 10.7% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.8 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.4 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.6 min` |
| **Route 22** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.9 min` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+6.0 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-418.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-41.0s` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `50.0%` | `+3.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+21.1 min (+1269.0s)` | `+21.1 min (+1269s)` | 1 | `0.0%` |
| **Route 924** | `+6.6 min (+394.5s)` | `+18.9 min (+1131s)` | 4 | `75.0%` |
| **Route 3** | `+6.0 min (+362.8s)` | `+10.7 min (+640s)` | 4 | `25.0%` |
| **Route 22** | `+4.9 min (+294.7s)` | `+6.9 min (+414s)` | 3 | `66.67%` |
| **Route 2** | `+4.6 min (+277.0s)` | `+4.9 min (+295s)` | 2 | `100.0%` |
| **Route 18** | `+4.4 min (+261.3s)` | `+5.2 min (+313s)` | 3 | `66.67%` |
| **Route 10** | `+3.8 min (+226.0s)` | `+4.4 min (+265s)` | 2 | `100.0%` |
| **Route 62** | `+3.3 min (+195.5s)` | `+7.0 min (+418s)` | 1 | `50.0%` |
| **Route 925** | `+2.5 min (+151.5s)` | `+4.6 min (+275s)` | 2 | `100.0%` |
| **Route 17** | `+2.0 min (+118.3s)` | `+2.8 min (+170s)` | 3 | `100.0%` |

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
| `2026-11-28 07:00:18` | `0.0%` | `75.0%` | 56 | 56 | `+126.9s` |
| `2026-11-28 06:30:17` | `0.0%` | `57.41%` | 108 | 108 | `+188.7s` |
| `2026-11-28 06:00:17` | `2.42%` | `59.01%` | 165 | 161 | `+92.5s` |
| `2026-11-28 05:30:18` | `4.98%` | `60.29%` | 221 | 209 | `+114.6s` |
| `2026-11-28 05:00:18` | `5.51%` | `64.45%` | 272 | 256 | `+98.8s` |
| `2026-11-28 04:30:17` | `6.1%` | `62.54%` | 328 | 307 | `+101.4s` |
| `2026-11-28 04:00:18` | `7.59%` | `65.59%` | 369 | 340 | `+90.3s` |
| `2026-11-28 03:30:18` | `9.2%` | `71.77%` | 424 | 379 | `+90.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:18.006000+00:00`.*
