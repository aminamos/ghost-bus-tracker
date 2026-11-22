# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-22T07:00:18.670000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`84.21%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `20` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+51.6s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+44.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 80.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 10.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 5.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 5.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.0 min` |
| **Route 9899** | 4 | 3 | 0 | **`0.0%`** | `75.0%` | `+0.1 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `66.67%` | `+1.2 min` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+1.8 min (+108.0s)` | `+2.2 min (+133s)` | 2 | `100.0%` |
| **Route 107** | `+1.4 min (+81.8s)` | `+3.7 min (+223s)` | 2 | `100.0%` |
| **Route 77** | `+1.2 min (+70.3s)` | `+5.1 min (+306s)` | 4 | `66.67%` |
| **Route 9899** | `+0.1 min (+3.8s)` | `+1.2 min (+71s)` | 3 | `75.0%` |
| **Route 20** | `+0.0 min (+0.3s)` | `+0.7 min (+44s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~12.0m | ~12.0m | **`+0.0 min`** | `81.9 / 100` |
| **Route 107** | ~11.0m | ~11.0m | **`+0.0 min`** | `87.2 / 100` |
| **Route 9899** | ~26.0m | ~26.0m | **`+0.0 min`** | `95.2 / 100` |
| **Route 20** | ~19.0m | ~19.0m | **`+0.0 min`** | `96.9 / 100` |
| **Route 1** | ~13.0m | ~13.0m | **`+0.0 min`** | `96.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2027121` | Route 20 | `02:10:00` | `SCHEDULED` | Assigned vehicle C2621 is broadcasting off-schedule with no vehicle covering 2027121 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `5.0%` | `84.21%` | 20 | 14 | `+51.6s` |
| `2026-11-22 06:30:18` | `3.45%` | `89.29%` | 29 | 18 | `+57.2s` |
| `2026-11-22 06:00:18` | `6.98%` | `87.5%` | 43 | 27 | `+51.5s` |
| `2026-11-22 05:00:18` | `3.8%` | `93.42%` | 79 | 55 | `+54.7s` |
| `2026-11-22 04:30:18` | `12.96%` | `87.23%` | 108 | 59 | `+73.4s` |
| `2026-11-22 04:00:18` | `3.08%` | `88.1%` | 130 | 78 | `+58.1s` |
| `2026-11-22 03:30:21` | `4.61%` | `89.66%` | 152 | 87 | `+80.4s` |
| `2026-11-22 03:00:19` | `7.65%` | `90.53%` | 183 | 98 | `+58.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.670000+00:00`.*
