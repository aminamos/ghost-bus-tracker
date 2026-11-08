# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-08T07:00:18.233000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`94.74%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `20` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+81.7s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+36.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 18 | 90.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 5.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 5.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+1.1 min` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 9899** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `83.33%` | `+1.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+2.1 min (+124.5s)` | `+5.0 min (+299s)` | 3 | `100.0%` |
| **Route 1** | `+1.3 min (+75.5s)` | `+1.6 min (+96s)` | 2 | `100.0%` |
| **Route 77** | `+1.2 min (+71.5s)` | `+6.4 min (+386s)` | 4 | `83.33%` |
| **Route 107** | `+1.2 min (+70.5s)` | `+3.6 min (+218s)` | 2 | `100.0%` |
| **Route 20** | `+1.1 min (+64.3s)` | `+2.6 min (+157s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~12.0m | ~12.0m | **`+0.0 min`** | `79.8 / 100` |
| **Route 107** | ~11.0m | ~11.0m | **`+0.0 min`** | `86.9 / 100` |
| **Route 9899** | ~26.0m | ~26.0m | **`+0.0 min`** | `92.7 / 100` |
| **Route 20** | ~19.0m | ~19.0m | **`+0.0 min`** | `94.1 / 100` |
| **Route 1** | ~13.0m | ~13.0m | **`+0.0 min`** | `97.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2027121` | Route 20 | `02:10:00` | `SCHEDULED` | Assigned vehicle C2615 is broadcasting off-schedule with no vehicle covering 2027121 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `5.0%` | `94.74%` | 20 | 14 | `+81.7s` |
| `2026-11-08 06:30:20` | `3.45%` | `85.71%` | 29 | 18 | `+15.2s` |
| `2026-11-08 06:00:18` | `7.14%` | `87.18%` | 42 | 28 | `+43.5s` |
| `2026-11-08 05:30:20` | `3.33%` | `84.48%` | 60 | 39 | `+52.4s` |
| `2026-11-08 05:00:18` | `6.33%` | `90.54%` | 79 | 54 | `+39.0s` |
| `2026-11-08 04:30:26` | `6.42%` | `89.22%` | 109 | 60 | `+74.4s` |
| `2026-11-08 04:00:19` | `6.87%` | `91.8%` | 131 | 76 | `+56.4s` |
| `2026-11-08 03:30:18` | `5.16%` | `88.44%` | 155 | 89 | `+59.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.233000+00:00`.*
