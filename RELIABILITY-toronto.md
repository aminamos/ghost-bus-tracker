# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T06:42:13.210719+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `330` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `914` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `18` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 5.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 307** | 5 | 5 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 339** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 363** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 325** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 395** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 5 | 2 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 352** | 6 | 4 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 353** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 335** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 336** | 9 | 9 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |

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
| `83880020` | Route 325 | `N/A` | `SCHEDULED` | Assigned vehicle 8656 is broadcasting off-schedule with no vehicle covering 83880020 |
| `62627020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3627 is broadcasting off-schedule with no vehicle covering 62627020 |
| `94228020` | Route 363 | `N/A` | `SCHEDULED` | Assigned vehicle 3570 is broadcasting off-schedule with no vehicle covering 94228020 |
| `16030020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 3448 is broadcasting off-schedule with no vehicle covering 16030020 |
| `21904020` | Route 337 | `N/A` | `SCHEDULED` | Assigned vehicle 8182 is broadcasting off-schedule with no vehicle covering 21904020 |
| `80872020` | Route 335 | `N/A` | `SCHEDULED` | Assigned vehicle 1382 is broadcasting off-schedule with no vehicle covering 80872020 |
| `28966020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 9011 is broadcasting off-schedule with no vehicle covering 28966020 |
| `117273020` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 9417 is broadcasting off-schedule with no vehicle covering 117273020 |
| `43660020` | Route 307 | `N/A` | `SCHEDULED` | Assigned vehicle 7132 is broadcasting off-schedule with no vehicle covering 43660020 |
| `35590020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8947 is broadcasting off-schedule with no vehicle covering 35590020 |
| `72725020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 9072 is broadcasting off-schedule with no vehicle covering 72725020 |
| `42362020` | Route 353 | `N/A` | `SCHEDULED` | Assigned vehicle 3218 is broadcasting off-schedule with no vehicle covering 42362020 |
| `23428020` | Route 307 | `N/A` | `SCHEDULED` | Assigned vehicle 9068 is broadcasting off-schedule with no vehicle covering 23428020 |
| `122481020` | Route 352 | `N/A` | `SCHEDULED` | Assigned vehicle 3313 is broadcasting off-schedule with no vehicle covering 122481020 |
| `123485020` | Route 395 | `N/A` | `SCHEDULED` | Assigned vehicle 8808 is broadcasting off-schedule with no vehicle covering 123485020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 06:42:13` | `5.45%` | `0.0%` | 330 | 914 | `+0.0s` |
| `2026-10-06 00:28:48` | `7.06%` | `0.0%` | 1529 | 1714 | `+0.0s` |
| `2026-10-05 18:39:14` | `6.89%` | `0.0%` | 2205 | 1784 | `+0.0s` |
| `2026-10-05 18:02:22` | `7.34%` | `0.0%` | 1976 | 1653 | `+0.0s` |
| `2026-10-05 17:57:50` | `8.33%` | `0.0%` | 1945 | 1629 | `+0.0s` |
| `2026-10-05 17:20:41` | `8.56%` | `0.0%` | 1881 | 1525 | `+0.0s` |
| `2026-10-05 16:34:19` | `9.38%` | `0.0%` | 1866 | 1452 | `+0.0s` |
| `2026-10-05 12:15:28` | `6.56%` | `0.0%` | 2422 | 1818 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T06:42:13.210719+00:00`.*
