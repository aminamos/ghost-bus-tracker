# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-01T23:17:02.007739+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.31%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`54.51%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `838` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `733` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `78` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+125.8s` (`2.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+20.5s` (`0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 399 | 47.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 200 | 23.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 106 | 12.6% |
| 🔴 **Severe Delay** | Over 15m late | 27 | 3.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 78 | 9.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 27 | 3.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 7 | 1 | 4 | **`57.14%`** | `100.0%` | `-13.0s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `50.0%` | `+1.5m` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `85.71%` | `+1.3m` |
| **Route 67** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `+0.3m` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `-72.0s` |
| **Route 18** | 26 | 15 | 7 | **`26.92%`** | `64.29%` | `+2.8m` |
| **Route 538** | 8 | 3 | 2 | **`25.0%`** | `75.0%` | `+0.7m` |
| **Route 9** | 13 | 8 | 3 | **`23.08%`** | `50.0%` | `+3.9m` |
| **Route 924** | 35 | 19 | 8 | **`22.86%`** | `71.43%` | `+2.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 781** | `+33.8 min (2025.5s)` | `+84.2 min (5052s)` | 3 | `33.33%` |
| **Route 904** | `+11.0 min (660.8s)` | `+44.3 min (2659s)` | 9 | `38.89%` |
| **Route 46** | `+9.3 min (555.3s)` | `+33.7 min (2023s)` | 3 | `57.14%` |
| **Route 113** | `+8.8 min (528.0s)` | `+8.8 min (528s)` | 1 | `0.0%` |
| **Route 2** | `+5.8 min (345.9s)` | `+26.6 min (1596s)` | 14 | `70.0%` |
| **Route 54** | `+5.7 min (341.1s)` | `+27.4 min (1647s)` | 10 | `60.0%` |
| **Route 467** | `+5.7 min (341.0s)` | `+5.7 min (341s)` | 1 | `0.0%` |
| **Route 921** | `+5.1 min (306.5s)` | `+17.4 min (1044s)` | 9 | `66.67%` |
| **Route 698** | `+5.1 min (303.3s)` | `+9.3 min (558s)` | 3 | `33.33%` |
| **Route 925** | `+4.6 min (278.7s)` | `+28.0 min (1682s)` | 17 | `59.09%` |

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
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331338` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332105` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332797` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318708` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319558` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356087` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356389` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360967` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361079` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-01T23:17:02.007739+00:00`.*
