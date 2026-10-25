# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-25T06:15:49.153000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.76%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `21` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+49.0s` (`+0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 76.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 14.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 4.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 4.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 4 | 2 | 1 | **`25.0%`** | `100.0%` | `+1.4 min` |
| **Route 107** | 5 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `66.67%` | `-18.2s` |
| **Route 9899** | 4 | 3 | 0 | **`0.0%`** | `75.0%` | `+2.0 min` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+2.0 min (+120.5s)` | `+5.5 min (+330s)` | 3 | `75.0%` |
| **Route 20** | `+1.4 min (+83.3s)` | `+4.0 min (+243s)` | 2 | `100.0%` |
| **Route 1** | `+1.0 min (+60.0s)` | `+3.3 min (+200s)` | 2 | `50.0%` |
| **Route 107** | `+0.8 min (+47.2s)` | `+4.2 min (+250s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | ~13.0m | ~13.0m | **`+0.0 min`** | `82.1 / 100` |
| **Route 77** | ~12.0m | ~12.0m | **`+0.0 min`** | `86.2 / 100` |
| **Route 9899** | ~26.0m | ~26.0m | **`+0.0 min`** | `91.3 / 100` |
| **Route 20** | ~19.0m | ~19.0m | **`+0.0 min`** | `90.1 / 100` |
| **Route 107** | ~18.5m | ~18.5m | **`+0.0 min`** | `90.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2012392` | Route 20 | `01:40:00` | `SCHEDULED` | Assigned vehicle C2005 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:49` | `4.76%` | `80.0%` | 21 | 13 | `+49.0s` |
| `2026-10-25 06:00:59` | `10.0%` | `94.44%` | 20 | 14 | `+82.1s` |
| `2026-10-25 05:30:23` | `6.9%` | `88.89%` | 29 | 19 | `+45.9s` |
| `2026-10-25 04:33:58` | `8.47%` | `81.48%` | 59 | 42 | `+75.6s` |
| `2026-10-25 03:30:21` | `8.87%` | `87.61%` | 124 | 74 | `+106.6s` |
| `2026-10-25 03:00:22` | `4.7%` | `87.32%` | 149 | 85 | `+101.6s` |
| `2026-10-25 02:30:20` | `5.17%` | `86.06%` | 174 | 93 | `+62.5s` |
| `2026-10-25 01:30:20` | `6.4%` | `84.21%` | 203 | 102 | `+73.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:49.153000+00:00`.*
