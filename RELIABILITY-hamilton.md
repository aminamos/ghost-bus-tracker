# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T06:15:48.227000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`98.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `238` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `5` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `235` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+355.0s` (`+5.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+355.0s` (`+5.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 235 | 98.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5783** | 89 | 0 | 89 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 39 | 2 | 37 | **`94.87%`** | `0.0%` | `+5.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5808** | `+5.9 min (+355.0s)` | `+5.9 min (+355s)` | 2 | `0.0%` |

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
| `2198284` | Route 5808 | `23:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198281` | Route 5808 | `21:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198278` | Route 5808 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198263` | Route 5808 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198266` | Route 5808 | `17:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198269` | Route 5808 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198272` | Route 5808 | `14:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198275` | Route 5808 | `12:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198296` | Route 5808 | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198293` | Route 5808 | `09:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198290` | Route 5808 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198287` | Route 5808 | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198285` | Route 5808 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198282` | Route 5808 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198279` | Route 5808 | `20:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:48` | `98.74%` | `0.0%` | 238 | 5 | `+355.0s` |
| `2026-10-25 06:01:04` | `97.93%` | `100.0%` | 241 | 7 | `+133.0s` |
| `2026-10-25 05:30:23` | `85.56%` | `100.0%` | 277 | 39 | `+101.3s` |
| `2026-10-25 05:00:33` | `77.85%` | `83.33%` | 307 | 67 | `+139.0s` |
| `2026-10-25 04:33:58` | `75.08%` | `78.57%` | 325 | 82 | `+222.9s` |
| `2026-10-25 03:30:20` | `21.85%` | `68.75%` | 119 | 93 | `+362.2s` |
| `2026-10-25 03:00:22` | `24.03%` | `94.44%` | 129 | 94 | `+95.4s` |
| `2026-10-25 02:30:20` | `29.2%` | `93.75%` | 137 | 94 | `+96.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:48.227000+00:00`.*
