# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-17T12:18:36.540305+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.82%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.21%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `967` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `812` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `153` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+9.9s` (`0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-12.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 497 | 51.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 275 | 28.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 36 | 3.7% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 153 | 15.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 25 | 9 | 13 | **`52.0%`** | `100.0%` | `+0.0m` |
| **Route 65** | 10 | 3 | 5 | **`50.0%`** | `100.0%` | `-36.8s` |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.3m` |
| **Route 18** | 25 | 10 | 12 | **`48.0%`** | `87.5%` | `+0.6m` |
| **Route 11** | 26 | 11 | 12 | **`46.15%`** | `85.71%` | `-17.6s` |
| **Route 10** | 23 | 11 | 10 | **`43.48%`** | `100.0%` | `-58.8s` |
| **Route 921** | 20 | 7 | 8 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `+0.4m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 9** | 13 | 7 | 5 | **`38.46%`** | `100.0%` | `+0.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+20.1 min (1204.4s)` | `+59.9 min (3595s)` | 4 | `50.0%` |
| **Route 294** | `+4.8 min (286.0s)` | `+4.8 min (286s)` | 1 | `100.0%` |
| **Route 789** | `+4.3 min (260.5s)` | `+10.6 min (634s)` | 2 | `0.0%` |
| **Route 25** | `+4.2 min (249.5s)` | `+8.8 min (530s)` | 5 | `50.0%` |
| **Route 698** | `+4.1 min (248.8s)` | `+8.2 min (494s)` | 8 | `57.14%` |
| **Route 467** | `+4.1 min (247.8s)` | `+8.8 min (525s)` | 3 | `33.33%` |
| **Route 645** | `+3.6 min (213.8s)` | `+13.2 min (792s)` | 6 | `66.67%` |
| **Route 766** | `+3.3 min (198.5s)` | `+4.2 min (253s)` | 2 | `100.0%` |
| **Route 33** | `+2.3 min (137.5s)` | `+3.8 min (225s)` | 1 | `100.0%` |
| **Route 363** | `+2.2 min (134.5s)` | `+3.1 min (188s)` | 2 | `100.0%` |

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
| `1324952` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324979` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325089` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325352` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326203` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326506` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326907` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326971` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327118` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317986` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318353` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318512` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318573` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318761` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-17T12:18:36.540305+00:00`.*
