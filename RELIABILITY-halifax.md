# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:42.373000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`34.95%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.65%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `804` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `284` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `281` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+189.6s` (`+3.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+40.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 305 | 37.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 68 | 8.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 120 | 14.9% |
| 🔴 **Severe Delay** | Over 15m late | 27 | 3.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 281 | 35.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 51A** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 28 | 4 | 23 | **`82.14%`** | `100.0%` | `+1.4 min` |
| **Route 82** | 11 | 2 | 9 | **`81.82%`** | `100.0%` | `+1.4 min` |
| **Route 7B** | 41 | 4 | 33 | **`80.49%`** | `37.5%` | `+4.7 min` |
| **Route 7A** | 38 | 6 | 28 | **`73.68%`** | `50.0%` | `+4.9 min` |
| **Route 56** | 21 | 3 | 15 | **`71.43%`** | `83.33%` | `+2.5 min` |
| **Route 1** | 68 | 12 | 46 | **`67.65%`** | `38.1%` | `+5.6 min` |
| **Route 24** | 24 | 5 | 16 | **`66.67%`** | `87.5%` | `+0.8 min` |
| **Route 433** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+0.0s` |
| **Route 9B** | 25 | 6 | 16 | **`64.0%`** | `55.56%` | `+4.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 50** | `+20.3 min (+1219.5s)` | `+26.6 min (+1599s)` | 2 | `0.0%` |
| **Route 137** | `+16.2 min (+970.2s)` | `+39.4 min (+2361s)` | 5 | `40.0%` |
| **Route 61** | `+11.8 min (+710.8s)` | `+20.2 min (+1214s)` | 4 | `25.0%` |
| **Route 159** | `+11.2 min (+669.6s)` | `+29.2 min (+1754s)` | 5 | `40.0%` |
| **Route 59** | `+10.7 min (+640.5s)` | `+24.0 min (+1440s)` | 4 | `25.0%` |
| **Route 4** | `+10.6 min (+638.0s)` | `+22.7 min (+1360s)` | 13 | `11.76%` |
| **Route 10C** | `+9.1 min (+548.5s)` | `+22.6 min (+1358s)` | 8 | `41.67%` |
| **Route 10B** | `+9.0 min (+540.7s)` | `+21.7 min (+1304s)` | 7 | `33.33%` |
| **Route 161** | `+8.7 min (+524.2s)` | `+21.2 min (+1270s)` | 5 | `60.0%` |
| **Route 135** | `+8.4 min (+502.0s)` | `+17.7 min (+1063s)` | 4 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7A** | ~15.0m | ~15.0m | **`+0.0 min`** | `58.5 / 100` |
| **Route 127** | ~15.0m | ~15.0m | **`+0.0 min`** | `58.8 / 100` |
| **Route 1** | ~10.0m | ~10.0m | **`+0.0 min`** | `58.0 / 100` |
| **Route 87** | ~60.0m | ~60.0m | **`+0.0 min`** | `86.0 / 100` |
| **Route 7B** | ~15.0m | ~15.0m | **`+0.0 min`** | `72.1 / 100` |
| **Route 8** | ~30.0m | ~30.0m | **`+0.0 min`** | `84.3 / 100` |
| **Route 56** | ~30.0m | ~30.0m | **`+0.0 min`** | `86.3 / 100` |
| **Route 9A** | ~20.0m | ~20.0m | **`+0.0 min`** | `83.8 / 100` |
| **Route 9B** | ~30.0m | ~30.0m | **`+0.0 min`** | `87.3 / 100` |
| **Route 320** | ~30.0m | ~30.0m | **`+0.0 min`** | `89.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `4653013` | Route 3 | `N/A` | `SCHEDULED` | Assigned vehicle 3225 is broadcasting off-schedule with no vehicle covering 4653013 |
| `4649724` | Route 10B | `N/A` | `SCHEDULED` | Assigned vehicle 3412 is broadcasting off-schedule with no vehicle covering 4649724 |
| `4654456` | Route 4 | `N/A` | `SCHEDULED` | Assigned vehicle 4006 is broadcasting off-schedule with no vehicle covering 4654456 |
| `4657892` | Route 6B | `16:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4657864` | Route 6B | `16:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650188` | Route 127 | `17:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658705` | Route 7A | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658708` | Route 7A | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661518` | Route 9A | `16:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649383` | Route 1 | `16:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649394` | Route 1 | `18:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649403` | Route 1 | `20:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649412` | Route 1 | `21:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649419` | Route 1 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649425` | Route 1 | `24:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:42.373000+00:00`.*
