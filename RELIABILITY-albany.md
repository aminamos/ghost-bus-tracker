# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital District Transportation Authority** in **Albany, NY** (Capital District, New York).
> **Transit System:** CDTA | **Location:** Albany, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T06:00:19.021000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`40.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `15` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `12` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 40.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 452** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 910** | 6 | 3 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 905** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `13999260-OCT26-AlbRMB-Weekday-10` | Route 910 | `01:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `13999245-OCT26-AlbRMB-Weekday-10` | Route 910 | `01:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `13984160-OCT26-Sara-Weekday-10-0001100` | Route 452 | `01:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `13984161-OCT26-Sara-Weekday-10-0001100` | Route 452 | `01:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `13999257-OCT26-AlbRMB-Weekday-10-0000100` | Route 910 | `02:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `13998359-OCT26-AlbRMB-Weekday-10` | Route 1 | `01:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 06:00:19` | `40.0%` | `0.0%` | 15 | 12 | `+0.0s` |
| `2026-11-14 05:30:18` | `46.15%` | `0.0%` | 26 | 18 | `+0.0s` |
| `2026-11-14 04:30:18` | `23.75%` | `0.0%` | 80 | 51 | `+0.0s` |
| `2026-11-14 03:30:18` | `25.0%` | `0.0%` | 120 | 63 | `+0.0s` |
| `2026-11-14 03:00:18` | `18.05%` | `0.0%` | 133 | 68 | `+0.0s` |
| `2026-11-14 01:00:18` | `10.17%` | `0.0%` | 177 | 101 | `+0.0s` |
| `2026-11-14 00:30:18` | `20.11%` | `0.0%` | 189 | 106 | `+0.0s` |
| `2026-11-14 00:00:17` | `15.69%` | `0.0%` | 204 | 122 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T06:00:19.021000+00:00`.*
