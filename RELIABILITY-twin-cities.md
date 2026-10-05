# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T18:39:11.437384+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.53%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `962` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `749` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `133` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+13.5s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-11.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 424 | 44.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 273 | 28.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 51 | 5.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 133 | 13.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 79 | 8.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 275** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 8 | 2 | 5 | **`62.5%`** | `100.0%` | `+1.9 min` |
| **Route 67** | 11 | 5 | 5 | **`45.45%`** | `66.67%` | `+1.0 min` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `50.0%` | `+1.1 min` |
| **Route 850** | 7 | 3 | 3 | **`42.86%`** | `50.0%` | `-70.5s` |
| **Route 18** | 38 | 19 | 16 | **`42.11%`** | `50.0%` | `-17.8s` |
| **Route 721** | 10 | 2 | 4 | **`40.0%`** | `66.67%` | `+0.3 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.3 min` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `33.33%` | `-112.7s` |
| **Route 768** | 5 | 2 | 2 | **`40.0%`** | `33.33%` | `+2.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 781** | `+4.6 min (+274.5s)` | `+8.6 min (+513s)` | 2 | `50.0%` |
| **Route 38** | `+3.4 min (+202.4s)` | `+13.6 min (+817s)` | 5 | `57.14%` |
| **Route 904** | `+3.2 min (+191.9s)` | `+6.8 min (+405s)` | 9 | `78.57%` |
| **Route 9** | `+3.1 min (+188.1s)` | `+21.2 min (+1270s)` | 9 | `40.0%` |
| **Route 768** | `+2.8 min (+166.0s)` | `+8.2 min (+493s)` | 2 | `33.33%` |
| **Route 901** | `+2.6 min (+153.8s)` | `+7.0 min (+420s)` | 8 | `87.5%` |
| **Route 94** | `+2.5 min (+149.1s)` | `+4.7 min (+284s)` | 5 | `100.0%` |
| **Route 80** | `+2.4 min (+144.0s)` | `+2.4 min (+144s)` | 1 | `100.0%` |
| **Route 75** | `+2.3 min (+139.0s)` | `+6.0 min (+357s)` | 2 | `50.0%` |
| **Route 215** | `+2.3 min (+136.7s)` | `+4.8 min (+289s)` | 1 | `100.0%` |

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
| `1324974` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324995` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325813` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326592` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326803` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327219` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364825` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365792` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365913` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365940` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366368` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331028` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331451` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332196` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332687` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 18:39:11` | `13.83%` | `56.53%` | 962 | 749 | `+13.5s` |
| `2026-10-05 18:02:18` | `12.71%` | `58.11%` | 952 | 752 | `+37.7s` |
| `2026-10-05 17:57:47` | `12.3%` | `58.16%` | 943 | 748 | `+38.7s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:23` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:14:27` | `11.02%` | `64.16%` | 944 | 798 | `+31.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:39:11.437384+00:00`.*
