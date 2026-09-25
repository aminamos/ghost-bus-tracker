# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-25T02:29:37.153858+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.81%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `502` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `398` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `69` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+52.3s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 250 | 49.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 104 | 20.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 43 | 8.6% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 69 | 13.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 35 | 7.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-10.2s` |
| **Route 7** | 8 | 4 | 3 | **`37.5%`** | `100.0%` | `+0.2m` |
| **Route 61** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `-23.9s` |
| **Route 921** | 20 | 6 | 7 | **`35.0%`** | `100.0%` | `+1.7m` |
| **Route 18** | 23 | 12 | 8 | **`34.78%`** | `81.82%` | `-9.4s` |
| **Route 11** | 12 | 6 | 4 | **`33.33%`** | `66.67%` | `+1.2m` |
| **Route 4** | 12 | 6 | 4 | **`33.33%`** | `66.67%` | `+1.3m` |
| **Route 64** | 12 | 4 | 4 | **`33.33%`** | `100.0%` | `+0.4m` |
| **Route 723** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-37.5s` |
| **Route 38** | 14 | 7 | 4 | **`28.57%`** | `80.0%` | `-17.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+5.9 min (356.9s)` | `+12.1 min (725s)` | 7 | `35.71%` |
| **Route 9** | `+3.3 min (200.0s)` | `+13.2 min (793s)` | 4 | `50.0%` |
| **Route 2** | `+3.1 min (186.4s)` | `+9.8 min (590s)` | 6 | `57.14%` |
| **Route 30** | `+3.1 min (186.0s)` | `+3.1 min (186s)` | 1 | `100.0%` |
| **Route 802** | `+2.3 min (140.0s)` | `+2.3 min (140s)` | 1 | `100.0%` |
| **Route 827** | `+2.3 min (140.0s)` | `+2.3 min (140s)` | 1 | `100.0%` |
| **Route 94** | `+2.3 min (135.7s)` | `+5.8 min (349s)` | 4 | `71.43%` |
| **Route 71** | `+2.2 min (133.6s)` | `+12.6 min (753s)` | 4 | `75.0%` |
| **Route 725** | `+2.0 min (122.0s)` | `+4.8 min (286s)` | 2 | `100.0%` |
| **Route 3** | `+1.9 min (115.7s)` | `+7.6 min (455s)` | 8 | `75.0%` |

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
| `1319546` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319569` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349623` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351646` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331698` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332889` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333220` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1153305` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349388` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351246` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351494` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351741` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356654` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356938` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1357399` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-25T02:29:37.153858+00:00`.*
