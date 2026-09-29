# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-29T20:04:44.504923+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.74%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1080` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `895` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `156` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+56.5s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+20.0s` (`0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 589 | 54.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 229 | 21.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 70 | 6.5% |
| 🔴 **Severe Delay** | Over 15m late | 8 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 156 | 14.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 28 | 2.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 760** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `-65.0s` |
| **Route 578** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-46.0s` |
| **Route 766** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-15.0s` |
| **Route 882** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+0.4m` |
| **Route 768** | 8 | 3 | 5 | **`62.5%`** | `100.0%` | `+0.3m` |
| **Route 275** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+1.1m` |
| **Route 763** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-67.0s` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-139.0s` |
| **Route 860** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-10.0s` |
| **Route 850** | 9 | 5 | 4 | **`44.44%`** | `100.0%` | `-21.6s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 781** | `+9.9 min (593.8s)` | `+53.7 min (3222s)` | 6 | `83.33%` |
| **Route 747** | `+5.4 min (322.7s)` | `+12.5 min (752s)` | 3 | `66.67%` |
| **Route 725** | `+5.2 min (310.0s)` | `+16.2 min (974s)` | 2 | `75.0%` |
| **Route 777** | `+4.8 min (288.0s)` | `+4.8 min (288s)` | 1 | `100.0%` |
| **Route 784** | `+3.8 min (227.5s)` | `+7.2 min (432s)` | 2 | `50.0%` |
| **Route 904** | `+3.3 min (197.4s)` | `+17.2 min (1030s)` | 11 | `71.43%` |
| **Route 363** | `+3.1 min (189.0s)` | `+3.1 min (189s)` | 1 | `100.0%` |
| **Route 645** | `+3.0 min (182.3s)` | `+15.3 min (918s)` | 5 | `71.43%` |
| **Route 83** | `+3.0 min (181.2s)` | `+16.9 min (1014s)` | 4 | `66.67%` |
| **Route 3** | `+3.0 min (179.1s)` | `+31.2 min (1872s)` | 17 | `58.33%` |

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
| `1324998` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325282` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325699` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325853` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326419` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326896` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327099` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327148` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318378` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319090` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319236` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319607` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350099` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350334` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-29T20:04:44.504923+00:00`.*
