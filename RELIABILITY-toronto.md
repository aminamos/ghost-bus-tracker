# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-01T07:00:17.936000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.14%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `221` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `742` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 8.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 312** | 3 | 3 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 315** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 343** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 353** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 341** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 396** | 3 | 5 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 316** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 339** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `19685070` | Route 316 | `N/A` | `SCHEDULED` | Assigned vehicle 3327 is broadcasting off-schedule with no vehicle covering 19685070 |
| `112073070` | Route 353 | `N/A` | `SCHEDULED` | Assigned vehicle 7083 is broadcasting off-schedule with no vehicle covering 112073070 |
| `47284070` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9445 is broadcasting off-schedule with no vehicle covering 47284070 |
| `89968070` | Route 320 | `N/A` | `SCHEDULED` | Assigned vehicle 7071 is broadcasting off-schedule with no vehicle covering 89968070 |
| `124224070` | Route 341 | `N/A` | `SCHEDULED` | Assigned vehicle 7233 is broadcasting off-schedule with no vehicle covering 124224070 |
| `86263070` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4483 is broadcasting off-schedule with no vehicle covering 86263070 |
| `79286070` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4459 is broadcasting off-schedule with no vehicle covering 79286070 |
| `25497070` | Route 337 | `N/A` | `SCHEDULED` | Assigned vehicle 8143 is broadcasting off-schedule with no vehicle covering 25497070 |
| `17773070` | Route 353 | `N/A` | `SCHEDULED` | Assigned vehicle 3174 is broadcasting off-schedule with no vehicle covering 17773070 |
| `94361070` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 9201 is broadcasting off-schedule with no vehicle covering 94361070 |
| `109089070` | Route 396 | `N/A` | `SCHEDULED` | Assigned vehicle 3629 is broadcasting off-schedule with no vehicle covering 109089070 |
| `29691070` | Route 322 | `N/A` | `SCHEDULED` | Assigned vehicle 8510 is broadcasting off-schedule with no vehicle covering 29691070 |
| `10697070` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8792 is broadcasting off-schedule with no vehicle covering 10697070 |
| `104826070` | Route 315 | `N/A` | `SCHEDULED` | Assigned vehicle 8336 is broadcasting off-schedule with no vehicle covering 104826070 |
| `58638070` | Route 339 | `N/A` | `SCHEDULED` | Assigned vehicle 3132 is broadcasting off-schedule with no vehicle covering 58638070 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:17` | `8.14%` | `0.0%` | 221 | 742 | `+0.0s` |
| `2026-11-01 06:30:18` | `4.08%` | `0.0%` | 343 | 820 | `+0.0s` |
| `2026-11-01 06:00:18` | `7.6%` | `0.0%` | 526 | 943 | `+0.0s` |
| `2026-11-01 05:30:18` | `6.19%` | `0.0%` | 727 | 1062 | `+0.0s` |
| `2026-11-01 05:00:18` | `8.99%` | `0.0%` | 945 | 1064 | `+0.0s` |
| `2026-11-01 04:30:18` | `7.01%` | `0.0%` | 1084 | 1043 | `+0.0s` |
| `2026-11-01 04:00:17` | `8.12%` | `0.0%` | 1120 | 1036 | `+0.0s` |
| `2026-11-01 03:30:17` | `4.9%` | `0.0%` | 1143 | 1072 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:17.936000+00:00`.*
