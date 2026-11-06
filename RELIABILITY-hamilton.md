# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:18.222000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.05%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `253` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `9` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `243` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+38.5s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+38.5s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 243 | 96.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `+0.6 min` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+0.6 min (+38.5s)` | `+1.3 min (+77s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200280` | Route 5795 | `18:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200273` | Route 5795 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200278` | Route 5795 | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200251` | Route 5795 | `09:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200268` | Route 5795 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200243` | Route 5795 | `07:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200275` | Route 5795 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200246` | Route 5795 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200240` | Route 5795 | `06:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200242` | Route 5795 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200271` | Route 5795 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200292` | Route 5795 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200289` | Route 5795 | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200244` | Route 5795 | `07:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200284` | Route 5795 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `96.05%` | `100.0%` | 253 | 9 | `+38.5s` |
| `2026-11-06 06:30:19` | `82.59%` | `83.33%` | 293 | 50 | `+76.2s` |
| `2026-11-06 06:00:18` | `73.77%` | `88.89%` | 324 | 78 | `-11.4s` |
| `2026-11-06 05:30:20` | `70.12%` | `100.0%` | 338 | 88 | `+12.1s` |
| `2026-11-06 05:00:19` | `6.06%` | `100.0%` | 99 | 91 | `+8.9s` |
| `2026-11-06 04:30:19` | `8.82%` | `100.0%` | 102 | 92 | `+36.8s` |
| `2026-11-06 04:00:24` | `11.11%` | `82.35%` | 108 | 93 | `+70.6s` |
| `2026-11-06 03:30:21` | `12.39%` | `88.64%` | 113 | 98 | `+79.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.222000+00:00`.*
