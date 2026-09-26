# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-26T17:50:32.609595+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.6%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.61%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `807` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `649` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `134` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+114.4s` (`1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+68.0s` (`1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 477 | 59.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 76 | 9.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 89 | 11.0% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 134 | 16.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 24 | 3.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 30** | 10 | 3 | 6 | **`60.0%`** | `100.0%` | `+3.5m` |
| **Route 888** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+1.3m` |
| **Route 18** | 38 | 15 | 17 | **`44.74%`** | `87.5%` | `+0.1m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.7m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.1m` |
| **Route 10** | 37 | 14 | 13 | **`35.14%`** | `83.33%` | `+1.7m` |
| **Route 64** | 23 | 10 | 8 | **`34.78%`** | `66.67%` | `+2.6m` |
| **Route 17** | 24 | 12 | 8 | **`33.33%`** | `84.62%` | `+2.0m` |
| **Route 36** | 12 | 5 | 4 | **`33.33%`** | `71.43%` | `+2.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 721** | `+5.4 min (326.0s)` | `+12.6 min (758s)` | 3 | `66.67%` |
| **Route 904** | `+5.2 min (312.1s)` | `+17.8 min (1065s)` | 6 | `61.54%` |
| **Route 925** | `+5.1 min (306.6s)` | `+16.8 min (1008s)` | 15 | `44.44%` |
| **Route 9** | `+4.8 min (287.7s)` | `+12.7 min (763s)` | 7 | `60.0%` |
| **Route 645** | `+4.3 min (256.0s)` | `+8.1 min (485s)` | 2 | `50.0%` |
| **Route 14** | `+4.3 min (255.6s)` | `+19.6 min (1177s)` | 7 | `75.0%` |
| **Route 615** | `+4.2 min (253.8s)` | `+7.0 min (419s)` | 2 | `50.0%` |
| **Route 725** | `+3.9 min (231.0s)` | `+8.5 min (510s)` | 2 | `75.0%` |
| **Route 30** | `+3.5 min (209.8s)` | `+5.0 min (297s)` | 3 | `100.0%` |
| **Route 25** | `+3.5 min (207.6s)` | `+18.3 min (1100s)` | 3 | `66.67%` |

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
| `1325975` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326209` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326212` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326342` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326642` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326740` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327194` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327796` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330214` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1341120` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352070` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355655` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318496` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319110` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-26T17:50:32.609595+00:00`.*
