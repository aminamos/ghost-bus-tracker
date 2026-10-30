# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-30T07:00:25.399000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.37%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `54` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `342` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+195.9s` (`+3.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+92.0s` (`+1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 38 | 70.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 7.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 10 | 18.5% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+4.9 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+3.8 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.7 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+19.3 min` |
| **Route 41** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `-45.5s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 0** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+9.8 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-47.5s` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-33.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 3** | `+19.3 min (+1156.5s)` | `+33.8 min (+2028s)` | 2 | `50.0%` |
| **Route 72** | `+14.6 min (+878.0s)` | `+14.6 min (+878s)` | 1 | `0.0%` |
| **Route 0** | `+9.8 min (+587.5s)` | `+20.4 min (+1221s)` | 3 | `50.0%` |
| **Route 19** | `+4.9 min (+292.2s)` | `+11.3 min (+680s)` | 4 | `50.0%` |
| **Route 27** | `+4.7 min (+281.3s)` | `+10.1 min (+604s)` | 3 | `66.67%` |
| **Route 51** | `+4.6 min (+278.0s)` | `+4.6 min (+278s)` | 1 | `100.0%` |
| **Route B** | `+3.9 min (+231.4s)` | `+8.0 min (+480s)` | 7 | `57.14%` |
| **Route 7** | `+3.8 min (+227.5s)` | `+10.7 min (+643s)` | 4 | `75.0%` |
| **Route 35** | `+3.8 min (+225.0s)` | `+11.3 min (+678s)` | 3 | `33.33%` |
| **Route 44** | `+3.4 min (+202.0s)` | `+3.4 min (+202s)` | 1 | `100.0%` |

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
| `2026-10-30 07:00:25` | `0.0%` | `70.37%` | 54 | 342 | `+195.9s` |
| `2026-10-30 06:30:27` | `0.0%` | `68.92%` | 148 | 389 | `+211.4s` |
| `2026-10-30 06:00:26` | `3.41%` | `76.08%` | 264 | 416 | `+208.2s` |
| `2026-10-30 05:30:26` | `3.17%` | `73.36%` | 315 | 447 | `+233.6s` |
| `2026-10-30 05:00:20` | `4.11%` | `70.57%` | 365 | 492 | `+214.2s` |
| `2026-10-30 04:30:18` | `4.02%` | `76.64%` | 398 | 506 | `+208.1s` |
| `2026-10-30 04:00:21` | `2.14%` | `71.22%` | 420 | 565 | `+218.4s` |
| `2026-10-30 03:30:19` | `2.59%` | `72.4%` | 424 | 590 | `+220.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:25.399000+00:00`.*
