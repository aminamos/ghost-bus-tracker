# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-15T07:00:19.113000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.06%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `530` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `904` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 48 | 9.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 151** | 3 | 1 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 44** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 106** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 339** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 352** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 65** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 84** | 6 | 5 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 70** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `38605070` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3129 is broadcasting off-schedule with no vehicle covering 38605070 |
| `68942070` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 3365 is broadcasting off-schedule with no vehicle covering 68942070 |
| `31985070` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3212 is broadcasting off-schedule with no vehicle covering 31985070 |
| `48957070` | Route 51 | `N/A` | `SCHEDULED` | Assigned vehicle 8691 is broadcasting off-schedule with no vehicle covering 48957070 |
| `12892070` | Route 70 | `N/A` | `SCHEDULED` | Assigned vehicle 8520 is broadcasting off-schedule with no vehicle covering 12892070 |
| `48799070` | Route 151 | `N/A` | `SCHEDULED` | Assigned vehicle 3178 is broadcasting off-schedule with no vehicle covering 48799070 |
| `71216070` | Route 106 | `N/A` | `SCHEDULED` | Assigned vehicle 7082 is broadcasting off-schedule with no vehicle covering 71216070 |
| `77919070` | Route 304 | `N/A` | `SCHEDULED` | Assigned vehicle 4451 is broadcasting off-schedule with no vehicle covering 77919070 |
| `9157070` | Route 503 | `N/A` | `SCHEDULED` | Assigned vehicle 8774 is broadcasting off-schedule with no vehicle covering 9157070 |
| `54732070` | Route 129 | `N/A` | `SCHEDULED` | Assigned vehicle 3161 is broadcasting off-schedule with no vehicle covering 54732070 |
| `58852070` | Route 165 | `N/A` | `SCHEDULED` | Assigned vehicle 3608 is broadcasting off-schedule with no vehicle covering 58852070 |
| `28383070` | Route 53 | `N/A` | `SCHEDULED` | Assigned vehicle 3144 is broadcasting off-schedule with no vehicle covering 28383070 |
| `7915070` | Route 151 | `N/A` | `SCHEDULED` | Assigned vehicle 3178 is broadcasting off-schedule with no vehicle covering 7915070 |
| `17528070` | Route 84 | `N/A` | `SCHEDULED` | Assigned vehicle 8922 is broadcasting off-schedule with no vehicle covering 17528070 |
| `67504070` | Route 102 | `N/A` | `SCHEDULED` | Assigned vehicle 8728 is broadcasting off-schedule with no vehicle covering 67504070 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:19` | `9.06%` | `0.0%` | 530 | 904 | `+0.0s` |
| `2026-11-15 06:30:18` | `8.12%` | `0.0%` | 727 | 969 | `+0.0s` |
| `2026-11-15 06:00:20` | `7.75%` | `0.0%` | 968 | 994 | `+0.0s` |
| `2026-11-15 05:30:18` | `6.96%` | `0.0%` | 1107 | 1003 | `+0.0s` |
| `2026-11-15 05:00:18` | `6.51%` | `0.0%` | 1121 | 1014 | `+0.0s` |
| `2026-11-15 04:30:18` | `6.0%` | `0.0%` | 1134 | 1045 | `+0.0s` |
| `2026-11-15 04:00:18` | `6.74%` | `0.0%` | 1142 | 1142 | `+0.0s` |
| `2026-11-15 03:30:18` | `6.87%` | `0.0%` | 1237 | 1211 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.113000+00:00`.*
