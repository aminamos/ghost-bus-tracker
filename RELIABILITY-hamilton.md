# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:22.512000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`94.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `264` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `12` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `250` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-21.5s` (`-0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-21.5s` (`-0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 250 | 94.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `-21.5s` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200174` | Route 5794 | `07:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200181` | Route 5794 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200211` | Route 5794 | `16:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200190` | Route 5794 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200218` | Route 5794 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200221` | Route 5794 | `19:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200203` | Route 5794 | `14:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200213` | Route 5794 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200216` | Route 5794 | `17:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200176` | Route 5794 | `07:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200183` | Route 5794 | `09:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200170` | Route 5794 | `06:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200197` | Route 5794 | `12:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200205` | Route 5794 | `14:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200186` | Route 5794 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:22` | `94.7%` | `100.0%` | 264 | 12 | `-21.5s` |
| `2026-11-17 06:30:19` | `83.11%` | `100.0%` | 302 | 49 | `+4.8s` |
| `2026-11-17 06:00:21` | `75.38%` | `92.31%` | 329 | 76 | `-11.9s` |
| `2026-11-17 05:30:20` | `72.17%` | `95.24%` | 345 | 87 | `-1.0s` |
| `2026-11-17 05:00:18` | `5.1%` | `100.0%` | 98 | 91 | `+54.6s` |
| `2026-11-17 04:30:19` | `8.82%` | `100.0%` | 102 | 92 | `+63.2s` |
| `2026-11-17 04:00:18` | `12.15%` | `91.67%` | 107 | 94 | `+59.6s` |
| `2026-11-17 03:30:23` | `12.93%` | `92.31%` | 116 | 98 | `+64.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:22.512000+00:00`.*
