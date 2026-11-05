# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-05T07:00:17.848000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `45` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 4.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route ILLINI EVENING** | 17 | 7 | 2 | **`11.76%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route GREEN LATE NIGHT** | 6 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER LATE NIGHT** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT** | 6 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `[@7.0.41950648@][1244056065453]/241__I1_UI_MTH_LATE` | Route ILLINI EVENING | `01:00:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/241__I1_UI_MTH_LATE |
| `[@7.0.41950648@][1244056065453]/113__I1_UI_MTH_LATE` | Route ILLINI EVENING | `01:35:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/113__I1_UI_MTH_LATE |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:17` | `4.44%` | `0.0%` | 45 | 15 | `+0.0s` |
| `2026-11-05 06:30:17` | `4.35%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-11-05 06:00:17` | `17.78%` | `0.0%` | 45 | 15 | `+0.0s` |
| `2026-11-05 05:30:18` | `5.36%` | `0.0%` | 56 | 25 | `+0.0s` |
| `2026-11-05 05:00:17` | `10.0%` | `0.0%` | 60 | 28 | `+0.0s` |
| `2026-11-05 04:30:18` | `9.09%` | `0.0%` | 66 | 29 | `+0.0s` |
| `2026-11-05 03:30:18` | `2.82%` | `0.0%` | 71 | 31 | `+0.0s` |
| `2026-11-05 03:00:17` | `18.57%` | `0.0%` | 70 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.848000+00:00`.*
