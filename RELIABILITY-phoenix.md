# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-03T07:00:20.550000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.54%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.25%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `65` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `343` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+332.3s` (`+5.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+77.5s` (`+1.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 55.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 20.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 9 | 13.8% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 9.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 13** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+33.3 min` |
| **Route 19** | 4 | 5 | 0 | **`0.0%`** | `50.0%` | `-129.2s` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+1.3 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-44.0s` |
| **Route 90** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+32.5 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.2 min` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+38.0 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.4 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.3 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 15** | `+50.5 min (+3033.0s)` | `+50.5 min (+3033s)` | 2 | `0.0%` |
| **Route 3** | `+38.0 min (+2280.2s)` | `+66.4 min (+3986s)` | 4 | `25.0%` |
| **Route 13** | `+33.3 min (+1996.0s)` | `+33.3 min (+1996s)` | 2 | `0.0%` |
| **Route 90** | `+32.5 min (+1948.0s)` | `+56.9 min (+3416s)` | 2 | `0.0%` |
| **Route 32** | `+9.8 min (+586.0s)` | `+9.8 min (+586s)` | 1 | `0.0%` |
| **Route FBUZ** | `+6.6 min (+398.0s)` | `+6.6 min (+398s)` | 1 | `0.0%` |
| **Route 72** | `+6.4 min (+386.0s)` | `+6.4 min (+386s)` | 1 | `0.0%` |
| **Route 51** | `+4.4 min (+261.5s)` | `+6.8 min (+407s)` | 2 | `50.0%` |
| **Route 17** | `+3.9 min (+233.5s)` | `+5.2 min (+310s)` | 2 | `50.0%` |
| **Route 50** | `+3.3 min (+196.0s)` | `+3.6 min (+218s)` | 2 | `100.0%` |

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
| `24731777` | Route 13 | `N/A` | `SCHEDULED` | Assigned vehicle 5328 is broadcasting off-schedule with no vehicle covering 24731777 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:20` | `1.54%` | `56.25%` | 65 | 343 | `+332.3s` |
| `2026-11-03 06:30:26` | `0.0%` | `69.74%` | 152 | 397 | `+312.6s` |
| `2026-11-03 06:00:19` | `3.75%` | `76.26%` | 267 | 431 | `+159.6s` |
| `2026-11-03 05:30:19` | `3.8%` | `75.33%` | 316 | 465 | `+212.0s` |
| `2026-11-03 05:00:26` | `4.18%` | `75.0%` | 359 | 509 | `+182.7s` |
| `2026-11-03 04:30:21` | `4.04%` | `74.21%` | 396 | 525 | `+187.7s` |
| `2026-11-03 04:00:19` | `4.84%` | `77.1%` | 413 | 559 | `+201.3s` |
| `2026-11-03 03:30:20` | `3.72%` | `78.26%` | 430 | 608 | `+194.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:20.550000+00:00`.*
