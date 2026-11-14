# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-14T07:00:18.373000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.66%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `561` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `943` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `43` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 43 | 7.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 343** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 6 | 6 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 70** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 373** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 3562 is broadcasting off-schedule with no vehicle covering 33114020 |
| `54882020` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 8863 is broadcasting off-schedule with no vehicle covering 54882020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3101 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8330 is broadcasting off-schedule with no vehicle covering 26944020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3184 is broadcasting off-schedule with no vehicle covering 65345020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4508 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8460 is broadcasting off-schedule with no vehicle covering 27458020 |
| `56365020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8653 is broadcasting off-schedule with no vehicle covering 56365020 |
| `75378020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7019 is broadcasting off-schedule with no vehicle covering 75378020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 3649 is broadcasting off-schedule with no vehicle covering 32959020 |
| `72823020` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 8653 is broadcasting off-schedule with no vehicle covering 72823020 |
| `11040020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3184 is broadcasting off-schedule with no vehicle covering 11040020 |
| `96253020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 7317 is broadcasting off-schedule with no vehicle covering 96253020 |
| `33781020` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3328 is broadcasting off-schedule with no vehicle covering 33781020 |
| `43639020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7009 is broadcasting off-schedule with no vehicle covering 43639020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:18` | `7.66%` | `0.0%` | 561 | 943 | `+0.0s` |
| `2026-11-14 06:30:18` | `7.64%` | `0.0%` | 772 | 1022 | `+0.0s` |
| `2026-11-14 06:00:18` | `8.7%` | `0.0%` | 1000 | 1039 | `+0.0s` |
| `2026-11-14 05:30:18` | `7.46%` | `0.0%` | 1140 | 1047 | `+0.0s` |
| `2026-11-14 05:00:19` | `7.97%` | `0.0%` | 1167 | 1104 | `+0.0s` |
| `2026-11-14 04:30:18` | `7.91%` | `0.0%` | 1175 | 1160 | `+0.0s` |
| `2026-11-14 04:00:19` | `7.63%` | `0.0%` | 1205 | 1285 | `+0.0s` |
| `2026-11-14 03:30:18` | `5.78%` | `0.0%` | 1298 | 1402 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:18.373000+00:00`.*
