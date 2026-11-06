# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:17.880000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`72.41%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `116` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `31` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `84` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 84 | 72.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78853179` | Route 220 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:17` | `72.41%` | `0.0%` | 116 | 31 | `+0.0s` |
| `2026-11-06 06:30:18` | `41.41%` | `0.0%` | 198 | 106 | `+0.0s` |
| `2026-11-06 06:00:18` | `22.01%` | `0.0%` | 359 | 208 | `+0.0s` |
| `2026-11-06 05:30:18` | `13.54%` | `0.0%` | 576 | 274 | `+0.0s` |
| `2026-11-06 05:00:18` | `10.71%` | `0.0%` | 728 | 300 | `+0.0s` |
| `2026-11-06 04:30:19` | `9.81%` | `0.0%` | 785 | 326 | `+0.0s` |
| `2026-11-06 04:00:19` | `10.64%` | `0.0%` | 818 | 352 | `+0.0s` |
| `2026-11-06 03:30:18` | `23.97%` | `0.0%` | 951 | 373 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:17.880000+00:00`.*
