# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-30T07:00:21.790000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`47.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `36` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `17` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 17 | 47.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route YELLOW LATE NIGHT** | 4 | 2 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT** | 5 | 1 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER LATE NIGHT** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route GREEN LATE NIGHT** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING** | 14 | 7 | 4 | **`28.57%`** | `0.0%` | `+0.0s` |

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
| `[@6.0.14328542@][2][1623952601601]/0__I2_UI_MTH` | Route ILLINI EVENING | `02:40:00` | `SCHEDULED` | Assigned vehicle 2103 is broadcasting off-schedule with no vehicle covering [@6.0.14328542@][2][1623952601601]/0__I2_UI_MTH |
| `[@7.0.38114521@][1][1214492461671]/4__Y2_UI_MF` | Route YELLOW LATE NIGHT | `02:00:00` | `SCHEDULED` | Assigned vehicle 1726 is broadcasting off-schedule with no vehicle covering [@7.0.38114521@][1][1214492461671]/4__Y2_UI_MF |
| `[@12.0.42230752@][4][1246897581031]/21__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `02:25:00` | `SCHEDULED` | Assigned vehicle 2017 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][4][1246897581031]/21__SV4_SCH_UIMTH |
| `[@124.0.94416648@][2][1497378263893]/1__Y2_UI_MF` | Route YELLOW LATE NIGHT | `02:34:00` | `SCHEDULED` | Assigned vehicle 1726 is broadcasting off-schedule with no vehicle covering [@124.0.94416648@][2][1497378263893]/1__Y2_UI_MF |
| `[@7.0.38112640@][4][1217017960328]/1__GR3_UI` | Route GREEN LATE NIGHT | `02:23:00` | `SCHEDULED` | Assigned vehicle 2148 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][4][1217017960328]/1__GR3_UI |
| `[@7.0.41950648@][1244056065453]/119__I8_UIMTH_LATE` | Route ILLINI EVENING | `02:35:00` | `SCHEDULED` | Assigned vehicle 2105 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/119__I8_UIMTH_LATE |
| `[@7.0.41950648@][1244056065453]/116__I2_UI_MTH` | Route ILLINI EVENING | `02:05:00` | `SCHEDULED` | Assigned vehicle 2103 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/116__I2_UI_MTH |
| `[@12.0.42230752@][3][1246897512562]/8__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `02:46:00` | `SCHEDULED` | Assigned vehicle 2017 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][3][1246897512562]/8__SV4_SCH_UIMTH |
| `[@7.0.41905826@][4][1246487009734]/15__T1_UIMTH` | Route TEAL LATE NIGHT | `02:16:00` | `SCHEDULED` | Assigned vehicle 2365 is missing from active GPS transponder fleet |
| `[@124.0.94416648@][2][1497378133653]/0__Y5_UIMF` | Route YELLOW LATE NIGHT | `02:04:00` | `SCHEDULED` | Assigned vehicle 2041 is broadcasting off-schedule with no vehicle covering [@124.0.94416648@][2][1497378133653]/0__Y5_UIMF |
| `[@7.0.38112640@][3][1219153537453]/5__GR3_UI` | Route GREEN LATE NIGHT | `02:40:00` | `SCHEDULED` | Assigned vehicle 2148 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153537453]/5__GR3_UI |
| `[@12.0.42230752@][3][1246897512562]/6__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `02:06:00` | `SCHEDULED` | Assigned vehicle 2017 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][3][1246897512562]/6__SV4_SCH_UIMTH |
| `[@7.0.41905826@][3][1246486974015]/5__T1_UIMTH` | Route TEAL LATE NIGHT | `01:55:00` | `SCHEDULED` | Assigned vehicle 2365 is missing from active GPS transponder fleet |
| `[@7.0.38112640@][3][1219153533843]/4__GR3_UI` | Route GREEN LATE NIGHT | `02:00:00` | `SCHEDULED` | Assigned vehicle 2148 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153533843]/4__GR3_UI |
| `[@7.0.41905826@][3][1246486974015]/7__T1_UIMTH` | Route TEAL LATE NIGHT | `02:35:00` | `SCHEDULED` | Assigned vehicle 2365 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 07:00:21` | `47.22%` | `0.0%` | 36 | 14 | `+0.0s` |
| `2026-10-30 06:30:19` | `10.42%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-10-30 06:00:20` | `11.9%` | `0.0%` | 42 | 14 | `+0.0s` |
| `2026-10-30 05:30:20` | `4.35%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-10-30 05:00:19` | `28.89%` | `0.0%` | 45 | 14 | `+0.0s` |
| `2026-10-30 04:30:18` | `16.36%` | `0.0%` | 55 | 23 | `+0.0s` |
| `2026-10-30 04:00:19` | `20.0%` | `0.0%` | 60 | 29 | `+0.0s` |
| `2026-10-30 03:30:18` | `17.91%` | `0.0%` | 67 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:21.790000+00:00`.*
