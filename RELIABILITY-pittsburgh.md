# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Pittsburgh Regional Transit** in **Pittsburgh, PA** (Pittsburgh Metropolitan Area, Pennsylvania).
> **Transit System:** PRT | **Location:** Pittsburgh, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-16T04:30:18.424000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `77` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `126` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 28X** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route P1** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61B** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 71A** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 86** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 83** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `7622010` | Route 16 | `N/A` | `SCHEDULED` | Assigned vehicle 6210 is broadcasting off-schedule with no vehicle covering 7622010 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 04:30:18` | `1.3%` | `0.0%` | 77 | 126 | `+0.0s` |
| `2026-11-16 04:00:18` | `4.82%` | `0.0%` | 83 | 129 | `+0.0s` |
| `2026-11-16 03:30:17` | `4.95%` | `0.0%` | 101 | 167 | `+0.0s` |
| `2026-11-16 02:30:18` | `4.92%` | `0.0%` | 122 | 154 | `+0.0s` |
| `2026-11-16 01:00:18` | `2.16%` | `0.0%` | 139 | 166 | `+0.0s` |
| `2026-11-16 00:30:18` | `2.58%` | `0.0%` | 155 | 178 | `+0.0s` |
| `2026-11-15 23:30:18` | `1.94%` | `0.0%` | 155 | 191 | `+0.0s` |
| `2026-11-15 23:00:17` | `3.59%` | `0.0%` | 167 | 212 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T04:30:18.424000+00:00`.*
