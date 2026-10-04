# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-04T12:37:23.909599+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`74.03%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `555` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `413` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `140` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+160.6s` (`2.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+101.0s` (`1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 305 | 55.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 28 | 5.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 73 | 13.2% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 140 | 25.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 645** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+6.4m` |
| **Route 67** | 5 | 2 | 3 | **`60.0%`** | `100.0%` | `+1.8m` |
| **Route 83** | 7 | 3 | 4 | **`57.14%`** | `100.0%` | `-73.3s` |
| **Route 63** | 13 | 4 | 7 | **`53.85%`** | `80.0%` | `+2.8m` |
| **Route 4** | 12 | 5 | 6 | **`50.0%`** | `83.33%` | `+2.4m` |
| **Route 46** | 6 | 2 | 3 | **`50.0%`** | `100.0%` | `+1.7m` |
| **Route 62** | 11 | 4 | 5 | **`45.45%`** | `100.0%` | `+1.3m` |
| **Route 61** | 7 | 3 | 3 | **`42.86%`** | `75.0%` | `+4.2m` |
| **Route 22** | 20 | 8 | 8 | **`40.0%`** | `41.67%` | `+8.3m` |
| **Route 921** | 20 | 5 | 8 | **`40.0%`** | `60.0%` | `+3.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | `+8.3 min (498.6s)` | `+27.1 min (1624s)` | 8 | `41.67%` |
| **Route 9** | `+7.2 min (432.8s)` | `+18.4 min (1101s)` | 6 | `62.5%` |
| **Route 645** | `+6.4 min (382.0s)` | `+6.4 min (382s)` | 1 | `0.0%` |
| **Route 14** | `+5.9 min (351.9s)` | `+17.4 min (1042s)` | 6 | `60.0%` |
| **Route 11** | `+5.7 min (343.7s)` | `+13.6 min (818s)` | 5 | `55.56%` |
| **Route 7** | `+5.2 min (314.3s)` | `+16.3 min (980s)` | 6 | `50.0%` |
| **Route 65** | `+5.0 min (297.3s)` | `+7.6 min (456s)` | 2 | `33.33%` |
| **Route 923** | `+4.8 min (289.7s)` | `+24.3 min (1456s)` | 7 | `69.23%` |
| **Route 10** | `+4.6 min (278.0s)` | `+9.2 min (551s)` | 4 | `71.43%` |
| **Route 5** | `+4.4 min (264.5s)` | `+7.3 min (438s)` | 3 | `50.0%` |

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
| `1317773` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319316` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367610` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368149` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331478` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332022` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332078` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332944` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361391` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361511` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361536` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362014` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364591` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364691` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366806` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-04T12:37:23.909599+00:00`.*
