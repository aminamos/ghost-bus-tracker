# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-30T04:30:20.865000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.14%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`78.65%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `98` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `99` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+120.8s` (`+2.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+56.0s` (`+0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 70 | 71.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 4.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 15 | 15.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 7.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 53** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `-245.0s` |
| **Route CN1** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+1.5 min` |
| **Route 66** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+1.6 min` |
| **Route 21** | 5 | 4 | 1 | **`20.0%`** | `75.0%` | `+3.5 min` |
| **Route 80** | 6 | 5 | 1 | **`16.67%`** | `100.0%` | `+0.8 min` |
| **Route 35** | 7 | 4 | 1 | **`14.29%`** | `50.0%` | `+4.1 min` |
| **Route 92** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+4.8 min` |
| **Route 56** | 4 | 2 | 0 | **`0.0%`** | `75.0%` | `+1.6 min` |
| **Route 19** | 7 | 5 | 0 | **`0.0%`** | `85.71%` | `+2.5 min` |
| **Route 76** | 6 | 5 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 73** | `+5.2 min (+309.0s)` | `+5.7 min (+342s)` | 2 | `50.0%` |
| **Route 92** | `+4.8 min (+287.3s)` | `+13.8 min (+831s)` | 3 | `33.33%` |
| **Route 14** | `+4.5 min (+271.0s)` | `+7.0 min (+420s)` | 3 | `66.67%` |
| **Route 35** | `+4.1 min (+243.7s)` | `+10.0 min (+601s)` | 4 | `50.0%` |
| **Route 54** | `+3.7 min (+223.0s)` | `+6.8 min (+409s)` | 3 | `75.0%` |
| **Route 21** | `+3.5 min (+210.0s)` | `+8.1 min (+484s)` | 4 | `75.0%` |
| **Route 30** | `+2.5 min (+151.5s)` | `+5.6 min (+336s)` | 5 | `33.33%` |
| **Route 19** | `+2.5 min (+150.9s)` | `+5.7 min (+340s)` | 5 | `85.71%` |
| **Route BLU** | `+1.9 min (+113.2s)` | `+6.8 min (+406s)` | 3 | `75.0%` |
| **Route 66** | `+1.6 min (+98.7s)` | `+3.6 min (+214s)` | 3 | `100.0%` |

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
| `37803829` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 6516 is broadcasting off-schedule with no vehicle covering 37803829 |
| `37803589` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 6203 is missing from active GPS transponder fleet |
| `37806330` | Route 80 | `N/A` | `SCHEDULED` | Assigned vehicle 6533 is broadcasting off-schedule with no vehicle covering 37806330 |
| `37843598` | Route 21 | `N/A` | `SCHEDULED` | Assigned vehicle 6313 is broadcasting off-schedule with no vehicle covering 37843598 |
| `37802528` | Route 60 | `N/A` | `SCHEDULED` | Assigned vehicle 6305 is broadcasting off-schedule with no vehicle covering 37802528 |
| `37803473` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 6307 is broadcasting off-schedule with no vehicle covering 37803473 |
| `37804691` | Route CN1 | `N/A` | `SCHEDULED` | Assigned vehicle 1003 is broadcasting off-schedule with no vehicle covering 37804691 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 04:30:20` | `7.14%` | `78.65%` | 98 | 99 | `+120.8s` |
| `2026-10-30 03:30:18` | `11.93%` | `85.71%` | 109 | 109 | `+109.9s` |
| `2026-10-30 02:00:18` | `15.5%` | `100.0%` | 129 | 131 | `+11.0s` |
| `2026-10-30 01:00:19` | `12.58%` | `0.0%` | 151 | 146 | `+0.0s` |
| `2026-10-29 23:30:19` | `6.67%` | `0.0%` | 180 | 173 | `+0.0s` |
| `2026-10-29 23:00:19` | `8.04%` | `0.0%` | 199 | 199 | `+0.0s` |
| `2026-10-29 22:30:19` | `4.05%` | `0.0%` | 222 | 214 | `+0.0s` |
| `2026-10-29 22:00:20` | `7.49%` | `0.0%` | 227 | 213 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T04:30:20.865000+00:00`.*
