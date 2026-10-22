# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:00:21.431000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `994` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `782` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `194` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+40.0s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 448 | 45.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 246 | 24.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 69 | 6.9% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 194 | 19.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 28 | 2.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 355** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 275** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 470** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 768** | 5 | 1 | 4 | **`80.0%`** | `100.0%` | `-20.0s` |
| **Route 785** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+0.1 min` |
| **Route 781** | 5 | 2 | 3 | **`60.0%`** | `100.0%` | `+0.2 min` |
| **Route 827** | 5 | 2 | 3 | **`60.0%`** | `0.0%` | `-146.5s` |
| **Route 850** | 7 | 2 | 4 | **`57.14%`** | `66.67%` | `-43.3s` |
| **Route 46** | 10 | 2 | 5 | **`50.0%`** | `25.0%` | `+0.0 min` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 75** | `+3.8 min (+227.8s)` | `+10.4 min (+626s)` | 2 | `33.33%` |
| **Route 904** | `+3.7 min (+219.9s)` | `+9.2 min (+549s)` | 9 | `78.57%` |
| **Route 54** | `+3.6 min (+219.0s)` | `+24.4 min (+1462s)` | 17 | `65.38%` |
| **Route 5** | `+3.1 min (+185.2s)` | `+7.8 min (+469s)` | 3 | `25.0%` |
| **Route 645** | `+2.9 min (+172.2s)` | `+9.4 min (+565s)` | 7 | `62.5%` |
| **Route 94** | `+2.8 min (+170.4s)` | `+6.7 min (+400s)` | 5 | `88.89%` |
| **Route 11** | `+2.4 min (+143.5s)` | `+12.4 min (+747s)` | 11 | `66.67%` |
| **Route 63** | `+2.0 min (+121.1s)` | `+19.0 min (+1140s)` | 11 | `77.78%` |
| **Route 901** | `+1.9 min (+111.4s)` | `+6.0 min (+360s)` | 7 | `85.71%` |
| **Route 716** | `+1.8 min (+109.0s)` | `+4.9 min (+293s)` | 1 | `100.0%` |

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
| `1131287` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1133480` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134199` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1135640` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1136024` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1136082` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1187364` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318988` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319645` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319664` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319758` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364635` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364825` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365913` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365940` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:00:21` | `19.52%` | `58.33%` | 994 | 782 | `+40.0s` |
| `2026-10-22 18:30:37` | `17.91%` | `56.46%` | 977 | 773 | `+21.0s` |
| `2026-10-22 15:01:09` | `16.82%` | `53.5%` | 886 | 714 | `-4.2s` |
| `2026-10-22 13:31:54` | `15.92%` | `57.37%` | 911 | 760 | `+35.3s` |
| `2026-10-22 13:03:21` | `14.75%` | `60.8%` | 949 | 801 | `+39.5s` |
| `2026-10-22 12:30:37` | `14.21%` | `67.22%` | 985 | 836 | `+39.0s` |
| `2026-10-22 12:00:40` | `14.89%` | `65.16%` | 967 | 818 | `+11.8s` |
| `2026-10-22 11:30:35` | `16.47%` | `61.36%` | 923 | 766 | `-1.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:00:21.431000+00:00`.*
