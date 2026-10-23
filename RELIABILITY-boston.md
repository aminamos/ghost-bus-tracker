# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:21.755000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`80.39%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `102` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `17` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `82` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 82 | 80.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 10 | 9.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route Boat-Lynn** | 10 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78853217` | Route 220 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853134` | Route 220 | `24:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853096` | Route 220 | `05:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853131` | Route 220 | `23:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853201` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853187` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853253` | Route 220 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853195` | Route 220 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853116` | Route 220 | `15:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853130` | Route 220 | `22:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853233` | Route 220 | `19:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853183` | Route 220 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853249` | Route 220 | `23:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853247` | Route 220 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853223` | Route 220 | `16:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:21` | `80.39%` | `0.0%` | 102 | 17 | `+0.0s` |
| `2026-10-23 06:30:20` | `92.41%` | `0.0%` | 395 | 22 | `+0.0s` |
| `2026-10-23 06:00:19` | `89.37%` | `0.0%` | 414 | 31 | `+0.0s` |
| `2026-10-23 05:30:19` | `74.04%` | `0.0%` | 497 | 104 | `+0.0s` |
| `2026-10-23 05:15:26` | `65.54%` | `0.0%` | 563 | 152 | `+0.0s` |
| `2026-10-23 05:00:36` | `56.79%` | `0.0%` | 641 | 201 | `+0.0s` |
| `2026-10-23 04:30:33` | `41.2%` | `0.0%` | 864 | 277 | `+0.0s` |
| `2026-10-23 04:00:37` | `35.57%` | `0.0%` | 998 | 297 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:21.755000+00:00`.*
