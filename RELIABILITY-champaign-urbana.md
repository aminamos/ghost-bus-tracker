# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-13T07:00:19.486000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.04%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 13.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route YELLOW LATE NIGHT** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER LATE NIGHT** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route GREEN LATE NIGHT** | 7 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING** | 18 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `[@12.0.42230752@][4][1246897581031]/19__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `01:45:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][4][1246897581031]/19__SV4_SCH_UIMTH |
| `[@7.0.38114521@][2][1214492894609]/13__Y2_UI_MF` | Route YELLOW LATE NIGHT | `01:31:00` | `SCHEDULED` | Assigned vehicle 2426 is broadcasting off-schedule with no vehicle covering [@7.0.38114521@][2][1214492894609]/13__Y2_UI_MF |
| `[@12.0.42230752@][4][1246897567828]/17__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `01:05:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering [@12.0.42230752@][4][1246897567828]/17__SV4_SCH_UIMTH |
| `[@6.0.51701618@][1][1716488446871]/2__SV4_SCH_UIMTH` | Route SILVER LATE NIGHT | `01:26:00` | `SCHEDULED` | Assigned vehicle 2366 is broadcasting off-schedule with no vehicle covering [@6.0.51701618@][1][1716488446871]/2__SV4_SCH_UIMTH |
| `[@7.0.38114521@][1][1214492461671]/4__Y2_UI_MF` | Route YELLOW LATE NIGHT | `02:00:00` | `SCHEDULED` | Assigned vehicle 2426 is broadcasting off-schedule with no vehicle covering [@7.0.38114521@][1][1214492461671]/4__Y2_UI_MF |
| `[@7.0.38114521@][1][1214492461671]/2__Y2_UI_MF` | Route YELLOW LATE NIGHT | `01:00:00` | `SCHEDULED` | Assigned vehicle 2426 is broadcasting off-schedule with no vehicle covering [@7.0.38114521@][1][1214492461671]/2__Y2_UI_MF |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:19` | `13.04%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-11-13 06:30:18` | `4.17%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-11-13 06:00:20` | `17.78%` | `0.0%` | 45 | 15 | `+0.0s` |
| `2026-11-13 05:30:18` | `3.57%` | `0.0%` | 56 | 25 | `+0.0s` |
| `2026-11-13 05:00:18` | `16.67%` | `0.0%` | 60 | 28 | `+0.0s` |
| `2026-11-13 04:30:18` | `7.46%` | `0.0%` | 67 | 30 | `+0.0s` |
| `2026-11-13 04:00:19` | `25.0%` | `0.0%` | 72 | 30 | `+0.0s` |
| `2026-11-13 03:30:18` | `7.35%` | `0.0%` | 68 | 30 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:19.486000+00:00`.*
