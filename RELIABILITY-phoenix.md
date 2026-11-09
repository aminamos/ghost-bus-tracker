# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-09T07:00:19.400000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `297` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+157.0s` (`+2.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+67.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 30 | 50.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 17 | 28.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 11 | 18.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+0.3 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.4 min` |
| **Route 16** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.0 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.3 min` |
| **Route 29** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-29.3s` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-201.5s` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+1.4 min` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+5.3 min` |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.8 min` |
| **Route 35** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+1.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | `+46.0 min (+2762.0s)` | `+46.0 min (+2762s)` | 1 | `0.0%` |
| **Route 13** | `+10.4 min (+626.0s)` | `+10.4 min (+626s)` | 1 | `0.0%` |
| **Route 27** | `+5.3 min (+315.5s)` | `+11.5 min (+688s)` | 4 | `25.0%` |
| **Route 16** | `+5.0 min (+299.7s)` | `+9.2 min (+550s)` | 3 | `66.67%` |
| **Route 17** | `+4.3 min (+255.5s)` | `+6.1 min (+367s)` | 2 | `50.0%` |
| **Route 50** | `+3.8 min (+225.3s)` | `+15.2 min (+911s)` | 3 | `33.33%` |
| **Route 3** | `+3.0 min (+180.5s)` | `+5.1 min (+306s)` | 2 | `50.0%` |
| **Route 41** | `+2.9 min (+174.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 7** | `+2.8 min (+168.3s)` | `+7.0 min (+422s)` | 3 | `66.67%` |
| **Route A** | `+2.0 min (+120.0s)` | `+9.0 min (+540s)` | 7 | `57.14%` |

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
| `2026-11-09 07:00:19` | `0.0%` | `50.0%` | 60 | 297 | `+157.0s` |
| `2026-11-09 06:30:21` | `0.78%` | `67.97%` | 129 | 307 | `+238.6s` |
| `2026-11-09 06:00:19` | `3.74%` | `73.3%` | 214 | 330 | `+195.9s` |
| `2026-11-09 05:30:19` | `5.12%` | `73.86%` | 254 | 329 | `+223.0s` |
| `2026-11-09 05:00:19` | `2.48%` | `76.0%` | 282 | 338 | `+199.9s` |
| `2026-11-09 04:30:19` | `3.55%` | `71.24%` | 310 | 334 | `+216.9s` |
| `2026-11-09 04:00:20` | `1.56%` | `75.0%` | 321 | 356 | `+221.2s` |
| `2026-11-09 03:30:18` | `3.83%` | `72.09%` | 339 | 383 | `+262.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.400000+00:00`.*
