# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:23.451000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `434` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `421` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+63.0s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 421 | 97.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5801** | 110 | 0 | 110 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `-26.0s` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 61 | 1 | 59 | **`96.72%`** | `50.0%` | `+2.5 min` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | `+2.5 min (+152.0s)` | `+5.1 min (+304s)` | 1 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | ~20.0m | ~20.0m | **`+0.0 min`** | `87.3 / 100` |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200262` | Route 5795 | `13:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200200` | Route 5794 | `13:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200208` | Route 5794 | `15:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200230` | Route 5794 | `24:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200203` | Route 5794 | `14:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200213` | Route 5794 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200267` | Route 5795 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200195` | Route 5794 | `12:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200202` | Route 5794 | `14:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200224` | Route 5794 | `21:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200227` | Route 5794 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200257` | Route 5795 | `11:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200186` | Route 5794 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200193` | Route 5794 | `11:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200176` | Route 5794 | `07:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:23` | `97.0%` | `75.0%` | 434 | 11 | `+63.0s` |
| `2026-11-13 06:30:19` | `88.98%` | `86.67%` | 472 | 50 | `-15.0s` |
| `2026-11-13 05:30:19` | `80.96%` | `92.93%` | 520 | 87 | `+40.7s` |
| `2026-11-13 05:00:22` | `10.48%` | `94.51%` | 105 | 91 | `+29.6s` |
| `2026-11-13 04:30:18` | `15.32%` | `100.0%` | 111 | 92 | `+22.6s` |
| `2026-11-13 04:00:20` | `19.33%` | `100.0%` | 119 | 94 | `+41.3s` |
| `2026-11-13 03:30:19` | `21.54%` | `0.0%` | 130 | 98 | `+0.0s` |
| `2026-11-13 03:00:21` | `23.13%` | `0.0%` | 147 | 108 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:23.451000+00:00`.*
