# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Central Florida Regional Transportation Authority** in **Orlando, FL** (Orlando Metropolitan Area, Florida).
> **Transit System:** LYNX | **Location:** Orlando, FL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-19T05:00:18.355000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.15%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `54` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `38` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+380.7s` (`+6.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+214.0s` (`+3.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 63.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 12 | 22.2% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 13.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17567** | 8 | 4 | 0 | **`0.0%`** | `37.5%` | `+13.2 min` |
| **Route 17585** | 5 | 4 | 0 | **`0.0%`** | `40.0%` | `+13.3 min` |
| **Route 17579** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `+3.6 min` |
| **Route 17608** | 4 | 3 | 0 | **`0.0%`** | `50.0%` | `+6.9 min` |
| **Route 17604** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.8 min` |
| **Route 17592** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `+3.3 min` |
| **Route 17614** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.9 min` |
| **Route 17591** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 17602** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+4.2 min` |
| **Route 17600** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17585** | `+13.3 min (+797.4s)` | `+32.2 min (+1931s)` | 4 | `40.0%` |
| **Route 17567** | `+13.2 min (+794.9s)` | `+38.4 min (+2304s)` | 4 | `37.5%` |
| **Route 17618** | `+11.5 min (+687.5s)` | `+13.4 min (+807s)` | 2 | `0.0%` |
| **Route 17583** | `+9.7 min (+584.0s)` | `+15.4 min (+924s)` | 2 | `50.0%` |
| **Route 17608** | `+6.9 min (+414.8s)` | `+16.2 min (+972s)` | 3 | `50.0%` |
| **Route 17575** | `+6.9 min (+414.0s)` | `+9.4 min (+566s)` | 1 | `50.0%` |
| **Route 17576** | `+6.1 min (+365.0s)` | `+6.1 min (+365s)` | 1 | `0.0%` |
| **Route 17614** | `+5.9 min (+355.0s)` | `+11.8 min (+705s)` | 2 | `50.0%` |
| **Route 17604** | `+4.8 min (+288.3s)` | `+11.0 min (+660s)` | 3 | `66.67%` |
| **Route 17602** | `+4.2 min (+251.0s)` | `+4.6 min (+277s)` | 3 | `100.0%` |

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
| `2026-11-19 05:00:18` | `0.0%` | `64.15%` | 54 | 38 | `+380.7s` |
| `2026-11-19 04:30:17` | `0.0%` | `63.1%` | 85 | 52 | `+323.9s` |
| `2026-11-19 03:30:18` | `1.19%` | `79.88%` | 168 | 83 | `+199.8s` |
| `2026-11-19 03:00:18` | `0.93%` | `84.83%` | 215 | 98 | `+154.8s` |
| `2026-11-19 02:30:17` | `0.0%` | `87.31%` | 262 | 104 | `+92.3s` |
| `2026-11-19 02:00:18` | `0.0%` | `87.5%` | 330 | 123 | `+103.5s` |
| `2026-11-19 01:00:18` | `0.44%` | `84.53%` | 452 | 153 | `+162.1s` |
| `2026-11-19 00:30:18` | `0.56%` | `79.35%` | 531 | 172 | `+189.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T05:00:18.355000+00:00`.*
