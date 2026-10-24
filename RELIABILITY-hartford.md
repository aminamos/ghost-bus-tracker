# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Connecticut Transit** in **Hartford, CT** (Hartford Metropolitan Area, Connecticut).
> **Transit System:** CTtransit | **Location:** Hartford, CT | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:22.201000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `24` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `24` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 24 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16221** | 24 | 0 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2026-10-24 06:30:22` | `100.0%` | `0.0%` | 24 | 0 | `+0.0s` |
| `2026-10-24 05:30:20` | `0.0%` | `0.0%` | 9 | 9 | `+0.0s` |
| `2026-10-24 05:00:23` | `2.86%` | `0.0%` | 35 | 34 | `+0.0s` |
| `2026-10-24 04:30:21` | `1.45%` | `0.0%` | 69 | 68 | `+0.0s` |
| `2026-10-24 04:00:22` | `2.0%` | `0.0%` | 100 | 98 | `+0.0s` |
| `2026-10-24 03:30:34` | `1.74%` | `100.0%` | 115 | 113 | `+0.0s` |
| `2026-10-24 03:00:20` | `3.28%` | `0.0%` | 122 | 118 | `+0.0s` |
| `2026-10-24 02:30:33` | `3.12%` | `100.0%` | 128 | 124 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.201000+00:00`.*
