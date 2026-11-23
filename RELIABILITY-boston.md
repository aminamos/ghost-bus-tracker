# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:17.823000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`80.38%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `158` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `31` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `127` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 127 | 80.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 742** | 125 | 0 | 125 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 2 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 216** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78590744` | Route 742 | `17:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590890` | Route 742 | `22:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590812` | Route 742 | `21:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590714` | Route 742 | `08:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590720` | Route 742 | `17:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590902` | Route 742 | `23:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590820` | Route 742 | `20:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590702` | Route 742 | `09:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590866` | Route 742 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591211` | Route 742 | `16:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591851` | Route 742 | `05:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590803` | Route 742 | `18:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590833` | Route 742 | `15:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78590761` | Route 742 | `16:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78591861` | Route 742 | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:17` | `80.38%` | `0.0%` | 158 | 31 | `+0.0s` |
| `2026-11-23 06:30:17` | `56.14%` | `0.0%` | 228 | 74 | `+0.0s` |
| `2026-11-23 06:00:18` | `35.81%` | `0.0%` | 363 | 174 | `+0.0s` |
| `2026-11-23 05:30:17` | `22.42%` | `0.0%` | 553 | 246 | `+0.0s` |
| `2026-11-23 05:00:17` | `17.62%` | `0.0%` | 698 | 271 | `+0.0s` |
| `2026-11-23 04:30:18` | `16.38%` | `0.0%` | 745 | 280 | `+0.0s` |
| `2026-11-23 04:00:18` | `16.2%` | `0.0%` | 753 | 285 | `+0.0s` |
| `2026-11-23 03:30:17` | `19.65%` | `0.0%` | 789 | 312 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:17.823000+00:00`.*
