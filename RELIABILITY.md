# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-17T20:26:25.846896+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.79%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1113` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `905` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `190` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+61.3s` (`1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+12.0s` (`0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 523 | 47.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 257 | 23.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 120 | 10.8% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 190 | 17.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 18 | 1.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 537** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 760** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `-81.5s` |
| **Route 763** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-68.0s` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-95.0s` |
| **Route 860** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-42.0s` |
| **Route 11** | 28 | 12 | 12 | **`42.86%`** | `77.78%` | `+0.1m` |
| **Route 64** | 28 | 12 | 12 | **`42.86%`** | `63.64%` | `+1.2m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.5m` |
| **Route 921** | 33 | 12 | 14 | **`42.42%`** | `84.62%` | `+0.4m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 785** | `+11.5 min (689.5s)` | `+25.6 min (1538s)` | 3 | `50.0%` |
| **Route 667** | `+11.0 min (658.0s)` | `+11.0 min (658s)` | 1 | `0.0%` |
| **Route 777** | `+9.3 min (560.5s)` | `+11.1 min (665s)` | 2 | `0.0%` |
| **Route 542** | `+4.3 min (257.2s)` | `+9.9 min (592s)` | 6 | `66.67%` |
| **Route 673** | `+4.1 min (247.6s)` | `+7.3 min (437s)` | 4 | `60.0%` |
| **Route 46** | `+3.9 min (236.3s)` | `+7.0 min (422s)` | 4 | `50.0%` |
| **Route 645** | `+3.8 min (230.4s)` | `+16.3 min (977s)` | 6 | `57.14%` |
| **Route 363** | `+3.8 min (225.5s)` | `+4.3 min (257s)` | 2 | `100.0%` |
| **Route 904** | `+3.7 min (220.8s)` | `+13.8 min (827s)` | 11 | `75.0%` |
| **Route 94** | `+3.3 min (195.1s)` | `+11.1 min (663s)` | 10 | `76.92%` |

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
| `1325432` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326096` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326419` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326430` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327099` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327148` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-17T20:26:25.846896+00:00`.*
