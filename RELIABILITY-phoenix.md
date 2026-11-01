# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-01T07:00:19.409000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.82%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `63` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `275` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+410.3s` (`+6.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+180.0s` (`+3.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 54.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 7.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 12 | 19.0% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 6.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 12.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+6.9 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.8 min` |
| **Route 170** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.4 min` |
| **Route 44** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+6.5 min` |
| **Route 29** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 50** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+11.7 min` |
| **Route 35** | 5 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.9 min` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.5 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+26.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | `+26.1 min (+1566.0s)` | `+48.5 min (+2909s)` | 2 | `50.0%` |
| **Route S** | `+22.5 min (+1350.0s)` | `+49.0 min (+2940s)` | 2 | `0.0%` |
| **Route 27** | `+21.6 min (+1294.6s)` | `+89.3 min (+5356s)` | 5 | `60.0%` |
| **Route 50** | `+11.7 min (+699.7s)` | `+40.1 min (+2406s)` | 3 | `0.0%` |
| **Route 16** | `+8.2 min (+491.0s)` | `+8.2 min (+491s)` | 3 | `0.0%` |
| **Route 7** | `+6.9 min (+416.3s)` | `+10.6 min (+636s)` | 3 | `33.33%` |
| **Route 17** | `+6.5 min (+392.7s)` | `+12.5 min (+748s)` | 3 | `66.67%` |
| **Route 35** | `+5.9 min (+353.3s)` | `+12.9 min (+776s)` | 3 | `66.67%` |
| **Route 138** | `+5.8 min (+351.0s)` | `+5.8 min (+351s)` | 1 | `0.0%` |
| **Route 3** | `+5.5 min (+327.0s)` | `+5.5 min (+327s)` | 2 | `0.0%` |

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
| `2026-11-01 07:00:19` | `0.0%` | `61.82%` | 63 | 275 | `+410.3s` |
| `2026-11-01 06:30:19` | `0.66%` | `62.04%` | 151 | 310 | `+298.4s` |
| `2026-11-01 06:00:21` | `4.0%` | `66.36%` | 250 | 339 | `+288.4s` |
| `2026-11-01 05:30:20` | `2.97%` | `68.15%` | 303 | 336 | `+288.3s` |
| `2026-11-01 05:00:20` | `2.32%` | `69.71%` | 345 | 358 | `+261.5s` |
| `2026-11-01 04:30:20` | `4.28%` | `68.83%` | 374 | 362 | `+291.4s` |
| `2026-11-01 04:00:20` | `2.16%` | `68.75%` | 416 | 394 | `+267.3s` |
| `2026-11-01 03:30:19` | `2.25%` | `69.97%` | 445 | 419 | `+290.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:19.409000+00:00`.*
