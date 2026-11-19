# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** MCTS | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-19T05:00:18.955000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.8%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`83.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `102` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `103` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+112.2s` (`+1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+48.5s` (`+0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 75 | 73.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 2.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 13 | 12.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 9.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 56** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 73** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route BLU** | 3 | 3 | 2 | **`66.67%`** | `100.0%` | `+3.6 min` |
| **Route 12** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+1.1 min` |
| **Route 92** | 4 | 3 | 1 | **`25.0%`** | `66.67%` | `+4.1 min` |
| **Route 66** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.9 min` |
| **Route 30** | 6 | 5 | 1 | **`16.67%`** | `100.0%` | `+1.2 min` |
| **Route 22** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19** | 7 | 5 | 0 | **`0.0%`** | `83.33%` | `+2.3 min` |
| **Route 76** | 6 | 5 | 0 | **`0.0%`** | `50.0%` | `+3.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 88** | `+4.2 min (+252.5s)` | `+4.2 min (+255s)` | 1 | `100.0%` |
| **Route 92** | `+4.1 min (+247.3s)` | `+9.9 min (+593s)` | 3 | `66.67%` |
| **Route BLU** | `+3.6 min (+214.0s)` | `+3.6 min (+214s)` | 3 | `100.0%` |
| **Route 76** | `+3.0 min (+182.5s)` | `+9.9 min (+592s)` | 5 | `50.0%` |
| **Route CN1** | `+2.9 min (+176.4s)` | `+8.7 min (+524s)` | 4 | `60.0%` |
| **Route 35** | `+2.8 min (+169.1s)` | `+9.3 min (+561s)` | 5 | `71.43%` |
| **Route 14** | `+2.5 min (+150.0s)` | `+5.3 min (+319s)` | 3 | `75.0%` |
| **Route 19** | `+2.3 min (+140.2s)` | `+5.3 min (+316s)` | 5 | `83.33%` |
| **Route 80** | `+2.1 min (+128.6s)` | `+5.7 min (+343s)` | 5 | `57.14%` |
| **Route 21** | `+2.0 min (+120.2s)` | `+7.5 min (+449s)` | 4 | `83.33%` |

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
| `37802164` | Route 92 | `N/A` | `SCHEDULED` | Assigned vehicle 6312 is broadcasting off-schedule with no vehicle covering 37802164 |
| `37806003` | Route 56 | `N/A` | `SCHEDULED` | Assigned vehicle 6538 is broadcasting off-schedule with no vehicle covering 37806003 |
| `37803387` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 6223 is broadcasting off-schedule with no vehicle covering 37803387 |
| `37806013` | Route 56 | `N/A` | `SCHEDULED` | Assigned vehicle 6512 is broadcasting off-schedule with no vehicle covering 37806013 |
| `37805162` | Route 30 | `N/A` | `SCHEDULED` | Assigned vehicle 6212 is broadcasting off-schedule with no vehicle covering 37805162 |
| `37844070` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 6218 is broadcasting off-schedule with no vehicle covering 37844070 |
| `37806706` | Route BLU | `N/A` | `SCHEDULED` | Assigned vehicle 6402 is broadcasting off-schedule with no vehicle covering 37806706 |
| `37806698` | Route BLU | `N/A` | `SCHEDULED` | Assigned vehicle 5902 is broadcasting off-schedule with no vehicle covering 37806698 |
| `37806594` | Route 73 | `N/A` | `SCHEDULED` | Assigned vehicle 6112 is broadcasting off-schedule with no vehicle covering 37806594 |
| `37806591` | Route 73 | `N/A` | `SCHEDULED` | Assigned vehicle 5721 is broadcasting off-schedule with no vehicle covering 37806591 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 05:00:18` | `9.8%` | `83.33%` | 102 | 103 | `+112.2s` |
| `2026-11-19 04:30:19` | `12.26%` | `83.67%` | 106 | 108 | `+121.0s` |
| `2026-11-19 03:30:18` | `14.17%` | `0.0%` | 120 | 120 | `+0.0s` |
| `2026-11-19 03:00:18` | `10.61%` | `0.0%` | 132 | 128 | `+0.0s` |
| `2026-11-19 02:30:18` | `8.63%` | `0.0%` | 139 | 138 | `+0.0s` |
| `2026-11-19 02:00:18` | `13.51%` | `0.0%` | 148 | 147 | `+0.0s` |
| `2026-11-19 00:00:18` | `8.0%` | `0.0%` | 200 | 195 | `+0.0s` |
| `2026-11-18 23:30:25` | `7.73%` | `0.0%` | 220 | 214 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T05:00:18.955000+00:00`.*
