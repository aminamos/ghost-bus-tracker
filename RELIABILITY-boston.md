# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-22T07:00:17.877000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.59%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `63` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `62` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 3.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 116** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 7 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Red** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 110** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78533113` | Route 116 | `25:35:00` | `SCHEDULED` | Assigned vehicle y3335 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:17` | `1.59%` | `0.0%` | 63 | 62 | `+0.0s` |
| `2026-11-22 06:30:17` | `3.47%` | `0.0%` | 173 | 128 | `+0.0s` |
| `2026-11-22 06:00:17` | `0.6%` | `0.0%` | 334 | 230 | `+0.0s` |
| `2026-11-22 05:30:20` | `0.39%` | `0.0%` | 513 | 281 | `+0.0s` |
| `2026-11-22 05:00:18` | `0.32%` | `0.0%` | 627 | 299 | `+0.0s` |
| `2026-11-22 04:30:17` | `1.06%` | `0.0%` | 663 | 306 | `+0.0s` |
| `2026-11-22 04:00:17` | `3.36%` | `0.0%` | 684 | 316 | `+0.0s` |
| `2026-11-22 03:30:18` | `4.85%` | `0.0%` | 701 | 340 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:17.877000+00:00`.*
