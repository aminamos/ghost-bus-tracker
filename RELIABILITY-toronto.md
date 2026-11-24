# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-24T07:00:18.913000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `561` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1081` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `42` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 42 | 7.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 105** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 6 | 5 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
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
| `41698020` | Route 504 | `N/A` | `SCHEDULED` | Assigned vehicle 4649 is broadcasting off-schedule with no vehicle covering 41698020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7281 is broadcasting off-schedule with no vehicle covering 67227020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3204 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3335 is broadcasting off-schedule with no vehicle covering 26944020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3628 is broadcasting off-schedule with no vehicle covering 65345020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4624 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8462 is broadcasting off-schedule with no vehicle covering 27458020 |
| `56365020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8772 is broadcasting off-schedule with no vehicle covering 56365020 |
| `21609020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 3578 is broadcasting off-schedule with no vehicle covering 21609020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8937 is broadcasting off-schedule with no vehicle covering 32959020 |
| `54511020` | Route 105 | `N/A` | `SCHEDULED` | Assigned vehicle 3578 is broadcasting off-schedule with no vehicle covering 54511020 |
| `72823020` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 8772 is broadcasting off-schedule with no vehicle covering 72823020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7327 is broadcasting off-schedule with no vehicle covering 32095020 |
| `11040020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3628 is broadcasting off-schedule with no vehicle covering 11040020 |
| `96253020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 6197 is broadcasting off-schedule with no vehicle covering 96253020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:18` | `7.49%` | `0.0%` | 561 | 1081 | `+0.0s` |
| `2026-11-24 06:30:18` | `7.88%` | `0.0%` | 774 | 1129 | `+0.0s` |
| `2026-11-24 06:00:18` | `8.95%` | `0.0%` | 994 | 1159 | `+0.0s` |
| `2026-11-24 05:30:17` | `7.26%` | `0.0%` | 1129 | 1180 | `+0.0s` |
| `2026-11-24 05:00:18` | `8.42%` | `0.0%` | 1164 | 1196 | `+0.0s` |
| `2026-11-24 04:30:18` | `6.87%` | `0.0%` | 1193 | 1218 | `+0.0s` |
| `2026-11-24 04:00:18` | `8.21%` | `0.0%` | 1206 | 1322 | `+0.0s` |
| `2026-11-24 03:30:20` | `6.13%` | `0.0%` | 1305 | 1438 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:18.913000+00:00`.*
