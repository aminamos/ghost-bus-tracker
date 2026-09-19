# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T14:34:03.431184+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.62%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.91%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `717` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `561` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `155` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+80.6s` (`1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+45.0s` (`0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 409 | 57.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 94 | 13.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 53 | 7.4% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 155 | 21.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `+0.9m` |
| **Route 10** | 26 | 9 | 13 | **`50.0%`** | `90.91%` | `+2.0m` |
| **Route 17** | 18 | 6 | 9 | **`50.0%`** | `87.5%` | `+2.1m` |
| **Route 18** | 28 | 10 | 13 | **`46.43%`** | `84.62%` | `+1.9m` |
| **Route 36** | 11 | 4 | 5 | **`45.45%`** | `80.0%` | `+2.9m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.8m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.3m` |
| **Route 11** | 24 | 8 | 10 | **`41.67%`** | `90.91%` | `+1.1m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+0.0m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.4m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+6.0 min (360.5s)` | `+11.0 min (662s)` | 2 | `50.0%` |
| **Route 94** | `+6.0 min (357.9s)` | `+21.3 min (1277s)` | 4 | `57.14%` |
| **Route 9** | `+4.3 min (255.9s)` | `+18.5 min (1110s)` | 6 | `57.14%` |
| **Route 725** | `+4.0 min (239.2s)` | `+5.8 min (348s)` | 2 | `75.0%` |
| **Route 921** | `+3.8 min (227.9s)` | `+12.5 min (749s)` | 7 | `61.54%` |
| **Route 46** | `+3.7 min (220.0s)` | `+5.7 min (340s)` | 1 | `50.0%` |
| **Route 67** | `+3.2 min (190.5s)` | `+12.1 min (724s)` | 5 | `62.5%` |
| **Route 3** | `+3.1 min (187.8s)` | `+7.2 min (429s)` | 12 | `64.71%` |
| **Route 36** | `+2.9 min (172.2s)` | `+16.7 min (1001s)` | 4 | `80.0%` |
| **Route 904** | `+2.8 min (168.3s)` | `+6.5 min (392s)` | 7 | `58.33%` |

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
| `1325057` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325118` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325132` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327908` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329200` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333832` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1339533` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344034` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1344512` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1353582` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359083` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359796` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360164` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319373` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348766` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |
| `2026-09-19 11:16:01` | `28.18%` | `71.05%` | 479 | 343 | `+48.3s` |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T14:34:03.431184+00:00`.*
