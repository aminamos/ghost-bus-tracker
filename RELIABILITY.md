# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-22T07:00:17.933000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `54` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `54` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+73.2s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+4.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 72.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 14.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 13.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-29.5s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-146.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-35.7s` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.3 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.3 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-168.0s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+6.4 min` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-4.0s` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+10.3 min (+619.0s)` | `+10.3 min (+619s)` | 1 | `0.0%` |
| **Route 3** | `+6.4 min (+381.2s)` | `+10.8 min (+651s)` | 4 | `50.0%` |
| **Route 921** | `+4.0 min (+237.0s)` | `+11.1 min (+664s)` | 3 | `66.67%` |
| **Route 923** | `+3.8 min (+228.7s)` | `+6.5 min (+387s)` | 3 | `66.67%` |
| **Route 922** | `+3.7 min (+222.3s)` | `+9.1 min (+544s)` | 3 | `66.67%` |
| **Route 2** | `+3.3 min (+199.5s)` | `+6.4 min (+386s)` | 2 | `50.0%` |
| **Route 5** | `+2.9 min (+172.0s)` | `+4.0 min (+238s)` | 2 | `100.0%` |
| **Route 18** | `+2.3 min (+135.7s)` | `+3.4 min (+206s)` | 3 | `100.0%` |
| **Route 64** | `+1.5 min (+88.5s)` | `+3.0 min (+181s)` | 1 | `100.0%` |
| **Route 4** | `+1.4 min (+81.0s)` | `+3.0 min (+183s)` | 3 | `100.0%` |

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
| `2026-11-22 07:00:17` | `0.0%` | `72.22%` | 54 | 54 | `+73.2s` |
| `2026-11-22 06:30:17` | `0.0%` | `69.23%` | 104 | 104 | `+85.4s` |
| `2026-11-22 06:00:17` | `2.41%` | `68.32%` | 166 | 161 | `+109.9s` |
| `2026-11-22 05:00:18` | `4.48%` | `70.98%` | 268 | 255 | `+122.0s` |
| `2026-11-22 04:30:17` | `4.4%` | `72.7%` | 318 | 304 | `+143.4s` |
| `2026-11-22 04:00:17` | `5.11%` | `72.97%` | 352 | 335 | `+134.6s` |
| `2026-11-22 03:30:19` | `6.52%` | `74.8%` | 399 | 373 | `+128.8s` |
| `2026-11-22 03:00:18` | `7.48%` | `78.88%` | 428 | 393 | `+125.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:17.933000+00:00`.*
