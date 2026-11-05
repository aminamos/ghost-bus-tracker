# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:18.138000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `293` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `10` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `282` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+83.8s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+30.5s` (`+0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 4 | 1.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 282 | 96.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `+0.5 min` |
| **Route 5783** | 118 | 2 | 115 | **`97.46%`** | `100.0%` | `+2.3 min` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5783** | `+2.3 min (+137.0s)` | `+4.6 min (+274s)` | 2 | `100.0%` |
| **Route 5782** | `+0.5 min (+30.5s)` | `+1.0 min (+61s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5783** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.4 / 100` |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2190448` | Route 5783 | `23:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190316` | Route 5783 | `25:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190344` | Route 5783 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190432` | Route 5783 | `20:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190447` | Route 5783 | `23:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190187` | Route 5783 | `05:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190334` | Route 5783 | `06:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190214` | Route 5783 | `08:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190361` | Route 5783 | `10:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190236` | Route 5783 | `12:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190382` | Route 5783 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190262` | Route 5783 | `15:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190410` | Route 5783 | `17:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190287` | Route 5783 | `19:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190433` | Route 5783 | `20:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:18` | `96.25%` | `100.0%` | 293 | 10 | `+83.8s` |
| `2026-11-05 06:30:18` | `84.34%` | `91.67%` | 332 | 47 | `+13.3s` |
| `2026-11-05 06:00:18` | `76.65%` | `88.24%` | 364 | 76 | `+38.5s` |
| `2026-11-05 05:30:19` | `73.09%` | `96.43%` | 379 | 86 | `+75.9s` |
| `2026-11-05 05:00:18` | `10.78%` | `100.0%` | 102 | 89 | `+50.7s` |
| `2026-11-05 04:30:18` | `17.59%` | `78.57%` | 108 | 90 | `+152.4s` |
| `2026-11-05 04:00:20` | `18.26%` | `78.57%` | 115 | 92 | `+173.4s` |
| `2026-11-05 03:30:19` | `19.2%` | `94.44%` | 125 | 98 | `+74.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:18.138000+00:00`.*
