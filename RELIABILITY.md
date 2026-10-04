# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-04T06:05:55.120964+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`42.31%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `52` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+138.4s` (`2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+52.5s` (`0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 42.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 15 | 28.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 14 | 26.9% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3m` |
| **Route 17** | 4 | 3 | 0 | **`0.0%`** | `50.0%` | `+0.5m` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+7.2m` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.4m` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-359.0s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+8.6m` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `-222.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-155.5s` |
| **Route 61** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+15.6m` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-78.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 61** | `+15.6 min (934.0s)` | `+30.5 min (1828s)` | 2 | `50.0%` |
| **Route 3** | `+8.6 min (516.8s)` | `+11.3 min (677s)` | 4 | `0.0%` |
| **Route 36** | `+8.0 min (479.0s)` | `+8.0 min (479s)` | 1 | `0.0%` |
| **Route 18** | `+7.2 min (433.0s)` | `+14.7 min (880s)` | 2 | `50.0%` |
| **Route 921** | `+6.0 min (357.0s)` | `+6.0 min (357s)` | 1 | `0.0%` |
| **Route 923** | `+5.4 min (322.0s)` | `+8.7 min (522s)` | 3 | `66.67%` |
| **Route 924** | `+4.2 min (251.0s)` | `+7.4 min (445s)` | 4 | `50.0%` |
| **Route 922** | `+3.5 min (209.8s)` | `+9.0 min (538s)` | 4 | `33.33%` |
| **Route 2** | `+3.4 min (202.0s)` | `+7.2 min (429s)` | 2 | `50.0%` |
| **Route 64** | `+1.8 min (109.0s)` | `+2.5 min (153s)` | 1 | `100.0%` |

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
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-04T06:05:55.120964+00:00`.*
