# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-03T18:04:11.498762+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.62%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.93%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `753` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `657` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `95` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+130.4s` (`2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+99.0s` (`1.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 466 | 61.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 84 | 11.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 101 | 13.4% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 95 | 12.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-23.5s` |
| **Route 65** | 10 | 3 | 6 | **`60.0%`** | `100.0%` | `+1.9m` |
| **Route 888** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-142.0s` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `83.33%` | `+1.8m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.9m` |
| **Route 67** | 11 | 5 | 4 | **`36.36%`** | `40.0%` | `+2.6m` |
| **Route 68** | 25 | 10 | 9 | **`36.0%`** | `100.0%` | `-30.5s` |
| **Route 18** | 36 | 18 | 12 | **`33.33%`** | `80.0%` | `+1.3m` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+2.2m` |
| **Route 645** | 6 | 2 | 2 | **`33.33%`** | `75.0%` | `+3.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 925** | `+6.2 min (370.2s)` | `+21.3 min (1276s)` | 17 | `59.09%` |
| **Route 54** | `+5.8 min (350.0s)` | `+17.9 min (1076s)` | 11 | `64.71%` |
| **Route 904** | `+4.6 min (277.8s)` | `+8.5 min (512s)` | 7 | `66.67%` |
| **Route 921** | `+4.6 min (276.8s)` | `+14.3 min (856s)` | 10 | `52.38%` |
| **Route 83** | `+4.2 min (249.0s)` | `+8.9 min (536s)` | 3 | `71.43%` |
| **Route 46** | `+3.9 min (236.0s)` | `+7.4 min (446s)` | 2 | `60.0%` |
| **Route 645** | `+3.9 min (232.0s)` | `+7.7 min (460s)` | 2 | `75.0%` |
| **Route 721** | `+3.7 min (219.3s)` | `+7.2 min (430s)` | 3 | `83.33%` |
| **Route 538** | `+3.6 min (217.8s)` | `+6.4 min (382s)` | 2 | `80.0%` |
| **Route 94** | `+3.5 min (211.2s)` | `+5.8 min (348s)` | 4 | `83.33%` |

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
| `1345502` | Route 10 | `N/A` | `SCHEDULED` | Assigned vehicle 2009 is missing from active GPS transponder fleet |
| `1332587` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1335553` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360120` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1241416` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242173` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361143` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361722` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365229` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365577` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366882` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367344` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367994` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368256` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368352` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-03T18:04:11.498762+00:00`.*
