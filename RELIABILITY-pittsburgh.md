# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Pittsburgh Regional Transit** in **Pittsburgh, PA** (Pittsburgh Metropolitan Area, Pennsylvania).
> **Transit System:** Pittsburgh | **Location:** Pittsburgh, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:39.626000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `382` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `415` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `9` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 9 | 2.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 53L** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 27** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 86** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 29** | 4 | 4 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 71D** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 71A** | 9 | 6 | 1 | **`11.11%`** | `0.0%` | `+0.0s` |
| **Route 24** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 5 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `8958020` | Route 29 | `N/A` | `SCHEDULED` | Assigned vehicle 6518 is broadcasting off-schedule with no vehicle covering 8958020 |
| `2506020` | Route 53L | `N/A` | `SCHEDULED` | Assigned vehicle 6620 is missing from active GPS transponder fleet |
| `13730020` | Route 53L | `N/A` | `SCHEDULED` | Assigned vehicle 6620 is missing from active GPS transponder fleet |
| `5002020` | Route 27 | `N/A` | `SCHEDULED` | Assigned vehicle 6272 is broadcasting off-schedule with no vehicle covering 5002020 |
| `8130020` | Route 86 | `N/A` | `SCHEDULED` | Assigned vehicle 6546 is broadcasting off-schedule with no vehicle covering 8130020 |
| `11612020` | Route 71A | `N/A` | `SCHEDULED` | Assigned vehicle 6023 is broadcasting off-schedule with no vehicle covering 11612020 |
| `11080020` | Route 16 | `N/A` | `SCHEDULED` | Assigned vehicle 6004 is broadcasting off-schedule with no vehicle covering 11080020 |
| `4025020` | Route 71D | `N/A` | `SCHEDULED` | Assigned vehicle 6041 is broadcasting off-schedule with no vehicle covering 4025020 |
| `5274020` | Route 26 | `N/A` | `SCHEDULED` | Assigned vehicle 6231 is broadcasting off-schedule with no vehicle covering 5274020 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:39.626000+00:00`.*
