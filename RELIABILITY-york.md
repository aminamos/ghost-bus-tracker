# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-24T07:00:19.301000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+21.3s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 88.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 8.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 4.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 1 | **`14.29%`** | `100.0%` | `+0.1 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `-11.8s` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+0.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+2.4 min (+146.0s)` | `+2.4 min (+146s)` | 1 | `100.0%` |
| **Route 77** | `+0.6 min (+37.5s)` | `+4.1 min (+246s)` | 4 | `83.33%` |
| **Route 9899** | `+0.6 min (+35.8s)` | `+1.4 min (+82s)` | 4 | `100.0%` |
| **Route 20** | `+0.1 min (+5.5s)` | `+0.5 min (+27s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `79.2 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `85.8 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `97.2 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `98.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2003 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:19` | `4.0%` | `91.67%` | 25 | 15 | `+21.3s` |
| `2026-11-24 06:30:22` | `0.0%` | `85.29%` | 34 | 19 | `+44.5s` |
| `2026-11-24 06:00:18` | `2.22%` | `79.55%` | 45 | 28 | `+35.1s` |
| `2026-11-24 05:30:18` | `5.88%` | `92.19%` | 68 | 46 | `+47.2s` |
| `2026-11-24 05:00:28` | `7.29%` | `84.27%` | 96 | 62 | `+75.5s` |
| `2026-11-24 04:30:20` | `7.14%` | `86.32%` | 126 | 76 | `+34.2s` |
| `2026-11-24 04:00:20` | `4.61%` | `87.59%` | 152 | 84 | `+45.6s` |
| `2026-11-24 03:30:26` | `1.1%` | `91.62%` | 181 | 98 | `+53.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:19.301000+00:00`.*
