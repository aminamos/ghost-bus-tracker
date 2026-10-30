# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Pittsburgh Regional Transit** in **Pittsburgh, PA** (Pittsburgh Metropolitan Area, Pennsylvania).
> **Transit System:** PRT | **Location:** Pittsburgh, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-30T05:00:18.989000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `50` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `203` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 71A** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 61A** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 54** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61B** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71D** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61C** | 5 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61D** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71B** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71C** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `11707020` | Route 71A | `N/A` | `SCHEDULED` | Assigned vehicle 6731 is broadcasting off-schedule with no vehicle covering 11707020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 05:00:18` | `2.0%` | `0.0%` | 50 | 203 | `+0.0s` |
| `2026-10-30 04:30:18` | `4.0%` | `0.0%` | 75 | 178 | `+0.0s` |
| `2026-10-30 03:30:18` | `3.88%` | `0.0%` | 129 | 180 | `+0.0s` |
| `2026-10-30 02:00:18` | `1.69%` | `0.0%` | 177 | 237 | `+0.0s` |
| `2026-10-30 01:00:18` | `1.57%` | `0.0%` | 191 | 254 | `+0.0s` |
| `2026-10-29 23:30:18` | `2.85%` | `0.0%` | 246 | 302 | `+0.0s` |
| `2026-10-29 23:00:18` | `1.89%` | `0.0%` | 264 | 344 | `+0.0s` |
| `2026-10-29 22:30:18` | `3.58%` | `0.0%` | 307 | 390 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T05:00:18.989000+00:00`.*
