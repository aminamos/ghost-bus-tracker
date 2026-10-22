# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Des Moines Area Regional Transit Authority** in **Des Moines, IA** (Des Moines Metropolitan Area, Iowa).
> **Transit System:** Des Moines | **Location:** Des Moines, IA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:48.698000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`75.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`82.86%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `144` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `35` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `108` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+140.6s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+113.0s` (`+1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 29 | 20.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 6 | 4.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 108 | 75.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3** | 53 | 6 | 46 | **`86.79%`** | `100.0%` | `+1.0 min` |
| **Route 9** | 18 | 3 | 15 | **`83.33%`** | `66.67%` | `+3.1 min` |
| **Route 11** | 15 | 3 | 12 | **`80.0%`** | `66.67%` | `+4.1 min` |
| **Route 12** | 15 | 3 | 12 | **`80.0%`** | `100.0%` | `+2.0 min` |
| **Route 5** | 16 | 4 | 12 | **`75.0%`** | `100.0%` | `+0.9 min` |
| **Route 4** | 17 | 6 | 11 | **`64.71%`** | `83.33%` | `+3.6 min` |
| **Route 6** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+4.7 min` |
| **Route 2** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+2.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | `+4.7 min (+280.3s)` | `+6.3 min (+376s)` | 3 | `33.33%` |
| **Route 11** | `+4.1 min (+245.0s)` | `+7.5 min (+450s)` | 3 | `66.67%` |
| **Route 4** | `+3.6 min (+215.0s)` | `+10.2 min (+615s)` | 6 | `83.33%` |
| **Route 9** | `+3.1 min (+186.3s)` | `+5.6 min (+334s)` | 3 | `66.67%` |
| **Route 2** | `+2.0 min (+119.5s)` | `+6.8 min (+405s)` | 4 | `75.0%` |
| **Route 12** | `+2.0 min (+117.7s)` | `+3.5 min (+210s)` | 3 | `100.0%` |
| **Route 7** | `+1.2 min (+70.0s)` | `+1.2 min (+70s)` | 1 | `100.0%` |
| **Route 3** | `+1.0 min (+59.3s)` | `+5.0 min (+300s)` | 6 | `100.0%` |
| **Route 5** | `+0.9 min (+56.8s)` | `+3.0 min (+180s)` | 4 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 4** | ~30.0m | ~30.0m | **`+0.0 min`** | `87.4 / 100` |
| **Route 2** | ~15.0m | ~15.0m | **`+0.0 min`** | `83.8 / 100` |
| **Route 3** | ~15.0m | ~15.0m | **`+0.0 min`** | `85.7 / 100` |
| **Route 5** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.3 / 100` |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.8 / 100` |
| **Route 5** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.6 / 100` |
| **Route 4** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.9 / 100` |
| **Route 12** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.6 / 100` |
| **Route 11** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 9** | ~57.5m | ~57.5m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `750738` | Route 5 | `17:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750741` | Route 5 | `20:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750734` | Route 5 | `15:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750739` | Route 5 | `18:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750740` | Route 5 | `21:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750736` | Route 5 | `16:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750242` | Route 3 | `20:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750310` | Route 3 | `21:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750244` | Route 3 | `21:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750258` | Route 3 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750304` | Route 3 | `17:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750252` | Route 3 | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750284` | Route 3 | `19:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750240` | Route 3 | `19:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `750308` | Route 3 | `20:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:48.698000+00:00`.*
