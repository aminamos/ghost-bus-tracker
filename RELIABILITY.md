# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-18T01:00:45.312805+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.8%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `595` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `494` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `91` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+67.2s` (`1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+30.0s` (`0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 330 | 55.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 108 | 18.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 55 | 9.2% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 91 | 15.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 10 | 1.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 11** | 12 | 3 | 7 | **`58.33%`** | `80.0%` | `+2.8m` |
| **Route 18** | 23 | 9 | 11 | **`47.83%`** | `70.0%` | `+1.5m` |
| **Route 921** | 21 | 6 | 10 | **`47.62%`** | `77.78%` | `+1.9m` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-88.7s` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `83.33%` | `+2.3m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.5m` |
| **Route 10** | 21 | 7 | 8 | **`38.1%`** | `88.89%` | `-6.8s` |
| **Route 9** | 8 | 4 | 3 | **`37.5%`** | `50.0%` | `+3.2m` |
| **Route 68** | 12 | 6 | 4 | **`33.33%`** | `85.71%` | `+2.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+4.4 min (264.5s)` | `+10.3 min (616s)` | 3 | `75.0%` |
| **Route 67** | `+3.7 min (221.3s)` | `+8.9 min (536s)` | 4 | `66.67%` |
| **Route 2** | `+3.6 min (217.3s)` | `+14.1 min (846s)` | 9 | `72.73%` |
| **Route 94** | `+3.4 min (204.1s)` | `+13.5 min (808s)` | 3 | `85.71%` |
| **Route 219** | `+3.2 min (195.0s)` | `+11.9 min (714s)` | 2 | `66.67%` |
| **Route 9** | `+3.2 min (195.0s)` | `+10.6 min (635s)` | 4 | `50.0%` |
| **Route 904** | `+3.1 min (183.9s)` | `+9.7 min (583s)` | 9 | `78.57%` |
| **Route 54** | `+2.9 min (173.8s)` | `+9.1 min (546s)` | 11 | `87.5%` |
| **Route 64** | `+2.8 min (169.9s)` | `+7.6 min (457s)` | 7 | `72.73%` |
| **Route 11** | `+2.8 min (169.2s)` | `+7.5 min (448s)` | 3 | `80.0%` |

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
| `1325266` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325371` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325397` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325715` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325968` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326639` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326793` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319093` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319876` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319879` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348999` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349261` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349633` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349744` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-18T01:00:45.312805+00:00`.*
