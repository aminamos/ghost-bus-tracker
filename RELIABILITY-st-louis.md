# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-21T07:00:18.776000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `43` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `29` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+36.5s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 34.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 16.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 32.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-90.0s` |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.5 min` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19792** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+5.0 min` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19777** | `+6.0 min (+360.0s)` | `+6.0 min (+360s)` | 1 | `0.0%` |
| **Route 19792** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 3 | `100.0%` |
| **Route 19763** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19779** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19784** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19798** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19755** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19782** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19780** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `78.6 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `86.4 / 100` |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `90.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `0.0%` | `65.22%` | 43 | 29 | `+36.5s` |
| `2026-11-21 06:30:33` | `0.0%` | `68.63%` | 74 | 59 | `+98.8s` |
| `2026-11-21 06:00:18` | `0.0%` | `78.33%` | 90 | 72 | `+89.0s` |
| `2026-11-21 05:30:18` | `0.0%` | `83.33%` | 86 | 77 | `+64.2s` |
| `2026-11-21 05:00:20` | `0.0%` | `79.37%` | 94 | 82 | `+124.8s` |
| `2026-11-21 04:30:18` | `0.0%` | `80.88%` | 86 | 79 | `+114.7s` |
| `2026-11-21 04:00:18` | `0.0%` | `83.1%` | 95 | 93 | `+97.2s` |
| `2026-11-21 03:30:18` | `0.0%` | `82.61%` | 83 | 83 | `+127.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.776000+00:00`.*
