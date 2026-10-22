# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:16:53.837000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `517` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `180` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `24` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+620.7s` (`+10.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+29.0s` (`+0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 150 | 29.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 32 | 6.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 34 | 6.6% |
| 🔴 **Severe Delay** | Over 15m late | 31 | 6.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 24 | 4.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 240 | 46.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 42** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 88** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `-159.0s` |
| **Route 80** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-47.0s` |
| **Route 7** | 8 | 6 | 2 | **`25.0%`** | `83.33%` | `+1.2 min` |
| **Route 89** | 10 | 6 | 2 | **`20.0%`** | `75.0%` | `+22.4 min` |
| **Route 193** | 6 | 4 | 1 | **`16.67%`** | `80.0%` | `+2.4 min` |
| **Route 49** | 6 | 3 | 1 | **`16.67%`** | `100.0%` | `+1.3 min` |
| **Route 26** | 6 | 2 | 1 | **`16.67%`** | `0.0%` | `+7.8 min` |
| **Route 75** | 6 | 4 | 1 | **`16.67%`** | `60.0%` | `+60.7 min` |
| **Route 180** | 6 | 4 | 1 | **`16.67%`** | `60.0%` | `-297.4s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 84** | `+75.1 min (+4503.5s)` | `+222.2 min (+13333s)` | 2 | `25.0%` |
| **Route 75** | `+60.7 min (+3644.4s)` | `+157.2 min (+9433s)` | 4 | `60.0%` |
| **Route 20** | `+60.3 min (+3617.0s)` | `+60.3 min (+3617s)` | 1 | `0.0%` |
| **Route 132** | `+55.1 min (+3309.0s)` | `+57.7 min (+3461s)` | 1 | `0.0%` |
| **Route 95** | `+50.6 min (+3039.0s)` | `+283.4 min (+17001s)` | 3 | `50.0%` |
| **Route 187** | `+37.5 min (+2249.0s)` | `+43.0 min (+2581s)` | 1 | `0.0%` |
| **Route 74** | `+35.3 min (+2115.3s)` | `+106.0 min (+6362s)` | 2 | `66.67%` |
| **Route 32** | `+33.5 min (+2010.3s)` | `+99.2 min (+5949s)` | 3 | `33.33%` |
| **Route 71** | `+26.5 min (+1587.7s)` | `+82.5 min (+4951s)` | 2 | `33.33%` |
| **Route 96** | `+24.6 min (+1477.2s)` | `+82.0 min (+4917s)` | 3 | `33.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 83** | ~24.0m | ~24.0m | **`+1.4 min`** | `0.0 / 100` |
| **Route 95** | ~135.0m | ~135.0m | **`+1.1 min`** | `3.1 / 100` |
| **Route 89** | ~15.0m | ~15.0m | **`+0.7 min`** | `0.0 / 100` |
| **Route 75** | ~64.0m | ~64.0m | **`+0.7 min`** | `0.0 / 100` |
| **Route 84** | ~196.0m | ~196.0m | **`+0.5 min`** | `44.3 / 100` |
| **Route 32** | ~40.0m | ~40.0m | **`+0.5 min`** | `0.0 / 100` |
| **Route 89** | ~33.0m | ~33.0m | **`+0.4 min`** | `0.0 / 100` |
| **Route 71** | ~40.0m | ~40.0m | **`+0.4 min`** | `0.0 / 100` |
| **Route 75** | ~120.0m | ~120.0m | **`+0.4 min`** | `38.1 / 100` |
| **Route 2** | ~15.0m | ~15.0m | **`+0.3 min`** | `0.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `11713556` | Route 74 | `15:15:00` | `SCHEDULED` | Assigned vehicle 2313 is broadcasting off-schedule with no vehicle covering 11713556 |
| `11729895` | Route 127 | `15:30:00` | `SCHEDULED` | Assigned vehicle 2317 is broadcasting off-schedule with no vehicle covering 11729895 |
| `11783671` | Route 117 | `15:21:00` | `SCHEDULED` | Assigned vehicle 2327 is broadcasting off-schedule with no vehicle covering 11783671 |
| `11704874` | Route 26 | `15:14:00` | `SCHEDULED` | Assigned vehicle 2379 is broadcasting off-schedule with no vehicle covering 11704874 |
| `11706660` | Route 39 | `13:16:00` | `SCHEDULED` | Assigned vehicle 2418 is broadcasting off-schedule with no vehicle covering 11706660 |
| `11715145` | Route 78 | `15:25:00` | `SCHEDULED` | Assigned vehicle 3507 is broadcasting off-schedule with no vehicle covering 11715145 |
| `11720740` | Route 89 | `15:14:00` | `SCHEDULED` | Assigned vehicle 3523 is broadcasting off-schedule with no vehicle covering 11720740 |
| `11708737` | Route 49 | `15:26:00` | `SCHEDULED` | Assigned vehicle 3552 is broadcasting off-schedule with no vehicle covering 11708737 |
| `11719416` | Route 87 | `15:25:00` | `SCHEDULED` | Assigned vehicle 3607 is broadcasting off-schedule with no vehicle covering 11719416 |
| `11699384` | Route 12 | `15:15:00` | `SCHEDULED` | Assigned vehicle 3610 is broadcasting off-schedule with no vehicle covering 11699384 |
| `11736591` | Route 193 | `15:25:00` | `SCHEDULED` | Assigned vehicle 3624 is broadcasting off-schedule with no vehicle covering 11736591 |
| `11720778` | Route 89 | `15:29:00` | `SCHEDULED` | Assigned vehicle 3695 is broadcasting off-schedule with no vehicle covering 11720778 |
| `11697728` | Route 7 | `15:15:00` | `SCHEDULED` | Assigned vehicle 3704 is broadcasting off-schedule with no vehicle covering 11697728 |
| `11725306` | Route 115 | `15:15:00` | `SCHEDULED` | Assigned vehicle 3719 is broadcasting off-schedule with no vehicle covering 11725306 |
| `11697768` | Route 7 | `15:15:00` | `SCHEDULED` | Assigned vehicle 3739 is broadcasting off-schedule with no vehicle covering 11697768 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:16:53` | `4.64%` | `60.73%` | 517 | 180 | `+620.7s` |
| `2026-10-22 19:00:22` | `6.21%` | `0.0%` | 451 | 176 | `+0.0s` |
| `2026-10-22 18:30:37` | `8.08%` | `0.0%` | 421 | 176 | `+0.0s` |
| `2026-10-22 15:01:10` | `8.5%` | `0.0%` | 412 | 178 | `+0.0s` |
| `2026-10-22 12:30:38` | `6.65%` | `0.0%` | 481 | 185 | `+0.0s` |
| `2026-10-22 12:00:43` | `7.73%` | `0.0%` | 440 | 180 | `+0.0s` |
| `2026-10-22 11:30:36` | `9.66%` | `0.0%` | 435 | 181 | `+0.0s` |
| `2026-10-22 11:00:36` | `9.29%` | `0.0%` | 452 | 187 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:16:53.837000+00:00`.*
