# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-24T06:30:22.920000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `150` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `378` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+248.7s` (`+4.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+126.5s` (`+2.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 93 | 62.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 18 | 12.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 30 | 20.0% |
| 🔴 **Severe Delay** | Over 15m late | 9 | 6.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route EART** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.6 min` |
| **Route 77** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+0.7 min` |
| **Route 72** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.9 min` |
| **Route 70** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+4.4 min` |
| **Route 106** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+30.2 min` |
| **Route 80** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 81** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 35** | 7 | 8 | 0 | **`0.0%`** | `42.86%` | `+4.2 min` |
| **Route 186** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `-9.0s` |
| **Route 13** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 106** | `+30.2 min (+1813.0s)` | `+61.7 min (+3702s)` | 2 | `0.0%` |
| **Route 75** | `+17.6 min (+1054.3s)` | `+45.2 min (+2713s)` | 3 | `33.33%` |
| **Route 29** | `+10.7 min (+639.8s)` | `+27.0 min (+1618s)` | 5 | `20.0%` |
| **Route 1** | `+10.6 min (+636.0s)` | `+10.6 min (+636s)` | 2 | `0.0%` |
| **Route 17** | `+9.6 min (+576.4s)` | `+25.9 min (+1554s)` | 6 | `40.0%` |
| **Route 96** | `+9.4 min (+564.0s)` | `+9.4 min (+564s)` | 1 | `0.0%` |
| **Route A** | `+7.9 min (+471.4s)` | `+14.0 min (+840s)` | 7 | `28.57%` |
| **Route 7** | `+7.5 min (+451.7s)` | `+22.5 min (+1350s)` | 6 | `66.67%` |
| **Route 51** | `+6.9 min (+415.2s)` | `+16.2 min (+975s)` | 4 | `75.0%` |
| **Route 67** | `+6.7 min (+404.0s)` | `+6.7 min (+404s)` | 1 | `0.0%` |

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
| `2026-10-24 06:30:22` | `0.0%` | `62.0%` | 150 | 378 | `+248.7s` |
| `2026-10-24 05:30:21` | `4.15%` | `70.03%` | 313 | 417 | `+225.6s` |
| `2026-10-24 05:00:24` | `2.82%` | `68.71%` | 355 | 462 | `+237.4s` |
| `2026-10-24 04:30:22` | `2.78%` | `66.67%` | 395 | 475 | `+259.5s` |
| `2026-10-24 04:00:23` | `3.15%` | `71.25%` | 413 | 527 | `+198.8s` |
| `2026-10-24 03:00:21` | `4.62%` | `69.21%` | 455 | 596 | `+244.3s` |
| `2026-10-24 02:00:23` | `2.9%` | `64.67%` | 552 | 655 | `+269.7s` |
| `2026-10-24 01:30:22` | `2.61%` | `67.06%` | 612 | 686 | `+248.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.920000+00:00`.*
