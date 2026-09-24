# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-24T20:37:01.605278+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.62%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.31%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1109` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `923` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `140` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+92.5s` (`1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+22.0s` (`0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 529 | 47.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 250 | 22.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 133 | 12.0% |
| 🔴 **Severe Delay** | Over 15m late | 11 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 140 | 12.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 46 | 4.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-142.0s` |
| **Route 9** | 15 | 5 | 7 | **`46.67%`** | `83.33%` | `+1.1m` |
| **Route 36** | 11 | 4 | 5 | **`45.45%`** | `100.0%` | `-130.0s` |
| **Route 645** | 9 | 5 | 4 | **`44.44%`** | `80.0%` | `+2.8m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.5m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+4.4m` |
| **Route 921** | 33 | 12 | 13 | **`39.39%`** | `80.0%` | `+2.2m` |
| **Route 768** | 9 | 6 | 3 | **`33.33%`** | `83.33%` | `+1.9m` |
| **Route 850** | 9 | 5 | 3 | **`33.33%`** | `100.0%` | `-59.5s` |
| **Route 578** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-95.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 784** | `+25.6 min (1534.0s)` | `+50.5 min (3028s)` | 2 | `50.0%` |
| **Route 781** | `+12.9 min (775.1s)` | `+97.8 min (5870s)` | 7 | `87.5%` |
| **Route 667** | `+11.0 min (658.0s)` | `+11.0 min (658s)` | 1 | `0.0%` |
| **Route 904** | `+10.1 min (604.0s)` | `+46.8 min (2807s)` | 11 | `40.91%` |
| **Route 716** | `+8.7 min (519.3s)` | `+14.9 min (892s)` | 1 | `33.33%` |
| **Route 777** | `+7.6 min (456.0s)` | `+7.6 min (456s)` | 1 | `0.0%` |
| **Route 538** | `+5.5 min (330.0s)` | `+21.2 min (1272s)` | 3 | `57.14%` |
| **Route 673** | `+4.5 min (272.5s)` | `+10.0 min (600s)` | 5 | `66.67%` |
| **Route 54** | `+4.5 min (271.8s)` | `+20.2 min (1214s)` | 14 | `57.14%` |
| **Route 215** | `+4.4 min (266.3s)` | `+9.6 min (573s)` | 1 | `66.67%` |

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
| `1331480` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331679` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332154` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332799` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1219522` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1221639` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242853` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1243338` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349871` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350333` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350506` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350551` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350919` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351667` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356754` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-24T20:37:01.605278+00:00`.*
