# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-03T08:42:45.557627+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`50.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `90` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `45` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `45` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+56.7s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+24.0s` (`0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 36.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 7.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 5.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 45 | 50.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 62** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 22** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 7** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 9** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 36** | 4 | 1 | 3 | **`75.0%`** | `100.0%` | `+0.4m` |
| **Route 924** | 10 | 3 | 7 | **`70.0%`** | `100.0%` | `-36.3s` |
| **Route 18** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `+0.4m` |
| **Route 38** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-228.0s` |
| **Route 65** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+3.1m` |
| **Route 68** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-12.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 921** | `+6.0 min (360.0s)` | `+6.0 min (362s)` | 3 | `0.0%` |
| **Route 904** | `+5.7 min (340.5s)` | `+6.6 min (394s)` | 2 | `50.0%` |
| **Route 54** | `+3.2 min (194.6s)` | `+9.7 min (584s)` | 3 | `80.0%` |
| **Route 65** | `+3.1 min (186.0s)` | `+3.1 min (186s)` | 1 | `100.0%` |
| **Route 14** | `+1.5 min (88.0s)` | `+1.5 min (88s)` | 1 | `100.0%` |
| **Route 3** | `+1.2 min (70.0s)` | `+2.4 min (142s)` | 2 | `100.0%` |
| **Route 64** | `+0.6 min (34.5s)` | `+3.0 min (180s)` | 1 | `100.0%` |
| **Route 11** | `+0.5 min (29.0s)` | `+0.8 min (49s)` | 2 | `100.0%` |
| **Route 18** | `+0.4 min (24.5s)` | `+0.9 min (55s)` | 2 | `100.0%` |
| **Route 36** | `+0.4 min (24.0s)` | `+0.4 min (24s)` | 1 | `100.0%` |

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
| `1359826` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361020` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367493` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367736` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368865` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365656` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368057` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1180125` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1322860` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1323618` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1178660` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1180803` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368734` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350999` | Route 38 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354181` | Route 38 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-03T08:42:45.557627+00:00`.*
