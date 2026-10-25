# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-25T06:15:48.121000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.6%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.65%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `187` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `325` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+234.2s` (`+3.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+137.5s` (`+2.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 130 | 69.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 7.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 31 | 16.6% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 5.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 1.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 106** | 3 | 2 | 1 | **`33.33%`** | `50.0%` | `+4.8 min` |
| **Route 80** | 3 | 3 | 1 | **`33.33%`** | `100.0%` | `+0.8 min` |
| **Route 72** | 6 | 6 | 1 | **`16.67%`** | `80.0%` | `+1.1 min` |
| **Route 43** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+15.7 min` |
| **Route 59** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 51** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+4.3 min` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+2.8 min` |
| **Route 45** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.8 min` |
| **Route 61** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+2.1 min` |
| **Route 186** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 43** | `+15.7 min (+939.7s)` | `+37.9 min (+2272s)` | 3 | `33.33%` |
| **Route 17** | `+12.3 min (+740.2s)` | `+27.9 min (+1676s)` | 5 | `40.0%` |
| **Route 138** | `+10.4 min (+626.5s)` | `+42.0 min (+2519s)` | 4 | `75.0%` |
| **Route 108** | `+8.3 min (+499.0s)` | `+15.8 min (+950s)` | 1 | `50.0%` |
| **Route 75** | `+7.4 min (+441.5s)` | `+11.0 min (+658s)` | 2 | `50.0%` |
| **Route 83** | `+7.2 min (+430.7s)` | `+20.7 min (+1243s)` | 3 | `66.67%` |
| **Route 30** | `+6.9 min (+415.0s)` | `+20.4 min (+1226s)` | 3 | `75.0%` |
| **Route 27** | `+6.3 min (+379.3s)` | `+14.1 min (+843s)` | 7 | `42.86%` |
| **Route 44** | `+5.9 min (+352.6s)` | `+22.4 min (+1346s)` | 5 | `60.0%` |
| **Route 45** | `+5.8 min (+346.0s)` | `+13.7 min (+823s)` | 3 | `66.67%` |

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
| `24276826` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 5667 is broadcasting off-schedule with no vehicle covering 24276826 |
| `24168226` | Route 72 | `N/A` | `SCHEDULED` | Assigned vehicle 2416 is broadcasting off-schedule with no vehicle covering 24168226 |
| `24276812` | Route 80 | `N/A` | `SCHEDULED` | Assigned vehicle 5636 is broadcasting off-schedule with no vehicle covering 24276812 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:48` | `1.6%` | `70.65%` | 187 | 325 | `+234.2s` |
| `2026-10-25 06:00:59` | `2.1%` | `75.11%` | 238 | 337 | `+213.5s` |
| `2026-10-25 05:30:23` | `2.17%` | `73.33%` | 277 | 354 | `+256.1s` |
| `2026-10-25 04:33:58` | `3.14%` | `70.54%` | 350 | 379 | `+257.9s` |
| `2026-10-25 03:30:21` | `3.72%` | `75.07%` | 403 | 427 | `+235.1s` |
| `2026-10-25 03:00:22` | `2.17%` | `73.12%` | 414 | 464 | `+238.7s` |
| `2026-10-25 02:30:20` | `3.31%` | `71.75%` | 423 | 436 | `+241.6s` |
| `2026-10-25 01:30:20` | `3.53%` | `66.74%` | 453 | 443 | `+325.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:48.121000+00:00`.*
