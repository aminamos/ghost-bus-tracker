# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-13T07:00:18.841000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.34%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `58` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+44.2s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-14.5s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 35 | 60.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 19 | 32.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.4% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.1 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-170.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 18** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+9.3 min` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+1.2 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-81.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-18.0s` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-103.3s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-157.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 18** | `+9.3 min (+555.2s)` | `+33.3 min (+1999s)` | 4 | `75.0%` |
| **Route 924** | `+3.9 min (+236.0s)` | `+17.1 min (+1024s)` | 4 | `50.0%` |
| **Route 923** | `+3.1 min (+189.0s)` | `+5.9 min (+356s)` | 2 | `66.67%` |
| **Route 17** | `+2.0 min (+120.7s)` | `+3.2 min (+192s)` | 3 | `100.0%` |
| **Route 925** | `+1.4 min (+84.5s)` | `+1.6 min (+96s)` | 2 | `100.0%` |
| **Route 922** | `+1.2 min (+73.5s)` | `+4.0 min (+241s)` | 4 | `100.0%` |
| **Route 2** | `+1.2 min (+71.3s)` | `+6.5 min (+387s)` | 3 | `33.33%` |
| **Route 62** | `+0.9 min (+53.0s)` | `+2.4 min (+142s)` | 1 | `100.0%` |
| **Route 515** | `+0.8 min (+48.0s)` | `+0.8 min (+48s)` | 1 | `100.0%` |
| **Route 11** | `+0.5 min (+31.5s)` | `+0.6 min (+37s)` | 2 | `100.0%` |

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
| `2026-11-13 07:00:18` | `0.0%` | `60.34%` | 58 | 58 | `+44.2s` |
| `2026-11-13 06:30:18` | `0.0%` | `66.67%` | 111 | 111 | `+126.5s` |
| `2026-11-13 05:30:18` | `4.42%` | `56.81%` | 226 | 213 | `+45.8s` |
| `2026-11-13 04:30:18` | `4.96%` | `59.75%` | 343 | 323 | `+35.5s` |
| `2026-11-13 04:00:19` | `5.93%` | `59.12%` | 388 | 362 | `+49.7s` |
| `2026-11-13 03:30:18` | `6.98%` | `58.59%` | 430 | 396 | `+48.7s` |
| `2026-11-13 02:30:18` | `7.18%` | `63.73%` | 515 | 466 | `+53.3s` |
| `2026-11-13 02:00:18` | `7.26%` | `65.2%` | 551 | 506 | `+61.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:18.841000+00:00`.*
