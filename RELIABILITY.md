# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-25T18:15:51.325126+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.87%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.61%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `928` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `776` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `138` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+30.8s` (`0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-10.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 431 | 46.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 267 | 28.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 73 | 7.9% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 138 | 14.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 1.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-13.5s` |
| **Route 850** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `-28.5s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.0m` |
| **Route 921** | 33 | 11 | 14 | **`42.42%`** | `72.22%` | `+2.0m` |
| **Route 64** | 27 | 12 | 11 | **`40.74%`** | `91.67%` | `+0.6m` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `75.0%` | `+0.6m` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-20.0s` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `80.0%` | `+1.2m` |
| **Route 18** | 38 | 20 | 13 | **`34.21%`** | `76.92%` | `-6.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 992** | `+4.7 min (281.8s)` | `+28.5 min (1710s)` | 9 | `64.71%` |
| **Route 904** | `+4.2 min (253.3s)` | `+10.0 min (599s)` | 7 | `53.85%` |
| **Route 94** | `+2.8 min (170.6s)` | `+13.2 min (792s)` | 6 | `90.91%` |
| **Route 645** | `+2.6 min (153.1s)` | `+13.2 min (795s)` | 5 | `71.43%` |
| **Route 87** | `+2.3 min (139.2s)` | `+8.8 min (526s)` | 5 | `80.0%` |
| **Route 54** | `+2.1 min (128.7s)` | `+17.8 min (1070s)` | 13 | `84.21%` |
| **Route 38** | `+2.1 min (126.9s)` | `+14.4 min (867s)` | 7 | `71.43%` |
| **Route 921** | `+2.0 min (119.8s)` | `+8.6 min (517s)` | 11 | `72.22%` |
| **Route 9** | `+2.0 min (119.0s)` | `+11.7 min (700s)` | 8 | `71.43%` |
| **Route 542** | `+1.8 min (110.3s)` | `+4.7 min (282s)` | 4 | `100.0%` |

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
| `1332196` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332584` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332687` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333002` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1219732` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1221300` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1240955` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242793` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348839` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349385` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350360` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350434` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350910` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350948` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351242` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-25T18:15:51.325126+00:00`.*
