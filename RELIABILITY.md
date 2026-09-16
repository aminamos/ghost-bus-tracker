# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-09-16T06:30:26.688976+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.74%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `31` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `31` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+88.8s` (`1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+41.0s` (`0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 21 | 67.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 25.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 3.2% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 3.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2m` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-37.0s` |
| **Route 17** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `-1.7s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4m` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.5m` |
| **Route 4** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-44.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-52.5s` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1m` |
| **Route 922** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5m` |
| **Route 924** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-63.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 925** | `+15.6 min (935.5s)` | `+28.9 min (1733s)` | 2 | `50.0%` |
| **Route 64** | `+6.6 min (396.0s)` | `+6.6 min (396s)` | 1 | `0.0%` |
| **Route 3** | `+3.5 min (209.0s)` | `+3.9 min (234s)` | 2 | `100.0%` |
| **Route 18** | `+1.8 min (108.0s)` | `+1.8 min (108s)` | 1 | `100.0%` |
| **Route 922** | `+1.5 min (88.5s)` | `+1.7 min (101s)` | 2 | `100.0%` |
| **Route 11** | `+1.2 min (72.0s)` | `+4.2 min (251s)` | 2 | `100.0%` |
| **Route 36** | `+0.8 min (47.0s)` | `+0.8 min (47s)` | 1 | `100.0%` |
| **Route 923** | `+0.8 min (46.0s)` | `+0.8 min (46s)` | 1 | `100.0%` |
| **Route 62** | `+0.7 min (41.0s)` | `+0.7 min (41s)` | 1 | `100.0%` |
| **Route 22** | `+0.4 min (23.0s)` | `+3.5 min (210s)` | 2 | `100.0%` |

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
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |
| `2026-09-15 07:55:59` | `0.0%` | `100.0%` | 6 | 6 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-16T06:30:26.688976+00:00`.*
