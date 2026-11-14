# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:19.243000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `388` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `388` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 388 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 31 | 0 | 31 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 25 | 0 | 25 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4659365` | Route 8 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653685` | Route 320 | `09:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649052` | Route 1 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649059` | Route 1 | `18:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649078` | Route 1 | `23:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659360` | Route 8 | `05:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659366` | Route 8 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659379` | Route 8 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661633` | Route 9B | `19:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653707` | Route 320 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653705` | Route 320 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653689` | Route 320 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656084` | Route 56 | `17:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4656087` | Route 56 | `19:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649066` | Route 1 | `20:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `100.0%` | `0.0%` | 388 | 0 | `+0.0s` |
| `2026-11-14 06:30:21` | `100.0%` | `0.0%` | 388 | 0 | `+0.0s` |
| `2026-11-14 06:00:20` | `50.0%` | `0.0%` | 2 | 1 | `-181.0s` |
| `2026-11-14 05:30:18` | `16.67%` | `80.0%` | 6 | 5 | `+96.6s` |
| `2026-11-14 05:00:24` | `6.45%` | `63.64%` | 31 | 24 | `-2.3s` |
| `2026-11-14 04:30:18` | `4.69%` | `77.59%` | 64 | 43 | `+3.5s` |
| `2026-11-14 04:00:22` | `10.19%` | `80.22%` | 108 | 59 | `+49.3s` |
| `2026-11-14 03:30:18` | `12.86%` | `82.79%` | 140 | 67 | `+62.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.243000+00:00`.*
