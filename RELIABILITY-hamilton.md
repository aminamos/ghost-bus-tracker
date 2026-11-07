# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:19.666000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.26%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `211` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `201` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+175.0s` (`+2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+175.0s` (`+2.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 201 | 95.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5795** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 97 | 1 | 96 | **`98.97%`** | `100.0%` | `+2.9 min` |
| **Route 5783** | 68 | 2 | 66 | **`97.06%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+2.9 min (+175.0s)` | `+2.9 min (+175s)` | 1 | `100.0%` |

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
| `2194069` | Route 5795 | `12:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194060` | Route 5795 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194047` | Route 5795 | `17:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194041` | Route 5795 | `13:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194052` | Route 5795 | `15:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194077` | Route 5795 | `11:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194063` | Route 5795 | `09:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194075` | Route 5795 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194070` | Route 5795 | `06:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194062` | Route 5795 | `24:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194058` | Route 5795 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194067` | Route 5795 | `21:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194054` | Route 5795 | `19:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194049` | Route 5795 | `16:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194046` | Route 5795 | `11:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:19` | `95.26%` | `100.0%` | 211 | 11 | `+175.0s` |
| `2026-11-07 06:30:19` | `80.4%` | `100.0%` | 250 | 51 | `+42.6s` |
| `2026-11-07 06:00:20` | `72.14%` | `85.71%` | 280 | 77 | `-3.6s` |
| `2026-11-07 05:30:19` | `69.15%` | `92.86%` | 295 | 88 | `+31.2s` |
| `2026-11-07 05:00:18` | `6.93%` | `91.67%` | 101 | 91 | `+22.2s` |
| `2026-11-07 04:30:19` | `10.38%` | `100.0%` | 106 | 92 | `+53.0s` |
| `2026-11-07 04:00:23` | `12.5%` | `79.59%` | 112 | 94 | `+104.4s` |
| `2026-11-07 03:30:22` | `15.57%` | `92.23%` | 122 | 100 | `+83.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:19.666000+00:00`.*
