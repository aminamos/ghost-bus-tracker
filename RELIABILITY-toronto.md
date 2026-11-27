# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-27T07:00:18.180000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `556` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1026` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `48` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 48 | 8.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 185** | 3 | 1 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 3503 is broadcasting off-schedule with no vehicle covering 33114020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7286 is broadcasting off-schedule with no vehicle covering 67227020 |
| `44586020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 3562 is missing from active GPS transponder fleet |
| `54882020` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 3612 is broadcasting off-schedule with no vehicle covering 54882020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3112 is broadcasting off-schedule with no vehicle covering 36540020 |
| `36265020` | Route 31 | `N/A` | `SCHEDULED` | Assigned vehicle 8457 is broadcasting off-schedule with no vehicle covering 36265020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 8951 is broadcasting off-schedule with no vehicle covering 65345020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4472 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8466 is broadcasting off-schedule with no vehicle covering 27458020 |
| `56365020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8789 is broadcasting off-schedule with no vehicle covering 56365020 |
| `75378020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 3577 is broadcasting off-schedule with no vehicle covering 75378020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8757 is broadcasting off-schedule with no vehicle covering 32959020 |
| `40771020` | Route 185 | `N/A` | `SCHEDULED` | Assigned vehicle 1679 is broadcasting off-schedule with no vehicle covering 40771020 |
| `72823020` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 8789 is broadcasting off-schedule with no vehicle covering 72823020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7205 is broadcasting off-schedule with no vehicle covering 32095020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:18` | `8.63%` | `0.0%` | 556 | 1026 | `+0.0s` |
| `2026-11-27 06:30:18` | `8.49%` | `0.0%` | 766 | 1093 | `+0.0s` |
| `2026-11-27 06:00:17` | `9.18%` | `0.0%` | 991 | 1117 | `+0.0s` |
| `2026-11-27 05:30:18` | `6.42%` | `0.0%` | 1153 | 1136 | `+0.0s` |
| `2026-11-27 05:00:17` | `6.28%` | `0.0%` | 1163 | 1193 | `+0.0s` |
| `2026-11-27 04:30:18` | `6.86%` | `0.0%` | 1195 | 1245 | `+0.0s` |
| `2026-11-27 04:00:17` | `6.75%` | `0.0%` | 1186 | 1362 | `+0.0s` |
| `2026-11-27 03:30:18` | `6.89%` | `0.0%` | 1292 | 1436 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:18.180000+00:00`.*
