# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-19T07:00:19.912000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `361` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+194.8s` (`+3.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+25.0s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 41 | 68.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 16.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 8.3% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 6.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `20.0%` | `+6.2 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-16.0s` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.5 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-84.5s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 75** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+22.6 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+10.8 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route S** | `+65.0 min (+3900.0s)` | `+65.0 min (+3900s)` | 1 | `0.0%` |
| **Route 75** | `+22.6 min (+1354.0s)` | `+31.6 min (+1896s)` | 2 | `0.0%` |
| **Route 70** | `+10.8 min (+649.0s)` | `+23.4 min (+1402s)` | 2 | `0.0%` |
| **Route 35** | `+6.2 min (+373.2s)` | `+19.1 min (+1145s)` | 5 | `20.0%` |
| **Route 3** | `+4.5 min (+267.5s)` | `+8.2 min (+494s)` | 2 | `50.0%` |
| **Route 7** | `+2.6 min (+157.5s)` | `+4.5 min (+272s)` | 4 | `100.0%` |
| **Route 50** | `+2.1 min (+127.0s)` | `+4.0 min (+238s)` | 2 | `100.0%` |
| **Route 29** | `+2.0 min (+121.0s)` | `+3.5 min (+211s)` | 2 | `100.0%` |
| **Route 45** | `+1.9 min (+114.0s)` | `+1.9 min (+114s)` | 1 | `100.0%` |
| **Route 51** | `+1.8 min (+110.0s)` | `+1.8 min (+110s)` | 1 | `100.0%` |

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
| `2026-11-19 07:00:19` | `0.0%` | `68.33%` | 60 | 361 | `+194.8s` |
| `2026-11-19 06:30:19` | `0.74%` | `75.37%` | 135 | 385 | `+152.6s` |
| `2026-11-19 06:00:23` | `2.99%` | `80.77%` | 268 | 414 | `+127.7s` |
| `2026-11-19 05:30:25` | `2.56%` | `77.63%` | 312 | 432 | `+151.3s` |
| `2026-11-19 05:00:19` | `4.21%` | `75.07%` | 356 | 496 | `+156.3s` |
| `2026-11-19 04:30:19` | `4.52%` | `72.89%` | 398 | 510 | `+180.7s` |
| `2026-11-19 04:00:20` | `4.81%` | `76.01%` | 416 | 556 | `+176.6s` |
| `2026-11-19 03:30:19` | `3.39%` | `76.87%` | 443 | 578 | `+202.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:19.912000+00:00`.*
