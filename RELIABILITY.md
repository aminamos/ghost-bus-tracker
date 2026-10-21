# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-21T22:30:36.045000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`49.94%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `996` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `843` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `127` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+156.6s` (`+2.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+34.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 422 | 42.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 219 | 22.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 160 | 16.1% |
| 🔴 **Severe Delay** | Over 15m late | 44 | 4.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 127 | 12.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 24 | 2.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 470** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 768** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+0.0s` |
| **Route 5** | 6 | 2 | 3 | **`50.0%`** | `66.67%` | `-14.3s` |
| **Route 784** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-120.0s` |
| **Route 534** | 10 | 2 | 4 | **`40.0%`** | `50.0%` | `+0.7 min` |
| **Route 539** | 10 | 4 | 4 | **`40.0%`** | `50.0%` | `+7.8 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.4 min` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `57.14%` | `+2.2 min` |
| **Route 25** | 6 | 4 | 2 | **`33.33%`** | `75.0%` | `+2.6 min` |
| **Route 827** | 6 | 2 | 2 | **`33.33%`** | `25.0%` | `-26.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 667** | `+19.0 min (+1142.0s)` | `+19.0 min (+1142s)` | 1 | `0.0%` |
| **Route 467** | `+16.8 min (+1005.0s)` | `+27.7 min (+1662s)` | 2 | `0.0%` |
| **Route 673** | `+16.1 min (+967.5s)` | `+30.1 min (+1805s)` | 2 | `50.0%` |
| **Route 134** | `+13.7 min (+823.0s)` | `+13.7 min (+823s)` | 1 | `0.0%` |
| **Route 766** | `+9.8 min (+587.0s)` | `+9.8 min (+587s)` | 1 | `0.0%` |
| **Route 824** | `+9.5 min (+570.0s)` | `+9.5 min (+570s)` | 1 | `0.0%` |
| **Route 645** | `+8.5 min (+512.2s)` | `+36.0 min (+2159s)` | 6 | `25.0%` |
| **Route 695** | `+8.4 min (+506.0s)` | `+8.4 min (+506s)` | 1 | `0.0%` |
| **Route 546** | `+8.2 min (+494.7s)` | `+37.2 min (+2233s)` | 4 | `71.43%` |
| **Route 698** | `+8.1 min (+487.8s)` | `+24.4 min (+1467s)` | 5 | `60.0%` |

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
| `1131607` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132610` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134375` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319860` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365073` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366602` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331262` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331972` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332794` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1369579` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1369703` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1369998` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1135705` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 22:30:36` | `12.75%` | `49.94%` | 996 | 843 | `+156.6s` |
| `2026-10-21 22:00:35` | `14.19%` | `52.75%` | 1064 | 891 | `+157.5s` |
| `2026-10-21 21:30:36` | `13.98%` | `55.9%` | 1109 | 930 | `+127.3s` |
| `2026-10-21 21:00:36` | `15.28%` | `57.42%` | 1132 | 938 | `+113.2s` |
| `2026-10-21 20:30:36` | `17.16%` | `61.51%` | 1148 | 928 | `+82.6s` |
| `2026-10-21 20:00:36` | `18.42%` | `62.94%` | 1102 | 890 | `+55.4s` |
| `2026-10-21 18:30:39` | `19.92%` | `56.76%` | 1004 | 778 | `+20.4s` |
| `2026-10-21 18:00:37` | `18.26%` | `54.81%` | 975 | 770 | `+19.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T22:30:36.045000+00:00`.*
