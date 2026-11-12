# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-12T07:00:19.747000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+38.8s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 24 | 96.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 4.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 1 | **`14.29%`** | `100.0%` | `+0.7 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | `+1.0 min (+61.7s)` | `+2.0 min (+119s)` | 4 | `100.0%` |
| **Route 20** | `+0.7 min (+44.3s)` | `+4.6 min (+274s)` | 4 | `100.0%` |
| **Route 9899** | `+0.7 min (+39.2s)` | `+2.3 min (+138s)` | 4 | `100.0%` |
| **Route 1** | `+0.5 min (+27.0s)` | `+0.5 min (+27s)` | 1 | `100.0%` |
| **Route 107** | `+0.2 min (+12.2s)` | `+1.5 min (+89s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `84.4 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `90.3 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `94.4 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `92.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2003 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:19` | `4.0%` | `100.0%` | 25 | 15 | `+38.8s` |
| `2026-11-12 06:30:19` | `2.94%` | `96.97%` | 34 | 18 | `+42.7s` |
| `2026-11-12 06:00:18` | `4.44%` | `88.37%` | 45 | 28 | `+51.0s` |
| `2026-11-12 05:30:18` | `5.88%` | `89.06%` | 68 | 45 | `+62.8s` |
| `2026-11-12 05:00:18` | `9.47%` | `91.86%` | 95 | 60 | `+51.6s` |
| `2026-11-12 04:30:19` | `10.24%` | `88.6%` | 127 | 77 | `+36.8s` |
| `2026-11-12 04:00:20` | `3.9%` | `91.22%` | 154 | 87 | `+56.3s` |
| `2026-11-12 03:30:20` | `10.5%` | `87.65%` | 181 | 97 | `+75.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:19.747000+00:00`.*
