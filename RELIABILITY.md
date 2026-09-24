# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-09-24T06:56:04.233366+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `11` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+521.7s` (`8.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+47.0s` (`0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 72.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 9.1% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 18.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+23.1m` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+18.0m` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 18** | `+23.1 min (1384.0s)` | `+42.4 min (2541s)` | 2 | `50.0%` |
| **Route 22** | `+18.0 min (1078.5s)` | `+32.1 min (1929s)` | 2 | `50.0%` |
| **Route 64** | `+12.0 min (718.0s)` | `+12.0 min (718s)` | 1 | `0.0%` |
| **Route 3** | `+0.6 min (35.5s)` | `+0.8 min (47s)` | 2 | `100.0%` |
| **Route 36** | `+0.4 min (25.0s)` | `+0.4 min (25s)` | 1 | `100.0%` |
| **Route 17** | `+0.1 min (8.0s)` | `+0.1 min (8s)` | 1 | `100.0%` |

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
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-24T06:56:04.233366+00:00`.*
