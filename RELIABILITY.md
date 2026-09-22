# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-22T17:26:26.013664+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.48%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.47%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `958` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `743` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `177` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+26.2s` (`0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-4.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 427 | 44.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 257 | 26.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 52 | 5.4% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 177 | 18.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 38 | 4.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-176.0s` |
| **Route 921** | 32 | 10 | 16 | **`50.0%`** | `100.0%` | `+1.1m` |
| **Route 11** | 26 | 11 | 12 | **`46.15%`** | `83.33%` | `-118.8s` |
| **Route 36** | 11 | 5 | 5 | **`45.45%`** | `100.0%` | `+1.0m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-8.5s` |
| **Route 17** | 25 | 10 | 10 | **`40.0%`** | `90.0%` | `-5.3s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-25.7s` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+0.8m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-3.7s` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `50.0%` | `+2.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 542** | `+3.9 min (235.2s)` | `+7.4 min (442s)` | 4 | `66.67%` |
| **Route 904** | `+3.9 min (234.6s)` | `+9.0 min (538s)` | 8 | `57.14%` |
| **Route 924** | `+3.3 min (198.1s)` | `+30.9 min (1857s)` | 18 | `55.56%` |
| **Route 923** | `+2.8 min (165.8s)` | `+8.8 min (529s)` | 11 | `72.22%` |
| **Route 87** | `+2.7 min (163.2s)` | `+14.6 min (874s)` | 6 | `85.71%` |
| **Route 83** | `+2.5 min (148.9s)` | `+11.7 min (702s)` | 3 | `50.0%` |
| **Route 10** | `+2.2 min (134.0s)` | `+32.4 min (1944s)` | 14 | `53.85%` |
| **Route 537** | `+2.0 min (122.0s)` | `+5.7 min (340s)` | 1 | `50.0%` |
| **Route 903** | `+1.9 min (112.0s)` | `+6.7 min (401s)` | 2 | `80.0%` |
| **Route 717** | `+1.7 min (102.3s)` | `+4.7 min (281s)` | 1 | `100.0%` |

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
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325697` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325814` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326096` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326587` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326706` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326861` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327089` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317828` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |
| `2026-09-22 07:02:34` | `0.0%` | `75.0%` | 5 | 4 | `+-5.5s` |
| `2026-09-22 01:41:09` | `16.23%` | `66.51%` | 530 | 430 | `+65.0s` |
| `2026-09-21 23:25:41` | `15.03%` | `53.0%` | 825 | 666 | `+13.2s` |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |
| `2026-09-21 08:05:04` | `0.0%` | `53.85%` | 13 | 13 | `+-52.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-22T17:26:26.013664+00:00`.*
