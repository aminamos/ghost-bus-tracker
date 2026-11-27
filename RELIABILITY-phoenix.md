# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-27T07:00:20.398000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `53` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `264` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+85.5s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+39.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 31 | 58.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 12 | 22.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 9 | 17.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+0.8 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+5.7 min` |
| **Route 29** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+4.8 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 90** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.0 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.6 min` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `66.67%` | `+0.6 min` |
| **Route 7** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.5 min` |
| **Route 35** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 138** | `+5.9 min (+354.0s)` | `+5.9 min (+354s)` | 1 | `0.0%` |
| **Route 41** | `+5.7 min (+341.7s)` | `+11.3 min (+681s)` | 3 | `66.67%` |
| **Route 17** | `+5.7 min (+339.7s)` | `+7.4 min (+445s)` | 3 | `33.33%` |
| **Route 29** | `+4.8 min (+289.5s)` | `+11.7 min (+699s)` | 2 | `0.0%` |
| **Route 8** | `+3.6 min (+216.0s)` | `+3.6 min (+216s)` | 1 | `100.0%` |
| **Route 70** | `+2.8 min (+170.5s)` | `+4.8 min (+287s)` | 2 | `100.0%` |
| **Route 44** | `+2.6 min (+157.0s)` | `+5.5 min (+332s)` | 2 | `50.0%` |
| **Route 7** | `+2.5 min (+148.7s)` | `+6.5 min (+392s)` | 3 | `66.67%` |
| **Route 16** | `+1.9 min (+115.0s)` | `+2.0 min (+119s)` | 2 | `100.0%` |
| **Route 43** | `+1.1 min (+68.0s)` | `+1.1 min (+68s)` | 1 | `100.0%` |

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
| `2026-11-27 07:00:20` | `0.0%` | `59.62%` | 53 | 264 | `+85.5s` |
| `2026-11-27 06:30:20` | `0.0%` | `71.54%` | 130 | 282 | `+131.0s` |
| `2026-11-27 06:00:18` | `3.14%` | `76.74%` | 223 | 297 | `+141.6s` |
| `2026-11-27 05:30:20` | `4.37%` | `76.25%` | 252 | 304 | `+169.7s` |
| `2026-11-27 05:00:18` | `2.5%` | `72.16%` | 280 | 311 | `+205.9s` |
| `2026-11-27 04:30:20` | `5.69%` | `74.02%` | 299 | 316 | `+213.9s` |
| `2026-11-27 04:00:18` | `4.4%` | `71.38%` | 318 | 345 | `+267.6s` |
| `2026-11-27 03:30:20` | `3.88%` | `74.22%` | 335 | 366 | `+218.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:20.398000+00:00`.*
