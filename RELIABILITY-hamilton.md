# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:19.672000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `252` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `12` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `241` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+161.0s` (`+2.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+161.0s` (`+2.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 241 | 95.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 97 | 1 | 96 | **`98.97%`** | `100.0%` | `+2.3 min` |
| **Route 5795** | 40 | 1 | 39 | **`97.5%`** | `100.0%` | `+3.0 min` |
| **Route 5783** | 68 | 2 | 66 | **`97.06%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | `+3.0 min (+182.0s)` | `+3.0 min (+182s)` | 1 | `100.0%` |
| **Route 5782** | `+2.3 min (+140.0s)` | `+2.3 min (+140s)` | 1 | `100.0%` |

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
| `2199317` | Route 5813 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194045` | Route 5795 | `15:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194041` | Route 5795 | `13:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194056` | Route 5795 | `20:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194073` | Route 5795 | `18:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194047` | Route 5795 | `17:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194052` | Route 5795 | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194051` | Route 5795 | `07:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194066` | Route 5795 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194062` | Route 5795 | `24:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194058` | Route 5795 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194059` | Route 5795 | `05:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194060` | Route 5795 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194040` | Route 5795 | `10:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193763` | Route 5794 | `20:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `95.63%` | `100.0%` | 252 | 12 | `+161.0s` |
| `2026-11-14 06:30:22` | `83.16%` | `66.67%` | 291 | 51 | `+59.7s` |
| `2026-11-14 06:00:21` | `76.34%` | `89.33%` | 317 | 75 | `+18.9s` |
| `2026-11-14 05:30:18` | `73.87%` | `90.7%` | 333 | 85 | `+27.9s` |
| `2026-11-14 05:00:27` | `8.91%` | `100.0%` | 101 | 89 | `+25.2s` |
| `2026-11-14 04:30:18` | `14.15%` | `100.0%` | 106 | 90 | `+46.0s` |
| `2026-11-14 04:00:22` | `15.79%` | `100.0%` | 114 | 93 | `+58.1s` |
| `2026-11-14 03:30:18` | `19.35%` | `94.44%` | 124 | 98 | `+64.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.672000+00:00`.*
