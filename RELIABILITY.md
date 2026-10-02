# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-02T02:21:57.035127+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.25%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `478` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `420` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `49` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+57.4s` (`1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.5s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 266 | 55.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 112 | 23.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 39 | 8.2% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 49 | 10.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 9 | 1.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 36** | 11 | 6 | 4 | **`36.36%`** | `100.0%` | `+0.1m` |
| **Route 18** | 25 | 12 | 8 | **`32.0%`** | `87.5%` | `-11.7s` |
| **Route 68** | 10 | 5 | 3 | **`30.0%`** | `100.0%` | `-17.3s` |
| **Route 9** | 7 | 3 | 2 | **`28.57%`** | `100.0%` | `-56.4s` |
| **Route 540** | 8 | 3 | 2 | **`25.0%`** | `100.0%` | `+0.5m` |
| **Route 723** | 4 | 2 | 1 | **`25.0%`** | `100.0%` | `-47.7s` |
| **Route 924** | 25 | 12 | 6 | **`24.0%`** | `58.33%` | `+2.3m` |
| **Route 63** | 9 | 5 | 2 | **`22.22%`** | `100.0%` | `+0.1m` |
| **Route 7** | 9 | 5 | 2 | **`22.22%`** | `83.33%` | `+1.7m` |
| **Route 925** | 20 | 10 | 4 | **`20.0%`** | `83.33%` | `+0.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 30** | `+5.6 min (338.6s)` | `+14.5 min (872s)` | 3 | `25.0%` |
| **Route 904** | `+4.5 min (271.3s)` | `+18.6 min (1113s)` | 7 | `64.29%` |
| **Route 22** | `+3.5 min (212.4s)` | `+16.8 min (1008s)` | 8 | `62.5%` |
| **Route 827** | `+3.5 min (212.0s)` | `+3.5 min (212s)` | 1 | `100.0%` |
| **Route 2** | `+2.9 min (172.6s)` | `+13.6 min (818s)` | 6 | `75.0%` |
| **Route 924** | `+2.3 min (140.8s)` | `+14.6 min (875s)` | 12 | `58.33%` |
| **Route 923** | `+2.3 min (135.5s)` | `+7.7 min (460s)` | 6 | `72.73%` |
| **Route 902** | `+2.2 min (132.9s)` | `+8.5 min (510s)` | 7 | `85.71%` |
| **Route 903** | `+2.2 min (131.8s)` | `+7.6 min (457s)` | 2 | `83.33%` |
| **Route 538** | `+2.1 min (127.3s)` | `+5.2 min (311s)` | 3 | `66.67%` |

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
| `1325324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327003` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319546` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319569` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332889` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333220` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317845` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318826` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356654` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356938` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357399` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361540` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361581` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361969` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362017` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-02T02:21:57.035127+00:00`.*
