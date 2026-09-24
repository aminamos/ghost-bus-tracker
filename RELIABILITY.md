# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-24T12:27:28.673441+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.19%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.43%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `940` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `809` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `124` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+45.2s` (`0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-10.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 497 | 52.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 259 | 27.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 43 | 4.6% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 124 | 13.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 0.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.6m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.2m` |
| **Route 64** | 25 | 10 | 10 | **`40.0%`** | `100.0%` | `-52.3s` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `+0.1m` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-55.8s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-14.3s` |
| **Route 2** | 33 | 12 | 12 | **`36.36%`** | `91.67%` | `-12.8s` |
| **Route 921** | 22 | 7 | 8 | **`36.36%`** | `92.86%` | `+1.9m` |
| **Route 540** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `+0.4m` |
| **Route 68** | 23 | 9 | 8 | **`34.78%`** | `100.0%` | `-41.3s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 705** | `+31.4 min (1881.2s)` | `+81.5 min (4892s)` | 2 | `0.0%` |
| **Route 888** | `+21.4 min (1282.0s)` | `+69.8 min (4188s)` | 4 | `33.33%` |
| **Route 25** | `+19.7 min (1180.0s)` | `+65.2 min (3915s)` | 6 | `28.57%` |
| **Route 784** | `+12.3 min (735.8s)` | `+50.5 min (3028s)` | 4 | `50.0%` |
| **Route 790** | `+7.0 min (417.7s)` | `+18.6 min (1115s)` | 3 | `66.67%` |
| **Route 667** | `+5.0 min (300.0s)` | `+5.0 min (300s)` | 1 | `100.0%` |
| **Route 645** | `+3.8 min (229.6s)` | `+14.9 min (895s)` | 5 | `85.71%` |
| **Route 781** | `+3.3 min (196.5s)` | `+46.7 min (2803s)` | 9 | `83.33%` |
| **Route 698** | `+3.1 min (183.5s)` | `+6.8 min (410s)` | 6 | `60.0%` |
| **Route 542** | `+3.1 min (183.2s)` | `+8.6 min (516s)` | 4 | `66.67%` |

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
| `1331609` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332665` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332882` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349775` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349904` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350068` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350659` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350697` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351306` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357883` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357994` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1263260` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1264755` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1264863` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1270044` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-24T12:27:28.673441+00:00`.*
