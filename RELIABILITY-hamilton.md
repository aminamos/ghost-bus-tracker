# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:20.072000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.26%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `211` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `9` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `201` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+26.3s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 1.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 201 | 95.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5823** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 77 | 2 | 75 | **`97.4%`** | `100.0%` | `+0.0s` |
| **Route 5782** | 56 | 1 | 54 | **`96.43%`** | `100.0%` | `+0.7 min` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+0.7 min (+39.5s)` | `+1.3 min (+79s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2199660` | Route 5823 | `15:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2199662` | Route 5823 | `15:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200232` | Route 5794 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200233` | Route 5794 | `09:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2199663` | Route 5823 | `06:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200202` | Route 5794 | `14:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200210` | Route 5794 | `16:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200176` | Route 5794 | `07:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200183` | Route 5794 | `09:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200203` | Route 5794 | `14:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200211` | Route 5794 | `16:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200174` | Route 5794 | `07:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200181` | Route 5794 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200188` | Route 5794 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200195` | Route 5794 | `12:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:20` | `95.26%` | `100.0%` | 211 | 9 | `+26.3s` |
| `2026-11-27 06:30:20` | `79.45%` | `83.33%` | 253 | 49 | `-53.7s` |
| `2026-11-27 06:00:18` | `70.71%` | `91.67%` | 280 | 77 | `+63.0s` |
| `2026-11-27 05:30:20` | `69.62%` | `83.33%` | 293 | 86 | `+257.4s` |
| `2026-11-27 05:00:17` | `8.25%` | `83.33%` | 97 | 90 | `+38.5s` |
| `2026-11-27 04:30:20` | `10.78%` | `71.43%` | 102 | 91 | `+347.4s` |
| `2026-11-27 04:00:17` | `11.11%` | `90.91%` | 108 | 94 | `+164.5s` |
| `2026-11-27 03:30:20` | `13.79%` | `100.0%` | 116 | 99 | `+48.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:20.072000+00:00`.*
