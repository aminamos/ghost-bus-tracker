# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T07:00:35.038000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `558` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `558` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 558 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7A** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7B** | 54 | 0 | 54 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 24** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4653682` | Route 320 | `06:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653702` | Route 320 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653684` | Route 320 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653704` | Route 320 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653686` | Route 320 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653706` | Route 320 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653688` | Route 320 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653708` | Route 320 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659362` | Route 8 | `06:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659368` | Route 8 | `09:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656062` | Route 56 | `06:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656067` | Route 56 | `09:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659375` | Route 8 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653683` | Route 320 | `07:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653703` | Route 320 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 07:00:35` | `100.0%` | `0.0%` | 558 | 0 | `+0.0s` |
| `2026-10-24 06:30:22` | `100.0%` | `0.0%` | 558 | 0 | `+0.0s` |
| `2026-10-24 06:00:33` | `100.0%` | `0.0%` | 558 | 0 | `+0.0s` |
| `2026-10-24 05:30:20` | `100.0%` | `0.0%` | 558 | 0 | `+0.0s` |
| `2026-10-24 05:00:23` | `50.0%` | `0.0%` | 2 | 1 | `-157.0s` |
| `2026-10-24 04:30:21` | `20.0%` | `50.0%` | 5 | 4 | `+2.8s` |
| `2026-10-24 04:00:22` | `16.67%` | `60.87%` | 36 | 24 | `+170.4s` |
| `2026-10-24 03:30:34` | `13.24%` | `82.76%` | 68 | 43 | `-19.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T07:00:35.038000+00:00`.*
