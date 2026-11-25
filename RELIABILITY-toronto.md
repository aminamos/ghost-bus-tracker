# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-25T07:00:18.474000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.2%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `558` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1107` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `29` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 29 | 5.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 70** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 168** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 900** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 373** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 396** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 315** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `33114020` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7097 is broadcasting off-schedule with no vehicle covering 33114020 |
| `67227020` | Route 168 | `N/A` | `SCHEDULED` | Assigned vehicle 7279 is broadcasting off-schedule with no vehicle covering 67227020 |
| `36540020` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3262 is broadcasting off-schedule with no vehicle covering 36540020 |
| `26944020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3272 is broadcasting off-schedule with no vehicle covering 26944020 |
| `65345020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3615 is broadcasting off-schedule with no vehicle covering 65345020 |
| `69272020` | Route 310 | `N/A` | `SCHEDULED` | Assigned vehicle 4493 is broadcasting off-schedule with no vehicle covering 69272020 |
| `75378020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 3567 is broadcasting off-schedule with no vehicle covering 75378020 |
| `32959020` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8851 is broadcasting off-schedule with no vehicle covering 32959020 |
| `32095020` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 6139 is broadcasting off-schedule with no vehicle covering 32095020 |
| `11040020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3615 is broadcasting off-schedule with no vehicle covering 11040020 |
| `96253020` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 7254 is broadcasting off-schedule with no vehicle covering 96253020 |
| `33781020` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3215 is broadcasting off-schedule with no vehicle covering 33781020 |
| `43639020` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7042 is broadcasting off-schedule with no vehicle covering 43639020 |
| `101032020` | Route 27 | `N/A` | `SCHEDULED` | Assigned vehicle 7330 is broadcasting off-schedule with no vehicle covering 101032020 |
| `2328020` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 8726 is broadcasting off-schedule with no vehicle covering 2328020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `5.2%` | `0.0%` | 558 | 1107 | `+0.0s` |
| `2026-11-25 06:30:18` | `8.78%` | `0.0%` | 763 | 1147 | `+0.0s` |
| `2026-11-25 06:00:18` | `7.77%` | `0.0%` | 991 | 1182 | `+0.0s` |
| `2026-11-25 05:30:18` | `7.64%` | `0.0%` | 1112 | 1191 | `+0.0s` |
| `2026-11-25 05:00:17` | `8.94%` | `0.0%` | 1141 | 1190 | `+0.0s` |
| `2026-11-25 04:30:17` | `6.8%` | `0.0%` | 1162 | 1242 | `+0.0s` |
| `2026-11-25 04:00:18` | `7.71%` | `0.0%` | 1194 | 1348 | `+0.0s` |
| `2026-11-25 03:30:19` | `6.97%` | `0.0%` | 1276 | 1446 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.474000+00:00`.*
