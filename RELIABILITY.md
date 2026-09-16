# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-16T20:17:29.307515+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.39%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1105` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `883` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `194` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+35.4s` (`0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 515 | 46.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 276 | 25.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 84 | 7.6% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 194 | 17.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 28 | 2.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 9 | 4 | 5 | **`55.56%`** | `100.0%` | `-42.5s` |
| **Route 65** | 9 | 3 | 5 | **`55.56%`** | `0.0%` | `+1.6m` |
| **Route 17** | 27 | 11 | 14 | **`51.85%`** | `77.78%` | `+0.8m` |
| **Route 921** | 33 | 11 | 17 | **`51.52%`** | `100.0%` | `-68.2s` |
| **Route 11** | 26 | 10 | 13 | **`50.0%`** | `57.14%` | `+0.5m` |
| **Route 30** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `-36.7s` |
| **Route 760** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `-81.5s` |
| **Route 763** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-70.0s` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-75.0s` |
| **Route 860** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-37.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 667** | `+11.0 min (658.0s)` | `+11.0 min (658s)` | 1 | `0.0%` |
| **Route 716** | `+8.2 min (493.5s)` | `+18.2 min (1095s)` | 1 | `0.0%` |
| **Route 903** | `+4.9 min (294.5s)` | `+16.0 min (959s)` | 2 | `66.67%` |
| **Route 777** | `+4.0 min (238.0s)` | `+4.0 min (238s)` | 1 | `100.0%` |
| **Route 645** | `+3.8 min (230.1s)` | `+19.5 min (1172s)` | 6 | `77.78%` |
| **Route 542** | `+3.7 min (220.8s)` | `+6.2 min (370s)` | 6 | `66.67%` |
| **Route 904** | `+3.5 min (208.1s)` | `+10.5 min (632s)` | 11 | `70.0%` |
| **Route 113** | `+3.4 min (204.0s)` | `+4.8 min (288s)` | 2 | `100.0%` |
| **Route 673** | `+3.4 min (203.2s)` | `+6.4 min (384s)` | 4 | `80.0%` |
| **Route 54** | `+3.3 min (197.3s)` | `+21.4 min (1286s)` | 15 | `66.67%` |

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
| `1325041` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325699` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325813` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326160` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326419` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326711` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326803` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327099` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327148` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-16T20:17:29.307515+00:00`.*
