# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:18.264000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.26%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 28.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GREEN LATE NIGHT SATURDAY** | 7 | 2 | 4 | **`57.14%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT SATURDAY** | 8 | 2 | 4 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT SATURDAY** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route ILLINI EVENING SATURDAY** | 18 | 7 | 2 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route SILVER EVENING SATURDAY** | 7 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `[@124.0.92344750@][1484579800344]/2__GN2_UISA` | Route GREEN LATE NIGHT SATURDAY | `01:43:00` | `SCHEDULED` | Assigned vehicle 2149 is broadcasting off-schedule with no vehicle covering [@124.0.92344750@][1484579800344]/2__GN2_UISA |
| `[@124.0.92275054@][1484344751044]/49__T2_UISA` | Route TEAL LATE NIGHT SATURDAY | `01:16:00` | `SCHEDULED` | Assigned vehicle 2420 is broadcasting off-schedule with no vehicle covering [@124.0.92275054@][1484344751044]/49__T2_UISA |
| `[@124.0.92275054@][1484344751044]/83__T2_UISA` | Route TEAL LATE NIGHT SATURDAY | `01:56:00` | `SCHEDULED` | Assigned vehicle 2420 is broadcasting off-schedule with no vehicle covering [@124.0.92275054@][1484344751044]/83__T2_UISA |
| `[@124.0.92275054@][1484344751044]/30__T2_UISA` | Route TEAL LATE NIGHT SATURDAY | `00:55:00` | `SCHEDULED` | Assigned vehicle 2420 is broadcasting off-schedule with no vehicle covering [@124.0.92275054@][1484344751044]/30__T2_UISA |
| `[@124.0.92344750@][1484579800344]/83__GN2_UISA` | Route GREEN LATE NIGHT SATURDAY | `02:00:00` | `SCHEDULED` | Assigned vehicle 2149 is broadcasting off-schedule with no vehicle covering [@124.0.92344750@][1484579800344]/83__GN2_UISA |
| `[@124.0.92260187@][1484328831455]/17__I3UISA` | Route ILLINI EVENING SATURDAY | `01:40:00` | `SCHEDULED` | Assigned vehicle 2019 is broadcasting off-schedule with no vehicle covering [@124.0.92260187@][1484328831455]/17__I3UISA |
| `[@124.0.92260187@][1484328831455]/308__I3UISA` | Route ILLINI EVENING SATURDAY | `01:05:00` | `SCHEDULED` | Assigned vehicle 2019 is broadcasting off-schedule with no vehicle covering [@124.0.92260187@][1484328831455]/308__I3UISA |
| `[@124.0.92327957@][1484578220911]/12__Y2_UI_SA` | Route YELLOW LATE NIGHT SATURDAY | `02:00:00` | `SCHEDULED` | Assigned vehicle 1604 is broadcasting off-schedule with no vehicle covering [@124.0.92327957@][1484578220911]/12__Y2_UI_SA |
| `[@124.0.92344750@][1484579800344]/42__GN2_UISA` | Route GREEN LATE NIGHT SATURDAY | `01:03:00` | `SCHEDULED` | Assigned vehicle 2149 is broadcasting off-schedule with no vehicle covering [@124.0.92344750@][1484579800344]/42__GN2_UISA |
| `[@124.0.92327957@][1484578220911]/20__Y2_UI_SA` | Route YELLOW LATE NIGHT SATURDAY | `01:00:00` | `SCHEDULED` | Assigned vehicle 1604 is broadcasting off-schedule with no vehicle covering [@124.0.92327957@][1484578220911]/20__Y2_UI_SA |
| `[@124.0.92327957@][1484578220911]/63__Y2_UI_SA` | Route YELLOW LATE NIGHT SATURDAY | `01:31:00` | `SCHEDULED` | Assigned vehicle 1604 is broadcasting off-schedule with no vehicle covering [@124.0.92327957@][1484578220911]/63__Y2_UI_SA |
| `[@124.0.92344750@][1484579800344]/65__GN2_UISA` | Route GREEN LATE NIGHT SATURDAY | `01:20:00` | `SCHEDULED` | Assigned vehicle 2149 is broadcasting off-schedule with no vehicle covering [@124.0.92344750@][1484579800344]/65__GN2_UISA |
| `[@124.0.92275054@][1484344751044]/40__T2_UISA` | Route TEAL LATE NIGHT SATURDAY | `01:35:00` | `SCHEDULED` | Assigned vehicle 2420 is broadcasting off-schedule with no vehicle covering [@124.0.92275054@][1484344751044]/40__T2_UISA |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `28.26%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-11-15 06:30:18` | `10.42%` | `0.0%` | 48 | 15 | `+0.0s` |
| `2026-11-15 06:00:20` | `13.04%` | `0.0%` | 46 | 16 | `+0.0s` |
| `2026-11-15 05:30:18` | `0.0%` | `0.0%` | 57 | 23 | `+0.0s` |
| `2026-11-15 05:00:18` | `6.9%` | `0.0%` | 58 | 28 | `+0.0s` |
| `2026-11-15 04:30:18` | `2.99%` | `0.0%` | 67 | 29 | `+0.0s` |
| `2026-11-15 04:00:18` | `15.94%` | `0.0%` | 69 | 29 | `+0.0s` |
| `2026-11-15 03:30:18` | `15.49%` | `0.0%` | 71 | 29 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.264000+00:00`.*
