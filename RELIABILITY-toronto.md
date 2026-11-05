# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-05T07:00:17.819000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.37%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `565` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1003` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `36` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 36 | 6.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 329** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 12** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 373** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 396** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7052 is broadcasting off-schedule with no vehicle covering 33114020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7235 is broadcasting off-schedule with no vehicle covering 67227020 |
| `72397020` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9457 is broadcasting off-schedule with no vehicle covering 72397020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3141 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3335 is broadcasting off-schedule with no vehicle covering 26944020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4477 is broadcasting off-schedule with no vehicle covering 69272020 |
| `27458020` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 8418 is broadcasting off-schedule with no vehicle covering 27458020 |
| `22478020` | Route 301 | `N/A` | `SCHEDULED` | Assigned vehicle 8581 is broadcasting off-schedule with no vehicle covering 22478020 |
| `75378020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7091 is broadcasting off-schedule with no vehicle covering 75378020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8891 is broadcasting off-schedule with no vehicle covering 32959020 |
| `59341020` | Route 25 | `N/A` | `SCHEDULED` | Assigned vehicle 8696 is broadcasting off-schedule with no vehicle covering 59341020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 7324 is broadcasting off-schedule with no vehicle covering 32095020 |
| `96253020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 7289 is broadcasting off-schedule with no vehicle covering 96253020 |
| `33781020` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 9210 is broadcasting off-schedule with no vehicle covering 33781020 |
| `43639020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 3579 is broadcasting off-schedule with no vehicle covering 43639020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:17` | `6.37%` | `0.0%` | 565 | 1003 | `+0.0s` |
| `2026-11-05 06:30:17` | `8.02%` | `0.0%` | 773 | 1079 | `+0.0s` |
| `2026-11-05 06:00:17` | `8.56%` | `0.0%` | 993 | 1114 | `+0.0s` |
| `2026-11-05 05:30:18` | `8.38%` | `0.0%` | 1122 | 1120 | `+0.0s` |
| `2026-11-05 05:00:17` | `7.23%` | `0.0%` | 1162 | 1194 | `+0.0s` |
| `2026-11-05 04:30:18` | `7.05%` | `0.0%` | 1177 | 1239 | `+0.0s` |
| `2026-11-05 04:00:18` | `8.08%` | `0.0%` | 1201 | 1326 | `+0.0s` |
| `2026-11-05 03:30:18` | `7.29%` | `0.0%` | 1289 | 1443 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.819000+00:00`.*
