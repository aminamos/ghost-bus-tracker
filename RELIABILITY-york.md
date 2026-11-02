# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-02T07:00:18.497000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`90.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `20` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+97.6s` (`+1.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+19.5s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 18 | 90.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 5.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 5.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 20** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 77** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 9899** | 5 | 3 | 0 | **`0.0%`** | `80.0%` | `+4.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+4.3 min (+258.4s)` | `+14.6 min (+876s)` | 3 | `80.0%` |
| **Route 107** | `+1.3 min (+76.2s)` | `+3.5 min (+211s)` | 2 | `100.0%` |
| **Route 20** | `+0.9 min (+55.8s)` | `+2.4 min (+142s)` | 4 | `100.0%` |
| **Route 77** | `+0.5 min (+29.4s)` | `+1.8 min (+108s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | ~23.0m | ~23.0m | **`+0.0 min`** | `76.6 / 100` |
| **Route 107** | ~10.0m | ~10.0m | **`+0.0 min`** | `86.6 / 100` |
| **Route 20** | ~23.0m | ~23.0m | **`+0.0 min`** | `95.0 / 100` |
| **Route 77** | ~20.0m | ~20.0m | **`+0.0 min`** | `96.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `0.0%` | `90.0%` | 20 | 13 | `+97.6s` |
| `2026-11-02 06:30:18` | `12.0%` | `77.27%` | 25 | 14 | `+33.6s` |
| `2026-11-02 06:00:24` | `0.0%` | `80.56%` | 36 | 22 | `+20.7s` |
| `2026-11-02 05:30:23` | `5.77%` | `85.71%` | 52 | 34 | `+32.8s` |
| `2026-11-02 05:00:19` | `13.04%` | `93.33%` | 69 | 45 | `+44.6s` |
| `2026-11-02 04:30:21` | `7.69%` | `89.29%` | 91 | 49 | `+33.1s` |
| `2026-11-02 04:00:18` | `5.88%` | `90.62%` | 102 | 54 | `+35.2s` |
| `2026-11-02 03:30:27` | `5.45%` | `86.54%` | 110 | 58 | `+25.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.497000+00:00`.*
