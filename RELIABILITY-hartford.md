# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Connecticut Transit** in **Hartford, CT** (Hartford Metropolitan Area, Connecticut).
> **Transit System:** CTtransit | **Location:** Hartford, CT | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-27T07:00:34.130000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `33` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `33` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 33 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16221** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `1924176` | Route 16221 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924146` | Route 16221 | `08:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924164` | Route 16221 | `08:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924152` | Route 16221 | `10:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924147` | Route 16221 | `13:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924154` | Route 16221 | `15:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924165` | Route 16221 | `07:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924160` | Route 16221 | `10:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924148` | Route 16221 | `12:46:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924155` | Route 16221 | `15:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924171` | Route 16221 | `17:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924177` | Route 16221 | `20:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924172` | Route 16221 | `22:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924180` | Route 16221 | `00:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924162` | Route 16221 | `09:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 07:00:34` | `100.0%` | `0.0%` | 33 | 0 | `+0.0s` |
| `2026-10-27 06:30:33` | `100.0%` | `0.0%` | 33 | 0 | `+0.0s` |
| `2026-10-27 05:30:34` | `0.0%` | `0.0%` | 9 | 9 | `+0.0s` |
| `2026-10-27 05:00:22` | `2.7%` | `0.0%` | 37 | 36 | `+0.0s` |
| `2026-10-27 04:30:19` | `1.52%` | `0.0%` | 66 | 65 | `+0.0s` |
| `2026-10-27 04:00:23` | `2.08%` | `0.0%` | 96 | 94 | `+0.0s` |
| `2026-10-27 03:30:23` | `1.8%` | `100.0%` | 111 | 109 | `+0.0s` |
| `2026-10-27 03:00:36` | `3.31%` | `0.0%` | 121 | 117 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T07:00:34.130000+00:00`.*
