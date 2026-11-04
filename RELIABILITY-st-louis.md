# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T07:00:21.000000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.17%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `41` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `27` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+70.0s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 19 | 46.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 7.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 4.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 34.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19754** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-150.0s` |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.5 min` |
| **Route 19759** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-150.0s` |
| **Route 19792** | 3 | 3 | 0 | **`0.0%`** | `50.0%` | `+5.5 min` |
| **Route 19797** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19792** | `+5.5 min (+330.0s)` | `+6.0 min (+360s)` | 3 | `50.0%` |
| **Route 19779** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19778** | `+3.5 min (+210.0s)` | `+6.0 min (+360s)` | 2 | `50.0%` |
| **Route 19789** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19775** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19768** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19785** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19797** | `+2.0 min (+120.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |
| **Route 19798** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 19759** | `+1.0 min (+60.0s)` | `+5.0 min (+300s)` | 2 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19759** | ~1.0m | ~1.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 19778** | ~5.0m | ~5.0m | **`+0.0 min`** | `50.0 / 100` |
| **Route 19754** | ~21.0m | ~21.0m | **`+0.0 min`** | `92.9 / 100` |
| **Route 19797** | ~11.0m | ~11.0m | **`+0.0 min`** | `90.9 / 100` |
| **Route 19750** | ~26.0m | ~26.0m | **`+0.0 min`** | `94.2 / 100` |
| **Route 19792** | ~17.5m | ~17.5m | **`+0.0 min`** | `97.1 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:21` | `0.0%` | `79.17%` | 41 | 27 | `+70.0s` |
| `2026-11-04 06:30:33` | `0.0%` | `75.0%` | 76 | 59 | `+58.8s` |
| `2026-11-04 06:00:18` | `0.0%` | `81.48%` | 96 | 71 | `+130.0s` |
| `2026-11-04 05:30:18` | `1.19%` | `84.75%` | 84 | 71 | `+76.3s` |
| `2026-11-04 05:00:17` | `0.0%` | `80.88%` | 92 | 82 | `+130.6s` |
| `2026-11-04 04:30:17` | `0.0%` | `73.44%` | 99 | 79 | `+124.7s` |
| `2026-11-04 04:00:24` | `0.0%` | `83.33%` | 107 | 90 | `+100.8s` |
| `2026-11-04 03:30:21` | `0.0%` | `82.67%` | 98 | 87 | `+116.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:21.000000+00:00`.*
