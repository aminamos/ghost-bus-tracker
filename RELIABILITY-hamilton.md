# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-19T07:00:19.963000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.51%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `481` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `10` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `469` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+44.0s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+44.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 469 | 97.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5801** | 96 | 0 | 96 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5807** | 65 | 1 | 64 | **`98.46%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `+0.7 min` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+0.7 min (+44.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200165` | Route 5794 | `25:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200230` | Route 5794 | `24:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200148` | Route 5794 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200211` | Route 5794 | `16:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200140` | Route 5794 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200142` | Route 5794 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200205` | Route 5794 | `14:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200134` | Route 5794 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200218` | Route 5794 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200147` | Route 5794 | `17:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200210` | Route 5794 | `16:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200139` | Route 5794 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200111` | Route 5794 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200183` | Route 5794 | `09:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200113` | Route 5794 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 07:00:19` | `97.51%` | `100.0%` | 481 | 10 | `+44.0s` |
| `2026-11-19 06:30:19` | `90.0%` | `100.0%` | 520 | 48 | `+15.0s` |
| `2026-11-19 06:00:20` | `83.7%` | `92.31%` | 552 | 76 | `+8.8s` |
| `2026-11-19 05:30:25` | `81.4%` | `100.0%` | 570 | 86 | `+3.3s` |
| `2026-11-19 05:00:18` | `8.82%` | `90.0%` | 102 | 90 | `+8.3s` |
| `2026-11-19 04:30:19` | `13.89%` | `90.0%` | 108 | 91 | `+71.5s` |
| `2026-11-19 04:00:21` | `16.52%` | `91.67%` | 115 | 93 | `+60.1s` |
| `2026-11-19 03:30:18` | `18.7%` | `100.0%` | 123 | 95 | `+17.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:19.963000+00:00`.*
