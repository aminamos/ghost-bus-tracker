# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-29T23:49:28.225441+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.82%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.97%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `764` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `642` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `75` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+78.4s` (`1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+7.5s` (`0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 385 | 50.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 176 | 23.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 67 | 8.8% |
| 🔴 **Severe Delay** | Over 15m late | 14 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 75 | 9.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 47 | 6.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-69.2s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.0m` |
| **Route 36** | 12 | 5 | 4 | **`33.33%`** | `100.0%` | `-52.1s` |
| **Route 645** | 6 | 4 | 2 | **`33.33%`** | `50.0%` | `+5.5m` |
| **Route 18** | 26 | 13 | 8 | **`30.77%`** | `64.29%` | `+2.5m` |
| **Route 924** | 32 | 17 | 8 | **`25.0%`** | `84.62%` | `+0.5m` |
| **Route 11** | 16 | 9 | 4 | **`25.0%`** | `81.82%` | `+3.0m` |
| **Route 32** | 8 | 4 | 2 | **`25.0%`** | `100.0%` | `+1.7m` |
| **Route 723** | 4 | 2 | 1 | **`25.0%`** | `100.0%` | `-42.7s` |
| **Route 10** | 18 | 10 | 4 | **`22.22%`** | `63.64%` | `+1.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 790** | `+45.5 min (2728.0s)` | `+45.5 min (2728s)` | 1 | `0.0%` |
| **Route 888** | `+15.3 min (918.0s)` | `+31.2 min (1874s)` | 2 | `50.0%` |
| **Route 777** | `+12.5 min (749.0s)` | `+12.5 min (749s)` | 1 | `0.0%` |
| **Route 25** | `+11.4 min (682.8s)` | `+45.0 min (2703s)` | 3 | `66.67%` |
| **Route 698** | `+10.3 min (617.0s)` | `+10.3 min (617s)` | 1 | `0.0%` |
| **Route 615** | `+9.1 min (547.2s)` | `+19.3 min (1158s)` | 2 | `50.0%` |
| **Route 904** | `+8.4 min (501.9s)` | `+25.1 min (1506s)` | 7 | `42.86%` |
| **Route 645** | `+5.5 min (328.0s)` | `+8.8 min (528s)` | 4 | `50.0%` |
| **Route 925** | `+4.8 min (287.0s)` | `+23.2 min (1395s)` | 16 | `52.17%` |
| **Route 774** | `+4.5 min (273.0s)` | `+8.6 min (516s)` | 2 | `50.0%` |

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
| `1326327` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327097` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319876` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349744` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349828` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331338` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332593` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332797` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318708` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318773` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351501` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351730` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-29T23:49:28.225441+00:00`.*
