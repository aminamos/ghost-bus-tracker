# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-03T02:53:57.531112+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.89%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.81%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `431` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `384` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `34` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+89.2s` (`1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+5.0s` (`0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 222 | 51.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 109 | 25.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 45 | 10.4% |
| 🔴 **Severe Delay** | Over 15m late | 8 | 1.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 34 | 7.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 13 | 3.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 9** | 7 | 4 | 3 | **`42.86%`** | `100.0%` | `-72.2s` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-10.8s` |
| **Route 68** | 10 | 5 | 3 | **`30.0%`** | `80.0%` | `+0.6m` |
| **Route 18** | 23 | 12 | 6 | **`26.09%`** | `91.67%` | `-24.5s` |
| **Route 924** | 23 | 12 | 5 | **`21.74%`** | `50.0%` | `+0.8m` |
| **Route 14** | 10 | 6 | 2 | **`20.0%`** | `80.0%` | `+1.5m` |
| **Route 5** | 5 | 4 | 1 | **`20.0%`** | `50.0%` | `+1.1m` |
| **Route 38** | 11 | 7 | 2 | **`18.18%`** | `100.0%` | `-95.7s` |
| **Route 63** | 11 | 5 | 2 | **`18.18%`** | `60.0%` | `+1.1m` |
| **Route 925** | 20 | 10 | 3 | **`15.0%`** | `62.5%` | `+3.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 323** | `+22.5 min (1349.1s)` | `+61.1 min (3668s)` | 2 | `0.0%` |
| **Route 645** | `+14.4 min (864.0s)` | `+14.4 min (864s)` | 1 | `0.0%` |
| **Route 67** | `+5.9 min (354.0s)` | `+5.9 min (354s)` | 2 | `0.0%` |
| **Route 925** | `+3.6 min (218.2s)` | `+18.6 min (1115s)` | 10 | `62.5%` |
| **Route 2** | `+3.6 min (213.4s)` | `+10.5 min (628s)` | 7 | `50.0%` |
| **Route 923** | `+3.6 min (213.1s)` | `+12.5 min (750s)` | 5 | `70.0%` |
| **Route 902** | `+3.2 min (195.0s)` | `+11.0 min (660s)` | 8 | `87.5%` |
| **Route 72** | `+2.8 min (167.8s)` | `+8.4 min (504s)` | 4 | `75.0%` |
| **Route 901** | `+2.4 min (145.0s)` | `+7.0 min (420s)` | 6 | `83.33%` |
| **Route 4** | `+2.3 min (139.0s)` | `+12.8 min (767s)` | 7 | `66.67%` |

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
| `1331698` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332889` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357399` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357743` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361046` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361581` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361969` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363353` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356943` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1179334` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1180571` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1221056` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1221089` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361538` | Route 38 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362119` | Route 38 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-03T02:53:57.531112+00:00`.*
