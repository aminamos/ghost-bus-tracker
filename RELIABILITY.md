# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-30T16:01:00.984943+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.97%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `889` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `739` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `134` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+9.4s` (`0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-17.0s` (`-0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 434 | 48.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 254 | 28.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 45 | 5.1% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 134 | 15.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 16 | 1.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 827** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-7.0s` |
| **Route 850** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+0.5m` |
| **Route 537** | 5 | 1 | 3 | **`60.0%`** | `100.0%` | `+0.1m` |
| **Route 25** | 6 | 2 | 3 | **`50.0%`** | `100.0%` | `+1.4m` |
| **Route 5** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `-32.5s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.0m` |
| **Route 32** | 15 | 5 | 6 | **`40.0%`** | `100.0%` | `-45.9s` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `66.67%` | `-73.5s` |
| **Route 64** | 22 | 10 | 8 | **`36.36%`** | `100.0%` | `+0.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 113** | `+3.7 min (223.0s)` | `+3.7 min (223s)` | 1 | `100.0%` |
| **Route 698** | `+3.4 min (204.0s)` | `+4.5 min (270s)` | 2 | `100.0%` |
| **Route 925** | `+3.2 min (192.2s)` | `+16.8 min (1008s)` | 17 | `55.0%` |
| **Route 902** | `+3.0 min (180.0s)` | `+17.0 min (1020s)` | 11 | `81.82%` |
| **Route 801** | `+2.5 min (151.2s)` | `+5.3 min (317s)` | 2 | `75.0%` |
| **Route 921** | `+2.5 min (148.4s)` | `+4.8 min (290s)` | 10 | `100.0%` |
| **Route 48** | `+2.0 min (121.3s)` | `+9.7 min (579s)` | 2 | `0.0%` |
| **Route 542** | `+1.9 min (115.8s)` | `+7.1 min (424s)` | 4 | `83.33%` |
| **Route 645** | `+1.9 min (112.2s)` | `+16.6 min (994s)` | 5 | `80.0%` |
| **Route 94** | `+1.7 min (103.7s)` | `+4.1 min (248s)` | 5 | `100.0%` |

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
| `1324991` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325001` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325219` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325816` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326056` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326238` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326546` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318029` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318093` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319440` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319476` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348961` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350603` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350654` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351083` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-30T16:01:00.984943+00:00`.*
