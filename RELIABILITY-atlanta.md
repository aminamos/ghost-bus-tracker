# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T13:46:38.647844+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.35%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `443` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `174` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `37` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 37 | 8.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 143 | 32.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 21** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 34** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 95** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 187** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 162** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 22** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 11** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 118** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `11721753` | Route 95 | `09:56:00` | `SCHEDULED` | Assigned vehicle 2325 is broadcasting off-schedule with no vehicle covering 11721753 |
| `11704829` | Route 26 | `09:45:00` | `SCHEDULED` | Assigned vehicle 2355 is broadcasting off-schedule with no vehicle covering 11704829 |
| `11697186` | Route 5 | `09:58:00` | `SCHEDULED` | Assigned vehicle 2381 is broadcasting off-schedule with no vehicle covering 11697186 |
| `11706646` | Route 39 | `09:45:00` | `SCHEDULED` | Assigned vehicle 2416 is broadcasting off-schedule with no vehicle covering 11706646 |
| `11715123` | Route 78 | `09:55:00` | `SCHEDULED` | Assigned vehicle 3507 is broadcasting off-schedule with no vehicle covering 11715123 |
| `11708701` | Route 49 | `09:45:00` | `SCHEDULED` | Assigned vehicle 3512 is broadcasting off-schedule with no vehicle covering 11708701 |
| `11736574` | Route 193 | `09:55:00` | `SCHEDULED` | Assigned vehicle 3513 is broadcasting off-schedule with no vehicle covering 11736574 |
| `11720753` | Route 89 | `09:49:00` | `SCHEDULED` | Assigned vehicle 3532 is broadcasting off-schedule with no vehicle covering 11720753 |
| `11735286` | Route 187 | `09:48:00` | `SCHEDULED` | Assigned vehicle 3537 is broadcasting off-schedule with no vehicle covering 11735286 |
| `11733651` | Route 180 | `09:45:00` | `SCHEDULED` | Assigned vehicle 3571 is broadcasting off-schedule with no vehicle covering 11733651 |
| `11732012` | Route 162 | `09:57:00` | `SCHEDULED` | Assigned vehicle 3588 is broadcasting off-schedule with no vehicle covering 11732012 |
| `11707264` | Route 42 | `09:45:00` | `SCHEDULED` | Assigned vehicle 3593 is broadcasting off-schedule with no vehicle covering 11707264 |
| `11718836` | Route 85 | `09:53:00` | `SCHEDULED` | Assigned vehicle 3606 is broadcasting off-schedule with no vehicle covering 11718836 |
| `11719405` | Route 87 | `09:55:00` | `SCHEDULED` | Assigned vehicle 3611 is broadcasting off-schedule with no vehicle covering 11719405 |
| `11710370` | Route 55 | `09:57:00` | `SCHEDULED` | Assigned vehicle 3625 is broadcasting off-schedule with no vehicle covering 11710370 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 13:46:38` | `8.35%` | `0.0%` | 443 | 174 | `+0.0s` |
| `2026-10-06 06:42:12` | `0.0%` | `0.0%` | 6 | 5 | `+0.0s` |
| `2026-10-06 00:28:48` | `12.35%` | `0.0%` | 332 | 165 | `+0.0s` |
| `2026-10-05 18:39:13` | `6.9%` | `0.0%` | 290 | 170 | `+0.0s` |
| `2026-10-05 18:02:21` | `9.06%` | `0.0%` | 320 | 180 | `+0.0s` |
| `2026-10-05 17:57:50` | `9.26%` | `0.0%` | 324 | 177 | `+0.0s` |
| `2026-10-05 17:20:40` | `9.46%` | `0.0%` | 349 | 176 | `+0.0s` |
| `2026-10-05 16:34:19` | `6.72%` | `0.0%` | 372 | 172 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T13:46:38.647844+00:00`.*
