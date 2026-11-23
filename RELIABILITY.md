# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-23T07:00:17.824000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.44%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `45` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `45` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+1.7s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+40.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 29 | 64.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 12 | 26.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 8.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.7 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-20.5s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+0.6 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-133.0s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+3.7 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-294.3s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `50.0%` | `-17.0s` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-30.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+11.2 min (+674.0s)` | `+11.2 min (+674s)` | 1 | `0.0%` |
| **Route 36** | `+5.3 min (+316.0s)` | `+5.3 min (+316s)` | 1 | `0.0%` |
| **Route 323** | `+4.2 min (+252.0s)` | `+4.2 min (+252s)` | 1 | `100.0%` |
| **Route 3** | `+3.7 min (+223.8s)` | `+7.7 min (+461s)` | 4 | `75.0%` |
| **Route 10** | `+2.7 min (+162.0s)` | `+3.7 min (+224s)` | 2 | `100.0%` |
| **Route 68** | `+2.5 min (+153.0s)` | `+2.5 min (+153s)` | 1 | `100.0%` |
| **Route 923** | `+2.1 min (+124.3s)` | `+5.3 min (+321s)` | 3 | `66.67%` |
| **Route 724** | `+1.8 min (+108.0s)` | `+1.8 min (+108s)` | 1 | `100.0%` |
| **Route 18** | `+1.7 min (+102.5s)` | `+3.2 min (+191s)` | 2 | `100.0%` |
| **Route 922** | `+1.3 min (+80.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |

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
| `2026-11-23 07:00:17` | `0.0%` | `64.44%` | 45 | 45 | `+1.7s` |
| `2026-11-23 06:30:17` | `0.0%` | `81.72%` | 94 | 93 | `+52.0s` |
| `2026-11-23 05:30:17` | `3.72%` | `72.63%` | 188 | 179 | `+59.9s` |
| `2026-11-23 04:00:18` | `5.13%` | `75.0%` | 312 | 296 | `+81.0s` |
| `2026-11-23 03:30:17` | `6.8%` | `72.7%` | 338 | 315 | `+56.1s` |
| `2026-11-23 03:00:18` | `7.07%` | `74.78%` | 368 | 341 | `+65.7s` |
| `2026-11-23 02:30:19` | `6.98%` | `74.09%` | 387 | 359 | `+72.2s` |
| `2026-11-23 02:00:22` | `6.71%` | `77.06%` | 417 | 388 | `+76.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:17.824000+00:00`.*
