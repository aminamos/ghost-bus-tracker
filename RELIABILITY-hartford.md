# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Connecticut Transit** in **Hartford, CT** (Hartford Metropolitan Area, Connecticut).
> **Transit System:** CTtransit | **Location:** Hartford, CT | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:32.557000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `45` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `45` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 45 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16221** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16479** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `1924093` | Route 16221 | `08:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924092` | Route 16221 | `09:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924089` | Route 16221 | `11:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924086` | Route 16221 | `13:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924083` | Route 16221 | `15:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924076` | Route 16221 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924095` | Route 16221 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924097` | Route 16221 | `21:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924099` | Route 16221 | `23:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924090` | Route 16221 | `10:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924087` | Route 16221 | `12:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924084` | Route 16221 | `14:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924081` | Route 16221 | `16:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924101` | Route 16221 | `18:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1924096` | Route 16221 | `20:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:32` | `100.0%` | `0.0%` | 45 | 0 | `+0.0s` |
| `2026-10-31 06:30:19` | `100.0%` | `0.0%` | 45 | 0 | `+0.0s` |
| `2026-10-31 06:00:19` | `0.0%` | `0.0%` | 2 | 2 | `+0.0s` |
| `2026-10-31 05:30:20` | `0.0%` | `0.0%` | 13 | 13 | `+0.0s` |
| `2026-10-31 05:00:33` | `2.44%` | `0.0%` | 41 | 40 | `+0.0s` |
| `2026-10-31 04:30:22` | `1.47%` | `0.0%` | 68 | 67 | `+0.0s` |
| `2026-10-31 04:00:18` | `2.08%` | `0.0%` | 96 | 94 | `+0.0s` |
| `2026-10-31 03:30:17` | `1.8%` | `100.0%` | 111 | 109 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:32.557000+00:00`.*
