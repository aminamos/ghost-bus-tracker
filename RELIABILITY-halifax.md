# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:32.766000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `235` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `235` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 235 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 75 | 0 | 75 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 51A** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 87** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 17 | 0 | 17 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4659396` | Route 8 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659390` | Route 8 | `20:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659384` | Route 8 | `17:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661752` | Route ecs | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660503` | Route 87 | `23:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4660502` | Route 87 | `22:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659393` | Route 8 | `21:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659387` | Route 8 | `18:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659679` | Route 82 | `20:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659680` | Route 82 | `21:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659681` | Route 82 | `22:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659673` | Route 82 | `14:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659674` | Route 82 | `15:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659675` | Route 82 | `16:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4659676` | Route 82 | `17:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:32` | `100.0%` | `0.0%` | 235 | 1 | `+0.0s` |
| `2026-10-31 06:30:19` | `100.0%` | `0.0%` | 235 | 0 | `+0.0s` |
| `2026-10-31 06:00:19` | `100.0%` | `0.0%` | 235 | 0 | `+0.0s` |
| `2026-10-31 05:30:21` | `100.0%` | `0.0%` | 235 | 0 | `+0.0s` |
| `2026-10-31 05:00:30` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-10-31 04:30:22` | `25.0%` | `66.67%` | 4 | 3 | `+44.7s` |
| `2026-10-31 04:00:21` | `3.23%` | `77.27%` | 31 | 23 | `+499.3s` |
| `2026-10-31 03:30:17` | `11.11%` | `81.82%` | 63 | 43 | `+11.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:32.766000+00:00`.*
