# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-03T14:04:12.019417+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.74%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.54%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `682` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `560` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `121` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+89.0s` (`1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+56.5s` (`0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 395 | 57.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 101 | 14.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 60 | 8.8% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 121 | 17.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 65** | 10 | 3 | 5 | **`50.0%`** | `100.0%` | `+1.4m` |
| **Route 3** | 22 | 11 | 10 | **`45.45%`** | `63.64%` | `+3.8m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.1m` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+0.9m` |
| **Route 67** | 10 | 5 | 4 | **`40.0%`** | `50.0%` | `+2.3m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.5m` |
| **Route 540** | 8 | 2 | 3 | **`37.5%`** | `100.0%` | `+0.7m` |
| **Route 83** | 11 | 3 | 4 | **`36.36%`** | `71.43%` | `+3.8m` |
| **Route 68** | 25 | 12 | 9 | **`36.0%`** | `100.0%` | `-99.5s` |
| **Route 922** | 31 | 13 | 11 | **`35.48%`** | `93.75%` | `+0.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 72** | `+9.4 min (564.4s)` | `+46.5 min (2789s)` | 4 | `60.0%` |
| **Route 903** | `+5.6 min (335.6s)` | `+17.1 min (1028s)` | 2 | `60.0%` |
| **Route 48** | `+4.8 min (285.7s)` | `+14.9 min (892s)` | 2 | `50.0%` |
| **Route 921** | `+4.5 min (269.4s)` | `+9.4 min (564s)` | 7 | `40.0%` |
| **Route 904** | `+3.8 min (230.9s)` | `+8.4 min (503s)` | 7 | `69.23%` |
| **Route 25** | `+3.8 min (230.8s)` | `+9.0 min (540s)` | 3 | `50.0%` |
| **Route 3** | `+3.8 min (227.6s)` | `+14.0 min (840s)` | 11 | `63.64%` |
| **Route 83** | `+3.8 min (225.1s)` | `+9.7 min (579s)` | 3 | `71.43%` |
| **Route 46** | `+3.5 min (213.0s)` | `+5.5 min (328s)` | 2 | `75.0%` |
| **Route 17** | `+3.3 min (195.1s)` | `+8.3 min (496s)` | 6 | `66.67%` |

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
| `1331416` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331637` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332739` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1241861` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362100` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364463` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367567` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367772` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368112` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368677` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368708` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1369422` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1267920` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1272700` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366893` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-03T14:04:12.019417+00:00`.*
