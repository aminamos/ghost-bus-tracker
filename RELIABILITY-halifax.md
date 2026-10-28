# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.694000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `682` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `682` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 682 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7B** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7A** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 55 | 0 | 55 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 34 | 0 | 34 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `4650507` | Route 182 | `07:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651875` | Route 24 | `09:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651911` | Route 24 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651878` | Route 24 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651914` | Route 24 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651881` | Route 24 | `12:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651917` | Route 24 | `12:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651884` | Route 24 | `13:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651920` | Route 24 | `14:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660576` | Route 87 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651342` | Route 21 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651314` | Route 21 | `15:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658286` | Route 72 | `08:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661717` | Route 9B | `11:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659516` | Route 8 | `08:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-28 06:30:21` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-28 06:00:21` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-28 05:30:26` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-28 05:00:25` | `0.0%` | `100.0%` | 2 | 1 | `+98.0s` |
| `2026-10-28 04:30:28` | `20.0%` | `100.0%` | 5 | 3 | `-4.5s` |
| `2026-10-28 04:00:29` | `12.9%` | `63.64%` | 31 | 24 | `-51.4s` |
| `2026-10-28 03:30:18` | `10.77%` | `66.67%` | 65 | 43 | `-28.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.694000+00:00`.*
