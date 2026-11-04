# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Pittsburgh Regional Transit** in **Pittsburgh, PA** (Pittsburgh Metropolitan Area, Pennsylvania).
> **Transit System:** PRT | **Location:** Pittsburgh, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T06:00:18.348000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `50` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `197` | GPS transponders broadcasting valid coordinates |
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
| **Route 71A** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 61A** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 54** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61B** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61C** | 5 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61D** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71B** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71C** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route P1** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `11707020` | Route 71A | `N/A` | `SCHEDULED` | Assigned vehicle 6828 is broadcasting off-schedule with no vehicle covering 11707020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 06:00:18` | `2.0%` | `0.0%` | 50 | 197 | `+0.0s` |
| `2026-11-04 05:30:17` | `5.26%` | `0.0%` | 76 | 192 | `+0.0s` |
| `2026-11-04 05:00:17` | `1.83%` | `0.0%` | 109 | 160 | `+0.0s` |
| `2026-11-04 04:30:17` | `4.8%` | `0.0%` | 125 | 186 | `+0.0s` |
| `2026-11-04 02:30:18` | `5.26%` | `0.0%` | 190 | 250 | `+0.0s` |
| `2026-11-04 02:00:18` | `3.0%` | `0.0%` | 200 | 245 | `+0.0s` |
| `2026-11-04 01:30:18` | `1.48%` | `0.0%` | 203 | 247 | `+0.0s` |
| `2026-11-04 01:00:18` | `2.24%` | `0.0%` | 223 | 259 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T06:00:18.348000+00:00`.*
