# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-21T07:00:19.100000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`74.6%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `63` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `332` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+132.1s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 47 | 74.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 11.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 11.1% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 35** | 5 | 6 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+2.4 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+4.8 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-11.0s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.8 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.5 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-37.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 90** | `+48.5 min (+2908.0s)` | `+48.5 min (+2908s)` | 1 | `0.0%` |
| **Route 29** | `+10.4 min (+625.0s)` | `+21.1 min (+1265s)` | 3 | `50.0%` |
| **Route 72** | `+7.6 min (+458.0s)` | `+7.6 min (+458s)` | 1 | `0.0%` |
| **Route 77** | `+5.3 min (+316.0s)` | `+5.3 min (+316s)` | 1 | `0.0%` |
| **Route 3** | `+4.8 min (+289.0s)` | `+6.1 min (+364s)` | 3 | `33.33%` |
| **Route 17** | `+4.8 min (+287.0s)` | `+7.8 min (+471s)` | 2 | `50.0%` |
| **Route 44** | `+3.5 min (+211.5s)` | `+7.7 min (+464s)` | 2 | `50.0%` |
| **Route 45** | `+2.8 min (+165.0s)` | `+2.8 min (+165s)` | 1 | `100.0%` |
| **Route 27** | `+2.4 min (+143.8s)` | `+6.5 min (+389s)` | 4 | `50.0%` |
| **Route 51** | `+2.4 min (+143.0s)` | `+2.4 min (+143s)` | 2 | `100.0%` |

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
| `2026-11-21 07:00:19` | `0.0%` | `74.6%` | 63 | 332 | `+132.1s` |
| `2026-11-21 06:30:31` | `0.68%` | `65.99%` | 148 | 388 | `+299.3s` |
| `2026-11-21 06:00:20` | `4.65%` | `73.98%` | 258 | 423 | `+184.6s` |
| `2026-11-21 05:30:18` | `3.21%` | `73.84%` | 312 | 440 | `+219.0s` |
| `2026-11-21 05:00:20` | `2.74%` | `69.86%` | 365 | 470 | `+229.9s` |
| `2026-11-21 04:30:19` | `2.98%` | `70.08%` | 403 | 475 | `+255.9s` |
| `2026-11-21 04:00:18` | `3.1%` | `72.17%` | 419 | 524 | `+233.4s` |
| `2026-11-21 03:30:18` | `2.5%` | `71.5%` | 440 | 565 | `+231.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:19.100000+00:00`.*
