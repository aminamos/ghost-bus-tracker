# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:18.489000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`33.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `36` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 33.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route SILVER LATE NIGHT** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route GREEN LATE NIGHT** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING** | 14 | 6 | 4 | **`28.57%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT** | 5 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `[@12.0.42230752@][4][1246897581031]/21__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `02:25:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][4][1246897581031]/21__SV4_SCH_UIMTH |
| `[@12.0.42230752@][3][1246897512562]/8__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `02:46:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][3][1246897512562]/8__SV4_SCH_UIMTH |
| `[@7.0.41950648@][1244056065453]/248__I1_UI_MTH_LATE` | Route ILLINI EVENING | `02:10:00` | `SCHEDULED` | Assigned vehicle 2260 is missing from active GPS transponder fleet |
| `[@12.0.42230752@][3][1246897512562]/6__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `02:06:00` | `SCHEDULED` | Assigned vehicle 2104 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][3][1246897512562]/6__SV4_SCH_UIMTH |
| `[@124.0.94416648@][2][1497378133653]/0__Y5_UIMF` | Route YELLOW LATE NIGHT | `02:04:00` | `SCHEDULED` | Assigned vehicle 1836 is broadcasting off-schedule with no vehicle covering [@124.0.94416648@][2][1497378133653]/0__Y5_UIMF |
| `[@7.0.41950648@][1244056065453]/119__I8_UIMTH_LATE` | Route ILLINI EVENING | `02:35:00` | `SCHEDULED` | Assigned vehicle 2105 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/119__I8_UIMTH_LATE |
| `[@7.0.38112640@][3][1219153533843]/4__GR3_UI` | Route GREEN LATE NIGHT | `02:00:00` | `SCHEDULED` | Assigned vehicle 2435 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153533843]/4__GR3_UI |
| `[@7.0.38114521@][1][1214492709250]/6__Y5_UIMF` | Route YELLOW LATE NIGHT | `02:30:00` | `SCHEDULED` | Assigned vehicle 1836 is broadcasting off-schedule with no vehicle covering [@7.0.38114521@][1][1214492709250]/6__Y5_UIMF |
| `[@7.0.38112640@][3][1219153537453]/5__GR3_UI` | Route GREEN LATE NIGHT | `02:40:00` | `SCHEDULED` | Assigned vehicle 2435 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][3][1219153537453]/5__GR3_UI |
| `[@7.0.41950648@][1244056065453]/113__I1_UI_MTH_LATE` | Route ILLINI EVENING | `01:35:00` | `SCHEDULED` | Assigned vehicle 2260 is missing from active GPS transponder fleet |
| `[@7.0.38112640@][4][1217017960328]/1__GR3_UI` | Route GREEN LATE NIGHT | `02:23:00` | `SCHEDULED` | Assigned vehicle 2435 is broadcasting off-schedule with no vehicle covering [@7.0.38112640@][4][1217017960328]/1__GR3_UI |
| `[@7.0.41950648@][1244056065453]/247__I8_UIMTH_LATE` | Route ILLINI EVENING | `02:00:00` | `SCHEDULED` | Assigned vehicle 2105 is broadcasting off-schedule with no vehicle covering [@7.0.41950648@][1244056065453]/247__I8_UIMTH_LATE |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `33.33%` | `0.0%` | 36 | 14 | `+0.0s` |
| `2026-10-29 06:30:19` | `6.25%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-10-29 06:00:19` | `15.22%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-10-29 05:30:18` | `4.17%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-10-29 03:30:18` | `3.12%` | `0.0%` | 64 | 29 | `+0.0s` |
| `2026-10-29 03:00:18` | `16.42%` | `0.0%` | 67 | 29 | `+0.0s` |
| `2026-10-29 02:30:18` | `13.89%` | `0.0%` | 72 | 30 | `+0.0s` |
| `2026-10-29 02:00:19` | `16.9%` | `0.0%` | 71 | 32 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.489000+00:00`.*
