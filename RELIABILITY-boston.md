# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T12:15:24.608477+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1731` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `808` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `178` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 178 | 10.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 18 | 1.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 68 | 5 | 61 | **`89.71%`** | `0.0%` | `+0.0s` |
| **Route 116** | 110 | 15 | 85 | **`77.27%`** | `0.0%` | `+0.0s` |
| **Route 436** | 15 | 3 | 11 | **`73.33%`** | `0.0%` | `+0.0s` |
| **Route Boat-F10** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 222** | 6 | 3 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 465** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 713** | 6 | 2 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 226** | 6 | 2 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 429** | 6 | 4 | 1 | **`16.67%`** | `0.0%` | `+0.0s` |
| **Route 238** | 7 | 4 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |

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
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517176` | Route 116 | `13:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516460` | Route 116 | `21:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517232` | Route 116 | `13:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517207` | Route 116 | `15:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516641` | Route 116 | `20:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517234` | Route 116 | `15:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516450` | Route 116 | `23:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517231` | Route 116 | `11:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516473` | Route 116 | `11:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854550` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854570` | Route 220 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 12:15:24` | `10.28%` | `0.0%` | 1731 | 808 | `+0.0s` |
| `2026-10-05 12:14:27` | `10.27%` | `0.0%` | 1724 | 808 | `+0.0s` |
| `2026-10-05 12:05:46` | `9.89%` | `0.0%` | 1779 | 815 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T12:15:24.608477+00:00`.*
