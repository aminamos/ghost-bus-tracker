# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:20.725000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`56.1%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `41` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `23` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 23 | 56.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GREEN LATE NIGHT** | 7 | 2 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT** | 5 | 3 | 4 | **`80.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER LATE NIGHT** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING** | 18 | 7 | 7 | **`38.89%`** | `0.0%` | `+0.0s` |

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
| `[@7.0.41950648@][1244056065453]/246__I7_UIF_LATE` | Route ILLINI EVENING | `01:50:00` | `SCHEDULED` | Assigned vehicle 2364 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/246__I7_UIF_LATE |
| `[@14.0.56288930@][4][1310416578748]/0__GN7_UIF` | Route GREEN LATE NIGHT | `02:33:00` | `SCHEDULED` | Assigned vehicle 2439 is broadcasting off-schedule with no vehicle covering [@14.0.56288930@][4][1310416578748]/0__GN7_UIF |
| `[@7.0.41950648@][1244056065453]/118__I7_UIF_LATE` | Route ILLINI EVENING | `02:25:00` | `SCHEDULED` | Assigned vehicle 2364 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/118__I7_UIF_LATE |
| `[@124.0.94416648@][2][1497378263893]/1__Y2_UI_MF` | Route YELLOW LATE NIGHT | `02:34:00` | `SCHEDULED` | Assigned vehicle 2425 is broadcasting off-schedule with no vehicle covering [@124.0.94416648@][2][1497378263893]/1__Y2_UI_MF |
| `[@7.0.41950648@][1244056065453]/247__I8_UIF_LATE` | Route ILLINI EVENING | `02:00:00` | `SCHEDULED` | Assigned vehicle 2017 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/247__I8_UIF_LATE |
| `[@7.0.41905826@][4][1246487009734]/14__T2_UIMF` | Route TEAL LATE NIGHT | `01:56:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@7.0.41905826@][4][1246487009734]/14__T2_UIMF |
| `[@124.0.94416648@][2][1497378133653]/0__Y5_UIMF` | Route YELLOW LATE NIGHT | `02:04:00` | `SCHEDULED` | Assigned vehicle 1724 is broadcasting off-schedule with no vehicle covering [@124.0.94416648@][2][1497378133653]/0__Y5_UIMF |
| `[@12.0.42230752@][3][1246897512562]/8__SV4_SCH_UIF` | Route SILVER LATE NIGHT | `02:46:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][3][1246897512562]/8__SV4_SCH_UIF |
| `[@7.0.41905826@][3][1246486974015]/6__T2_UIMF` | Route TEAL LATE NIGHT | `02:15:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@7.0.41905826@][3][1246486974015]/6__T2_UIMF |
| `[@14.0.56288930@][3][1310416762630]/0__GN7_UIF` | Route GREEN LATE NIGHT | `02:46:00` | `SCHEDULED` | Assigned vehicle 2439 is broadcasting off-schedule with no vehicle covering [@14.0.56288930@][3][1310416762630]/0__GN7_UIF |
| `[@6.0.14328542@][2][1623952601601]/0__I2_UIF_LATE` | Route ILLINI EVENING | `02:40:00` | `SCHEDULED` | Assigned vehicle 2262 is broadcasting off-schedule with no vehicle covering [@6.0.14328542@][2][1623952601601]/0__I2_UIF_LATE |
| `[@12.0.42230752@][4][1246897581031]/21__SV4_SCH_UIF` | Route SILVER LATE NIGHT | `02:25:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][4][1246897581031]/21__SV4_SCH_UIF |
| `[@7.0.38112640@][3][1219153537453]/5__GR3_UI` | Route GREEN LATE NIGHT | `02:40:00` | `SCHEDULED` | Assigned vehicle 2645 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153537453]/5__GR3_UI |
| `[@12.0.42230752@][3][1246897512562]/6__SV4_SCH_UIF` | Route SILVER LATE NIGHT | `02:06:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][3][1246897512562]/6__SV4_SCH_UIF |
| `[@7.0.38114521@][1][1214492709250]/6__Y5_UIMF` | Route YELLOW LATE NIGHT | `02:30:00` | `SCHEDULED` | Assigned vehicle 1724 is broadcasting off-schedule with no vehicle covering [@7.0.38114521@][1][1214492709250]/6__Y5_UIMF |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:20` | `56.1%` | `0.0%` | 41 | 15 | `+0.0s` |
| `2026-10-31 06:30:18` | `18.75%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-10-31 06:00:19` | `29.79%` | `0.0%` | 47 | 18 | `+0.0s` |
| `2026-10-31 05:30:18` | `20.83%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-10-31 05:00:21` | `42.22%` | `0.0%` | 45 | 17 | `+0.0s` |
| `2026-10-31 04:30:20` | `19.64%` | `0.0%` | 56 | 25 | `+0.0s` |
| `2026-10-31 04:00:17` | `27.87%` | `0.0%` | 61 | 29 | `+0.0s` |
| `2026-10-31 03:30:17` | `29.69%` | `0.0%` | 64 | 29 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:20.725000+00:00`.*
