# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-24T01:32:00.642742+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.93%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.6%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `576` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `456` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `86` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+105.3s` (`1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+36.5s` (`0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 290 | 50.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 93 | 16.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 65 | 11.3% |
| 🔴 **Severe Delay** | Over 15m late | 8 | 1.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 86 | 14.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 34 | 5.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 4** | 13 | 5 | 6 | **`46.15%`** | `25.0%` | `+2.0m` |
| **Route 921** | 23 | 6 | 10 | **`43.48%`** | `81.82%` | `+2.7m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.1m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-28.3s` |
| **Route 64** | 13 | 4 | 5 | **`38.46%`** | `100.0%` | `+1.3m` |
| **Route 18** | 24 | 12 | 9 | **`37.5%`** | `75.0%` | `+2.2m` |
| **Route 36** | 11 | 6 | 4 | **`36.36%`** | `75.0%` | `+1.3m` |
| **Route 61** | 12 | 6 | 4 | **`33.33%`** | `80.0%` | `+1.7m` |
| **Route 68** | 12 | 6 | 4 | **`33.33%`** | `71.43%` | `+2.9m` |
| **Route 9** | 9 | 5 | 3 | **`33.33%`** | `60.0%` | `+5.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | `+6.8 min (406.5s)` | `+27.5 min (1650s)` | 7 | `60.0%` |
| **Route 904** | `+6.1 min (367.4s)` | `+17.8 min (1069s)` | 8 | `42.86%` |
| **Route 9** | `+5.5 min (329.5s)` | `+19.5 min (1168s)` | 5 | `60.0%` |
| **Route 645** | `+4.3 min (260.7s)` | `+9.0 min (542s)` | 2 | `0.0%` |
| **Route 25** | `+4.3 min (256.0s)` | `+4.3 min (256s)` | 1 | `100.0%` |
| **Route 67** | `+3.8 min (228.6s)` | `+10.2 min (611s)` | 3 | `60.0%` |
| **Route 11** | `+3.5 min (213.0s)` | `+11.9 min (714s)` | 5 | `62.5%` |
| **Route 540** | `+3.1 min (184.9s)` | `+7.1 min (424s)` | 4 | `85.71%` |
| **Route 68** | `+2.9 min (174.5s)` | `+14.3 min (858s)` | 6 | `71.43%` |
| **Route 716** | `+2.7 min (164.0s)` | `+2.7 min (164s)` | 1 | `100.0%` |

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
| `1319879` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348999` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351263` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332519` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332776` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349140` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349553` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349678` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349864` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350078` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350799` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356538` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356567` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356619` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1274035` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-24T01:32:00.642742+00:00`.*
