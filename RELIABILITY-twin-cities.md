# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-09T07:00:18.418000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.18%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `44` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `44` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+172.2s` (`+2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 30 | 68.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 18.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 9.1% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 4.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.2 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-91.5s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+5.1 min` |
| **Route 323** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+33.4 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-0.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-31.0s` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `50.0%` | `-27.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 323** | `+33.4 min (+2005.0s)` | `+34.9 min (+2092s)` | 1 | `0.0%` |
| **Route 54** | `+12.3 min (+738.0s)` | `+12.3 min (+738s)` | 1 | `0.0%` |
| **Route 3** | `+5.1 min (+308.5s)` | `+8.8 min (+528s)` | 4 | `75.0%` |
| **Route 923** | `+5.0 min (+302.7s)` | `+6.0 min (+362s)` | 3 | `33.33%` |
| **Route 924** | `+2.4 min (+142.3s)` | `+3.9 min (+236s)` | 3 | `100.0%` |
| **Route 10** | `+2.1 min (+128.0s)` | `+3.3 min (+199s)` | 2 | `100.0%` |
| **Route 925** | `+2.0 min (+119.5s)` | `+3.1 min (+188s)` | 2 | `100.0%` |
| **Route 11** | `+1.4 min (+85.5s)` | `+3.2 min (+195s)` | 2 | `100.0%` |
| **Route 18** | `+1.2 min (+71.0s)` | `+4.9 min (+296s)` | 2 | `50.0%` |
| **Route 922** | `+1.0 min (+62.5s)` | `+2.1 min (+129s)` | 2 | `100.0%` |

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
| `2026-11-09 07:00:18` | `0.0%` | `68.18%` | 44 | 44 | `+172.2s` |
| `2026-11-09 06:00:18` | `2.8%` | `75.18%` | 143 | 137 | `+48.3s` |
| `2026-11-09 05:30:17` | `5.26%` | `72.47%` | 190 | 178 | `+76.0s` |
| `2026-11-09 05:00:17` | `5.53%` | `70.45%` | 235 | 220 | `+75.3s` |
| `2026-11-09 04:30:18` | `5.07%` | `79.77%` | 276 | 262 | `+90.6s` |
| `2026-11-09 04:00:18` | `7.35%` | `78.28%` | 313 | 290 | `+87.2s` |
| `2026-11-09 03:30:17` | `8.66%` | `73.2%` | 335 | 306 | `+90.2s` |
| `2026-11-09 02:30:18` | `8.44%` | `75.7%` | 391 | 358 | `+93.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:18.418000+00:00`.*
