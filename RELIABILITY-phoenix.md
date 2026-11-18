# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-18T06:30:19.616000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.03%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `145` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `397` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+148.6s` (`+2.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+71.0s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 103 | 71.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 20 | 13.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 19 | 13.1% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 2.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 6 | 6 | 0 | **`0.0%`** | `66.67%` | `+3.9 min` |
| **Route 35** | 7 | 7 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 16** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route EART** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-117.0s` |
| **Route 90** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.5 min` |
| **Route 27** | 5 | 6 | 0 | **`0.0%`** | `60.0%` | `+1.5 min` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.7 min` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+2.7 min` |
| **Route 43** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 51** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 15** | `+24.8 min (+1486.0s)` | `+50.1 min (+3006s)` | 2 | `50.0%` |
| **Route 17** | `+11.8 min (+708.0s)` | `+37.2 min (+2233s)` | 5 | `75.0%` |
| **Route 67** | `+11.3 min (+678.0s)` | `+11.3 min (+678s)` | 1 | `0.0%` |
| **Route 77** | `+10.1 min (+605.8s)` | `+30.0 min (+1802s)` | 3 | `75.0%` |
| **Route 51** | `+6.0 min (+362.5s)` | `+10.6 min (+636s)` | 4 | `50.0%` |
| **Route 29** | `+5.1 min (+304.8s)` | `+8.8 min (+526s)` | 4 | `50.0%` |
| **Route FBUZ** | `+3.9 min (+236.0s)` | `+3.9 min (+236s)` | 1 | `100.0%` |
| **Route 19** | `+3.9 min (+233.3s)` | `+9.6 min (+574s)` | 6 | `66.67%` |
| **Route 0** | `+3.8 min (+228.2s)` | `+5.7 min (+344s)` | 4 | `75.0%` |
| **Route 7** | `+3.8 min (+226.8s)` | `+11.4 min (+682s)` | 5 | `80.0%` |

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
| `2026-11-18 06:30:19` | `0.0%` | `71.03%` | 145 | 397 | `+148.6s` |
| `2026-11-18 06:00:25` | `3.31%` | `78.33%` | 272 | 425 | `+156.7s` |
| `2026-11-18 05:30:29` | `4.67%` | `79.72%` | 300 | 436 | `+173.7s` |
| `2026-11-18 05:00:20` | `4.09%` | `77.78%` | 367 | 495 | `+178.9s` |
| `2026-11-18 04:30:19` | `3.04%` | `76.96%` | 395 | 505 | `+194.6s` |
| `2026-11-18 04:00:18` | `2.83%` | `77.91%` | 424 | 546 | `+203.5s` |
| `2026-11-18 03:30:19` | `3.15%` | `77.16%` | 445 | 601 | `+195.9s` |
| `2026-11-18 03:00:19` | `4.11%` | `76.14%` | 462 | 644 | `+185.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:19.616000+00:00`.*
