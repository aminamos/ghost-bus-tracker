# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:17.851000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`23.08%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `65` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `48` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `15` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 15 | 23.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 18 | 6 | 12 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 5 | 1 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 14 | 14 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `881925891` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298592 is missing from active GPS transponder fleet |
| `881925901` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298593 is missing from active GPS transponder fleet |
| `881925221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298594 is missing from active GPS transponder fleet |
| `851804231` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298558 is missing from active GPS transponder fleet |
| `867187601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298557 is missing from active GPS transponder fleet |
| `851804721` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298550 is missing from active GPS transponder fleet |
| `851804791` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298550 is missing from active GPS transponder fleet |
| `851805201` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298548 is missing from active GPS transponder fleet |
| `851804811` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8298549 is missing from active GPS transponder fleet |
| `851804801` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298549 is missing from active GPS transponder fleet |
| `3292010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41516 is broadcasting off-schedule with no vehicle covering 3292010 |
| `3275010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41506 is broadcasting off-schedule with no vehicle covering 3275010 |
| `3875010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41509 is broadcasting off-schedule with no vehicle covering 3875010 |
| `1065010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9721 is broadcasting off-schedule with no vehicle covering 1065010 |
| `3936010` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9212 is broadcasting off-schedule with no vehicle covering 3936010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:17` | `23.08%` | `0.0%` | 65 | 48 | `+0.0s` |
| `2026-11-27 06:30:17` | `17.14%` | `0.0%` | 70 | 55 | `+0.0s` |
| `2026-11-27 06:00:17` | `15.07%` | `0.0%` | 73 | 54 | `+0.0s` |
| `2026-11-27 05:30:17` | `10.39%` | `0.0%` | 77 | 60 | `+0.0s` |
| `2026-11-27 05:00:17` | `19.23%` | `0.0%` | 78 | 59 | `+0.0s` |
| `2026-11-27 04:30:17` | `11.63%` | `0.0%` | 86 | 65 | `+0.0s` |
| `2026-11-27 04:00:17` | `14.12%` | `0.0%` | 85 | 66 | `+0.0s` |
| `2026-11-27 03:30:17` | `12.63%` | `0.0%` | 95 | 76 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:17.851000+00:00`.*
