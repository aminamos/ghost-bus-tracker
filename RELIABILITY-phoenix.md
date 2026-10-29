# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-29T07:00:19.848000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.07%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `43` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `360` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+101.1s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+63.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 79.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 9.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 11.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 35** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+3.4 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.8 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-1.0s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.3 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-60.5s` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-15.0s` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 72** | `+10.5 min (+632.0s)` | `+10.5 min (+632s)` | 1 | `0.0%` |
| **Route 45** | `+5.8 min (+347.0s)` | `+5.8 min (+347s)` | 1 | `0.0%` |
| **Route 27** | `+3.8 min (+226.3s)` | `+9.7 min (+583s)` | 3 | `66.67%` |
| **Route 0** | `+3.5 min (+212.5s)` | `+7.7 min (+460s)` | 2 | `50.0%` |
| **Route 35** | `+3.4 min (+202.5s)` | `+14.3 min (+860s)` | 4 | `75.0%` |
| **Route 17** | `+3.3 min (+200.5s)` | `+4.5 min (+273s)` | 2 | `100.0%` |
| **Route 29** | `+3.2 min (+192.0s)` | `+3.3 min (+197s)` | 2 | `100.0%` |
| **Route 7** | `+2.6 min (+156.0s)` | `+3.3 min (+199s)` | 2 | `100.0%` |
| **Route 43** | `+2.2 min (+132.0s)` | `+2.2 min (+132s)` | 2 | `100.0%` |
| **Route 51** | `+2.2 min (+132.0s)` | `+2.2 min (+132s)` | 1 | `100.0%` |

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
| `2026-10-29 07:00:19` | `0.0%` | `79.07%` | 43 | 360 | `+101.1s` |
| `2026-10-29 06:30:25` | `0.66%` | `70.0%` | 151 | 422 | `+111.8s` |
| `2026-10-29 06:00:24` | `4.56%` | `78.09%` | 263 | 437 | `+129.0s` |
| `2026-10-29 05:30:19` | `1.95%` | `75.75%` | 307 | 463 | `+207.7s` |
| `2026-10-29 05:00:20` | `4.97%` | `75.08%` | 342 | 504 | `+194.1s` |
| `2026-10-29 04:30:20` | `3.53%` | `69.19%` | 397 | 524 | `+225.6s` |
| `2026-10-29 04:00:20` | `3.29%` | `71.84%` | 426 | 564 | `+207.3s` |
| `2026-10-29 03:30:20` | `2.93%` | `71.93%` | 444 | 604 | `+228.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:19.848000+00:00`.*
