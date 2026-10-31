# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-31T06:30:19.119000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`94.12%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `17` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+81.2s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+23.0s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 94.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 107** | 5 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 20** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.0 min` |
| **Route 9899** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 77** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | `+2.0 min (+123.0s)` | `+5.9 min (+354s)` | 4 | `80.0%` |
| **Route 77** | `+2.0 min (+122.0s)` | `+3.7 min (+224s)` | 4 | `100.0%` |
| **Route 107** | `+0.8 min (+51.0s)` | `+2.1 min (+129s)` | 2 | `100.0%` |
| **Route 9899** | `+0.1 min (+7.3s)` | `+0.8 min (+47s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `78.5 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `86.2 / 100` |
| **Route 107** | ~16.0m | ~16.0m | **`+0.0 min`** | `93.5 / 100` |
| **Route 9899** | ~22.5m | ~22.5m | **`+0.0 min`** | `97.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 06:30:19` | `0.0%` | `94.12%` | 17 | 15 | `+81.2s` |
| `2026-10-31 06:00:20` | `4.17%` | `100.0%` | 24 | 16 | `+48.7s` |
| `2026-10-31 05:30:21` | `0.0%` | `97.06%` | 34 | 22 | `+41.9s` |
| `2026-10-31 04:30:23` | `7.59%` | `78.08%` | 79 | 56 | `+121.2s` |
| `2026-10-31 04:00:18` | `8.7%` | `82.86%` | 115 | 73 | `+89.6s` |
| `2026-10-31 03:30:18` | `11.49%` | `86.26%` | 148 | 84 | `+72.7s` |
| `2026-10-31 03:00:18` | `6.82%` | `85.98%` | 176 | 95 | `+72.9s` |
| `2026-10-31 02:30:19` | `8.42%` | `84.32%` | 202 | 107 | `+95.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T06:30:19.119000+00:00`.*
