# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-06T06:42:10.173766+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.25%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `17` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `16` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+237.0s` (`+4.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+158.0s` (`+2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 13 | 76.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 5.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 5.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 5.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+18.4 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.2 min` |
| **Route 924** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+5.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 18** | `+18.4 min (+1105.0s)` | `+34.0 min (+2041s)` | 2 | `50.0%` |
| **Route 924** | `+5.5 min (+327.0s)` | `+5.5 min (+327s)` | 1 | `0.0%` |
| **Route 14** | `+4.0 min (+242.0s)` | `+4.0 min (+242s)` | 1 | `100.0%` |
| **Route 922** | `+3.7 min (+221.0s)` | `+3.7 min (+221s)` | 1 | `100.0%` |
| **Route 64** | `+3.2 min (+193.0s)` | `+3.2 min (+193s)` | 1 | `100.0%` |
| **Route 925** | `+2.9 min (+175.0s)` | `+2.9 min (+175s)` | 1 | `100.0%` |
| **Route 22** | `+2.6 min (+156.0s)` | `+2.6 min (+156s)` | 1 | `100.0%` |
| **Route 63** | `+2.2 min (+131.0s)` | `+2.2 min (+131s)` | 1 | `100.0%` |
| **Route 17** | `+1.5 min (+90.0s)` | `+2.7 min (+160s)` | 1 | `100.0%` |
| **Route 3** | `+0.2 min (+9.5s)` | `+1.8 min (+110s)` | 2 | `50.0%` |

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
| `2026-10-06 06:42:10` | `0.0%` | `81.25%` | 17 | 16 | `+237.0s` |
| `2026-10-06 00:28:45` | `9.69%` | `67.95%` | 650 | 547 | `+74.2s` |
| `2026-10-05 18:39:10` | `13.83%` | `56.53%` | 962 | 749 | `+13.5s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:22` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:03:24` | `10.54%` | `64.02%` | 949 | 806 | `+28.8s` |
| `2026-10-05 11:43:44` | `10.82%` | `64.04%` | 915 | 773 | `+8.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T06:42:10.173766+00:00`.*
