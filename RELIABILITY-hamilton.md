# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:18.620000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`91.78%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `146` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `134` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+270.5s` (`+4.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+270.5s` (`+4.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 134 | 91.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 37 | 1 | 36 | **`97.3%`** | `0.0%` | `+5.3 min` |
| **Route 5783** | 61 | 2 | 59 | **`96.72%`** | `0.0%` | `+0.0s` |
| **Route 5793** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+5.3 min (+321.0s)` | `+5.3 min (+321s)` | 1 | `0.0%` |
| **Route 5795** | `+3.7 min (+220.0s)` | `+3.7 min (+220s)` | 1 | `100.0%` |

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
| `2199318` | Route 5813 | `25:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193835` | Route 5794 | `22:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193838` | Route 5794 | `21:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193841` | Route 5794 | `19:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193844` | Route 5794 | `18:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193847` | Route 5794 | `16:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193850` | Route 5794 | `15:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193853` | Route 5794 | `13:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193856` | Route 5794 | `12:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193859` | Route 5794 | `10:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193862` | Route 5794 | `09:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193865` | Route 5794 | `07:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193868` | Route 5794 | `06:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193834` | Route 5794 | `23:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:18` | `91.78%` | `50.0%` | 146 | 13 | `+270.5s` |
| `2026-11-22 06:30:18` | `78.03%` | `66.67%` | 173 | 40 | `+149.3s` |
| `2026-11-22 06:00:17` | `65.69%` | `100.0%` | 204 | 70 | `+34.6s` |
| `2026-11-22 05:00:18` | `4.35%` | `81.82%` | 92 | 88 | `+137.5s` |
| `2026-11-22 04:30:18` | `8.0%` | `76.92%` | 100 | 94 | `+258.0s` |
| `2026-11-22 04:00:18` | `7.84%` | `92.31%` | 102 | 94 | `+88.2s` |
| `2026-11-22 03:30:20` | `10.38%` | `90.91%` | 106 | 95 | `+110.5s` |
| `2026-11-22 03:00:18` | `12.17%` | `91.67%` | 115 | 101 | `+128.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:18.620000+00:00`.*
