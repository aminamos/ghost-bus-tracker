# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.081000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.91%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `67` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `53` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 17.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 19 | 10 | 9 | **`47.37%`** | `0.0%` | `+0.0s` |
| **Route 100236** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 14 | 14 | 2 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 560** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 12 | 12 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 578** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 4 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `881956891` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9687 is broadcasting off-schedule with no vehicle covering 881956891 |
| `2295020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9723 is broadcasting off-schedule with no vehicle covering 2295020 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2055` | Route 100479 | `10:59:30` | `DUPLICATED` | Assigned vehicle 521.797301 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2055 |
| `LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2055` | Route 100479 | `10:59:30` | `DUPLICATED` | Assigned vehicle 528.457928 is broadcasting off-schedule with no vehicle covering LLR_2026-10-19_20260903_Link_Fall26PHActive_Weekday_100479_2055 |
| `3660020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 51402 is broadcasting off-schedule with no vehicle covering 3660020 |
| `3010020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9203 is broadcasting off-schedule with no vehicle covering 3010020 |
| `79020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9213 is broadcasting off-schedule with no vehicle covering 79020 |
| `881956901` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298754 is missing from active GPS transponder fleet |
| `881957561` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298755 is missing from active GPS transponder fleet |
| `851857161` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298729 is missing from active GPS transponder fleet |
| `851857221` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8298706 is missing from active GPS transponder fleet |
| `559501081` | Route 100236 | `N/A` | `SCHEDULED` | Assigned vehicle 8298707 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `17.91%` | `0.0%` | 67 | 53 | `+0.0s` |
| `2026-11-25 06:30:18` | `20.78%` | `0.0%` | 77 | 59 | `+0.0s` |
| `2026-11-25 05:30:18` | `20.43%` | `0.0%` | 93 | 72 | `+0.0s` |
| `2026-11-25 05:00:17` | `26.53%` | `0.0%` | 98 | 72 | `+0.0s` |
| `2026-11-25 04:30:17` | `23.85%` | `0.0%` | 109 | 87 | `+0.0s` |
| `2026-11-25 03:30:18` | `26.23%` | `0.0%` | 122 | 99 | `+0.0s` |
| `2026-11-25 02:30:18` | `31.45%` | `0.0%` | 159 | 123 | `+0.0s` |
| `2026-11-25 02:00:17` | `20.11%` | `0.0%` | 179 | 142 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.081000+00:00`.*
