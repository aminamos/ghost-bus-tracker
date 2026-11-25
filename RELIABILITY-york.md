# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-25T07:00:18.959000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`92.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `16` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+39.7s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 23 | 92.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `100.0%` | `-1.2s` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+0.1 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+2.2 min (+134.6s)` | `+5.4 min (+326s)` | 4 | `80.0%` |
| **Route 1** | `+1.2 min (+72.0s)` | `+1.2 min (+72s)` | 1 | `100.0%` |
| **Route 20** | `+0.5 min (+31.4s)` | `+3.8 min (+227s)` | 4 | `100.0%` |
| **Route 77** | `+0.1 min (+5.8s)` | `+2.0 min (+120s)` | 4 | `83.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `86.7 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `87.9 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `89.6 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `95.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `0.0%` | `92.0%` | 25 | 16 | `+39.7s` |
| `2026-11-25 06:30:19` | `0.0%` | `88.24%` | 34 | 20 | `+29.8s` |
| `2026-11-25 06:00:19` | `4.44%` | `90.7%` | 45 | 28 | `+58.2s` |
| `2026-11-25 05:30:19` | `7.46%` | `93.55%` | 67 | 45 | `+72.3s` |
| `2026-11-25 05:00:18` | `7.29%` | `87.64%` | 96 | 61 | `+70.2s` |
| `2026-11-25 04:30:18` | `4.76%` | `85.0%` | 126 | 76 | `+44.5s` |
| `2026-11-25 04:00:19` | `5.23%` | `90.34%` | 153 | 88 | `+42.8s` |
| `2026-11-25 03:30:27` | `8.89%` | `87.2%` | 180 | 97 | `+68.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.959000+00:00`.*
