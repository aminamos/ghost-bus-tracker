# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-07T07:00:24.602000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `59` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `335` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+232.1s` (`+3.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+115.5s` (`+1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 57.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 13.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 11 | 18.6% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 8.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+8.5 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+4.3 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-26.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+12.3 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+6.8 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-177.5s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+7.0 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.1 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 43** | `+15.6 min (+936.0s)` | `+15.9 min (+956s)` | 3 | `0.0%` |
| **Route 3** | `+12.3 min (+736.3s)` | `+33.8 min (+2025s)` | 3 | `66.67%` |
| **Route 72** | `+9.4 min (+563.0s)` | `+9.4 min (+563s)` | 1 | `0.0%` |
| **Route 77** | `+9.4 min (+562.0s)` | `+9.4 min (+562s)` | 1 | `0.0%` |
| **Route 19** | `+8.5 min (+510.8s)` | `+34.2 min (+2051s)` | 5 | `60.0%` |
| **Route 0** | `+7.1 min (+428.0s)` | `+7.9 min (+474s)` | 2 | `0.0%` |
| **Route 17** | `+7.0 min (+419.5s)` | `+11.2 min (+674s)` | 2 | `50.0%` |
| **Route 51** | `+6.8 min (+406.5s)` | `+7.0 min (+420s)` | 2 | `0.0%` |
| **Route 45** | `+5.7 min (+342.0s)` | `+5.7 min (+342s)` | 1 | `0.0%` |
| **Route 35** | `+4.3 min (+260.2s)` | `+19.4 min (+1163s)` | 5 | `60.0%` |

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
| `2026-11-07 07:00:24` | `0.0%` | `58.62%` | 59 | 335 | `+232.1s` |
| `2026-11-07 06:30:19` | `0.0%` | `64.15%` | 159 | 371 | `+327.3s` |
| `2026-11-07 06:00:20` | `2.86%` | `69.49%` | 280 | 401 | `+281.4s` |
| `2026-11-07 05:30:19` | `3.87%` | `70.51%` | 310 | 416 | `+259.4s` |
| `2026-11-07 05:00:21` | `3.29%` | `69.23%` | 365 | 444 | `+254.7s` |
| `2026-11-07 04:30:20` | `2.76%` | `68.31%` | 398 | 464 | `+255.9s` |
| `2026-11-07 04:00:24` | `2.64%` | `72.28%` | 417 | 509 | `+226.7s` |
| `2026-11-07 03:30:20` | `3.2%` | `73.87%` | 437 | 554 | `+225.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:24.602000+00:00`.*
