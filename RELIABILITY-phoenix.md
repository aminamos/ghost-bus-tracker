# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-06T07:00:18.636000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.52%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `62` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `355` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+355.6s` (`+5.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 64.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 16.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 11.3% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 8.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+3.7 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+0.8 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-38.5s` |
| **Route 27** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+21.3 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.5 min` |
| **Route 70** | 3 | 4 | 0 | **`0.0%`** | `0.0%` | `+19.2 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-38.0s` |
| **Route 0** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+8.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 51** | `+64.7 min (+3879.0s)` | `+64.7 min (+3879s)` | 1 | `0.0%` |
| **Route 28** | `+54.1 min (+3249.0s)` | `+54.1 min (+3249s)` | 1 | `0.0%` |
| **Route 27** | `+21.3 min (+1276.4s)` | `+92.1 min (+5526s)` | 5 | `40.0%` |
| **Route 70** | `+19.2 min (+1152.0s)` | `+62.4 min (+3746s)` | 4 | `0.0%` |
| **Route 0** | `+8.0 min (+481.5s)` | `+14.8 min (+886s)` | 3 | `50.0%` |
| **Route 77** | `+6.4 min (+382.0s)` | `+6.4 min (+382s)` | 1 | `0.0%` |
| **Route 17** | `+4.5 min (+271.0s)` | `+4.7 min (+280s)` | 2 | `100.0%` |
| **Route 7** | `+3.8 min (+225.5s)` | `+7.6 min (+458s)` | 4 | `75.0%` |
| **Route 19** | `+3.7 min (+224.6s)` | `+15.4 min (+923s)` | 5 | `80.0%` |
| **Route 8** | `+3.6 min (+214.0s)` | `+3.6 min (+214s)` | 1 | `100.0%` |

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
| `2026-11-06 07:00:18` | `0.0%` | `64.52%` | 62 | 355 | `+355.6s` |
| `2026-11-06 06:30:19` | `0.0%` | `71.14%` | 149 | 393 | `+194.2s` |
| `2026-11-06 06:00:18` | `4.78%` | `75.29%` | 272 | 432 | `+244.3s` |
| `2026-11-06 05:30:20` | `3.12%` | `73.55%` | 320 | 451 | `+255.5s` |
| `2026-11-06 05:00:21` | `4.61%` | `70.45%` | 369 | 507 | `+216.8s` |
| `2026-11-06 04:30:20` | `2.9%` | `72.64%` | 414 | 526 | `+238.7s` |
| `2026-11-06 04:00:25` | `2.8%` | `71.33%` | 428 | 570 | `+229.1s` |
| `2026-11-06 03:30:21` | `3.39%` | `70.73%` | 443 | 611 | `+224.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.636000+00:00`.*
