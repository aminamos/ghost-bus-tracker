# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-25T07:00:20.815000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.84%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `282` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `705` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `8` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 8 | 2.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 329** | 4 | 4 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 312** | 2 | 3 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 343** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 336** | 9 | 8 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route 307** | 10 | 7 | 1 | **`10.0%`** | `0.0%` | `+0.0s` |
| **Route 334** | 15 | 11 | 1 | **`6.67%`** | `0.0%` | `+0.0s` |
| **Route 300** | 15 | 13 | 1 | **`6.67%`** | `0.0%` | `+0.0s` |
| **Route 316** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 386** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 301** | 20 | 15 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `86208070` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9465 is broadcasting off-schedule with no vehicle covering 86208070 |
| `90636070` | Route 312 | `N/A` | `SCHEDULED` | Assigned vehicle 4623 is broadcasting off-schedule with no vehicle covering 90636070 |
| `97204070` | Route 307 | `N/A` | `SCHEDULED` | Assigned vehicle 3520 is broadcasting off-schedule with no vehicle covering 97204070 |
| `4941070` | Route 329 | `N/A` | `SCHEDULED` | Assigned vehicle 9446 is broadcasting off-schedule with no vehicle covering 4941070 |
| `94361070` | Route 343 | `N/A` | `SCHEDULED` | Assigned vehicle 3212 is broadcasting off-schedule with no vehicle covering 94361070 |
| `10697070` | Route 334 | `N/A` | `SCHEDULED` | Assigned vehicle 8760 is broadcasting off-schedule with no vehicle covering 10697070 |
| `70827070` | Route 300 | `N/A` | `SCHEDULED` | Assigned vehicle 8203 is broadcasting off-schedule with no vehicle covering 70827070 |
| `130305070` | Route 336 | `N/A` | `SCHEDULED` | Assigned vehicle 3209 is broadcasting off-schedule with no vehicle covering 130305070 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 07:00:20` | `2.84%` | `0.0%` | 282 | 705 | `+0.0s` |
| `2026-10-25 06:30:19` | `3.29%` | `0.0%` | 365 | 821 | `+0.0s` |
| `2026-10-25 06:15:45` | `8.88%` | `0.0%` | 428 | 882 | `+0.0s` |
| `2026-10-25 06:00:56` | `8.74%` | `0.0%` | 538 | 943 | `+0.0s` |
| `2026-10-25 05:30:19` | `8.06%` | `0.0%` | 732 | 999 | `+0.0s` |
| `2026-10-25 05:00:19` | `8.46%` | `0.0%` | 981 | 997 | `+0.0s` |
| `2026-10-25 04:33:52` | `7.23%` | `0.0%` | 1148 | 1003 | `+0.0s` |
| `2026-10-25 04:00:21` | `6.47%` | `0.0%` | 1144 | 1043 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T07:00:20.815000+00:00`.*
