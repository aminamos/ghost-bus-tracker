# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-15T07:00:19.115000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.53%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `19` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+84.9s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+41.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 17 | 89.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 10.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 3 | 3 | 1 | **`33.33%`** | `100.0%` | `+0.3 min` |
| **Route 77** | 6 | 4 | 1 | **`16.67%`** | `100.0%` | `+2.0 min` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 9899** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 1** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+2.7 min (+159.5s)` | `+3.7 min (+221s)` | 2 | `100.0%` |
| **Route 77** | `+2.0 min (+123.0s)` | `+5.0 min (+298s)` | 4 | `100.0%` |
| **Route 107** | `+1.0 min (+61.5s)` | `+2.8 min (+168s)` | 2 | `100.0%` |
| **Route 9899** | `+0.9 min (+55.8s)` | `+1.8 min (+107s)` | 3 | `100.0%` |
| **Route 20** | `+0.3 min (+20.5s)` | `+0.7 min (+41s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 77** | ~12.0m | ~12.0m | **`+0.0 min`** | `80.8 / 100` |
| **Route 107** | ~11.0m | ~11.0m | **`+0.0 min`** | `90.4 / 100` |
| **Route 1** | ~13.0m | ~13.0m | **`+0.0 min`** | `92.1 / 100` |
| **Route 9899** | ~26.0m | ~26.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 20** | ~20.5m | ~20.5m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2027121` | Route 20 | `02:10:00` | `SCHEDULED` | Assigned vehicle C2647 is broadcasting off-schedule with no vehicle covering 2027121 |
| `2027239` | Route 77 | `02:05:00` | `SCHEDULED` | Assigned vehicle C1421 is broadcasting off-schedule with no vehicle covering 2027239 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:19` | `10.53%` | `100.0%` | 19 | 14 | `+84.9s` |
| `2026-11-15 06:30:18` | `10.71%` | `80.0%` | 28 | 18 | `+78.6s` |
| `2026-11-15 05:30:20` | `3.45%` | `85.71%` | 58 | 40 | `+61.6s` |
| `2026-11-15 05:00:23` | `5.41%` | `90.0%` | 74 | 51 | `+50.2s` |
| `2026-11-15 04:30:20` | `8.49%` | `86.6%` | 106 | 61 | `+84.6s` |
| `2026-11-15 04:00:20` | `5.47%` | `88.43%` | 128 | 75 | `+72.0s` |
| `2026-11-15 03:30:19` | `7.84%` | `91.49%` | 153 | 88 | `+48.6s` |
| `2026-11-15 03:00:20` | `6.56%` | `90.06%` | 183 | 98 | `+61.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.115000+00:00`.*
