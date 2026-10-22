# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** York Region | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:58.023000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.59%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.93%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `563` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `315` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `54` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+77.6s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 417 | 74.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 37 | 6.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 53 | 9.4% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 54 | 9.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 8301** | 4 | 2 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 462** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+0.1 min` |
| **Route 32** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+1.2 min` |
| **Route 414** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.0s` |
| **Route 9101** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.0s` |
| **Route 300** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.0s` |
| **Route 13** | 7 | 3 | 3 | **`42.86%`** | `75.0%` | `+2.6 min` |
| **Route 607** | 9 | 3 | 3 | **`33.33%`** | `100.0%` | `+0.5 min` |
| **Route 98** | 6 | 3 | 2 | **`33.33%`** | `100.0%` | `+0.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 411** | `+6.5 min (+388.5s)` | `+7.7 min (+459s)` | 2 | `0.0%` |
| **Route 420** | `+6.4 min (+386.0s)` | `+6.4 min (+386s)` | 1 | `0.0%` |
| **Route 85** | `+6.2 min (+373.3s)` | `+18.6 min (+1116s)` | 8 | `46.67%` |
| **Route 52** | `+5.6 min (+337.3s)` | `+8.4 min (+506s)` | 2 | `33.33%` |
| **Route 467** | `+5.5 min (+332.0s)` | `+5.5 min (+332s)` | 1 | `0.0%` |
| **Route 16** | `+4.0 min (+243.0s)` | `+10.4 min (+625s)` | 6 | `66.67%` |
| **Route 416** | `+3.5 min (+208.0s)` | `+3.5 min (+208s)` | 1 | `100.0%` |
| **Route 40** | `+3.4 min (+202.0s)` | `+10.3 min (+619s)` | 2 | `66.67%` |
| **Route 107** | `+3.4 min (+201.0s)` | `+8.2 min (+494s)` | 6 | `60.0%` |
| **Route 33** | `+3.3 min (+197.7s)` | `+8.0 min (+477s)` | 3 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 88** | ~8.5m | ~8.5m | **`+0.0 min`** | `29.9 / 100` |
| **Route 85** | ~9.0m | ~9.0m | **`+0.0 min`** | `40.2 / 100` |
| **Route 423** | ~1.0m | ~1.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 605** | ~8.0m | ~8.0m | **`+0.0 min`** | `39.9 / 100` |
| **Route 9002** | ~23.0m | ~23.0m | **`+0.0 min`** | `66.6 / 100` |
| **Route 522** | ~2.0m | ~2.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 77** | ~7.0m | ~7.0m | **`+0.0 min`** | `46.7 / 100` |
| **Route 91** | ~6.5m | ~6.5m | **`+0.0 min`** | `51.8 / 100` |
| **Route 57** | ~3.0m | ~3.0m | **`+0.0 min`** | `35.1 / 100` |
| **Route 16** | ~13.0m | ~13.0m | **`+0.0 min`** | `70.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2010344` | Route 20 | `15:23:00` | `SCHEDULED` | Assigned vehicle C2616 is broadcasting off-schedule with no vehicle covering 2010344 |
| `2016727` | Route 50 | `15:17:00` | `SCHEDULED` | Assigned vehicle F0918 is broadcasting off-schedule with no vehicle covering 2016727 |
| `2002853` | Route 60301 | `15:50:00` | `SCHEDULED` | Assigned vehicle V2607 is missing from active GPS transponder fleet |
| `2017075` | Route 98 | `16:17:00` | `SCHEDULED` | Assigned vehicle F2545 is broadcasting off-schedule with no vehicle covering 2017075 |
| `2009909` | Route 4 | `15:24:00` | `SCHEDULED` | Assigned vehicle C1033 is missing from active GPS transponder fleet |
| `2002429` | Route 601 | `15:15:00` | `SCHEDULED` | Assigned vehicle V2603 is broadcasting off-schedule with no vehicle covering 2002429 |
| `2006088` | Route 16 | `15:27:00` | `SCHEDULED` | Assigned vehicle M1613 is broadcasting off-schedule with no vehicle covering 2006088 |
| `2017159` | Route 607 | `15:47:00` | `SCHEDULED` | Assigned vehicle F2577 is broadcasting off-schedule with no vehicle covering 2017159 |
| `2011266` | Route 105 | `15:49:00` | `SCHEDULED` | Assigned vehicle C1818 is missing from active GPS transponder fleet |
| `2006954` | Route 414 | `15:46:00` | `SCHEDULED` | Assigned vehicle M1016 is missing from active GPS transponder fleet |
| `2005934` | Route 9 | `15:43:00` | `SCHEDULED` | Assigned vehicle M1009 is broadcasting off-schedule with no vehicle covering 2005934 |
| `2010438` | Route 20 | `15:32:00` | `SCHEDULED` | Assigned vehicle C2021 is missing from active GPS transponder fleet |
| `2010990` | Route 86 | `15:34:00` | `SCHEDULED` | Assigned vehicle C1606 is missing from active GPS transponder fleet |
| `2006236` | Route 24 | `15:14:00` | `SCHEDULED` | Assigned vehicle M0939 is missing from active GPS transponder fleet |
| `2016768` | Route 50 | `15:54:00` | `SCHEDULED` | Assigned vehicle F0909 is missing from active GPS transponder fleet |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:58.023000+00:00`.*
