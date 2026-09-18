# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-18T18:35:51.403234+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.26%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `979` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `751` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `179` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+9.8s` (`0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-9.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 415 | 42.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 284 | 29.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 50 | 5.1% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 179 | 18.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 49 | 5.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 275** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 64** | 28 | 11 | 14 | **`50.0%`** | `92.31%` | `+1.6m` |
| **Route 723** | 6 | 2 | 3 | **`50.0%`** | `100.0%` | `-35.3s` |
| **Route 850** | 6 | 2 | 3 | **`50.0%`** | `100.0%` | `-119.0s` |
| **Route 11** | 26 | 10 | 12 | **`46.15%`** | `77.78%` | `+1.0m` |
| **Route 10** | 37 | 15 | 17 | **`45.95%`** | `75.0%` | `-104.2s` |
| **Route 25** | 9 | 3 | 4 | **`44.44%`** | `100.0%` | `-31.2s` |
| **Route 18** | 39 | 18 | 17 | **`43.59%`** | `80.0%` | `-30.8s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-58.5s` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-43.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+6.8 min (406.8s)` | `+24.9 min (1496s)` | 4 | `80.0%` |
| **Route 904** | `+3.0 min (177.2s)` | `+15.4 min (924s)` | 9 | `86.67%` |
| **Route 87** | `+2.8 min (167.0s)` | `+11.0 min (659s)` | 5 | `60.0%` |
| **Route 94** | `+2.7 min (160.8s)` | `+7.5 min (448s)` | 6 | `90.0%` |
| **Route 542** | `+2.4 min (143.2s)` | `+7.0 min (419s)` | 5 | `83.33%` |
| **Route 345** | `+2.4 min (143.0s)` | `+7.5 min (453s)` | 2 | `75.0%` |
| **Route 781** | `+2.2 min (134.5s)` | `+4.1 min (244s)` | 2 | `100.0%` |
| **Route 716** | `+2.2 min (131.3s)` | `+5.1 min (304s)` | 1 | `66.67%` |
| **Route 615** | `+2.1 min (128.8s)` | `+11.9 min (717s)` | 2 | `50.0%` |
| **Route 54** | `+2.0 min (117.5s)` | `+11.3 min (677s)` | 16 | `86.96%` |

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
| `1324974` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324976` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324995` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325058` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325282` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325813` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326056` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326221` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326345` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326430` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326587` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326592` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326711` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-18T18:35:51.403234+00:00`.*
