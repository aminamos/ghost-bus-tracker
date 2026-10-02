# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-02T23:53:15.515631+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.34%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.71%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `731` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `637` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `61` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+87.4s` (`1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+14.0s` (`0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 390 | 53.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 155 | 21.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 74 | 10.1% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 61 | 8.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 36 | 4.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 540** | 10 | 6 | 4 | **`40.0%`** | `100.0%` | `+0.2m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.5m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `100.0%` | `-30.6s` |
| **Route 18** | 25 | 12 | 8 | **`32.0%`** | `84.62%` | `+0.7m` |
| **Route 7** | 10 | 5 | 3 | **`30.0%`** | `60.0%` | `+3.4m` |
| **Route 645** | 7 | 5 | 2 | **`28.57%`** | `40.0%` | `+7.9m` |
| **Route 924** | 31 | 18 | 8 | **`25.81%`** | `86.67%` | `+0.8m` |
| **Route 723** | 4 | 2 | 1 | **`25.0%`** | `100.0%` | `+0.4m` |
| **Route 538** | 9 | 3 | 2 | **`22.22%`** | `100.0%` | `+0.2m` |
| **Route 25** | 5 | 3 | 1 | **`20.0%`** | `100.0%` | `-37.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 323** | `+23.8 min (1428.9s)` | `+54.1 min (3248s)` | 2 | `25.0%` |
| **Route 673** | `+8.1 min (484.0s)` | `+8.1 min (484s)` | 1 | `0.0%` |
| **Route 645** | `+7.9 min (476.6s)` | `+12.4 min (745s)` | 5 | `40.0%` |
| **Route 768** | `+6.1 min (368.0s)` | `+6.1 min (368s)` | 1 | `0.0%` |
| **Route 54** | `+6.1 min (365.8s)` | `+45.3 min (2717s)` | 13 | `70.59%` |
| **Route 925** | `+4.5 min (268.6s)` | `+16.9 min (1014s)` | 15 | `50.0%` |
| **Route 7** | `+3.4 min (206.0s)` | `+17.4 min (1041s)` | 5 | `60.0%` |
| **Route 921** | `+3.3 min (197.9s)` | `+6.8 min (406s)` | 8 | `71.43%` |
| **Route 10** | `+3.1 min (188.4s)` | `+10.3 min (621s)` | 12 | `50.0%` |
| **Route 2** | `+3.0 min (181.7s)` | `+10.8 min (647s)` | 10 | `78.57%` |

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
| `1332593` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332797` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351501` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351730` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356087` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356430` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360967` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360980` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361513` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361606` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1271079` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1284353` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356955` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357365` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327992` | Route 25 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-02T23:53:15.515631+00:00`.*
