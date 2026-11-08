# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-08T07:00:17.758000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `55` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `55` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+56.2s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+78.0s` (`+1.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 60.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 17 | 30.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 9.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.7 min` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.9 min` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+2.8 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-344.0s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+4.2 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-50.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.7 min` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+13.4 min (+806.0s)` | `+13.4 min (+806s)` | 1 | `0.0%` |
| **Route 3** | `+4.2 min (+251.8s)` | `+5.3 min (+318s)` | 4 | `75.0%` |
| **Route 18** | `+2.9 min (+173.0s)` | `+4.3 min (+257s)` | 3 | `100.0%` |
| **Route 2** | `+2.8 min (+168.0s)` | `+6.7 min (+404s)` | 3 | `33.33%` |
| **Route 17** | `+2.7 min (+164.5s)` | `+5.6 min (+335s)` | 2 | `50.0%` |
| **Route 5** | `+2.7 min (+161.0s)` | `+4.0 min (+242s)` | 2 | `100.0%` |
| **Route 924** | `+2.6 min (+156.0s)` | `+5.4 min (+322s)` | 4 | `75.0%` |
| **Route 923** | `+2.5 min (+150.3s)` | `+3.0 min (+177s)` | 3 | `100.0%` |
| **Route 925** | `+1.7 min (+104.0s)` | `+2.0 min (+119s)` | 2 | `100.0%` |
| **Route 10** | `+1.7 min (+103.0s)` | `+2.4 min (+142s)` | 2 | `100.0%` |

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
| `2026-11-08 07:00:17` | `0.0%` | `60.0%` | 55 | 55 | `+56.2s` |
| `2026-11-08 06:30:18` | `0.0%` | `79.63%` | 108 | 108 | `+78.8s` |
| `2026-11-08 06:00:17` | `3.05%` | `75.47%` | 164 | 159 | `+84.8s` |
| `2026-11-08 05:30:18` | `4.07%` | `71.23%` | 221 | 212 | `+124.1s` |
| `2026-11-08 05:00:18` | `4.49%` | `69.8%` | 267 | 255 | `+119.3s` |
| `2026-11-08 04:30:20` | `5.06%` | `70.67%` | 316 | 300 | `+140.8s` |
| `2026-11-08 04:00:18` | `6.08%` | `70.29%` | 362 | 340 | `+159.5s` |
| `2026-11-08 03:30:18` | `7.44%` | `73.46%` | 403 | 372 | `+142.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.758000+00:00`.*
