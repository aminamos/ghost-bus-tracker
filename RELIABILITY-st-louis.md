# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-13T07:00:24.149000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `41` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `27` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+75.7s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 36.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 14.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.4% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 34.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-180.0s` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-120.0s` |
| **Route 19787** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+13.5 min` |
| **Route 19785** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-120.0s` |
| **Route 19792** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0s` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19787** | `+13.5 min (+810.0s)` | `+26.0 min (+1560s)` | 2 | `50.0%` |
| **Route 19779** | `+6.0 min (+360.0s)` | `+6.0 min (+360s)` | 1 | `0.0%` |
| **Route 19798** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19757** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19789** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19784** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19780** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19793** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |
| **Route 19800** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19787** | ~22.0m | ~22.0m | **`+0.1 min`** | `43.2 / 100` |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `80.0 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `86.4 / 100` |
| **Route 19792** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:24` | `0.0%` | `65.22%` | 41 | 27 | `+75.7s` |
| `2026-11-13 06:30:19` | `0.0%` | `67.44%` | 68 | 54 | `+39.1s` |
| `2026-11-13 05:30:19` | `0.0%` | `72.58%` | 76 | 76 | `+131.6s` |
| `2026-11-13 05:00:22` | `0.0%` | `73.13%` | 86 | 86 | `+120.0s` |
| `2026-11-13 04:30:18` | `0.0%` | `69.12%` | 83 | 80 | `+93.5s` |
| `2026-11-13 04:00:21` | `0.0%` | `83.75%` | 93 | 93 | `+63.8s` |
| `2026-11-13 03:30:19` | `0.0%` | `72.22%` | 87 | 87 | `+137.5s` |
| `2026-11-13 03:00:22` | `0.0%` | `73.68%` | 93 | 87 | `+97.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:24.149000+00:00`.*
