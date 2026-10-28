# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-28T07:00:19.077000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`52.08%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `48` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `341` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+186.1s` (`+3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+23.5s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 25 | 52.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 12 | 25.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 16.7% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 6.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `20.0%` | `+0.8 min` |
| **Route 16** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `-4.0s` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+6.0 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.3 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.1 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-112.5s` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+9.5 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 8** | `+30.4 min (+1821.0s)` | `+58.2 min (+3492s)` | 2 | `50.0%` |
| **Route 12** | `+13.1 min (+787.0s)` | `+13.1 min (+787s)` | 1 | `0.0%` |
| **Route 32** | `+9.6 min (+576.0s)` | `+9.6 min (+576s)` | 1 | `0.0%` |
| **Route FBUZ** | `+9.5 min (+572.0s)` | `+9.5 min (+572s)` | 1 | `0.0%` |
| **Route 44** | `+9.5 min (+570.5s)` | `+16.9 min (+1015s)` | 2 | `50.0%` |
| **Route 51** | `+9.3 min (+559.0s)` | `+9.3 min (+559s)` | 1 | `0.0%` |
| **Route 27** | `+6.0 min (+358.3s)` | `+16.4 min (+983s)` | 3 | `66.67%` |
| **Route 17** | `+5.1 min (+306.0s)` | `+7.8 min (+469s)` | 2 | `50.0%` |
| **Route 0** | `+3.1 min (+186.5s)` | `+6.0 min (+361s)` | 2 | `50.0%` |
| **Route 3** | `+2.3 min (+140.3s)` | `+6.0 min (+361s)` | 3 | `66.67%` |

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
| `2026-10-28 07:00:19` | `0.0%` | `52.08%` | 48 | 341 | `+186.1s` |
| `2026-10-28 06:30:21` | `0.67%` | `77.03%` | 149 | 414 | `+114.6s` |
| `2026-10-28 06:00:21` | `3.8%` | `78.66%` | 263 | 431 | `+158.6s` |
| `2026-10-28 05:30:27` | `4.22%` | `77.29%` | 308 | 457 | `+220.1s` |
| `2026-10-28 05:00:27` | `4.49%` | `75.29%` | 356 | 501 | `+214.8s` |
| `2026-10-28 04:30:32` | `3.32%` | `73.88%` | 392 | 510 | `+203.0s` |
| `2026-10-28 04:00:32` | `2.9%` | `76.87%` | 414 | 566 | `+185.8s` |
| `2026-10-28 03:30:19` | `3.21%` | `75.36%` | 436 | 608 | `+195.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:19.077000+00:00`.*
