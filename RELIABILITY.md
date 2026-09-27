# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-27T23:29:25.178858+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.87%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.48%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `537` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `478` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `53` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+215.8s` (`3.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+181.5s` (`3.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 313 | 58.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 30 | 5.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 129 | 24.0% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 53 | 9.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 6 | 1.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 10 | 0 | 10 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+3.8m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `57.14%` | `+4.6m` |
| **Route 18** | 24 | 12 | 8 | **`33.33%`** | `73.33%` | `+4.5m` |
| **Route 64** | 13 | 8 | 4 | **`30.77%`** | `62.5%` | `+3.3m` |
| **Route 540** | 7 | 2 | 2 | **`28.57%`** | `40.0%` | `+5.4m` |
| **Route 9** | 9 | 6 | 2 | **`22.22%`** | `28.57%` | `+6.3m` |
| **Route 5** | 5 | 4 | 1 | **`20.0%`** | `100.0%` | `+3.1m` |
| **Route 924** | 24 | 15 | 4 | **`16.67%`** | `75.0%` | `+3.8m` |
| **Route 63** | 12 | 8 | 2 | **`16.67%`** | `87.5%` | `+1.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+12.7 min (759.0s)` | `+26.8 min (1606s)` | 2 | `25.0%` |
| **Route 94** | `+8.1 min (486.7s)` | `+15.9 min (952s)` | 5 | `28.57%` |
| **Route 22** | `+8.1 min (483.4s)` | `+21.4 min (1283s)` | 12 | `28.57%` |
| **Route 10** | `+6.9 min (413.8s)` | `+18.7 min (1122s)` | 7 | `50.0%` |
| **Route 17** | `+6.7 min (404.2s)` | `+12.0 min (719s)` | 6 | `37.5%` |
| **Route 9** | `+6.3 min (379.9s)` | `+14.4 min (866s)` | 6 | `28.57%` |
| **Route 721** | `+6.0 min (357.0s)` | `+6.0 min (357s)` | 1 | `0.0%` |
| **Route 27** | `+5.9 min (356.0s)` | `+11.4 min (686s)` | 2 | `66.67%` |
| **Route 3** | `+5.7 min (342.9s)` | `+11.5 min (692s)` | 6 | `37.5%` |
| **Route 540** | `+5.4 min (321.4s)` | `+8.7 min (521s)` | 2 | `40.0%` |

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
| `1331241` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333050` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350612` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351642` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355748` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357154` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361382` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361678` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361727` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363902` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1281236` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1282829` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357263` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357775` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1176957` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |
| `2026-09-27 20:35:38` | `11.95%` | `66.38%` | 678 | 590 | `+197.7s` |
| `2026-09-27 17:51:50` | `12.29%` | `70.67%` | 667 | 583 | `+185.9s` |
| `2026-09-27 13:10:06` | `14.17%` | `79.59%` | 508 | 433 | `+124.5s` |
| `2026-09-27 07:19:56` | `0.0%` | `100.0%` | 2 | 2 | `+129.5s` |
| `2026-09-27 01:36:17` | `12.6%` | `73.35%` | 500 | 409 | `+161.6s` |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-27T23:29:25.178858+00:00`.*
