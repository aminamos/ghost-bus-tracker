# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-07T07:00:18.089000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `63` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 8 | 12.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 19 | 10 | 8 | **`42.11%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 11 | 11 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 512** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 10 | 10 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41501 is broadcasting off-schedule with no vehicle covering 3010020 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9715 is broadcasting off-schedule with no vehicle covering 2295020 |
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9125 is broadcasting off-schedule with no vehicle covering 79020 |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273975 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8273952 is missing from active GPS transponder fleet |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51401 is broadcasting off-schedule with no vehicle covering 3660020 |
| `3912020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9201 is broadcasting off-schedule with no vehicle covering 3912020 |
| `17068831__H:121:0:Weekday:3:26SEP:52057:12345` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:3:26SEP:52057:12345 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:18` | `12.7%` | `0.0%` | 63 | 52 | `+0.0s` |
| `2026-11-07 06:30:18` | `20.59%` | `0.0%` | 68 | 58 | `+0.0s` |
| `2026-11-07 06:00:18` | `16.67%` | `0.0%` | 90 | 69 | `+0.0s` |
| `2026-11-07 05:30:18` | `18.56%` | `0.0%` | 97 | 74 | `+0.0s` |
| `2026-11-07 05:00:17` | `22.22%` | `0.0%` | 108 | 84 | `+0.0s` |
| `2026-11-07 04:30:17` | `22.31%` | `0.0%` | 121 | 85 | `+0.0s` |
| `2026-11-07 04:00:18` | `14.84%` | `0.0%` | 128 | 93 | `+0.0s` |
| `2026-11-07 02:30:19` | `24.56%` | `0.0%` | 171 | 132 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.089000+00:00`.*
