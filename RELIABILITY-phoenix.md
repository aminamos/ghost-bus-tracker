# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-23T07:01:26.862000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`69.39%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `50` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `338` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+75.8s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+14.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 68.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 20.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 8.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `20.0%` | `+0.1 min` |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-63.2s` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+3.7 min` |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+1.4 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-12.5s` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.2 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.3 min` |
| **Route 29** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+11.1 min` |
| **Route B** | 6 | 6 | 0 | **`0.0%`** | `83.33%` | `+1.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 29** | `+11.1 min (+665.0s)` | `+20.2 min (+1212s)` | 2 | `50.0%` |
| **Route 3** | `+6.2 min (+373.0s)` | `+12.7 min (+760s)` | 2 | `50.0%` |
| **Route 41** | `+5.3 min (+321.0s)` | `+10.1 min (+604s)` | 2 | `50.0%` |
| **Route 16** | `+3.7 min (+222.0s)` | `+9.4 min (+562s)` | 2 | `0.0%` |
| **Route 51** | `+3.0 min (+179.0s)` | `+3.0 min (+179s)` | 1 | `100.0%` |
| **Route 61** | `+2.3 min (+138.0s)` | `+2.3 min (+138s)` | 1 | `100.0%` |
| **Route 44** | `+1.5 min (+88.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |
| **Route 27** | `+1.4 min (+84.0s)` | `+3.9 min (+234s)` | 3 | `66.67%` |
| **Route 7** | `+1.3 min (+80.0s)` | `+1.8 min (+108s)` | 3 | `100.0%` |
| **Route B** | `+1.3 min (+80.0s)` | `+4.0 min (+240s)` | 6 | `83.33%` |

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
| `24271113` | Route 39 | `N/A` | `SCHEDULED` | Assigned vehicle 5284 is broadcasting off-schedule with no vehicle covering 24271113 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:26` | `2.0%` | `69.39%` | 50 | 338 | `+75.8s` |
| `2026-10-23 06:30:26` | `0.0%` | `69.44%` | 144 | 392 | `+184.2s` |
| `2026-10-23 06:00:22` | `3.97%` | `77.69%` | 252 | 419 | `+173.3s` |
| `2026-10-23 05:30:23` | `3.25%` | `79.53%` | 308 | 449 | `+195.6s` |
| `2026-10-23 05:15:29` | `3.5%` | `76.13%` | 343 | 484 | `+190.3s` |
| `2026-10-23 05:00:40` | `2.83%` | `74.93%` | 353 | 505 | `+202.9s` |
| `2026-10-23 04:30:38` | `2.78%` | `72.92%` | 395 | 516 | `+210.3s` |
| `2026-10-23 04:00:42` | `3.58%` | `72.52%` | 419 | 543 | `+190.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:26.862000+00:00`.*
