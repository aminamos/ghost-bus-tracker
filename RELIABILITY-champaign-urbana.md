# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** MTD | **Location:** Champaign–Urbana, IL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-08T07:00:17.800000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.35%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 4.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route ILLINI EVENING SATURDAY** | 18 | 7 | 2 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route SILVER EVENING SATURDAY** | 7 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route TEAL LATE NIGHT SATURDAY** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route GREEN LATE NIGHT SATURDAY** | 7 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW LATE NIGHT SATURDAY** | 6 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `[@124.0.92260187@][1484328831455]/175__I7_UISA` | Route ILLINI EVENING SATURDAY | `01:00:00` | `SCHEDULED` | Assigned vehicle 2105 is broadcasting off-schedule with no vehicle covering [@124.0.92260187@][1484328831455]/175__I7_UISA |
| `[@124.0.92260187@][1484328831455]/286__I7_UISA` | Route ILLINI EVENING SATURDAY | `01:35:00` | `SCHEDULED` | Assigned vehicle 2105 is broadcasting off-schedule with no vehicle covering [@124.0.92260187@][1484328831455]/286__I7_UISA |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:17` | `4.35%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-11-08 06:30:18` | `8.7%` | `0.0%` | 46 | 15 | `+0.0s` |
| `2026-11-08 06:00:17` | `17.78%` | `0.0%` | 45 | 17 | `+0.0s` |
| `2026-11-08 05:00:18` | `14.29%` | `0.0%` | 56 | 27 | `+0.0s` |
| `2026-11-08 04:30:20` | `9.23%` | `0.0%` | 65 | 28 | `+0.0s` |
| `2026-11-08 04:00:18` | `17.65%` | `0.0%` | 68 | 28 | `+0.0s` |
| `2026-11-08 03:30:18` | `8.96%` | `0.0%` | 67 | 28 | `+0.0s` |
| `2026-11-08 03:00:17` | `19.12%` | `0.0%` | 68 | 28 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:17.800000+00:00`.*
