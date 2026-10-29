# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-29T07:00:18.392000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.46%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `293` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `765` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `16` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 16 | 5.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 343** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 312** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 329** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 345** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 306** | 12 | 10 | 2 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 396** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 334** | 15 | 13 | 2 | **`13.33%`** | `0.0%` | `+0.0s` |
| **Route 336** | 9 | 8 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |

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
| `68181020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8402 is broadcasting off-schedule with no vehicle covering 68181020 |
| `41875020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4515 is broadcasting off-schedule with no vehicle covering 41875020 |
| `128376020` | Route 306 | `N/A` | `SCHEDULED` | Assigned vehicle 4471 is broadcasting off-schedule with no vehicle covering 128376020 |
| `66115020` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4459 is broadcasting off-schedule with no vehicle covering 66115020 |
| `20869020` | Route 345 | `N/A` | `SCHEDULED` | Assigned vehicle 7331 is broadcasting off-schedule with no vehicle covering 20869020 |
| `21329020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 3403 is broadcasting off-schedule with no vehicle covering 21329020 |
| `113451020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3338 is broadcasting off-schedule with no vehicle covering 113451020 |
| `18602020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 7218 is broadcasting off-schedule with no vehicle covering 18602020 |
| `48196020` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3294 is broadcasting off-schedule with no vehicle covering 48196020 |
| `48547020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4629 is broadcasting off-schedule with no vehicle covering 48547020 |
| `57617020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8638 is broadcasting off-schedule with no vehicle covering 57617020 |
| `46232020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3225 is broadcasting off-schedule with no vehicle covering 46232020 |
| `78404020` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 9218 is broadcasting off-schedule with no vehicle covering 78404020 |
| `4978020` | Route 301 | `N/A` | `SCHEDULED` | Assigned vehicle 8206 is broadcasting off-schedule with no vehicle covering 4978020 |
| `59431020` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9438 is broadcasting off-schedule with no vehicle covering 59431020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `5.46%` | `0.0%` | 293 | 765 | `+0.0s` |
| `2026-10-29 06:30:19` | `3.55%` | `0.0%` | 394 | 898 | `+0.0s` |
| `2026-10-29 06:00:19` | `7.85%` | `0.0%` | 548 | 997 | `+0.0s` |
| `2026-10-29 05:30:18` | `7.36%` | `0.0%` | 774 | 1076 | `+0.0s` |
| `2026-10-29 05:00:18` | `8.8%` | `0.0%` | 1000 | 1112 | `+0.0s` |
| `2026-10-29 04:30:18` | `6.45%` | `0.0%` | 1148 | 1113 | `+0.0s` |
| `2026-10-29 04:00:18` | `9.0%` | `0.0%` | 1167 | 1133 | `+0.0s` |
| `2026-10-29 03:30:18` | `6.56%` | `0.0%` | 1205 | 1212 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.392000+00:00`.*
