# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-23T07:00:18.916000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `28` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+92.7s` (`+1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 28.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 7.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 3.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 50.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19777** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 1 | `0.0%` |
| **Route 19781** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19784** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19768** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |
| **Route 19792** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19749** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19775** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19778** | ~4.0m | ~4.0m | **`+0.0 min`** | `75.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:18` | `0.0%` | `72.73%` | 28 | 14 | `+92.7s` |
| `2026-11-23 06:30:18` | `0.0%` | `75.0%` | 52 | 38 | `+70.7s` |
| `2026-11-23 06:00:21` | `66.2%` | `0.0%` | 71 | 0 | `+0.0s` |
| `2026-11-23 05:30:18` | `0.0%` | `75.56%` | 78 | 54 | `+86.7s` |
| `2026-11-23 05:00:22` | `0.0%` | `74.07%` | 90 | 63 | `+96.7s` |
| `2026-11-23 04:30:22` | `0.0%` | `78.72%` | 98 | 65 | `+154.5s` |
| `2026-11-23 04:00:20` | `0.0%` | `86.44%` | 96 | 70 | `+125.1s` |
| `2026-11-23 03:30:18` | `0.0%` | `81.48%` | 93 | 66 | `+87.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:18.916000+00:00`.*
