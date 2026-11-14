# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-14T07:00:19.243000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.02%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `59` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `344` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+143.8s` (`+2.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+84.0s` (`+1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 61.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 16.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 11 | 18.6% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.1 min` |
| **Route 16** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+4.0 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+5.6 min` |
| **Route 3** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 17** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+3.5 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-39.5s` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 7** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+6.7 min` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 72** | `+8.0 min (+482.0s)` | `+8.0 min (+482s)` | 1 | `0.0%` |
| **Route 61** | `+7.5 min (+452.0s)` | `+15.5 min (+929s)` | 2 | `50.0%` |
| **Route 7** | `+6.7 min (+399.0s)` | `+19.0 min (+1142s)` | 5 | `40.0%` |
| **Route 77** | `+6.5 min (+393.0s)` | `+6.5 min (+393s)` | 1 | `0.0%` |
| **Route 27** | `+5.6 min (+336.0s)` | `+10.3 min (+618s)` | 3 | `33.33%` |
| **Route 51** | `+5.3 min (+319.0s)` | `+5.3 min (+319s)` | 1 | `0.0%` |
| **Route B** | `+5.2 min (+310.0s)` | `+10.0 min (+600s)` | 6 | `50.0%` |
| **Route 16** | `+4.0 min (+242.7s)` | `+10.4 min (+626s)` | 3 | `33.33%` |
| **Route 45** | `+3.6 min (+217.0s)` | `+3.6 min (+217s)` | 1 | `100.0%` |
| **Route 17** | `+3.5 min (+207.5s)` | `+5.7 min (+340s)` | 3 | `50.0%` |

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
| `2026-11-14 07:00:19` | `0.0%` | `61.02%` | 59 | 344 | `+143.8s` |
| `2026-11-14 06:30:21` | `0.0%` | `69.44%` | 144 | 377 | `+171.8s` |
| `2026-11-14 06:00:21` | `3.75%` | `70.43%` | 267 | 398 | `+164.6s` |
| `2026-11-14 05:30:19` | `4.85%` | `74.15%` | 309 | 422 | `+209.2s` |
| `2026-11-14 05:00:27` | `3.32%` | `75.36%` | 361 | 456 | `+185.4s` |
| `2026-11-14 04:30:19` | `4.86%` | `75.27%` | 391 | 479 | `+204.8s` |
| `2026-11-14 04:00:24` | `3.82%` | `77.92%` | 419 | 540 | `+167.2s` |
| `2026-11-14 03:30:19` | `3.46%` | `78.04%` | 434 | 565 | `+185.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.243000+00:00`.*
