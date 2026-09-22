# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-22T20:19:25.010619+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.97%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.02%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1155` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `910` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `196` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+57.0s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+3.5s` (`0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 528 | 45.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 262 | 22.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 111 | 9.6% |
| 🔴 **Severe Delay** | Over 15m late | 9 | 0.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 196 | 17.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 49 | 4.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 578** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-94.0s` |
| **Route 766** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+2.0m` |
| **Route 25** | 9 | 4 | 5 | **`55.56%`** | `100.0%` | `+1.2m` |
| **Route 36** | 12 | 3 | 6 | **`50.0%`** | `66.67%` | `+0.9m` |
| **Route 763** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-69.0s` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-75.0s` |
| **Route 860** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-33.0s` |
| **Route 11** | 26 | 11 | 12 | **`46.15%`** | `75.0%` | `-22.8s` |
| **Route 17** | 27 | 12 | 12 | **`44.44%`** | `81.82%` | `+0.7m` |
| **Route 921** | 32 | 12 | 14 | **`43.75%`** | `77.78%` | `+2.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 785** | `+11.5 min (691.2s)` | `+41.5 min (2490s)` | 3 | `75.0%` |
| **Route 667** | `+11.0 min (658.0s)` | `+11.0 min (658s)` | 1 | `0.0%` |
| **Route 777** | `+7.6 min (456.0s)` | `+7.6 min (456s)` | 1 | `0.0%` |
| **Route 65** | `+6.3 min (379.0s)` | `+17.0 min (1018s)` | 4 | `0.0%` |
| **Route 725** | `+5.1 min (308.2s)` | `+19.8 min (1190s)` | 2 | `33.33%` |
| **Route 904** | `+4.3 min (258.5s)` | `+9.7 min (582s)` | 11 | `45.0%` |
| **Route 94** | `+4.0 min (239.3s)` | `+16.2 min (974s)` | 9 | `72.73%` |
| **Route 7** | `+3.8 min (226.0s)` | `+17.9 min (1076s)` | 7 | `66.67%` |
| **Route 673** | `+3.7 min (224.8s)` | `+6.5 min (389s)` | 4 | `60.0%` |
| **Route 9** | `+3.7 min (222.4s)` | `+13.3 min (798s)` | 8 | `66.67%` |

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
| `1325041` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325058` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326160` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326419` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326592` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326711` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327099` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327148` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |
| `2026-09-22 07:02:34` | `0.0%` | `75.0%` | 5 | 4 | `+-5.5s` |
| `2026-09-22 01:41:09` | `16.23%` | `66.51%` | 530 | 430 | `+65.0s` |
| `2026-09-21 23:25:41` | `15.03%` | `53.0%` | 825 | 666 | `+13.2s` |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-22T20:19:25.010619+00:00`.*
