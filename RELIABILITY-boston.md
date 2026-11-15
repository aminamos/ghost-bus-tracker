# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:17.937000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`60.16%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `128` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `81` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `77` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 77 | 60.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 74 | 0 | 74 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 741** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 2 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route Orange** | 7 | 5 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 110** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 743** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78851624` | Route 220 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851525` | Route 220 | `23:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851505` | Route 220 | `13:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851510` | Route 220 | `16:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78205896` | Route 741 | `25:40:00` | `SCHEDULED` | Assigned vehicle y1333 is missing from active GPS transponder fleet |
| `78851526` | Route 220 | `24:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851598` | Route 220 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851568` | Route 220 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851509` | Route 220 | `15:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851498` | Route 220 | `10:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851636` | Route 220 | `24:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851616` | Route 220 | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851513` | Route 220 | `17:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851519` | Route 220 | `20:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78851523` | Route 220 | `22:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:17` | `60.16%` | `0.0%` | 128 | 81 | `+0.0s` |
| `2026-11-15 06:30:17` | `37.14%` | `0.0%` | 210 | 136 | `+0.0s` |
| `2026-11-15 06:00:19` | `20.87%` | `0.0%` | 369 | 232 | `+0.0s` |
| `2026-11-15 05:30:18` | `13.31%` | `0.0%` | 556 | 281 | `+0.0s` |
| `2026-11-15 05:00:18` | `10.7%` | `0.0%` | 673 | 302 | `+0.0s` |
| `2026-11-15 04:30:18` | `11.16%` | `0.0%` | 699 | 310 | `+0.0s` |
| `2026-11-15 04:00:18` | `12.02%` | `0.0%` | 724 | 322 | `+0.0s` |
| `2026-11-15 03:30:18` | `13.24%` | `0.0%` | 740 | 331 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:17.937000+00:00`.*
