# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-25T07:00:18.926000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.93%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `214` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `201` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+100.0s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+71.0s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 1.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 201 | 93.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 56 | 1 | 54 | **`96.43%`** | `100.0%` | `+1.9 min` |
| **Route 5828** | 5 | 1 | 4 | **`80.0%`** | `100.0%` | `+1.2 min` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+1.9 min (+114.5s)` | `+3.8 min (+229s)` | 1 | `100.0%` |
| **Route 5828** | `+1.2 min (+71.0s)` | `+1.2 min (+71s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `90.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2203491` | Route 5828 | `14:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2203470` | Route 5828 | `11:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2203453` | Route 5828 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2203432` | Route 5828 | `07:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200233` | Route 5794 | `09:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200232` | Route 5794 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200218` | Route 5794 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200213` | Route 5794 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200205` | Route 5794 | `14:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200211` | Route 5794 | `16:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200203` | Route 5794 | `14:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200230` | Route 5794 | `24:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200227` | Route 5794 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200224` | Route 5794 | `21:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200221` | Route 5794 | `19:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `93.93%` | `100.0%` | 214 | 11 | `+100.0s` |
| `2026-11-25 06:30:19` | `79.53%` | `75.0%` | 254 | 50 | `-37.1s` |
| `2026-11-25 06:00:19` | `70.67%` | `91.67%` | 283 | 78 | `+54.2s` |
| `2026-11-25 05:30:18` | `67.46%` | `89.47%` | 295 | 87 | `-13.4s` |
| `2026-11-25 05:00:18` | `7.14%` | `90.0%` | 98 | 90 | `+42.7s` |
| `2026-11-25 04:30:18` | `9.8%` | `100.0%` | 102 | 91 | `+20.1s` |
| `2026-11-25 04:00:18` | `12.38%` | `90.91%` | 105 | 91 | `+83.0s` |
| `2026-11-25 03:00:23` | `15.62%` | `76.92%` | 128 | 107 | `+61.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.926000+00:00`.*
