# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:21.585000+00:00` | **Source:** live GTFS-RT feed

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
| `4651349` | Route 21 | `18:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4651321` | Route 21 | `19:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659512` | Route 8 | `06:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660573` | Route 87 | `08:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660580` | Route 87 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659533` | Route 8 | `14:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4655377` | Route 51B | `14:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659745` | Route 82 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659532` | Route 8 | `14:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659739` | Route 82 | `16:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653773` | Route 320 | `14:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653800` | Route 320 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653776` | Route 320 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653803` | Route 320 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653764` | Route 320 | `06:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:21` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-29 06:30:23` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-29 06:00:23` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-29 05:30:18` | `100.0%` | `0.0%` | 682 | 0 | `+0.0s` |
| `2026-10-29 05:00:19` | `50.0%` | `0.0%` | 2 | 1 | `-171.0s` |
| `2026-10-29 04:30:20` | `16.67%` | `60.0%` | 6 | 4 | `-51.6s` |
| `2026-10-29 04:00:20` | `12.5%` | `59.09%` | 32 | 22 | `-40.0s` |
| `2026-10-29 03:30:18` | `12.86%` | `75.86%` | 70 | 45 | `-5.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:21.585000+00:00`.*
