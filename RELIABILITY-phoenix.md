# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-08T07:00:18.782000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `276` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+360.5s` (`+6.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+171.0s` (`+2.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 50.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 13.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 12 | 27.3% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 9.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-80.7s` |
| **Route 41** | 3 | 4 | 0 | **`0.0%`** | `0.0%` | `+11.4 min` |
| **Route 50** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-100.7s` |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+5.0 min` |
| **Route 170** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 19** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `+3.5 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 90** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+49.3 min` |
| **Route 27** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+2.3 min` |
| **Route 72** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+11.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 90** | `+49.3 min (+2955.5s)` | `+92.6 min (+5555s)` | 2 | `0.0%` |
| **Route 80** | `+43.3 min (+2596.0s)` | `+43.3 min (+2596s)` | 1 | `0.0%` |
| **Route 41** | `+11.4 min (+683.3s)` | `+15.0 min (+902s)` | 4 | `0.0%` |
| **Route 72** | `+11.3 min (+681.0s)` | `+17.8 min (+1068s)` | 2 | `50.0%` |
| **Route 16** | `+8.9 min (+536.0s)` | `+11.5 min (+690s)` | 2 | `0.0%` |
| **Route 51** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 7** | `+5.0 min (+298.0s)` | `+7.5 min (+451s)` | 3 | `33.33%` |
| **Route 44** | `+4.1 min (+248.0s)` | `+4.1 min (+248s)` | 2 | `100.0%` |
| **Route 17** | `+3.9 min (+235.5s)` | `+5.8 min (+346s)` | 3 | `50.0%` |
| **Route 45** | `+3.7 min (+224.0s)` | `+3.7 min (+224s)` | 1 | `100.0%` |

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
| `2026-11-08 07:00:18` | `0.0%` | `50.0%` | 44 | 276 | `+360.5s` |
| `2026-11-08 06:30:20` | `1.29%` | `62.75%` | 155 | 321 | `+261.9s` |
| `2026-11-08 06:00:19` | `2.81%` | `66.67%` | 249 | 333 | `+287.5s` |
| `2026-11-08 05:30:20` | `3.64%` | `63.19%` | 302 | 341 | `+377.7s` |
| `2026-11-08 05:00:22` | `3.45%` | `57.14%` | 348 | 373 | `+544.7s` |
| `2026-11-08 04:30:26` | `3.14%` | `58.93%` | 350 | 371 | `+466.1s` |
| `2026-11-08 04:00:19` | `3.11%` | `60.22%` | 386 | 394 | `+401.4s` |
| `2026-11-08 03:30:18` | `2.59%` | `63.41%` | 425 | 421 | `+325.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.782000+00:00`.*
