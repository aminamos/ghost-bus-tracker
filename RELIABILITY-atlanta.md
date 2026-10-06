# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T00:28:48.465577+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.35%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `332` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `165` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `41` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 41 | 12.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 59 | 17.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 5 | 4 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route 49** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 119** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 115** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 4** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 71** | 7 | 3 | 2 | **`28.57%`** | `0.0%` | `+0.0s` |
| **Route 116** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `11725820` | Route 116 | `20:35:00` | `SCHEDULED` | Assigned vehicle 2318 is broadcasting off-schedule with no vehicle covering 11725820 |
| `11697158` | Route 5 | `20:25:00` | `SCHEDULED` | Assigned vehicle 2350 is broadcasting off-schedule with no vehicle covering 11697158 |
| `11698862` | Route 11 | `20:39:00` | `SCHEDULED` | Assigned vehicle 2376 is broadcasting off-schedule with no vehicle covering 11698862 |
| `11706689` | Route 39 | `20:31:00` | `SCHEDULED` | Assigned vehicle 2434 is broadcasting off-schedule with no vehicle covering 11706689 |
| `11708717` | Route 49 | `20:30:00` | `SCHEDULED` | Assigned vehicle 3513 is broadcasting off-schedule with no vehicle covering 11708717 |
| `11722563` | Route 96 | `20:30:00` | `SCHEDULED` | Assigned vehicle 3532 is broadcasting off-schedule with no vehicle covering 11722563 |
| `11718403` | Route 84 | `20:40:00` | `SCHEDULED` | Assigned vehicle 3541 is broadcasting off-schedule with no vehicle covering 11718403 |
| `11708745` | Route 49 | `20:49:00` | `SCHEDULED` | Assigned vehicle 3562 is broadcasting off-schedule with no vehicle covering 11708745 |
| `11715166` | Route 78 | `20:40:00` | `SCHEDULED` | Assigned vehicle 3565 is broadcasting off-schedule with no vehicle covering 11715166 |
| `11720723` | Route 89 | `20:35:00` | `SCHEDULED` | Assigned vehicle 3575 is broadcasting off-schedule with no vehicle covering 11720723 |
| `11720783` | Route 89 | `20:32:00` | `SCHEDULED` | Assigned vehicle 3577 is broadcasting off-schedule with no vehicle covering 11720783 |
| `11720704` | Route 89 | `20:30:00` | `SCHEDULED` | Assigned vehicle 3581 is broadcasting off-schedule with no vehicle covering 11720704 |
| `11707324` | Route 42 | `20:30:00` | `SCHEDULED` | Assigned vehicle 3589 is broadcasting off-schedule with no vehicle covering 11707324 |
| `11734463` | Route 184 | `20:30:00` | `SCHEDULED` | Assigned vehicle 3593 is broadcasting off-schedule with no vehicle covering 11734463 |
| `11721795` | Route 95 | `20:25:00` | `SCHEDULED` | Assigned vehicle 3621 is broadcasting off-schedule with no vehicle covering 11721795 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 00:28:48` | `12.35%` | `0.0%` | 332 | 165 | `+0.0s` |
| `2026-10-05 18:39:13` | `6.9%` | `0.0%` | 290 | 170 | `+0.0s` |
| `2026-10-05 18:02:21` | `9.06%` | `0.0%` | 320 | 180 | `+0.0s` |
| `2026-10-05 17:57:50` | `9.26%` | `0.0%` | 324 | 177 | `+0.0s` |
| `2026-10-05 17:20:40` | `9.46%` | `0.0%` | 349 | 176 | `+0.0s` |
| `2026-10-05 16:34:19` | `6.72%` | `0.0%` | 372 | 172 | `+0.0s` |
| `2026-10-05 12:15:27` | `7.61%` | `0.0%` | 447 | 176 | `+0.0s` |
| `2026-10-05 12:14:31` | `7.4%` | `0.0%` | 446 | 175 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T00:28:48.465577+00:00`.*
