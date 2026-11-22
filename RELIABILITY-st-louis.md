# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-22T07:00:18.750000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `37` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `20` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+208.0s` (`+3.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+120.0s` (`+2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 27.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 5.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 5.4% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 18 | 48.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19780** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+5.0 min` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+2.5 min` |
| **Route 19778** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+7.0 min` |
| **Route 19792** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+5.0 min` |
| **Route UNKNOWN** | 18 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19787** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 1 | `0.0%` |
| **Route 19778** | `+7.0 min (+420.0s)` | `+23.0 min (+1380s)` | 3 | `66.67%` |
| **Route 19792** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 3 | `100.0%` |
| **Route 19780** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19784** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19749** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19768** | `+2.5 min (+150.0s)` | `+7.0 min (+420s)` | 2 | `0.0%` |
| **Route 19781** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19777** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~705.0m | ~705.0m | **`+0.0 min`** | `98.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3399081` | Route 19780 | `00:30:00` | `SCHEDULED` | Assigned vehicle 7020 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `2.7%` | `66.67%` | 37 | 20 | `+208.0s` |
| `2026-11-22 06:30:18` | `0.0%` | `64.71%` | 63 | 40 | `+127.1s` |
| `2026-11-22 06:00:18` | `0.0%` | `74.0%` | 98 | 57 | `+201.6s` |
| `2026-11-22 05:30:33` | `0.0%` | `74.42%` | 88 | 54 | `+207.9s` |
| `2026-11-22 05:00:18` | `0.0%` | `78.95%` | 100 | 61 | `+137.9s` |
| `2026-11-22 04:30:18` | `0.0%` | `80.77%` | 94 | 61 | `+153.5s` |
| `2026-11-22 04:00:18` | `0.0%` | `76.67%` | 100 | 73 | `+133.0s` |
| `2026-11-22 03:30:21` | `0.0%` | `74.19%` | 100 | 73 | `+212.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.750000+00:00`.*
