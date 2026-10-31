# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-31T07:00:21.710000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `148` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+210.7s` (`+3.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+72.0s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 17.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 4.3% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 48** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+16.8 min` |
| **Route 66** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+8.5 min` |
| **Route 1** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 6** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `-9.0s` |
| **Route 25** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 51** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 26** | `+16.8 min (+1008.0s)` | `+16.8 min (+1008s)` | 2 | `0.0%` |
| **Route 10** | `+8.5 min (+508.0s)` | `+8.5 min (+508s)` | 3 | `0.0%` |
| **Route 41** | `+4.0 min (+241.5s)` | `+6.8 min (+411s)` | 2 | `50.0%` |
| **Route 28** | `+2.2 min (+131.0s)` | `+2.2 min (+131s)` | 1 | `100.0%` |
| **Route 1** | `+1.9 min (+115.0s)` | `+1.9 min (+115s)` | 2 | `100.0%` |
| **Route 51** | `+1.1 min (+64.0s)` | `+1.1 min (+64s)` | 2 | `100.0%` |
| **Route 22** | `+0.3 min (+18.0s)` | `+0.3 min (+18s)` | 1 | `100.0%` |
| **Route 48** | `+0.1 min (+9.0s)` | `+0.1 min (+9s)` | 4 | `100.0%` |

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
| `2026-10-31 07:00:21` | `0.0%` | `72.73%` | 46 | 148 | `+210.7s` |
| `2026-10-31 06:30:18` | `0.0%` | `76.0%` | 31 | 145 | `+2869.6s` |
| `2026-10-31 06:00:19` | `0.0%` | `88.24%` | 36 | 160 | `+155.5s` |
| `2026-10-31 05:30:19` | `0.0%` | `75.0%` | 49 | 170 | `+163.4s` |
| `2026-10-31 05:00:22` | `1.52%` | `70.0%` | 66 | 170 | `+259.5s` |
| `2026-10-31 04:30:21` | `1.01%` | `83.08%` | 99 | 183 | `+1269.5s` |
| `2026-10-31 04:00:18` | `0.0%` | `70.0%` | 131 | 199 | `+498.7s` |
| `2026-10-31 03:30:17` | `0.0%` | `63.54%` | 163 | 209 | `+1155.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:21.710000+00:00`.*
